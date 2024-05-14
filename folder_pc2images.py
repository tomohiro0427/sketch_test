import open3d as o3d
import numpy as np
import os
from tqdm import tqdm
import sys

'''
## 改良点##
1. yamlファイルでディレクトリや数を指定
2. front back right left side のカメラ指定
3. ズーム距離指定
'''

def main():
    args = sys.argv

    # デフォルトのディレクトリと画像数の設定
    dir_path_pc = './PC_dataset'
    dir_path_img = './images/test'
    max_num = 10

    # コマンドライン引数を処理
    if len(args) == 2:
        max_num = int(args[1])
    elif len(args) == 4:
        max_num = int(args[1])
        dir_path_pc = args[2]
        dir_path_img = args[3]
    else:
        print("Usage: python script.py <output images num> <directory_input> <directory_output>")

    # ディレクトリが存在するかを確認
    assert os.path.exists(dir_path_pc), f"The directory '{dir_path_pc}' does not exist."
    assert os.path.exists(dir_path_img), f"The directory '{dir_path_img}' does not exist."

    # .npy ファイルのリストを取得
    file_list = [f for f in os.listdir(dir_path_pc) if f.endswith('.npy')]
    file_list = file_list[:max_num] if max_num < len(file_list) else file_list

    # プログレスバーの設定
    with tqdm(file_list, desc=f"Output") as tqdmbar:
        for i, file_name in enumerate(tqdmbar):
            point_cloud_data = np.load(f'{dir_path_pc}/{file_name}')

            # PointCloud オブジェクトを作成
            point_cloud = o3d.geometry.PointCloud()
            point_cloud.points = o3d.utility.Vector3dVector(point_cloud_data)

            # カメラのビューパラメータ
            view_params = {
                "zoom": 1,
                "front": [0, 1.0, -1.0],
                "lookat": [0.0, 0.0, 0.0],
                "up": [0.0, 1.0, 0.0]
            }

            # Visualizer を作成し、ウィンドウを非表示で開く
            vis = o3d.visualization.Visualizer()
            vis.create_window(visible=False)
            vis.add_geometry(point_cloud)

            # カメラのビューパラメータを設定
            ctr = vis.get_view_control()
            ctr.set_zoom(view_params["zoom"])
            ctr.set_front(view_params["front"])
            ctr.set_lookat(view_params["lookat"])
            ctr.set_up(view_params["up"])
            ctr.change_field_of_view(step=5)

            # ジオメトリの更新とレンダラーの更新
            vis.update_geometry(point_cloud)
            vis.poll_events()
            vis.update_renderer()

            # 画像をキャプチャして保存し、ウィンドウを破棄
            vis.capture_screen_image(f'{dir_path_img}/{file_name.split(".")[0]}.png',do_render=True)
            vis.destroy_window()

            # 不要な変数を削除
            del ctr
            del vis

            # 進捗表示の更新
            tqdmbar.update(1)

if __name__== "__main__":
    main()
