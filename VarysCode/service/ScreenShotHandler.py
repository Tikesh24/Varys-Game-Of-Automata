import os

import cv2
import mss
import mss.tools
import numpy as np
from PIL import Image

count = 0

# Var for screen shot selection
myKey = ''
xm, ym = 0, 0
mousePoints = []
cleanScreen = False
drawing = False
writer = None
x1, y1, x2, y2 = 0, 0, 0, 0
drawing = False
img2: any = ''
img: any = ''
num = 0


# ------------------------------------- Screen Shot with area selection---------------------------------

def main():
    global myKey
    global xm, ym
    global rectDone
    global x1, y1, x2, y2
    global img, img2
    global count
    with mss.mss() as sct:
        sct.shot()
    img = cv2.imread('monitor-1.png')  # reading image
    img2 = img.copy()
    cv2.namedWindow("main", cv2.WINDOW_NORMAL)
    cv2.setMouseCallback("main", draw_rect)
    cv2.setWindowProperty("main", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    num = 0
    key = ord('a')
    # PRESS w to confirm save selected bounded box
    while key != ord('w'):
        cv2.imshow("main", img)
        key = cv2.waitKey(1) & 0xFF
    print('Here are points:', x1, y1, x2, y2)
    if key == ord('w'):
        print(img2[y1:y2, x1:x2])
        cv2.imwrite("app_data/validataion/{0}.png".format(count), img2[y1:y2, x1:x2])
        # convert_to_npy(count)
        count += 1
        cv2.destroyAllWindows()
        print('Saved as snap.png')
        os.remove('monitor-1.png')


def draw_rect(event, x, y, flags, param):
    global x1, y1, drawing, num, img, img2, x2, y2
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        x1, y1 = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            a, b = x, y
            if a != x & b != y:
                img = img2.copy()

                cv2.rectangle(img, (x1, y1), (x, y), (0, 255, 0), 2)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        num += 1

        font = cv2.FONT_HERSHEY_SIMPLEX
        x2 = x
        y2 = y


if __name__ == "__main__":
    main()


def convert_to_npy(seq: any):
    im = Image.open('app_data/validataion/temp{0}.png'.format(seq))
    np.save('app_data/validataion/validate{0}'.format(seq), im)
# -------------------------------------- Screen shot with area selection ---------------------
