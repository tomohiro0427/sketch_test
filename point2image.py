import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt




# Loading point cloud data
name = 'pcd'
point_cloud_data = np.load(f'{name}.npy')

# Create a PointCloud object
point_cloud = o3d.geometry.PointCloud()
point_cloud.points = o3d.utility.Vector3dVector(point_cloud_data)

# Setting visualization parameters
view_params = {
    "zoom": 1.7,
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


vis.update_geometry(point_cloud)

vis.poll_events()
vis.update_renderer()

vis.capture_screen_image(f'{name}.png',do_render=True)
vis.destroy_window()

