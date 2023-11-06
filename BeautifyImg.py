# 把照片美化

import cv2
import numpy as np
from google.colab.patches import cv2_imshow

# 讀取圖片
image = cv2.imread('T29_FCLin.png')

# 調整亮度和對比度
alpha = 1.5  # 亮度增加因子
beta = 30    # 對比度增加因子
adjusted_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

# 高斯模糊
blurred_image = cv2.GaussianBlur(adjusted_image, (5, 5), 0)

# 中值濾波
median_filtered_image = cv2.medianBlur(blurred_image, 5)

# 銳化
sharpened_image = cv2.filter2D(median_filtered_image, -1, np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]]))

# 直方圖均衡化
gray_image = cv2.cvtColor(sharpened_image, cv2.COLOR_BGR2GRAY)
equalized_image = cv2.equalizeHist(gray_image)

# 合併到原始圖像
result_image = cv2.cvtColor(equalized_image, cv2.COLOR_GRAY2BGR)

# 保存美化後的圖片
cv2.imwrite('output.jpg', result_image)

# 顯示原始和美化後的圖片
cv2_imshow(image)
cv2_imshow(result_image)
