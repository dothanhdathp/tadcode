# Tips for Debug

- Set general debug level

  ```sh
  export GST_DEBUG=6 #5
  export GST_DEBUG=GST_REGISTRY:6,GST_PLUGIN:6
  ```

- Discover video file

  ```sh
  gst-discoverer-1.0 -v fat_bunny.ogg 
  ```

- Inspect plugin

  ```sh
  gst-inspect-1.0 avdec_h264
  ```

- Visualize a pipeline graph

**Graphviz** needs to be installed to convert those GStreamer generated `.dot` files into PDF and image file.

`GST_DEBUG_DUMP_DOT_DIR` environment variable must be defined firstly before creating the graph,
```sh
mkdir -p /tmp/pipeline
export GST_DEBUG_DUMP_DOT_DIR=/tmp/pipeline
```

Then run the pipeline,
```sh
gst-launch-1.0 playbin3 uri=http://$HOST:8080/live.m3u8
```

Five state change `.dot` files are created
```sh
❯ ls /tmp/pipeline
0.00.00.016386417-gst-launch.NULL_READY.dot
0.00.00.319950042-gst-launch.READY_PAUSED.dot
0.00.00.322555584-gst-launch.PAUSED_PLAYING.dot
0.00.07.145014292-gst-launch.PLAYING_PAUSED.dot
0.00.07.214058584-gst-launch.PAUSED_READY.dot
```

Finally convert these `.dot` files into PDF or image files,
```sh
# convert to PNG
dot -Tpng /tmp/pipeline/*.READY_PAUSED.dot -o ~/Desktop/pipeline-graph.png
# convert to PDF
dot -Tpdf /tmp/pipeline/*.READY_PAUSED.dot -o ~/Desktop/pipeline-graph.pdf
```