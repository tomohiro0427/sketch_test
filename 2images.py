import cv2
import numpy as np

# 2つの画像を読み込む
image1 = cv2.imread("./images/sketch/canny_part1.png")
image2 = cv2.imread("./images/sketch/canny_part2.png")
image3 = cv2.imread("./images/sketch/canny_part2_all.png")

# 画像のサイズを揃える（必要に応じて）
# image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))


image1 = cv2.bitwise_not(image1)
image2 = cv2.bitwise_not(image2)
image3 = cv2.bitwise_not(image3)

# 2つの画像のビットごとのAND演算を実行
result = cv2.bitwise_and(image1, image3)
result = cv2.bitwise_not(result)

# 結果を保存する（任意）
cv2.imwrite("./images/sketch/and_result.png", result)


result = cv2.absdiff(image3, image1)
result = cv2.bitwise_not(result)
cv2.imwrite("./images/sketch/sub_result.png", result)