# Fallbacksrc

```sh
gst-launch-1.0 fallbacksrc uri=http://192.168.2.24:8080/live.ts \
    fallback-uri=file:///tmp/black_frame.png restart-on-eos=True ! \
    tsdemux name=demux \
    demux. ! queue ! h264parse! flvmux name=mux ! rtmpsink location="rtmp://192.168.2.24/live/camera2" \
    demux. ! queue ! aacparse ! mux.

gst-launch-1.0 fallbacksrc uri=http://192.168.2.24:8080/live.ts \
    fallback-uri=file:///tmp/black_frame.png restart-on-eos=True ! \
    videoconvert ! autovideosink

gst-launch-1.0 fallbacksrc uri=http://192.168.2.24:8080/live.ts \
    fallback-uri=file:///tmp/black_frame.png restart-on-eos=True ! \
    decodebin ! audioconvert ! autoaudiosink

gst-launch-1.0 fallbacksrc uri=http://192.168.2.24:8080/live.ts \
    fallback-uri=file:///tmp/black_frame.png restart-on-eos=True name=d \
    d.video ! queue ! videoconvert ! autovideosink \
    d.audio ! queue ! audioconvert ! autoaudiosink

gst-launch-1.0 fallbacksrc uri=http://192.168.2.24:8080/live.ts \
    fallback-uri=file:///tmp/black_frame.png restart-on-eos=True name=d \
    d.video ! queue ! videoconvert ! x264enc ! flvmux name=mux ! rtmpsink location="rtmp://192.168.2.24/live/camera2" \
    d.audio ! queue ! audioconvert ! faac ! mux.
```