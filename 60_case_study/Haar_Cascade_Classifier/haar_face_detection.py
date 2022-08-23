import cv2

image_path = "medium_318eece991a391cf.jpg"
window_name = f"Detected Objects in {image_path}"
original_image = cv2.imread(image_path)

# Convert the image to grayscale for easier computation
image_grey = cv2.cvtColor(original_image, cv2.COLOR_RGB2GRAY)

# cascade_classifier = cv2.CascadeClassifier(
#     f"{cv2.data.haarcascades}haarcascade_eye.xml")
cascade_classifier = cv2.CascadeClassifier(
    f"{cv2.data.haarcascades}haarcascade_upperbody.xml")
detected_objects = cascade_classifier.detectMultiScale(image_grey, minSize=(150, 150))

# Draw rectangles on the detected objects
if len(detected_objects) != 0:
    for (x, y, width, height) in detected_objects:
        cv2.rectangle(original_image, (x, y),
                      (x + height, y + width),
                      (0, 255, 0), 2)

cv2.namedWindow(window_name, cv2.WINDOW_KEEPRATIO)
cv2.imshow(window_name, original_image)
# cv2.resizeWindow(window_name, 400, 400)
cv2.waitKey(0)
cv2.destroyAllWindows()