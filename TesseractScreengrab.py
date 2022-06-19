import cv2
import numpy as np
import pytesseract
from PIL import Image, ImageGrab , ImageOps


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

x = 548
y = 549
offx = 649
offy = 155

img = ImageGrab.grab(bbox=(x,y,x + offx , y+ offy))


img = ImageOps.invert(img)


img = np.array(img)

cv2.imshow('window',img)

text = pytesseract.image_to_string(img)

print(text)

if 'OVER' in text:
    print('yes')
else:
    print('no')

