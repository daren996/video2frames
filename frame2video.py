import cv2
import os

fps = 10  # adjust the speed of output video

fourcc = cv2.VideoWriter_fourcc(*'MJPG')
src_dir="./frames"
imgs_path = [os.path.join(src_dir, x) for x in os.listdir(
            src_dir) if x.endswith('.jpg')]
imgs_path.sort()

height, width, channels=cv2.imread(imgs_path[0]).shape

print(img)

videoWriter = cv2.VideoWriter('./videos/out.avi', fourcc, fps, (width, height))

for i in imgs_path:
    img = cv2.imread(i)
    videoWriter.write(img)
videoWriter.release()
