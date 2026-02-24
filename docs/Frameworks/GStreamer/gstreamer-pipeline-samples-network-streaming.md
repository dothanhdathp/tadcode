# Network streaming

HOST=192.168.31.175 [//]: # (destination receiving the stream)

## Video RTP Streaming

- sender

### send a test video with h264 rtp stream

```sh
gst-launch-1.0 -v videotestsrc ! x264enc tune=zerolatency bitrate=500 speed-preset=superfast ! rtph264pay ! udpsink port=5000 host=$HOST

gst-launch-1.0 -v videotestsrc pattern=snow ! "video/x-raw,format=I420,width=1920,height=1080,framerate=60/1" ! x264enc tune=zerolatency bitrate=500 speed-preset=superfast ! rtph264pay ! udpsink port=5000 host=$HOST

# grayscale
gst-launch-1.0 -v videotestsrc ! videobalance saturation=0 ! x264enc ! video/x-h264, stream-format=byte-stream ! rtph264pay ! udpsink host=$HOST port=5000

# control fps
gst-launch-1.0 -v videotestsrc ! videorate ! "video/x-raw,framerate=60/1" ! x264enc tune=zerolatency bitrate=16000000 speed-preset=superfast ! h264parse ! rtph264pay pt=96 ! udpsink port=5000 host=$HOST

gst-launch-1.0 -v videotestsrc ! videorate ! "video/x-raw,framerate=60/1" ! omxh264enc insert-sps-pps=true bitrate=16000000 ! h264parse ! rtph264pay pt=96 ! udpsink port=5000 host=$HOST

gst-launch-1.0 -v videotestsrc ! videorate ! "video/x-raw,width=1280,height=720,framerate=60/1" ! omxh264enc insert-sps-pps=true bitrate=16000000 ! h264parse ! rtph264pay pt=96 ! udpsink port=5000 host=$HOST

```

### send a screen capture with h264 rtp stream(linux)

```sh
gst-launch-1.0 -v ximagesrc ! video/x-raw,framerate=20/1 ! videoscale ! videoconvert ! x264enc tune=zerolatency bitrate=500 speed-preset=superfast ! rtph264pay ! udpsink host=127.0.0.1 port=5000
```

### send a screen capture with h264 rtp stream(osx)

```sh
gst-launch-1.0 -v avfvideosrc capture-screen=true ! video/x-raw,framerate=20/1 ! videoscale ! videoconvert ! x264enc tune=zerolatency bitrate=500 speed-preset=superfast ! rtph264pay ! udpsink host=127.0.0.1 port=5000
```

### send a `*.mp4` file with h264 rtp stream

```sh
gst-launch-1.0 -v filesrc location=test.mp4 ! qtdemux ! h264parse ! omxh264dec ! x264enc ! rtph264pay ! udpsink host=$HOST port=5000

gst-launch-1.0 -v filesrc location=test.mp4 ! qtdemux ! h264parse ! omxh264dec ! omxh264enc insert-sps-pps=true ! rtph264pay ! udpsink host=$HOST port=5000

gst-launch-1.0 -v filesrc location=test.mp4 ! qtdemux ! h264parse ! rtph264pay ! udpsink host=$HOST port=5000
```

### send a webcam with h264 rtp stream(jetson nano)

```sh
!!slow
gst-launch-1.0 nvarguscamerasrc ! 'video/x-raw(memory:NVMM),width=1280, height=720, framerate=60/1, format=NV12' ! nvvidconv ! x264enc bitrate=16000000 speed-preset=superfast ! rtph264pay ! udpsink port=5000 host=$HOST

!!fast
gst-launch-1.0 nvarguscamerasrc ! 'video/x-raw(memory:NVMM),width=1920, height=1080, framerate=30/1, format=NV12' ! nvvidconv flip-method=2 ! nvv4l2h264enc insert-sps-pps=true bitrate=16000000 ! rtph264pay ! udpsink port=5000 host=$HOST

gst-launch-1.0 nvarguscamerasrc ! 'video/x-raw(memory:NVMM),width=1920, height=1080, framerate=30/1, format=NV12' ! omxh264enc insert-sps-pps=true bitrate=16000000 ! rtph264pay ! udpsink port=5000 host=$HOST

# avoid receiver using sync=false

```

### send a webcam with h264 rtp stream while record (jetson nano)

```sh
gst-launch-1.0 nvarguscamerasrc sensor-id=0 ! 'video/x-raw(memory:NVMM),width=1920, height=1080, framerate=30/1, format=NV12' ! nvvidconv flip-method=2 ! omxh264enc insert-sps-pps=true bitrate=16000000 \
    ! tee name=t \
    t. ! queue ! rtph264pay ! udpsink port=5000 host=$OSX_HOST \
    t. ! queue ! qtmux ! filesink location=test.mp4 -e
```

- receiver

### receive h264 rtp stream(desktop host)

```sh
# display
gst-launch-1.0 -v udpsrc port=5000 ! "application/x-rtp, media=(string)video, clock-rate=(int)90000, encoding-name=(string)H264, payload=(int)96" ! rtph264depay ! h264parse ! decodebin ! videoconvert ! autovideosink sync=false

gst-launch-1.0 -v udpsrc port=5000 ! "application/x-rtp, media=(string)video, clock-rate=(int)90000, encoding-name=(string)H264, payload=(int)96" ! rtph264depay ! h264parse ! avdec_h264 ! videoconvert ! autovideosink

# fps
gst-launch-1.0 -v udpsrc port=5000 ! "application/x-rtp, media=(string)video, clock-rate=(int)90000, encoding-name=(string)H264, payload=(int)96" ! rtph264depay ! h264parse ! decodebin ! videoconvert ! fpsdisplaysink text-overlay=false sync=false

# record and display
gst-launch-1.0 -v udpsrc port=5000 ! "application/x-rtp, media=(string)video, clock-rate=(int)90000, encoding-name=(string)H264, payload=(int)96" \
! rtph264depay ! h264parse \
! tee name=t \
t. ! queue ! mp4mux ! filesink location=xyz.mp4 -e \
t. ! queue leaky=1 ! decodebin ! videoconvert ! autovideosink sync=false

```

> **tips**:
>
> 1. `sync=false`: remove dropped frame rate, lag and error message(`There may be a timestamping problem, or this computer is too slow`). see the [Streaming RTP/RTSP: sync/timestamp problems](https://stackoverflow.com/questions/11397655/streaming-rtp-rtsp-sync-timestamp-problems) for details.
> 2. `udpsrc port=5000 cap='application/x-rtp'`: will set the remaining properties to default.

## Audio RTP Streaming

### raw audio

```sh
# sender
gst-launch-1.0 audiotestsrc \
  ! audioconvert \
  ! audioresample \
  ! rtpL24pay \
  ! udpsink host=$HOST port=5001

# receiver
gst-launch-1.0 -v udpsrc port=5001 \
  ! 'application/x-rtp,media=audio,payload=96,clock-rate=44100,encoding-name=L24' \
  ! rtpL24depay \
  ! audioconvert \
  ! autoaudiosink sync=false
```

### encoded/decoded audio

```sh
# sender
gst-launch-1.0 audiotestsrc \
  ! audioconvert \
  ! audioresample \
  ! alawenc \
  ! rtppcmapay \
  ! udpsink host=$HOST port=5001

# receiver
gst-launch-1.0 -v udpsrc port=5001 \
  ! 'application/x-rtp,media=audio,payload=8,clock-rate=8000,encoding-name=PCMA'  \
  ! rtppcmadepay \
  ! alawdec \
  ! audioconvert \
  ! autoaudiosink sync=false
```

## Audio + Video RTP Streaming

```sh
# sender
gst-launch-1.0 -v videotestsrc \
  ! 'video/x-raw,format=I420,width=1920,height=1080,framerate=60/1' \
  ! omxh264enc insert-sps-pps=true bitrate=16000000 \
  ! h264parse \
  ! rtph264pay pt=96 \
  ! udpsink port=5000 host=$HOST audiotestsrc \
  ! audioconvert \
  ! audioresample \
  ! rtpL24pay \
  ! udpsink host=$HOST port=5001


# receiver
gst-launch-1.0 -v udpsrc port=5000 \
  ! 'application/x-rtp, media=(string)video, clock-rate=(int)90000, encoding-name=(string)H264, payload=(int)96' \
  ! rtph264depay \
  ! h264parse \
  ! decodebin \
  ! videoconvert \
  ! fpsdisplaysink text-overlay=false sync=false \
  udpsrc port=5001 \
  ! "application/x-rtp,channels=1,media=audio,payload=96,clock-rate=44100,encoding-name=L24" \
  ! rtpL24depay \
  ! audioconvert \
  ! autoaudiosink sync=false

#TODO: SDP file
v=0
c=IN IP4 <Receiver IP>
m=video 5000 RTP/AVP 96
a=recvonly
a=rtpmap:96 H264/90000
m=audio 5001 RTP/AVP 8
a=recvonly
a=rtpmap:8 PCMA/8000/1
```

## Media File RTP Streaming

### demux and split video and audio(not best)

```sh
# sender `mp4` file
gst-launch-1.0 -v filesrc location=/home/jetson/Videos/why_I_left_China_for_Good.mp4 \
  ! qtdemux name=demux  \
  demux.video_0 ! queue ! h264parse ! decodebin ! omxh264enc insert-sps-pps=true bitrate=16000000 ! rtph264pay pt=96 ! udpsink host=$HOST port=5000  \
  demux.audio_0 ! queue ! decodebin ! audioconvert ! audioresample ! avenc_ac3 ! rtpac3pay ! udpsink host=$HOST port=5001

# receiver
gst-launch-1.0 -v \
  udpsrc port=5000 \
  ! 'application/x-rtp,media=(string)video,clock-rate=(int)90000,encoding-name=(string)H264,payload=(int)96' \
  ! rtph264depay ! h264parse ! decodebin ! videoconvert ! fpsdisplaysink text-overlay=false sync=false  \
  udpsrc port=5001 \
  ! 'application/x-rtp,media=(string)audio,clock-rate=(int)44100,encoding-name=(string)AC3,payload=(int)96' \
  ! rtpac3depay ! ac3parse ! decodebin ! audioconvert ! autoaudiosink sync=false

# receiver(short version)
gst-launch-1.0 -v \
  udpsrc port=5000 caps='application/x-rtp' \
  ! rtph264depay ! decodebin ! videoconvert ! fpsdisplaysink text-overlay=false sync=false  \
  udpsrc port=5001 caps='application/x-rtp' \
  ! rtpac3depay ! decodebin ! audioconvert ! autoaudiosink sync=false
```

### remux to MPEGST(best)

It has several advantages like good re-synchronization after packet loss and that A/V always stays sync

#### mpegts sender

```sh
# sender `mp4` file
gst-launch-1.0 -v filesrc location=/home/jetson/Videos/why_I_left_China_for_Good.mp4 \
  ! qtdemux name=demux mpegtsmux name=mux alignment=7 \
  ! rtpmp2tpay \
  ! udpsink host=$HOST port=5000 demux. \
  ! queue ! h264parse ! decodebin ! omxh264enc insert-sps-pps=true bitrate=16000000 ! mux. demux. \
  ! queue ! aacparse ! mux.
```

#### mpegts receiver

```sh
# receiver
gst-launch-1.0 -v udpsrc port=5000 \
  ! 'application/x-rtp,clock-rate=(int)90000,media=(string)video,payload=(int)96,encoding-name=(string)MP2T' \
  ! rtpmp2tdepay ! tsparse ! tsdemux name=demux \
  demux. ! queue ! decodebin ! videoconvert ! fpsdisplaysink text-overlay=false sync=false \
  demux. ! queue ! decodebin ! audioconvert ! autoaudiosink sync=false

# receiver(short version)
gst-launch-1.0 -v udpsrc port=5000 caps="application/x-rtp" \
  ! rtpmp2tdepay ! tsparse ! tsdemux name=demux \
  demux. ! queue ! decodebin ! videoconvert ! fpsdisplaysink text-overlay=false sync=false \
  demux. ! queue ! decodebin ! audioconvert ! autoaudiosink sync=false

# receiver(`ts` file)
gst-launch-1.0 -v -e udpsrc port=5000 caps="application/x-rtp" \
  ! rtpmp2tdepay ! tsparse ! filesink location=foo.ts
```

> `tsdemux demux.video_0` not work, see the details belowing:
> You're using a name (video_0) that doesn't exist. The pad names of demuxers vary from demuxer to demuxer, and might sometimes also differ from version to version. In this case that first video pad is called video_0031 as you can see at the end. It's generally best not to specify pad names unless you have a good reason to do so.

## RTSP Server

### install server(jetson nano)

```sh
# install gst-rtsp-server libs
sudo apt-get install libgstrtspserver-1.0 libgstreamer1.0-dev

# install gst-rtsp-server test server(1.14 is your gst version, checked by gst-lanch-1.0 --version)
wget https://raw.githubusercontent.com/GStreamer/gst-rtsp-server/1.14/examples/test-launch.c
gcc test-launch.c -o test-launch $(pkg-config --cflags --libs gstreamer-1.0 gstreamer-rtsp-server-1.0)
```

### stream web-cam(jetson nano)

```sh
# server
./test-launch "nvarguscamerasrc ! video/x-raw(memory:NVMM), format=NV12, width=1920, height=1080, framerate=30/1 ! nvvidconv ! video/x-raw, width=640, height=480, format=NV12, framerate=30/1 ! omxh265enc ! rtph265pay name=pay0 pt=96 config-interval=1"

# client
gst-launch-1.0 rtspsrc location=rtsp://jetson-desktop.local:8554/test  ! decodebin ! videoconvert ! autovideosink
```

### stream media file(*.mp4)

1. video

    ```sh
    # server
    ./test-launch "filesrc location=/home/jetson/Videos/why_I_left_China_for_Good.mp4 \
      ! qtdemux \
      ! h264parse \
      ! decodebin \
      ! videoconvert \
      ! omxh264enc insert-sps-pps=true bitrate=16000000 \
      ! rtph264pay name=pay0"

    # client
    gst-launch-1.0 -v rtspsrc location=rtsp://jetson-desktop.local:8554/test \
      ! rtph264depay \
      ! h264parse \
      ! decodebin \
      ! videoconvert \
      ! autovideosink sync=false
    ```
  
2. audio

    ```sh
    # server
    ./test-launch "filesrc location=/home/jetson/Videos/why_I_left_China_for_Good.mp4 \
      ! qtdemux \
      ! aacparse \
      ! decodebin \
      ! audioconvert \
      ! avenc_aac \
      ! rtpmp4apay name=pay0"

    # client
    gst-launch-1.0 -v rtspsrc location=rtsp://jetson-desktop.local:8554/test \
      ! rtpmp4adepay \
      ! aacparse \
      ! decodebin \
      ! audioconvert \
      ! autoaudiosink sync=false
    ```

3. video + audio

    h264 + acc,

    ```sh
    # server
    ./test-launch "filesrc location=/home/jetson/Videos/why_I_left_China_for_Good.mp4 \
      ! qtdemux name=demux \
      demux. ! queue ! h264parse ! decodebin ! omxh264enc insert-sps-pps=true bitrate=16000000 ! rtph264pay name=pay0 \
      demux. ! queue ! aacparse ! decodebin ! audioconvert ! avenc_aac ! rtpmp4apay name=pay1"

    # client
    gst-launch-1.0 -v rtspsrc location=rtsp://jetson-desktop.local:8554/test name=src \
      src. ! rtph264depay ! h264parse ! decodebin ! videoconvert ! autovideosink sync=false \
      src. ! rtpmp4adepay ! aacparse ! decodebin ! audioconvert ! autoaudiosink sync=false

    # client(short)
    gst-launch-1.0 -v rtspsrc location=rtsp://jetson-desktop.local:8554/test name=src \
      src. ! decodebin ! videoconvert ! autovideosink sync=false \
      src. ! decodebin ! audioconvert ! autoaudiosink sync=false
    ```

    mpegts,

    ```sh
    # server
    ./test-launch "filesrc location=/home/jetson/Videos/why_I_left_China_for_Good.mp4 \
      ! qtdemux name=demux mpegtsmux name=mux alignment=7 \
      ! rtpmp2tpay name=pay0 demux. \
      ! queue ! h264parse ! decodebin ! omxh264enc insert-sps-pps=true bitrate=16000000 ! mux. demux. \
      ! queue ! aacparse ! decodebin ! audioconvert ! avenc_aac ! mux."

    # client
    gst-launch-1.0 -v rtspsrc location=rtsp://jetson-desktop.local:8554/test \
      ! rtpmp2tdepay ! tsparse ! tsdemux name=demux \
      demux. ! queue ! decodebin ! videoconvert ! fpsdisplaysink text-overlay=false sync=false \
      demux. ! queue leaky=1 ! decodebin ! audioconvert ! autoaudiosink sync=false

    # client(only video)
    gst-launch-1.0 -v rtspsrc location=rtsp://jetson-desktop.local:8554/test name=src \
      src. ! rtpmp2tdepay ! tsparse ! tsdemux name=demux ! h264parse ! avdec_h264 ! videoconvert ! autovideosink sync=false

    # client(only audio)
    gst-launch-1.0 -v rtspsrc location=rtsp://jetson-desktop.local:8554/test \
      ! rtpmp2tdepay ! tsparse ! tsdemux name=demux ! aacparse ! decodebin ! audioconvert ! autoaudiosink sync=false
    ```

## RTSP Server via MediaMTX

```sh
docker run --rm -it --network=host bluenviron/mediamtx
```

RTSP_SERVER=rtsp://192.168.2.24:8554
RTSP_SRC=$RTSP_SERVER/mystream

```sh
gst-launch-1.0 -v \
    videotestsrc is-live=true ! video/x-raw,framerate=60/1 ! clockoverlay time-format="%H:%M:%S" font-desc="Sans 24" ! \
    x264enc ! \
    queue ! mpegtsmux name=mux ! rtspclientsink location=$RTSP_SRC protocols=tcp \
    audiotestsrc is-live=true ! \
    queue ! faac bitrate=128000 ! mux.
```

```sh
gst-launch-1.0 -v \
    fallbacksrc uri=http://192.168.2.24:8080/live.ts \
    fallback-uri=file:///tmp/black_frame.png restart-on-eos=True name=d \
    d.video ! queue ! videoconvert ! x264enc ! mpegtsmux name=mux ! rtspclientsink location=$RTSP_SRC protocols=tcp \
    d.audio ! queue ! audioconvert ! faac ! mux.
```

```sh
gst-launch-1.0 playbin3 uri=$RTSP_SRC

gst-launch-1.0 -v \
    rtspsrc location=$RTSP_SRC protocols=tcp latency=100 \
    ! rtpmp2tdepay ! tsdemux name=demux \
    demux. ! queue max-size-time=0 max-size-bytes=0 max-size-buffers=0 ! decodebin ! videoconvert ! autovideosink \
    demux. ! queue max-size-time=0 max-size-bytes=0 max-size-buffers=0 ! decodebin ! audioconvert ! audioresample ! autoaudiosink
```

## Serving MPEG-TS `.ts` file by HTTP

**MPEG-TS** (MPEG Transport Stream) is a standard video container format used primarily for broadcasting and streaming applications, including HLS (HTTP Live Streaming). It is designed to be robust and fault-tolerant for delivering video and audio content over unreliable networks, such as satellite, cable, or the internet.

The live/vod video is always segmented to **MPEG-TS** chunks like 2-10s `.ts` files that are used in `HLS`.

Here, we can use a http server to serve a **MPEG-TS** files.

### Create a single `ts` streaming file

```sh
mkdir -p /tmp/video
```

To to creat mock video:

```sh
gst-launch-1.0 -v \
    videotestsrc is-live=true ! video/x-raw,framerate=60/1 ! clockoverlay time-format="%H:%M:%S" font-desc="Sans 24" ! \
    x264enc ! \
    h264parse ! \
    mpegtsmux ! filesink location=/tmp/video/live.ts
```

To to creat mock video and mock audio:

```sh
gst-launch-1.0 -v \
    videotestsrc is-live=true ! video/x-raw,framerate=60/1 ! clockoverlay time-format="%H:%M:%S" font-desc="Sans 24" ! \
    x264enc ! \
    queue ! \
    tsmux. audiotestsrc is-live=true ! \
    faac ! \
    queue ! \
    mpegtsmux name=tsmux ! filesink location=/tmp/video/live.ts
```

or

```sh
gst-launch-1.0 -v \
    videotestsrc is-live=true ! video/x-raw,framerate=60/1 ! clockoverlay time-format="%H:%M:%S" font-desc="Sans 24" ! \
    x264enc ! \
    queue ! \
    mpegtsmux name=tsmux ! filesink location=/tmp/video/live.ts \
    audiotestsrc is-live=true ! \
    faac ! \
    queue ! \
    tsmux.
```

### Run a simple web server

Run a simple web server to serve the **MPEG-TS** by using `Python`:

```sh
cd /tmp/video
python3 -m http.server 8080
```

### Client to play `.ts` files

```sh
HOST=127.0.0.1
```

Media Player like VLC can view **MPEG-TS**, and Browser needs third party libraries:
https://$HOST:8080/live.ts

GStreamer pipeline to fetch the **MPEG-TS** stream.

To use `playbin3`:
```sh
gst-launch-1.0 playbin3 uri=http://$HOST:8080/live.ts
```

To play only video:
```sh
gst-launch-1.0 souphttpsrc location=http://$HOST:8080/live.ts is-live=true ! tsdemux ! decodebin ! autovideosink
```

To play only audio:
```sh
gst-launch-1.0 souphttpsrc location=http://$HOST:8080/live.ts ! tsdemux ! decodebin ! autoaudiosink
```

To play both video and audio:
```sh
gst-launch-1.0 -v \
    souphttpsrc location=http://$HOST:8080/live.ts is-live=true ! \
    tsdemux name=demux \
    demux. ! queue ! decodebin ! videoconvert ! autovideosink \
    demux. ! queue ! decodebin ! audioconvert ! audioresample ! autoaudiosink
```

```sh
gst-launch-1.0 -v \
    souphttpsrc location=http://192.168.2.24:8080/live.ts is-live=true ! \
    tsdemux name=demux \
    demux. ! queue ! h264parse! flvmux name=mux ! rtmpsink location="rtmp://192.168.2.24/live/camera2" \
    demux. ! queue ! aacparse ! mux.
```

## HLS

**HLS** is served over **HTTP** and it support both **live** and **vod** stream, which makes it friendly for mobiles or PC to use modern browsers like Chrome and Safari to play the stream in real time with low latency.

- **Compatibility**: HTTP is widely supported by most network infrastructures, including firewalls, proxies, and content delivery networks (CDNs). This makes HLS a flexible and scalable protocol for streaming across different devices and platforms.
- **Adaptive Streaming**: HLS allows for adaptive bitrate streaming, where the playlist can contain links to different quality levels (e.g., low_quality.m3u8, medium_quality.m3u8, and high_quality.m3u8). The client can request the appropriate .m3u8 file and corresponding segments based on the current network conditions.
- **Standard Web Protocol**: Since HTTP is the standard protocol used for web traffic, it allows for easy integration with web servers, CDNs, and other network components. It’s also easier to set up than some other protocols like RTMP.

### Creating segemented **.ts** files and a **.m3u8** playlist

```sh
mkdir -p /tmp/video
```

Video for live stream(`.m3u8` playlist will be continuously updated as new segments are created)::

```sh
gst-launch-1.0 -v \
    videotestsrc is-live=true ! video/x-raw,framerate=60/1 ! clockoverlay time-format="%H:%M:%S" font-desc="Sans 24" ! \
    x264enc bitrate=1000 speed-preset=ultrafast tune=zerolatency ! \
    h264parse ! \
    hlssink2 location=/tmp/video/segment%05d.ts playlist-location=/tmp/video/live.m3u8 target-duration=2
```

Video for VOD stream:

```sh
gst-launch-1.0 -v \
    videotestsrc is-live=true ! video/x-raw,framerate=60/1 ! clockoverlay time-format="%H:%M:%S" font-desc="Sans 24" ! \
    x264enc bitrate=1000 speed-preset=ultrafast tune=zerolatency ! \
    h264parse ! \
    hlssink2 location=/tmp/video/segment%05d.ts playlist-location=/tmp/video/live.m3u8 target-duration=2 max-files=0 playlist-length=0
```

Then, MUST `CTRL+C` to exit the pipeline for adding `EXT-X-ENDLIST` into the end of the `.m3u8` file which indicates it is **VOD** stream.

To send both video and audio:

```sh
gst-launch-1.0 -v \
    videotestsrc is-live=true ! video/x-raw,framerate=60/1 ! \
    x264enc bitrate=1000 speed-preset=ultrafast tune=zerolatency ! \
    h264parse ! \
    queue ! \
    hlssink2 name=hls location=/tmp/video/segment%05d.ts playlist-location=/tmp/video/live.m3u8 target-duration=2 \
    audiotestsrc ! audio/x-raw,rate=44100,channels=2 ! \
    faac ! aacparse ! \
    queue \
    ! hls.audio
```

### Runing a web server for serving HLS

To run a simple web server to serve the MPEG-TS or HLS file by using `Python`,

```sh
cd /tmp/video
python3 -m http.server 8080
```

### Client to play HLS stream

Safari can play **HLS** with live update directly via `http://127.0.0.1:8080/live.m3u8`, while Chrome needs third-party javascript libraries like **hls.js**:

GStreamer pipeline,

To use `playbin3`:

```sh
gst-launch-1.0 playbin3 uri=http://$HOST:8080/live.m3u8
```

To play only video:
```sh
gst-launch-1.0 -v souphttpsrc location=http://$HOST:8080/live.m3u8 is-live=TRUE ! hlsdemux ! decodebin ! autovideosink
```

To play only audio:
```sh
gst-launch-1.0 souphttpsrc location=http://$HOST:8080/live.m3u8 ! hlsdemux ! decodebin ! audioconvert ! audioresample ! autoaudiosink
```

To play both video and audio:
```sh
gst-launch-1.0 -v \
    souphttpsrc location=http://$HOST:8080/live.m3u8 ! \
    hlsdemux ! tsdemux name=demux \
    demux. ! queue ! decodebin ! videoconvert ! autovideosink \
    demux. ! queue ! decodebin ! audioconvert ! audioresample ! autoaudiosink
```

> Note: `tsdemux` needs to be sitting between `hlsdemux` and `decodebin`!

## RTMP Server

RTMP server supports both live streams and on-demand streams.
RTMP server can only accept `FLV` container format.

### Set up a RTMP server

Here, if you need your own RTMP server, running the following docker container works quite simply well.

```sh
docker run -d -p 1935:1935 --name nginx-rtmp tiangolo/nginx-rtmp
```

A modified configuration file `nginx.config` can be used to serve either a RTMP stream or a HLS stream,

```conf title=/etc/nginx/nginx.conf
worker_processes auto;
rtmp_auto_push on;
events {}
rtmp {
    server {
        listen 1935;
        listen [::]:1935 ipv6only=on;

        application live {
            live on;
            record off;
	          interleave on; # Ensures audio and video packets are properly synchronized.

            hls on;
            hls_path /tmp/hls;
        }
    }
}

http {
    server {
        listen 8080;  # HTTP port for accessing HLS streams

        # Serve the HLS playlist and segments
        location /hls/ {
            root /tmp;  # Path to HLS files
            add_header Cache-Control no-cache;
            add_header Access-Control-Allow-Origin *;  # Allow cross-origin access
        }
    }
}
```

The RTMP url format is like: `rtmp://<ip_of_host>/live/<key>`, and the HLS can be visited at `http://<ip_of_host>/hls/<key>.m3u8`.

### Send a live stream to a RTMP server

```sh
HOST=192.168.2.24
RTMP_SRC="rtmp://$HOST/live/camera1"
```

To send a video:
```sh
gst-launch-1.0 -v \
    videotestsrc is-live=true ! video/x-raw,framerate=60/1 ! clockoverlay time-format="%H:%M:%S" font-desc="Sans 24" ! \
    x264enc ! \
    flvmux streamable=true name=mux ! rtmpsink location=$RTMP_SRC
```

To send a video and audio:
```sh
gst-launch-1.0 -v \
    videotestsrc is-live=true ! video/x-raw,framerate=60/1 ! clockoverlay time-format="%H:%M:%S" font-desc="Sans 24" ! \
    x264enc ! \
    queue ! flvmux streamable=true name=mux ! rtmpsink location=$RTMP_SRC \
    audiotestsrc is-live=true ! \
    queue ! faac bitrate=128000 ! mux.
```

```sh
gst-launch-1.0 \
    videotestsrc is-live=1 \
    ! videoconvert \
    ! "video/x-raw, width=1280, height=720, framerate=30/1" \
    ! queue \
    ! x264enc cabac=1 bframes=2 ref=1 \
    ! "video/x-h264,profile=main" \
    ! flvmux streamable=true name=mux \
    ! rtmpsink location="$RTMP_SRC live=1" \
    audiotestsrc is-live=1 wave=ticks \
    ! faac bitrate=128000 \
    ! mux.
```

### Receiver a live stream

Let's play the above `RTMP_SRC` which is a live stream.

> NOTE: A test RTMP on-demand stream is at: RTMP_SRC="rtmp://matthewc.co.uk/vod/scooter.flv", which can be used to test your pipeline.

To use `playbin3`, it's simple while versatile and magic:
```sh
gst-launch-1.0 playbin3 uri=$RTMP_SRC
```

To play only video:
```sh
gst-launch-1.0 rtmpsrc location=$RTMP_SRC ! decodebin ! videoconvert ! autovideosink
```

To play only audio:
```sh
gst-launch-1.0 rtmpsrc name=rtmpsrc location=$RTMP_SRC ! decodebin ! audioconvert ! autoaudiosink
```

To play video and audio in a fine-grained pipeline:
```sh
gst-launch-1.0 rtmpsrc location="$RTMP_SRC live=1" ! \
    flvdemux name=demux \
    demux.audio ! queue ! decodebin ! audioconvert ! autoaudiosink \
    demux.video ! queue ! decodebin ! videoconvert ! autovideosink 
```

```sh
gst-launch-1.0 rtmpsrc location="$RTMP_SRC live=1" ! \
    flvdemux name=demux \
    demux.audio ! queue max-size-time=0 max-size-bytes=0 max-size-buffers=0 ! decodebin ! audioconvert ! autoaudiosink \
    demux.video ! queue max-size-time=0 max-size-bytes=0 max-size-buffers=0 ! decodebin ! videoconvert ! autovideosink
```