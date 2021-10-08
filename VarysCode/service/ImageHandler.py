import cv2
import numpy as np
import pyautogui

count = 0

def get_screenshot(coordinates):
    print(coordinates)
    if len(coordinates) != 0:
        im = pyautogui.screenshot(region=(coordinates[0], coordinates[1], coordinates[2], coordinates[3]))
        global count
        im.save("app_data/validataion/temp{0}.png".format(count))
        count += 1
        print(count)
        return im
    else:
        im = pyautogui.screenshot()
        im.save("app_data/validataion/parent.png")
        return im


def is_image_valid(open_cv_image):
    method = cv2.TM_SQDIFF_NORMED
    # Read the images from the file

    open_cv_image_small = open_cv_image[:, :, ::-1].copy()

    open_cv_image_large = np.array(get_screenshot([]))
    open_cv_image_large = open_cv_image_large[:, :, ::-1].copy()

    small_image = open_cv_image_small
    large_image = open_cv_image_large

    result = cv2.matchTemplate(small_image, large_image, method)

    # We want the minimum squared difference
    mn, _, mnLoc, _ = cv2.minMaxLoc(result)
    print(mnLoc)
    if mnLoc[0] == 0 and mnLoc[1] == 0:
        print("Image Not found.")
        return False
    else:
        return True

def is_valid_image_2(seq: any):
    get_screenshot([])
    img_rgb = cv2.imread('app_data/validataion/parent.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('app_data/validataion/{0}.png'.format(seq), 0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    isValid = False
    for pt in zip(*loc[::-1]):
        isValid = True
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
    cv2.imwrite('res.png', img_rgb)
    print(isValid)
    return isValid
