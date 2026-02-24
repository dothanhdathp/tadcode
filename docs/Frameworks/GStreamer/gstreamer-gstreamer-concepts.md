# GStreamer Concepts

> Các khái niệm cơ bản trong Gstreamer

## Nguyên lý hoạt động

Về cơ bản, _gstreamer_ là một đường ống 

## Các khái niệm cơ bản

Trong _gstreamer_ có 4 khái niệm cơ bản sau

- __Elements__ là các thành phần cơ bản nhất của gstreamer
- __pipeline__ là đường ống, bao gồm một hoặc nhiều các khối Elements cơ bản.
- __Pad__ có thể coi như là các ổ cắm, chúng dùng để cho các Elements giao tiếp và kết nối với nhau hoặc truyền dữ liệu giữa hai nguyên tố (Elements). Có thể coi các Pads
- __Bus__ là đường riêng, cái mà gstreamer mở ra để đưa các thông báo lỗi ra ngoài hoặc nhận các cơ chế điều khiển từ bên ngoài. Bus giúp người dùng có thể can thiệp vào tiến trình của đường ống giữa lúc đường ống đang hoạt động.


## Foundations

Bài này giới thiệu <u>các khái niệm cơ bản của __Gstreamer__</u>. Hiểu được các khái niệm này sẽ rất quan trọng trong việc đọc bất kỳ phần còn lại của hướng dẫn này, tất cả chúng đều cho rằng sự hiểu biết về các khái niệm cơ bản này.

- __Elements__: Elements là thành phần quan trọng nhất của GStreammer
- __Bins__: 
- __Bus__: 

### Pads and capabilities

### Buffers and Events

<figure markdown="span">
    ![alt text](img/gstreamer-foundations.png)
    <figcaption></figcaption>
</figure>

<figure markdown="span">
    ![alt text](img/gstreamer-foundations-1.png)
    <figcaption></figcaption>
</figure>

## Tham khảo

- [Foundations](https://gstreamer.freedesktop.org/documentation/application-development/introduction/basics.html?gi-language=c)

## Phân tích

Các yếu tố là các khối xây dựng cơ bản của Gstreamer. Họ xử lý dữ liệu khi <mark>nó chảy xuôi dòng từ các phần tử nguồn (nhà sản xuất dữ liệu) đến các phần tử chìm (người tiêu dùng dữ liệu), đi qua các phần tử lọc</mark>.

!!! note "Note"
    Nguồn --> Bộ Lọc --> Đích

<figure markdown="span">
    ![alt text](img/gstreamer-u-gstreamer-concepts-1.png)
    <figcaption>Hình 1. Ví dụ về đường ống</figcaption>
</figure>

## Element

_Phần khởi tạo (gst_init()) sẽ bị bỏ qua vì nó giống phần trước_

```c
    /* Create the elements */
    source = gst_element_factory_make ("videotestsrc", "source");
    sink = gst_element_factory_make ("autovideosink", "sink");
```

Như đã thấy trong mã này, các __*element*__ mới có thể được tạo với __gst_element_factory_make()__.

- Tham số đầu tiên là <u>loại phần tử</u> để tạo.
- Tham số thứ hai là <u>tên</u> chúng tôi muốn đặt cho trường hợp cụ thể này.
    - Đặt tên cho các yếu tố của bạn rất hữu ích để truy xuất chúng sau nếu bạn không giữ một con trỏ (đồng thời nó cũng cho đầu ra gỡ lỗi có ý nghĩa hơn). <mark>Tuy nhiên, nếu bạn đưa và __NULL__ cho tên, Gstreamer sẽ cung cấp một tên duy nhất cho bạn.</mark>

!!! abstract "Tham khảo"
    Tham khảo thêm [Handy elements]() hiển thị một vài loại phổ biến và [GStreamer tools]() chỉ ra cách lấy danh sách tất cả các loại có sẵn

Đối với hướng dẫn này, chúng tôi tạo hai yếu tố: một __videoTestSRC__ và __AutoVideoSink__ và __*Không có yếu tố lọc*__. Do đó, đường ống sẽ trông giống như sau:

<figure markdown="span">
    ![alt text](img/gstreamer-u-gstreamer-concepts-2.png)
    <figcaption>Hình 2. Đường ống được xây dựng trong hướng dẫn này</figcaption>
</figure>

- `videotestsrc`là một yếu tố nguồn (nó tạo ra dữ liệu), tạo ra một mẫu video thử nghiệm.- Yếu tố này rất hữu ích cho mục đích gỡ lỗi (và hướng dẫn) và thường không được tìm thấy trong các ứng dụng thực.
- `autovideosink` là một phần tử chìm (nó tiêu thụ dữ liệu), hiển thị trên cửa sổ hình ảnh mà nó nhận được. Tồn tại một số __*video sinks*__, tùy thuộc vào hệ điều hành, với một loạt các khả năng khác nhau. __*AutoVideosInk*__ tự động chọn và khởi tạo tốt nhất, vì vậy bạn không phải lo lắng với các chi tiết và mã của bạn độc lập hơn về nền tảng.

## Pipeline creation

```c
    /* Create the empty pipeline */
    pipeline = gst_pipeline_new ("test-pipeline");
```

Tất cả các yếu tố trong Gstreamer thường phải được chứa bên trong một đường ống trước khi chúng có thể được sử dụng, bởi vì nó quan tâm đến một số chức năng đồng bộ và nhắn tin. Chúng tôi tạo ra đường ống với __gst_pipeline_new()__.

```c
    /* Build the pipeline */
    gst_bin_add_many (GST_BIN (pipeline), source, sink, NULL);
    if (gst_element_link (source, sink) != TRUE) {
        g_printerr ("Elements could not be linked.\n");
        gst_object_unref (pipeline);
        return -1;
    }
```

Một đường ống là một loại thùng cụ thể, là phần tử được sử dụng để chứa các yếu tố khác.Do đó, tất cả các phương pháp áp dụng cho các thùng cũng áp dụng cho các đường ống.

Trong trường hợp của chúng tôi, chúng tôi gọi __GST_BIN_ADD_MANY()__ để thêm các yếu tố vào đường ống (tâm trí của dàn diễn viên).Hàm này chấp nhận một danh sách các yếu tố sẽ được thêm vào, kết thúc bằng __*null*__. Các yếu tố riêng lẻ có thể được thêm vào với __gst_bin_add()__.

Các yếu tố này, tuy nhiên, chưa được liên kết với nhau.Đối với điều này, chúng ta cần sử dụng __gst_element_link()__. Tham số đầu tiên của nó là nguồn và cái thứ hai là đích. Số lượng đơn hàng, bởi vì các liên kết phải được thiết lập theo luồng dữ liệu (đây là, từ các phần tử nguồn đến các yếu tố chìm). Hãy nhớ rằng chỉ các yếu tố cư trú trong cùng một thùng có thể được liên kết với nhau, vì vậy hãy nhớ thêm chúng vào đường ống trước khi cố gắng liên kết chúng!

## Properties _(thuộc tính)_

Các yếu tố Gstreamer đều là một loại Gobject cụ thể, đó là thực thể cung cấp các cơ sở tài sản.

Hầu hết các phần tử GSTreamer đều có các __thuộc tính có thể tùy chỉnh__ _(các thuộc tính được đặt tên có thể được sửa đổi để thay đổi hành vi của phần tử (thuộc tính có thể ghi))_ hoặc được hỏi để tìm hiểu về trạng thái bên trong của phần tử _(thuộc tính có thể đọc được)_.

Các thuộc tính được đọc từ với __g_Object_get()__ và được ghi thành __g_object_set()__.

__G_OBject_set()__ chấp nhận danh sách kết thúc không có tên thuộc tính, các cặp giá trị tài sản, do đó, nhiều thuộc tính có thể được thay đổi trong một lần.

Đây là lý do tại sao các phương thức xử lý thuộc tính có tiền tố `g_`.

Trở lại với những gì trong ví dụ trên,

```bash
    /* Modify the source's properties */
    g_object_set (source, "pattern", 0, NULL);
```

Dòng mã trên thay đổi thuộc tính `“pattern”` của __*videotestsrc*__, điều khiển loại video thử nghiệm __*element*__ đầu ra. Hãy thử các giá trị khác nhau!

Các tên và giá trị có thể của tất cả các thuộc tính mà một phần tử hiển thị có thể được tìm thấy bằng cách sử dụng công cụ `gst-inspect-1.0` được mô tả trong __GStreamer tools__ hoặc khác trong các tài liệu cho yếu tố đó (ở đây trong trường hợp của __VideotestSRC__).

## Error checking

Tại thời điểm này, chúng tôi có toàn bộ đường ống được xây dựng và thiết lập, và phần còn lại của hướng dẫn rất giống với hướng dẫn trước đó, nhưng chúng tôi sẽ thêm nhiều lần kiểm tra lỗi:

```c
  /* Start playing */
  ret = gst_element_set_state (pipeline, GST_STATE_PLAYING);
  if (ret == GST_STATE_CHANGE_FAILURE) {
        g_printerr ("Unable to set the pipeline to the playing state.\n");
        gst_object_unref (pipeline);
        return -1;
  }
```

Chúng tôi gọi __gst_element_set_state()__, Nhưng lần này chúng tôi kiểm tra giá trị trả lại của nó cho các lỗi.Thay đổi trạng thái là một quy trình tinh tế và một vài chi tiết được đưa ra trong chương [Dynamic pipelines]().

```c
    /* Wait until error or EOS */
    bus = gst_element_get_bus (pipeline);
    msg = gst_bus_timed_pop_filtered (bus, GST_CLOCK_TIME_NONE, GST_MESSAGE_ERROR | GST_MESSAGE_EOS);

    /* Parse message */
    if (msg != NULL) {
        GError *err;
        gchar *debug_info;

        switch (GST_MESSAGE_TYPE (msg)) {
            case GST_MESSAGE_ERROR: {
                gst_message_parse_error (msg, &err, &debug_info);
                g_printerr ("Error received from element %s: %s\n", GST_OBJECT_NAME (msg->src), err->message);
                g_printerr ("Debugging information: %s\n", debug_info ? debug_info : "none");
                g_clear_error (&err);
                g_free (debug_info);
                break;
            }
            case GST_MESSAGE_EOS: {
                g_print ("End-Of-Stream reached.\n");
                break;
            }
            default: {
                /* We should not reach here because we only asked for ERRORs and EOS */
                g_printerr ("Unexpected message received.\n");
                break;
            }
        }
        gst_message_unref (msg);
    }
```

__gst_bus_timed_pop_filtered()__ chờ thực thi kết thúc và trở lại với một __GstMessage__ mà trước đây chúng tôi đã bỏ qua. Chúng tôi hỏi __gst_bus_timed_pop_filtered()__ Để trở lại khi Gstreamer gặp phải một điều kiện lỗi hoặc EOS, vì vậy chúng tôi cần kiểm tra xem nào đã xảy ra và in tin nhắn trên màn hình (ứng dụng của bạn có thể muốn thực hiện các hành động phức tạp hơn).

__GstMessage__ là một cấu trúc rất linh hoạt có thể cung cấp hầu như bất kỳ loại thông tin nào.May mắn thay, Gstreamer cung cấp một loạt các chức năng phân tích cú pháp cho từng loại tin nhắn.

Trong trường hợp này, một khi chúng ta biết thông báo có lỗi (bằng cách sử dụng macro __GST_MESSAGE_TYPE()__), chúng ta có thể sử dụng __gst_message_parse_error()__ trả về cấu trúc lỗi gerror glib và một chuỗi hữu ích để gỡ lỗi. Kiểm tra mã để xem chúng được sử dụng và giải phóng như thế nào sau đó.

## The GStreamer Bus

Tại thời điểm này, đáng để giới thiệu xe buýt __gstreamer__ chính thức hơn một chút.Đây là đối tượng chịu trách nhiệm cung cấp cho ứng dụng __gstmessages__ được tạo bởi các yếu tố, theo thứ tự và cho luồng ứng dụng.Điểm cuối cùng này rất quan trọng, bởi vì việc phát trực tuyến phương tiện thực tế được thực hiện trong một chủ đề khác so với ứng dụng.

__Messages__ có thể được trích xuất từ bus đồng bộ với __GST_BUS_TIMED_POP_FILTERED () __ và anh chị em của nó, hoặc không đồng bộ, sử dụng tín hiệu (hiển thị trong hướng dẫn tiếp theo).Ứng dụng của bạn phải luôn luôn để mắt đến xe buýt để được thông báo về các lỗi và các vấn đề khác liên quan đến phát lại.

Phần còn lại của mã là chuỗi dọn dẹp, giống như trong chương 1 [Hello World!](gstreamer-b-hello-world.md)

## Conclusion _(Phần kết luận)_

Bài hướng dẫn này giới thiệu về:

- Cách tạo các yếu tố với __gst_element_factory_make()__
- Cách tạo một đường ống trống với __gst_pipeline_new()__
- Cách thêm các yếu tố vào đường ống với __gst_bin_add_many()__
- Cách liên kết các yếu tố với nhau với __gst_element_link()__

Điều này kết thúc lần đầu tiên trong hai hướng dẫn dành cho các khái niệm cơ bản của Gstreamer.Cái thứ hai đến tiếp theo.

Hãy nhớ rằng được đính kèm với trang này, bạn nên tìm mã nguồn đầy đủ của hướng dẫn và bất kỳ tệp phụ kiện nào cần thiết để xây dựng nó.

Thật là một niềm vui khi có bạn ở đây, và hẹn gặp lại bạn!

## Một số tham khảo

### gst_element_factory_make

```bash
GstElement * gst_element_factory_make (const gchar * factoryname, const gchar * name)
```

- Hàm này có hai đầu vào là __*factoryname*__ và __*name*__, đều thuộc loại `const gchar *` _(một loại tương đương loại `char *` cơ bản của C thôi, có thể coi là tương đươn)_
    - __*factoryname*__ là tên của kiểu thuộc tính sẽ được tạo, có thể mà một trong ba loại cơ bản là `src`, `filter`, `sync`, ...
    - __*name*__ là tên của phần tử, do người dùng tự định nghĩa. Trong ví dụ nó tương đương với tên biến, nhưng  nói chung là nó thường dùng để "debug" nhiều hơn, và đôi  khi được dùng là tên để các đối tượng khác sử dụng chung đường ống có thể gọi lại đối tượng và sử dụng. Tên có thể để là __NULL__ nếu cảm thấy không cần thiết.
- Đầu ra trả về là một kiểu `GstElement *`, một nguyên tố của __*GStreammer*__, nó đại diện cho mỗi phần tử khi mà tạo mới.
- Nếu không thể tạo, hàm sẽ trả ra con trỏ __NULL__

### Tạo pipeline

3 bước tạo đường ống:

- 
### Ảnh mô tả đường ống tại bằng dot

<figure markdown="span">
    ![alt text](img/gstreamer-u-gstreamer-concepts-0.png)
    <figcaption>Hình: Pipeline Graph</figcaption>
</figure>