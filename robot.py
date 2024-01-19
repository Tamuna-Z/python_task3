import cv2
import os

# Show image captured by camera, True to turn on, you will need #DISPLAY and it also slows the speed of tracking
show_image_enable   = False
draw_circle_enable  = False
scan_enable         = False
rear_wheels_enable  = True
front_wheels_enable = True
pan_tilt_enable     = True

if (show_image_enable or draw_circle_enable) and "DISPLAY" not in os.environ:
    print('Warning: Display not found, turn off "show_image_enable" and "draw_circle_enable"')
    show_image_enable   = False
    draw_circle_enable  = False

# Setup video feed
img = cv2.VideoCapture(-1) # -1 for random camera
SCREEN_WIDTH = 160 # width in pixels
SCREEN_HIGHT = 120 # height in pixels
img.set(3,SCREEN_WIDTH)
img.set(4,SCREEN_HIGHT)

while(True):
    ret, frame = img.read() # Capture frame-by-frame

    # Q1: Why are we cropping the image?
    # Crop image
    crop_img = frame[60:120, 0:160]

    # Now we need to process the image we have captured.
    gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY) # Convert to grayscale
    blur = cv2.GaussianBlur(gray,(5,5),0) # Gaussian blur
    # Color thresholding
    ret,thresh = cv2.threshold(blur,60,255,cv2.THRESH_BINARY_INV)
    # Q2: What are we doing in each of these three image processing steps?

    # Find the contours of the frame
    contours,hierarchy = cv2.findContours(thresh.copy(), 1, cv2.CHAIN_APPROX_NONE)
    # Q3: Why do we input a copy of the thresholded image in findContours?

    # Q4: What is this if statement condition checking for?
    if len(contours) > 0:
        c = max(contours, key=cv2.contourArea)
        # Q5: What is the previous line using the max function for?
        M = cv2.moments(c) # Find the moments of the largest contour

        # Q6: What are these two lines doing?
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])

        # Draw the lines and contours
        cv2.line(crop_img,(cx,0),(cx,720),(255,0,0),1)
        cv2.line(crop_img,(0,cy),(1280,cy),(255,0,0),1)
        cv2.drawContours(crop_img, contours, -1, (0,255,0), 1)

        # Robot determines which way to turn
        if cx >= 120:
            print("Left")
        if cx < 120 and cx > 50:
            print("Center")
        if cx <= 50:
            print("Right")
        # Q7: How is the robot determining which way to move?

    # If there are no contours, print that the robot doesn't see the line
    else:
        print("No line")

    # Display the resulting frame
    cv2.imshow('frame',crop_img)

    # Show images
    if show_image_enable:
        cv2.namedWindow("Detected contours on the input image", cv2.WINDOW_AUTOSIZE)
        cv2.imshow("Detected contours on the input image", frame)

    # Q8: What does this if statement do?
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break