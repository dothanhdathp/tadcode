# GStreamer NamiDtv2Example

## Phase 1: Init

```puml
participant "<<JNI>>" as J
participant "<<libnative.so>>" as N
participant "<<thread>>\n//*app_function()//" as A
participant "<<libgstreamer.so>>" as G

== Step 1: Init ==

-> J: nativeClassInit()
J -> N: gst_native_class_init()
N --> N: << set **custom_data_field_id** >>
N --> N: << set **Jmethod** for //callback// >>
note right N
//Read note 1//
end note
```

## Phase 2: Init

```puml
participant "<<JNI>>" as J
participant "<<libnative.so>>" as N
participant "<<thread>>\n//*app_function()//" as A
participant "<<libgstreamer.so>>" as G

== Phase 2: Setup ==

-> J: nativeSurfaceInit()
J -> N: gst_native_surface_init()
N -> G: (ANativeWindow*) ANativeWindow_fromSurface()
N -> G: ANativeWindow_release()
N -> G: gst_video_overlay_expose()
note right G
Tạo mới và gán lại màn //surface//
end note
N [#red]-> N: check_initialization_complete()
N -> G: gst_video_overlay_set_window_handle()
N --> J: CallMethod(**METHOD_GST_INITIALIZED**)\n//(Trả lời khi init thành công)//
<-- J: onGStreamerInitialized()

-> J: nativeInit()
J -> N: gst_native_init()
N -> G: gst_debug_set_threshold_for_name()
N --> A: << pthread_create >>
A --> A: << start_thread >>
activate A #tomato
```

## Phase 3: Init

```puml
participant "<<JNI>>" as J
participant "<<libnative.so>>" as N
participant "<<thread>>\n//*app_function()//" as A
participant "<<libgstreamer.so>>" as G
activate A #tomato

== Phase 3: app_function run ==

alt Step inside app_function
else Create our own GLib Main Context and make it the default one
A -> G: data->context = g_main_context_new()
A -> G: datag_main_context_push_thread_default()
else #LightBlue Build pipeline
A -> G: gst_parse_launch(PIPELINE_DESCRIPTION_NAMI_DVBT2_90)
group #ffb499 (If) //**gst_parse_launch()**// error
A -> G: g_clear_error()
A -> G: g_free()
end
else Set the pipeline to READY
A -> G: gst_element_set_state(**GST_STATE_READY**)
A -> G: gst_bin_get_by_interface(**GST_STATE_READY**)
else Instruct the bus
A -> G: gst_element_get_bus
A -> G: gst_bus_create_watch
A -> G: g_source_set_callback
A -> G: g_source_attach
A -> G: g_source_unref
else #b3ffb3 Assign callback
A -> G: **g_signal_connect**("message::error", **error_cb()**)
A -> G: **g_signal_connect**("message::state-changed", **state_changed_cb()**)
A -> G: gst_object_unref()
else Create a GLib Main Loop and set it to run
A -> G: g_main_loop_new()
A [#red]-> N: check_initialization_complete()
N --> J: CallMethod(**METHOD_GST_INITIALIZED**)\n//(Trả lời khi init thành công)//
<-- J: onGStreamerInitialized()
A -> G: g_main_loop_run()
A -> G: g_main_loop_unref()
end
```

## Phase 4: Init

```puml
participant "<<JNI>>" as J
participant "<<libnative.so>>" as N
participant "<<thread>>\n//*app_function()//" as A
participant "<<libgstreamer.so>>" as G
activate A #tomato

== Phase 4: Request call ==

-> J: nativePlay()
J -> N: gst_native_play()
N -> G: gst_element_set_state (**GST_STATE_PLAYING**)
group #b3ffb3 [IF] Callback Assigned
G --> N: state_changed_cb(**GST_STATE_PLAYING**)
<-- N: //Setting function for send out STATE//
end
-> J: nativePause()
J -> N: gst_native_pause()
N -> G: gst_element_set_state (**GST_STATE_PAUSE**)
group #b3ffb3 [IF] Callback Assigned
G --> N: state_changed_cb(**GST_STATE_PAUSE**)
<-- N: //Setting function for send out STATE//
end
```

## Phase 5: Init

```puml
participant "<<JNI>>" as J
participant "<<libnative.so>>" as N
participant "<<thread>>\n//*app_function()//" as A
participant "<<libgstreamer.so>>" as G
activate A #tomato

== Phase 5: Finalize ==

-> J: nativeSurfaceFinalize()
J -> N: gst_native_surface_finalize()
group #lightgray [IF] Surface in use
N -> G: gst_video_overlay_set_window_handle(**NULL**)
N -> G: gst_element_set_state(**GST_STATE_READY**)
end
N -> G: ANativeWindow_release()
-> J: nativeFinalize()
J -> N: gst_native_finalize()
N -> G: g_main_loop_quit()
G --> A: //<<request exit main loop in app_function>>//
N -> N: pthread_join()
activate N
note over N
Wait app_function thread exit
end note
group Free (thread) resources
A -> G: g_main_context_pop_thread_default(context)
A -> G: g_main_context_unref(context)
A -> G: gst_element_set_state(**GST_STATE_NULL**)
A -> G: gst_object_unref(surface)
A -> G: gst_object_unref(pipeline)
deactivate A
end
A --> N: NULL //(Thread exit)//
deactivate N
N -> N: //<< DeleteGlobalRef >>//
N -> N: //<< Free CustomData >>//
```
