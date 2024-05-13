import open3d as o3d
import numpy as np

# 例としてランダムな点群とランダムな色情報を生成する関数を定義
def create_random_point_cloud_with_color(num_points):
    points = np.random.rand(num_points, 3)  # 100個のランダムな点を生成
    colors = np.random.rand(num_points, 4)  # RGBA色空間のランダムな色情報を生成
    return points, colors

def main():
    num_points = 100  # 点の数

    # ランダムな点群とランダムな色情報を生成
    points, colors = create_random_point_cloud_with_color(num_points)

    # Open3DのVector4dVectorを使用してRGBA色情報を持つ点群を作成
    point_cloud = o3d.geometry.PointCloud()
    point_cloud.points = o3d.utility.Vector3dVector(points)  # 点の座標を設定
    point_cloud.colors = o3d.utility.Vector4dVector(colors)  # RGBA色情報を設定

    # 3D表示ウィンドウの設定
    vis = o3d.visualization.Visualizer()
    vis.create_window()

    # 3D表示ウィンドウに点群を追加
    vis.add_geometry(point_cloud)

    # 3D表示ウィンドウを更新
    vis.run()
    vis.destroy_window()

if __name__ == "__main__":
    main()
