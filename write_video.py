import cv2
import glob
import numpy as np

image_paths = [
    "smplparameter2mesh/images/test_3_*.png",
]
video_paths = [
    "videos/test_3.mp4",
]

for i in range(0, 1):
    # print(image_paths[i])
    images = sorted(glob.glob(image_paths[i]))
    print(images)
    cap = cv2.VideoCapture()

    # Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
    out = cv2.VideoWriter(video_paths[i], cv2.VideoWriter_fourcc('m','p','4','v'), 60, (1920,1080))

    for image in images:
        # print(image)
        frame = cv2.imread(image)
        # Write the frame into the file 'output.avi'
        out.write(frame)

    # When everything done, release the video capture and video write objects
    out.release()
