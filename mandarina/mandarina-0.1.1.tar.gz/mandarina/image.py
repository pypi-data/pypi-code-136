"""
This module provides functionality to work with images
"""


def overlay(background_image, foreground_image, x_offset, y_offset):
    """
    Overlays a png image on another image.

    :param background_image: OpenCv image to be overlaid with foreground image
    :param foreground_image: OpenCv image to overlay
    :param x_offset: Position of the overlay in x direction
    :param y_offset: Position of the overlay in y direction
    :return: Image with overlay

    Example:
        s_img = cv2.imread("foreground.png", -1)
        l_img = cv2.imread("background.png")
        img = overlay(l_img, s_img, 50, 50)
        cv2.imshow("Overlay", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    """

    y1, y2 = y_offset, y_offset + foreground_image.shape[0]
    x1, x2 = x_offset, x_offset + foreground_image.shape[1]

    alpha_s = foreground_image[:, :, 3] / 255.0
    alpha_l = 1.0 - alpha_s

    for c in range(0, 3):
        background_image[y1:y2, x1:x2, c] = (
            alpha_s * foreground_image[:, :, c]
            + alpha_l * background_image[y1:y2, x1:x2, c]
        )

    return background_image
