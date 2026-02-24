# GStreamer Android Tutorial 2

## Preset

### JNI init

```puml
@startuml
participant MainActivity
participant GStreamer
participant "<<JNI>>"
participant libgstreamer_jni
participant app_function
participant libgstreamer_android

== JNI init ==
MainActivity -> MainActivity: //internal init()//
MainActivity -> MainActivity: loadLibrary("gstreamer_android")
MainActivity -> MainActivity: loadLibrary("gstreamer_jni")
MainActivity --> "<<JNI>>":
"<<JNI>>" --> libgstreamer_jni : JNI_OnLoad
libgstreamer_jni -> libgstreamer_jni : //<<RegisterNatives Method>>//
note right libgstreamer_jni
== Set Jni Call ==
nativeInit = gst_native_init
nativeFinalize = gst_native_finalize
nativePlay = gst_native_play
nativePause = gst_native_pause
nativeClassInit = gst_native_class_init
end note
MainActivity -> "<<JNI>>" : nativeClassInit()
"<<JNI>>" --> libgstreamer_jni : gst_native_class_init()
note right libgstreamer_jni
== Set Callback ==
(jfieldID) custom_data_field_id = MainActivity::nativeCustomData
(jmethodID) set_message_method_id = MainActivity::setMessage
(jmethodID) on_gstreamer_initialized_method_id = MainActivity::onGStreamerInitialized
end note
@enduml
```

#### JNI_OnLoad

__JNI_OnLoad()__ là hàm sẽ được gọi ngay sau khi __*loadLibrary("gstreamer_jni")*__. Trong hàm này sẽ có các chức năng:

### Preset Value

```puml
@startuml
participant MainActivity
participant GStreamer
participant "<<JNI>>"
participant libgstreamer_jni
participant app_function
participant libgstreamer_android

== Preset Values ==
MainActivity -> MainActivity: onCreate()
MainActivity -> GStreamer : init()
note right MainActivity
- set nativePlay() for button Play
- set nativePause() for button Pause
end note
MainActivity -> "<<JNI>>" : nativeInit()
"<<JNI>>" --> libgstreamer_jni : gst_native_init()
libgstreamer_jni -> libgstreamer_jni : **SET_CUSTOM_DATA(custom_data_field_id)**;
libgstreamer_jni -> libgstreamer_android : gst_debug_set_threshold_for_name()
libgstreamer_jni -> libgstreamer_jni: //<<Created CustomData>>//
libgstreamer_jni -> libgstreamer_jni: //<<Created GlobalRef>>//
libgstreamer_jni --> app_function: //Start thread//
@enduml
```

## Thread app_function

### Main method for the native code

```puml
@startuml
participant MainActivity
participant GStreamer
participant "<<JNI>>"
participant libgstreamer_jni
participant app_function
participant libgstreamer_android

== Main method for the native code ==
activate app_function
note right app_function
Create our own
**GLib Main Context**
and make it the
**default one**
end note
app_function -> libgstreamer_android: g_main_context_new
app_function -> libgstreamer_android: g_main_context_push_thread_default
note right app_function
Build pipeline
end note
app_function -> libgstreamer_android: **gst_parse_launch**
note right app_function
Instruct the bus to emit signals
for each received message, and
connect to the interesting signals
end note
app_function -> libgstreamer_android: **gst_element_get_bus**
app_function -> libgstreamer_android: gst_bus_create_watch
app_function -> libgstreamer_android: **g_source_set_callback**
app_function -> libgstreamer_android: g_source_attach
app_function -> libgstreamer_android: g_source_unref
app_function -> libgstreamer_android: gst_object_unref
note right app_function
Create a **GLib Main Loop**
and set it to run
end note
app_function -> libgstreamer_android: g_main_loop_new
app_function -> app_function: **check_initialization_complete**
app_function -> "<<JNI>>": **CallVoidMethod(check_initialization_complete)**
"<<JNI>>" --> MainActivity: **onGStreamerInitialized()**
app_function -> libgstreamer_android: **g_main_loop_run**
app_function -> libgstreamer_android: g_main_loop_unref
@enduml
```

### On living

```puml
@startuml
participant MainActivity
participant GStreamer
participant "<<JNI>>"
participant libgstreamer_jni
participant app_function
participant libgstreamer_android

== On living ==
MainActivity -> "<<JNI>>" :nativePlay()
"<<JNI>>" -> libgstreamer_jni: gst_native_play()
libgstreamer_jni -> libgstreamer_android : gst_element_set_state <<GST_STATE_PLAYING>>

MainActivity -> "<<JNI>>" :nativePause()
"<<JNI>>" -> libgstreamer_jni: gst_native_play()
libgstreamer_jni -> libgstreamer_android : gst_element_set_state <<GST_STATE_PAUSED>>
@enduml
```

### End of live

```puml
@startuml
participant MainActivity
participant GStreamer
participant "<<JNI>>"
participant libgstreamer_jni
participant app_function
participant libgstreamer_android

== End of live ==
-> MainActivity: onDestroy()
MainActivity -> "<<JNI>>" :nativeFinalize()
"<<JNI>>" -> libgstreamer_jni: gst_native_finalize()
libgstreamer_jni -> libgstreamer_android : g_main_loop_quit
libgstreamer_jni -> app_function: pthread_join\n//<<Wait thread exit suggestfully>>//

note right app_function
Free resources
end note
app_function -> libgstreamer_android: g_main_context_pop_thread_default
app_function -> libgstreamer_android: g_main_context_unref
app_function -> libgstreamer_android: gst_element_set_state
app_function -> libgstreamer_android: gst_object_unref
deactivate app_function
@enduml
```

## Warning

!!! danger "CustomData should be size long?"
    - Trong mô tả có nói về yêu cầu thành phần này phải có độ dài tương đương một giá trị `long`, vậy điều đó có nhất định hay không?
    - Và JNI nó có hoạt động giống với thằng C thuần thông thường hay không?
    - Tại sao lại không dùng C++ nhỉ?