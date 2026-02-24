# python-opencv

```py
import cv2
import time
# capture

# videotestsrc
gst_str = 'videotestsrc ! video/x-raw,framerate=20/1 ! videoscale ! videoconvert ! appsink'

# udpsrc
gst_str = 'udpsrc port=5000 ! "application/x-rtp, media=(string)video, clock-rate=(int)90000, encoding-name=(string)H264, payload=(int)96" ! rtph264depay ! h264parse ! decodebin ! videoconvert ! autovideosink'

gst_str = 'udpsrc port=5000 caps = "application/x-rtp, media=(string)video, clock-rate=(int)90000, encoding-name=(string)H264, payload=(int)96" ! rtph264depay ! decodebin ! videoconvert ! appsink'

cap = cv2.VideoCapture(gst_str, cv2.CAP_GSTREAMER)

cap.isOpened()
ret, frame = cap.read()
cv2.imwrite("result.jpg", frame)
cap.release()

# write

# udpsink
gst_str = 'appsrc ! videoconvert ! x264enc tune=zerolatency bitrate=500 speed-preset=superfast ! rtph264pay ! udpsink host=127.0.0.1 port=5000'

fps = 30
frame_width = 640
frame_height = 480
out = cv2.VideoWriter(gst_str, cv2.CAP_GSTREAMER, 0, fps, (frame_width, frame_height), True)
out.isOpened()

img = cv2.imread('WechatIMG1.jpeg')
img.shape
img = cv2.resize(img, (frame_width, frame_height))
img.shape
cv2.imwrite("result.jpg", img)
while True:
    out.write(img)
    time.sleep(1/60)

out.release()
```

[convert gstreamer pipeline to opencv in python](https://stackoverflow.com/questions/51539706/convert-gstreamer-pipeline-to-opencv-in-python)  
[python-opencv-gstreamer-examples](https://github.com/madams1337/python-opencv-gstreamer-examples)