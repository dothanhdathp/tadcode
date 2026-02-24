# Audio

```sh
gst-launch-1.0 audiotestsrc ! autoaudiosink

# This creates a higher beep:
gst-launch-1.0 audiotestsrc freq=1000 ! autoaudiosink

# volume
gst-launch-1.0 audiotestsrc volume=0.1 ! autoaudiosink

# White noise
gst-launch-1.0 audiotestsrc wave="white-noise" ! autoaudiosink

# Silence
gst-launch-1.0 audiotestsrc wave="silence" ! autoaudiosink
```