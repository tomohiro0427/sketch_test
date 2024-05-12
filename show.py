import open3d as o3d
import numpy as np


point_cloud_data = np.load('part1.npy')
print(point_cloud_data.shape)

# Setting visualization parameters
view_params = {
    "zoom": 1.7,
    "front": [0, 1.0, -1.0],#視線の方向を示すベクトル
    "lookat": [0.0, 0.0, 0.0],#点が向いている場所を示す点の座標
    "up": [0.0, 1.0, 0.0]#画面上での上方向を示すベクトル
}

point_cloud = o3d.geometry.PointCloud()
point_cloud.points = o3d.utility.Vector3dVector(point_cloud_data)

# # Rendering the point cloud
# o3d.visualization.draw_geometries([point_cloud])
o3d.visualization.draw_geometries([point_cloud], **view_params)