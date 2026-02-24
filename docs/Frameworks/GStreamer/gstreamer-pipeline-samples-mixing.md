# Mixing

## Mixing videos

```sh
# display
gst-launch-1.0 -e compositor name=comp sink_0::alpha=0.7 sink_1::alpha=0.5 \
    ! autovideosink \
    videotestsrc \
        ! video/x-raw, framerate=10/1, width=640, height=360 \
        ! comp.sink_0 \
    videotestsrc pattern="snow" \
        ! video/x-raw, framerate=10/1, width=200, height=150 \
        ! comp.sink_1
```

video + rtp/udp,

```sh
# sender
gst-launch-1.0 -e compositor name=comp sink_0::alpha=0.7 sink_1::alpha=0.5 \
    ! videoconvert ! omxh264enc insert-sps-pps=true bitrate=16000000 ! h264parse ! rtph264pay ! udpsink port=5000 host=$HOST \
    videotestsrc \
        ! video/x-raw, framerate=10/1, width=640, height=360 \
        ! comp.sink_0 \
    videotestsrc pattern="snow" \
        ! video/x-raw, framerate=10/1, width=200, height=150 \
        ! comp.sink_1
```

receiver

## Mixing video+audio

sender(mpegts + rtp/udp),

```sh
# sender(videotestsrc/audiotestsrc)
gst-launch-1.0 -v \
    mpegtsmux name=mux alignment=7 ! rtpmp2tpay \
    ! udpsink port=5000 host=$HOST sync=false \
    compositor name=videomix ! x264enc ! queue ! mux. \
    audiomixer name=audiomix ! audioconvert ! audioresample ! avenc_ac3 ! queue ! mux. \
    videotestsrc pattern=ball ! videomix. \
    videotestsrc pattern=pinwheel ! videoscale ! video/x-raw,width=100 ! videomix. \
    audiotestsrc freq=400 ! audiomix. \
    audiotestsrc freq=600 ! audiomix.

# sender(mp4 file)
SRC=/home/jetson/Videos/why_I_left_China_for_Good.mp4
gst-launch-1.0 -v \
    mpegtsmux name=mux alignment=7 ! rtpmp2tpay \
    ! udpsink port=5000 host=$HOST sync=false \
    compositor name=videomix ! omxh264enc bitrate=16000000 ! queue2 ! mux. \
    audiomixer name=audiomix ! audioconvert ! audioresample ! avenc_ac3 ! queue2 ! mux. \
    filesrc location=$SRC ! qtdemux name=demux \
    demux.video_0 ! queue2 ! h264parse ! omxh264dec ! videoconvert ! videomix. \
    demux.audio_0 ! queue2 ! decodebin ! audioconvert ! audioresample ! audiomix. \
    videotestsrc pattern=ball ! videoscale ! video/x-raw,width=100,height=100 ! videomix. \
    audiotestsrc freq=600 volume=0.1 ! audiomix.

# sender(mp4 file) `uridecodebin`
gst-launch-1.0 \
    mpegtsmux name=mux ! rtpmp2tpay \
    ! udpsink port=5000 host=$HOST sync=false \
    compositor name=videomix ! x264enc ! queue2 ! mux. \
    audiomixer name=audiomix ! audioconvert ! audioresample ! avenc_ac3 ! queue2 ! mux. \
    uridecodebin uri=file://$SRC name=dec \
    dec. ! queue2 ! audioconvert ! audioresample ! audiomix. \
    dec. ! queue2 ! nvvidconv ! videoconvert ! video/x-raw,width=640,height=360 ! videomix. \
    videotestsrc pattern=ball ! video/x-raw,width=100,height=100 ! videomix. \
    audiotestsrc freq=400 volume=0.2 ! audiomix.
```

tcp server,

```sh
# View this in VLC with tcp://localhost:7001
gst-launch-1.0 \
    mpegtsmux name=mux ! rtpmp2tpay ! \
    tcpserversink port=7001 host=0.0.0.0 recover-policy=keyframe sync-method=latest-keyframe sync=false \
    compositor name=videomix ! x264enc ! queue2 ! mux. \
    audiomixer name=audiomix ! audioconvert ! audioresample ! avenc_ac3 ! queue2 ! mux. \
    uridecodebin uri=file://$SRC name=demux ! \
    queue2 ! audioconvert ! audioresample ! audiomix. \
    demux. ! queue2 ! decodebin ! nvvidconv ! videoconvert ! videoscale ! video/x-raw,width=640,height=360 ! videomix. \
    videotestsrc pattern=ball ! videoscale ! video/x-raw,width=100,height=100 ! videomix. \
    audiotestsrc freq=400 volume=0.2 ! audiomix.
```

> **tips**
> for jetson nano, use `nvvidconv` instead of `videoconvert` because `decodebin` use `nvv4l2decoder` to decode H.264 in default. Otherwise, explictly decode H.264 with `omxh264dec`.

receiver,

```sh
# receiver
[mpegts receiver](#mpegts-receiver)
gst-launch-1.0 -v udpsrc port=5000 caps="application/x-rtp" \
  ! rtpmp2tdepay ! tsparse ! tsdemux name=demux \
  demux. ! queue ! decodebin ! videoconvert ! fpsdisplaysink text-overlay=false sync=false \
  demux. ! queue leaky=1 ! decodebin ! audioconvert ! autoaudiosink sync=false
```
