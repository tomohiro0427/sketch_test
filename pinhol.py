import numpy as np

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

# 結果の表示
print("連結された8つの角:", corners)