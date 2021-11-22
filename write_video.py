import cv2
import glob
import numpy as np

image_true_paths = [
    "testdata/gMH/restrueimages/*.png",
]

image_train_paths =[
    "testdata/gMH/resimages/*.png",
]

video_paths = [
    "videos/truevalidation_gMH_compare.mp4",
]

for i in range(0, 1):
    # print(image_paths[i])
    trueimages = sorted(glob.glob(image_true_paths[i]))
    trainimages = sorted(glob.glob(image_train_paths[i]))
    #(images)
    cap = cv2.VideoCapture()

    # Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
    out = cv2.VideoWriter(video_paths[i], cv2.VideoWriter_fourcc('m','p','4','v'), 60, (3840,1080))
    for j in range(len(trueimages)):
        trueimage=cv2.imread(trueimages[j])
        trainimage=cv2.imread(trainimages[j])
        frame=cv2.hconcat([trueimage,trainimage])
        # print(image)
        #frame = cv2.imread(image)
        # Write the frame into the file 'output.avi'
        out.write(frame)

    # When everything done, release the video capture and video write objects
    out.release()
