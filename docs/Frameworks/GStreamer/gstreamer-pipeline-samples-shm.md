# SHM(Shared Memory)

## raw video

```sh
# send
gst-launch-1.0 -v videotestsrc is-live=true ! 'video/x-raw,width=1280,height=720,format=(string)RGB,framerate=(fraction)60/1' ! videoconvert ! shmsink socket-path=/tmp/foo name=/tmp/shm sync=false wait-for-connection=false shm-size=20000000

# receive
gst-launch-1.0 -v shmsrc do-timestamp=true socket-path=/tmp/foo name=/tmp/shm ! 'video/x-raw,width=1280,height=720,format=(string)RGB,framerate=(fraction)60/1' ! videoconvert ! fpsdisplaysink text-overlay=false sync=false -e
```

**tips:**

1. `do-timestamp=true`: solve `gst_segment_to_stream_time: assertion 'segment->format == format' failed` error. Seeing at[Getting shmsink/shmsrc to work with videomixer](https://mazdermind.wordpress.com/2014/08/29/getting-shmsinkshmsrc-to-work-with-videomixer/)
2. In local host, use `raw video` faster than `h264` due to memory cheaper/faster that cpu
3. increase `shm-size` for large image

## h264 encode/decode

```sh
# send
gst-launch-1.0 -v videotestsrc ! x264enc ! shmsink socket-path=/tmp/foo sync=false wait-for-connection=false shm-size=10000000

gst-launch-1.0 -v videotestsrc ! 'video/x-raw,width=1280,height=720,format=NV12,framerate=60/1' ! x264enc ! shmsink socket-path=/tmp/foo sync=false wait-for-connection=false shm-size=10000000

# receive
gst-launch-1.0 -v shmsrc socket-path=/tmp/foo ! h264parse ! decodebin ! videoconvert ! fpsdisplaysink text-overlay=false sync=false
```