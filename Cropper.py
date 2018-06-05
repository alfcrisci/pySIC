###############################################################
import os
import cv2
import math
###############################################################
C_percentage = 0
ACCEPTED_EXTENSIONS = (".jpeg", ".jpg", ".png", ".tif", ".tiff", ".bmp", ".dib", ".jpe", ".jp2", ".webp", ".pbm", ".pgm", ".ppm", ".sr", ".ras")
###############################################################
def euclidian_distance(first, second):
    return math.sqrt(sum([pow(max(x, y) - min(x, y), 2) for x, y in zip(first, second)]))
def color_difference(first, second, precision = 100):
    return euclidian_distance(first, second) > precision
def Crop(abs_folder_in, abs_folder_out, debug):
    global C_percentage
    images_list = [i for i in os.listdir(abs_folder_in) if i.endswith(ACCEPTED_EXTENSIONS) and i[:2] != "ad"]
    if debug: print("\n".join(images_list))
    images_list = sorted(images_list, key = lambda i: int(i[:-4]))
    for c, image_path in enumerate(images_list, 1):
        original_image = cv2.imread(abs_folder_in + "\\" + image_path)
        w, h, z = original_image.shape
        K = 500 / max(w, h)
        resized_image = cv2.resize(original_image, (0, 0), fx = K, fy = K)
        w, h, z = resized_image.shape
        mx, my = int(w / 2), int(h / 2)
        for i in range(1, w):
            if color_difference(resized_image[i, my], resized_image[i - 1, my]):
                startx = i
                break
        for i in range(w - 2, 0, -1):
            if color_difference(resized_image[i, my], resized_image[i + 1, my]):
                endx = i
                break
        for i in range(1, h):
            if color_difference(resized_image[mx, i], resized_image[mx, i - 1]):
                starty = i
                break
        for i in range(h - 2, 0, -1):
            if color_difference(resized_image[mx, i], resized_image[mx, i + 1]):
                endy = i
                break
        startx, starty, endx, endy = int(startx * (1 / K)), int(starty * (1 / K)), int(endx * (1 / K)), int(endy * (1 / K))
        jump = int(1 / K * 10)
        if debug:
            print("K : ", K, " jump : ", jump)
            print("(", startx, ", ", starty, ") -> (",  endx, ", ", endy, ")")
            print("Saving...")
        cv2.imwrite(abs_folder_out + "\\" + str(c) + ".jpg", original_image[startx + jump : endx - jump, starty + jump : endy - jump])
        if debug: print("Done ", c, " of ", len(images_list))
        C_percentage += 1 / len(images_list)
    C_percentage = 0
def get_percentage():
    global C_percentage
    return C_percentage
###############################################################
