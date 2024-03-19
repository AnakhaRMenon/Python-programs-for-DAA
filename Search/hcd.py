#PART1: IMPORT IMAGE AND LIBRARIES
import pandas as pd
import cv2
import numpy as np

def Harris_Corner_Detection(image):
    img = cv2.imread(image)


#PART2: SHOWING ORIGINAL IMG AND GIVING GRAY SCALE TO THE IMAGE

    #Displays Original Image for Debug Purposes
    cv2.imshow('Original Image', img)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)

#PART3: DETECTING CORNER
    dst = cv2.cornerHarris(gray, 5, 3, 0.04)
    ret, dst = cv2.threshold(dst, 0.1 * dst.max(), 255, 0)

    dst = np.uint8(dst)
    ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
    corners = cv2.cornerSubPix(gray, np.float32(centroids), (5, 5), (-1, -1), criteria)


#PART4: FINDING NEXT CORNER->
# LOOPING THROUGH EACH CORNER AND DENOTING THEM WITH A COLORED POINT
    for i in range(1, len(corners)):
        print(corners[i])

    img[dst > 0.1 * dst.max()] = [0, 0, 255]

    # A for loop that rounds up the
    for i in corners :
        i[0] = np.round(i[0])
        i[1] = np.round(i[1])

    df = pd.DataFrame( data = corners, columns=["x","y"])

#PART5: DISPLAY THE FINAL OUTPUT
    cv2.imshow("Modified Image", dst)
    # Disable wait key to allow
    cv2.waitKey()

    print(df)
    return df

if __name__ == "__main__":
    Harris_Corner_Detection("Search/sample1.jpg")
    print("executed")