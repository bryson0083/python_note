import cv2 as cv
import pytesseract

gray = cv.imread('CAPTCHA_SMP_1.jpg', 0)
# cv.Threshold(gray, gray, 231, 255, cv.CV_THRESH_BINARY)
api = pytesseract.TessBaseAPI()
api.Init(".", "eng", pytesseract.OEM_DEFAULT)
api.SetVariable("tessedit_char_whitelist",
                "0123456789abcdefghijklmnopqrstuvwxyz")
api.SetPageSegMode(pytesseract.PSM_SINGLE_WORD)
pytesseract.SetCvImage(gray, api)
print(api.GetUTF8Text())
