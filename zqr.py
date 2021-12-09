import qrcode
from PIL import Image
import numpy as np
import time
#import cv2

def proc(url,logo,filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_Q,
        box_size=10,
        border=4
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image()
    a = np.asarray(img)

    h = len(a)
    w = len(a[0])
    aa = np.zeros((h,w,3),dtype=np.uint8)

    for row in range(0,h):
        for dot in range(0,w):
            if(a[row][dot] == True):
                aa[row][dot] = [255,255,255]
            else:
                aa[row][dot] = [0,0,0]

    dh = round(h/5)
    dw = round(w/5)
    ddh = round(h/2 - dh/2)
    ddw = round(w/2 - dw/2)
    print(h,w,dh,dw,ddh,ddw)
    logoSmall = logo.resize((dw, dh))
    b = np.asarray(logoSmall)
    aa[ddw:ddw+dw,ddh:ddh+dh] = b
    img = Image.fromarray(aa)

    with open(filename, 'wb') as f:
        img.save(f)
#logo = Image.open("lweiID2.jpg")
#proc("http://baidu.com",logo)
