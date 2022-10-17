import pytesseract
import numpy as np
import cv2
 
#image rotation
def rotate_bound(image, angle):
    # Get number of pixel horizontally and vertically
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)
 
    # getRotationMatrix2D creates a matrix needed for transformation
    M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])
 
    #get the new width and height
    nW = int((h * sin) + (w * cos))
    #nH = int((h * cos) + (w * sin))
    nH = h
 
    # Chage the value of enter coordinates
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY
 
    return cv2.warpAffine(image, M, (nW, nH),flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
 
# finding the minimum area rotated recctangle
def get_minAreaRect(image):
    # Use the cvtColor() function to grayscale the image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.bitwise_not(gray)

    # applying thresholding techniques on the input image
    thresh = cv2.threshold(gray, 0, 255,
        cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    coords = np.column_stack(np.where(thresh > 0))
    return cv2.minAreaRect(coords)

def convert_angle(angle):
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle

    return angle

image_path = "./picture/fuzzy_text_image.png"
image = cv2.imread(image_path)
angle = get_minAreaRect(image)[-1]
angle = convert_angle(angle)
rotated = rotate_bound(image, angle)
 
cv2.putText(rotated, "angle: {:.2f} ".format(angle),
    (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

norm_img = np.zeros((image.shape[0], image.shape[1]))
img_norm = cv2.normalize(rotated, norm_img, 0, 255, cv2.NORM_MINMAX)
img_lamp = cv2.Laplacian(img_norm, cv2.CV_8U, ksize=5)

text1 = pytesseract.image_to_string(img_lamp)
print("The text1 is \n {}".format(text1))

# show the output image
#cv2.imshow("imput", image)
#cv2.imshow("output", rotated)

cv2.waitKey(0)
