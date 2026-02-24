# Mux Video and Audio

```sh
gst-launch-1.0 -v audiotestsrc ! autoaudiosink videotestsrc ! autovideosink

# save to `*.mp4` file
gst-launch-1.0 -v -e videotestsrc \
  ! x264enc \
  ! mp4mux name=mux \
  ! filesink location="bla.mp4" \
  audiotestsrc ! lamemp3enc ! mux.

```

videotestsrc --> x264enc -----\
                               >---> mp4mux ---> filesink
audiotestsrc --> lamemp3enc --/
