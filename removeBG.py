# 照片去背
# 只能在 colab 上執行

from rembg import remove
from PIL import Image
import cv2
from google.colab.patches import cv2_imshow

input_path = 'T29_FCLin.png'
output_path = 'output.png'
input = Image.open(input_path)
output = remove(input)
output.save(output_path)

img = cv2.imread('output.png')
cv2_imshow(img)
