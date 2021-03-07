# coding=utf-8
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import cv2
import os

def mirror(path):
    pic = cv2.imread(path, cv2.IMREAD_UNCHANGED)

    pic_type = ''
    if(pic.ndim == 3):
        pic_type = 'rgb'
    if pic.ndim == 2 and pic.dtype.name == 'uint8':
        pic_type = 'ir'
    if pic.ndim == 2 and pic.dtype.name == 'uint16':
        pic_type = 'depth'

    print(f"mirror {pic_type}: {path}...")
    pic_mirror = cv2.flip(pic, 1)
    cv2.imwrite(path, pic_mirror)

def all_hand(dir):
    for root, dirs, files in os.walk(dir):
        for file in files:
            mirror(str(root + '/' + file))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    all_hand('mirror/rgb')
    all_hand('mirror/ir')
    all_hand('mirror/depth')

