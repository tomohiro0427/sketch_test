import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt




# Loading point cloud data
dir_path_pc = './point_cloud/'
dir_path_img = './images/pc_images/'
name = 'part2'
point_cloud_data = np.load(f'{dir_path_pc}{name}.npy')

# Create a PointCloud object
point_cloud = o3d.geometry.PointCloud()
point_cloud.points = o3d.utility.Vector3dVector(point_cloud_data)

# Setting visualization parameters
view_params = {
    "zoom": 1,
    "front": [0, 1.0, -1.0],
    "lookat": [0.0, 0.0, 0.0],
    "up": [0.0, 1.0, 0.0]
}


vis = o3d.visualization.Visualizer()
vis.create_window(visible=False)
vis.add_geometry(point_cloud)

ctr = vis.get_view_control()
ctr.set_zoom(view_params["zoom"])
ctr.set_front(view_params["front"])
ctr.set_lookat(view_params["lookat"])
ctr.set_up(view_params["up"])
# ctr.set_constant_z_near(1.5)
ctr.change_field_of_view(step=5)


vis.update_geometry(point_cloud)

vis.poll_events()
vis.update_renderer()

vis.capture_screen_image(f'{dir_path_img}{name}.png',do_render=True)
vis.destroy_window()

