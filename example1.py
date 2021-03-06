#!/usr/bin/env python
# -*- coding: utf-8 -*-
import idscamera
import time
import cv2
import numpy as np

if __name__ == '__main__':

    cam1 = idscamera.IDSCamera(1)
    cam1.set_auto_param()
    cam1.start_capture()

    cv2.namedWindow("frame1", cv2.WINDOW_NORMAL)

    i = 0
    while True:
        t0 = time.time()
        img1 = cam1.next()

        if len(img1) > 0:
            cv2.imshow("frame1", img1)
            #cv2.imwrite("cam1_%03d.jpg" % i, img1)

        print("%.2f %.2f fps" % (1.0 / (time.time()-t0), cam1.fps()))
        i += 1

        if cv2.waitKey(1) == 27:
            break
