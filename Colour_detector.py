# Import required libraries 

import cv2
import numpy as np

# taking the input from webcam
vid = cv2.VideoCapture(0)

# running while loop just to make sure that our code keeps running until we stop it 

while True:

    # Capturing teh current frame 

    _, frame = vid.read()

    # displayng the current frame 

    cv2.imshow("frame", frame )


    # setting values for base colors
    b = frame[:, :, :1]
    g = frame[:, :, 1:2]
    r = frame[:, :, 2:]

    # computing the mean
    b_mean = np.mean(b)
    g_mean = np.mean(g)
    r_mean = np.mean(r)

    # Displaying the most prominent color
    if (b_mean > g_mean and b_mean > r_mean):
        print("Blue")
    if (g_mean > b_mean and g_mean > r_mean):
        print("Green")
    else:
        print("Red")


    # exit when 'esc' or 'q' is pressed
    k = cv2.waitKey(10)
    if k == 113 or k == 27:
        break