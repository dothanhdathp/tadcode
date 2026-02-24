# Media File

```sh
# information of file
gst-discoverer-1.0 -v /home/jetson/Videos/why_I_left_China_for_Good.mp4
```

## Play Media File

```sh
# play `mp4` file with audio
gst-launch-1.0 filesrc location=/Users/siyao/Movies/why_I_left_China_for_Good.mp4 \
  ! qtdemux name=demux  demux.audio_0 \
  ! decodebin ! audioconvert ! audioresample ! autoaudiosink

# play `mp4` file with video
gst-launch-1.0 filesrc location=/Users/siyao/Movies/why_I_left_China_for_Good.mp4 \
  ! qtdemux \
  ! decodebin ! videoconvert ! videoscale ! autovideosink

# play `mkv` file with video
gst-launch-1.0 -v filesrc location=/Users/siyao/Movies/jellyfish-10-mbps-hd-h264.mkv \
  ! matroskademux name=demux  demux.video_0\
  ! decodebin \
  ! videoconvert \
  ! autovideosink

# play `mp4` file with both audio and video
gst-launch-1.0 filesrc location=/Users/siyao/Movies/why_I_left_China_for_Good.mp4 \
  ! qtdemux name=demux  demux.audio_0 \
  ! queue ! decodebin ! audioconvert ! audioresample ! autoaudiosink  demux.video_0 \
  ! queue ! decodebin ! videoconvert ! videoscale ! autovideosink

```

## Transcode Media File

```sh
# `mkv` to `mp4` with video
gst-launch-1.0 -v filesrc location=/home/jetson/Videos/jellyfish-10-mbps-hd-h264.mkv \
  ! matroskademux \
  ! h264parse \
  ! mp4mux \
  ! filesink location=jellyfish.mp4

# `mp4` to `mkv` with video
gst-launch-1.0 -v filesrc location=/Users/siyao/Movies/why_I_left_China_for_Good.mp4 \
  ! qtdemux name=demux matroskamux name=mux \
  ! filesink location=fat_bunny.mkv  demux.video_0 \
  ! queue ! h264parse ! mux.

# `mp4` to `mkv` with audio
gst-launch-1.0 -v filesrc location=/Users/siyao/Movies/why_I_left_China_for_Good.mp4 \
  ! qtdemux name=demux matroskamux name=mux \
  ! filesink location=fat_bunny.mka  demux.audio_0 \
  ! queue ! decodebin ! audioconvert ! vorbisenc ! mux.

# `mp4`to `mkv` with both audio and video
gst-launch-1.0 -v filesrc location=/Users/siyao/Movies/why_I_left_China_for_Good.mp4 \
  ! qtdemux name=demux matroskamux name=mux \
  ! filesink location=fat_bunny.mkv  demux.audio_0 \
  ! queue ! decodebin ! audioconvert ! audioresample ! vorbisenc ! mux.  demux.video_0 \
  ! queue ! h264parse ! mux.

```