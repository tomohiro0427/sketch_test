import cv2

input_image = 'pcd.png'
output_filename =  'canny_'+input_image

# 画像を読み込む
img = cv2.imread(input_image, 0)

# Cannyエッジ検出を適用
edges = cv2.Canny(img, 100, 200)

edges = cv2.bitwise_not(edges)


# 結果を表示
# cv2.imshow('Canny Edge Detection', edges)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 保存
cv2.imwrite(output_filename, edges)
