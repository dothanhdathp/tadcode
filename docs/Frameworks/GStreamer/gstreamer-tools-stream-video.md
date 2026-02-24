# Stream Video bằng Tools

## Video Test

### Linux

```bash
gst-launch-1.0 videotestsrc is-live=true ! videoconvert ! x264enc tune=zerolatency speed-preset=ultrafast ! rtph264pay ! udpsink host=192.168.100.96 port=5000
```

## Mp4

### Sender

```bash
gst-launch-1.0 filesrc location=example.mp4 ! decodebin name=demux \
demux. ! queue ! videoconvert ! x264enc tune=zerolatency speed-preset=ultrafast ! h264parse ! rtph264pay config-interval=1 pt=96 ! multiudpsink clients=192.168.100.96:5000 \
demux. ! queue ! audioconvert ! opusenc ! rtpopuspay pt=97 ! multiudpsink clients=192.168.100.96:5001
```

### Receiver

```bash
gst-launch-1.0 udpsrc port=5000 ! "application/x-rtp, media=(string)video, payload=(int)96, clock-rate=(int)90000, encoding-name=(string)H264" ! rtph264depay ! decodebin ! autovideosink
```

```bash
gst-launch-1.0 udpsrc port=5001 ! "application/x-rtp, media=(string)audio, payload=(int)97, clock-rate=(int)48000, encoding-name=(string)OPUS" ! rtpopusdepay ! decodebin ! audioconvert ! autoaudiosink
```

!!! danger "Danger"
    Cái lệnh này mình không chạy được trên máy tính của mình (__SER9__) vì thư viện chăng?

    Cái của nợ này thật sự khó vãi!