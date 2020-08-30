# F:\Tesseract-OCR\tesseract.exe
import pytesseract
import cv2
pytesseract.pytesseract.tesseract_cmd="F:\\Tesseract-OCR\\tesseract.exe"
def text_detector(img):
    img=cv2.imread(img)
    text=pytesseract.image_to_string(img)
    print(text)
    cv2.imshow("Image",img)
    cv2.waitKey(0)

text_detector("textdetectionimage.jpg")