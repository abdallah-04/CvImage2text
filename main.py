import cv2
import pytesseract
from dotenv import load_dotenv
import re
import os
load_dotenv()
pytesseract.pytesseract.tesseract_cmd = os.getenv("OCR_TH")
image = os.getenv("IMG_pATH") 
img = cv2.imread(image)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(gray, 9, 75, 75)
gray = cv2.adaptiveThreshold(gray, 255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,blockSize=11, C=2)
# cv2.imwrite("cleaned_image.jpg", gray)
text = pytesseract.image_to_string(gray, lang='eng')
ctext = text
ctext = re.sub(r'[^\x00-\x7F]+', ' ', ctext) 
ctext = re.sub(r'[\u2022•�+*]', '-', ctext)   
print(ctext)
output_path = "output.txt"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(ctext)