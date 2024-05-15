import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt

def connect_corners(min_values, max_values):
    corners = []
    for i in range(2):
        for j in range(2):
            for k in range(2):
                corner = [min_values[0] + i * (max_values[0] - min_values[0]),
                          min_values[1] + j * (max_values[1] - min_values[1]),
                          min_values[2] + k * (max_values[2] - min_values[2])]
                corners.append(corner)
    return corners

# npyファイルを読み込み
point_cloud = np.load("./point_cloud/pcd.npy")

# xyzにおける最大値と最小値を求める
min_values = np.min(point_cloud, axis=0)
max_values = np.max(point_cloud, axis=0)

# 8つの角を連結する
corners = connect_corners(min_values, max_values)

pc = o3d.geometry.PointCloud()
colors = np.tile([1, 1, 1], (8, 1))  # 赤色にする
pc.points = o3d.utility.Vector3dVector(corners)
pc.colors = o3d.utility.Vector3dVector(colors)


# Loading point cloud data
dir_path_pc = './point_cloud/'
dir_path_img = './images/pc_images/'
name1 = 'part1'
name2 = 'part2'


point_cloud_data1 = np.load(f'{dir_path_pc}{name1}.npy')
colors1 = np.tile([1, 0, 0], (point_cloud_data1.shape[0], 1))  # 赤色にする
# Create a PointCloud object
point_cloud1 = o3d.geometry.PointCloud()
point_cloud1.points = o3d.utility.Vector3dVector(point_cloud_data1)
point_cloud1.colors = o3d.utility.Vector3dVector(colors1)


point_cloud_data2 = np.load(f'{dir_path_pc}{name2}.npy')
colors2 = np.tile([0, 0, 1], (point_cloud_data2.shape[0], 1))  # 赤色にする

# Create a PointCloud object
point_cloud2 = o3d.geometry.PointCloud()
point_cloud2.points = o3d.utility.Vector3dVector(point_cloud_data2)
point_cloud2.colors = o3d.utility.Vector3dVector(colors2)


# Setting visualization parameters
view_params = {
    "zoom": 2,
    "front": [0, 0, -1.0],
    "lookat": [0.0, 0.0, 0.0],
    "up": [0.0, 1.0, 0.0]
}


vis = o3d.visualization.Visualizer()
vis.create_window(width=1920, height=1080,visible=False)
vis.add_geometry(point_cloud1)
vis.add_geometry(point_cloud2)
vis.add_geometry(pc)

ctr = vis.get_view_control()
ctr.set_zoom(view_params["zoom"])
ctr.set_front(view_params["front"])
ctr.set_lookat(view_params["lookat"])
ctr.set_up(view_params["up"])
ctr.change_field_of_view(step=5)

vis.update_geometry(point_cloud1)
vis.update_geometry(point_cloud2)
vis.update_geometry(pc)



vis.poll_events()
vis.update_renderer()

vis.capture_screen_image(f'{dir_path_img}{name1}sem.png',do_render=True)
vis.destroy_window()

