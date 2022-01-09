#!pip install imutils
#!pip install opencv-python 
import cv2
import imutils
import numpy as np

imgname = 'picture1'

final = cv2.imread("../static/images/test.jpg")

def card_to_objects():
    # just like before (with detecting the card)
    gray = cv2.cvtColor(final, cv2.COLOR_RGB2GRAY)
    thresh = cv2.threshold(gray, 195, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.bitwise_not(thresh)
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:10]# handle each contour
    i = 0
    for c in cnts:
        if cv2.contourArea(c) > 1000:
            # draw mask, keep contour
            mask = np.zeros(gray.shape, np.uint8)
            mask = cv2.drawContours(mask, [c], -1, 255, cv2.FILLED)        # white background
            fg_masked = cv2.bitwise_and(final, final, mask=mask)
            mask = cv2.bitwise_not(mask)
            bk = np.full(final.shape, 255, dtype=np.uint8)
            bk_masked = cv2.bitwise_and(bk, bk, mask=mask)
            finalcont = cv2.bitwise_or(fg_masked, bk_masked)        # bounding rectangle around contour
            output = finalcont.copy()
            x,y,w,h = cv2.boundingRect(c)
            # squares io rectangles
            if w < h:
                x += int((w-h)/2)
                w = h
            else:
                y += int((h-w)/2)
                h = w        # take out the square with the symbol
            roi = finalcont[y:y+h, x:x+w]
            roi = cv2.resize(roi, (400,400))        # save the symbol
            cv2.imwrite(f"{imgname}_icon{i}.jpg", roi)
            i += 1
        
card_to_objects()