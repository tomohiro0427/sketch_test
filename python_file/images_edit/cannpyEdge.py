import cv2

dir_path_input = './images/pc_images/'
dir_path_output = './images/sketch/'

input_image = 'part1.png'
output_filename =  'canny_'+input_image

# 画像を読み込む
img = cv2.imread(dir_path_input+input_image, 0)

# Cannyエッジ検出を適用
edges = cv2.Canny(img, 100, 200)
edges = cv2.bitwise_not(edges)



output_dir = dir_path_output+output_filename
# 保存
cv2.imwrite(output_dir, edges)
