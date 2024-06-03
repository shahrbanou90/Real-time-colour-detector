# Real-time colour detector of the detected frame from webcam
## What does the project do?
Every image is represented by 3 colors that are Red, Green and Blue. In this project you will find the most prominent colour that is captured by the webcam using Python.

## What is the approach? 

1. Import the cv2 and NumPy modules
2. Capture the webcam video using the cv2.VideoCapture(0) method.
3. Display the current frame using the cv2.imshow() method.
4. Run a while loop and take the current frame using the read() method.
5. Take the red, blue and green elements and store them in a list.
6. Compute the average of each colour list.
7. Whichever average has the greatest value, print that color.
8. Run the code until you press 'q' or 'esc'. 
