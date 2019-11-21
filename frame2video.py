import cv2

fps = 10  # adjust the speed of output video

fourcc = cv2.VideoWriter_fourcc(*'MJPG')
videoWriter = cv2.VideoWriter('./videos/out.avi', fourcc, fps, (640, 480))

for i in range(1, 251):
    img = cv2.imread('./frames/tennis_%04d.jpg' % i)
    videoWriter.write(img)
videoWriter.release()
