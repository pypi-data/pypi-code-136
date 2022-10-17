import cv2


def entering_face(path, name):
    cap = cv2.VideoCapture(0)
    num = 1
    while (cap.isOpened()):
        ret_flag, Vshow = cap.read()
        cv2.imshow("Capture_Test", Vshow)
        k = cv2.waitKey(1) & 0xFF
        if k == ord('s'):
            cv2.imwrite(path + str(num) + "." + name + ".jpg", Vshow)
            num += 1
        elif k == ord(' '):
            break

    cap.release()
    cv2.destroyAllWindows()
