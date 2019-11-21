import cv2

vc = cv2.VideoCapture('videos/tennis.mp4')
c = 0
rval = vc.isOpened()
while rval:
    c = c + 1
    rval, frame = vc.read()
    if rval:
        cv2.imwrite('frames/tennis_' + str(c).zfill(4) + '.jpg', frame)
        cv2.waitKey(1)
    else:
        break
