# \[C++\] Atomic

__atomic__ là loại biến đặc biệt sẽ tự đồng bộ hóa, an toàn với luồng và đảm bảo chương trình diễn ra theo thứ tự dự đoán được. Thường dùng trong lập trình đa luồng.

Để tối ưu hóa hiệu suất, CPU thường chọn cách *tự bản thân tối ưu quy trình* dẫn đến thứ tự các phép toán thực hiện sai, không đúng ý đồ, dẫn đến chương trình thực hiện sai hoặc nhiều nhất chính là treo.

## Tại sao cần Atomic

Có ba vấn đề chính dẫn đến việc biến atomic cần phải có:

1. Sự tối ưu hóa luồng của __*compiler*__: Các trình biên dịch có tự _thông minh_ để tối ưu hóa cho một đoạn mã nào đó khiến chúng nhanh hơn bình thường. Điều đó là tốt, nhưng vấn đề là góc nhìn của chúng hạn chế ở đơn luồng, thế nên ở cấc tác vụ đa luồng, kém. Ví dụ dơn giản nhất là với đơn luồng loop, khi đó nó sẽ tối ưu để CPU thực hiện toàn bộ công việc ở đó trước rồi mới cho luồng khác thực thi, điều đó dẫn đến việc chương trình bị treo _(hang)_ khi thực thi đa luồng trên biến cục bộ.
2. Điểm thứ hai cần lưu ý là __*CPU có cache*__! Công việc đơn luồng ở trên là một ví dụ, nếu tác vụ nhẹ hoặc lặp lại biến, giá trị nào đó, nó sẽ lưu giá trị vào cache và tiếp tục thực hiện thay vì lưu lại giá trị về ram trong các vòng lặp luồng. Điều đó dẫn đến việc nếu luồng 1 thực thi nó sẽ liên tục lặp và tiếp đang hoạt động với giá trị X chẳng hạn, thế nhưng luồng B khi đọc ra lại có thể là giá trị Y. Bởi vì để _tối ưu luồng cache_ cho luồng 1, giá trị tại biến đó đã bị lưu lại và sử dụng trong CPU cache, còn luồng B đọc ra lại là giá trị trên RAM, giá trị thực.<br>Thực ra việc đó là bình thường. Luồng 1 vẫn sẽ cập nhật lại giá trị, chỉ là không cùng thời điểm. Biến atomic sẽ ép cho giá trị bắt buộc ghi vào giá trị thanh ghi mới tính là kết thúc một phiên, giúp cho giá trị luôn được cập nhật.
3. Cuối cùng là lý do an toàn luồng, tối đa sự đồng bộ giữa các luồng thực thi, giúp cho giá trị được ghi vào / đọc ra chính xác và ổn định. Các luồng hoạt động đồng bộ, bất đồng bộ cùng thực hiện trên cùng một biến chính xác, tránh trường hợp cache như trên. Chẳng hạn nếu biến a được cập nhập, thì tại luồng thứ hai biến a cũng đang thao tác trên cùng vùng nhớ đó. Sự kiện này thường được sử dụng trong các tác vụ liên quan đến hình ảnh hoặc âm thanh, đảm bảo tính chính xác và vẹn toàn, hạn chế lỗi bất đồng bộ.

| Feature       | Non-Atomic (Raw Value)                                           | Atomic                                                    |
| :------------ | :--------------------------------------------------------------- | :-------------------------------------------------------- |
| Compiler View | Giả sử single-threaded; tối ưu hóa mạnh mẽ.                      | Giả sử các chủ đề khác có thể thay đổi nó bất cứ lúc nào. |
| Hardware View | Sử dụng bộ đệm/đăng ký cục bộ một cách tự do.                    | Buộc đồng bộ hóa bộ đệm (Memory Barriers).                |
| Kết quả       | Có khả năng xảy ra các vòng lặp vô hạn (bị treo) hoặc gặp sự cố. | "An toàn cho luồng, hiển thị và có thể dự đoán được."     |

## Thuộc tính

`atomic` có vẻ như chỉ là một khai báo. Có thể sử dụng atomic cho cả `class`, `struct` hoặc biến thành viên trong `class`, `struct`, ... Một số kiểu biến đặc biệt khác chưa thử, nhưng có lẽ cũng được. Vấn đề còn lại chỉ là nên xem xét các biến atomic hạn chế sử dụng, không nên lạm dụng.

Biến `atomic` nhanh hơn __*mutex*__, nhưng lại chậm hơn biến thông thường. An toàn với đọc ghi, nhưng trong các tiến trình liên tục cần đồng bộ hóa mạnh thì mutex lại tốt hơn vì nó sử dụng cơ chế khóa thực thi cho hẳn luồng.

## Ví dụ

```cpp
#include <iostream>
#include <thread>
#include <atomic>

#define sleep_for_ms(v)  std::this_thread::sleep_for(std::chrono::milliseconds(v));

// std::atomic_int value = 0;
std::atomic<int> value = 0;
// int             value = 0;

void thread_read(const char* thread_name) {
    while(value < 10000) {
        std::cout << "<" << value << ">";
    }
}

void thread_write(const char* thread_name) {
    while(value < 10000) {
        ++value;
    }
}

int main(int argc, const char* args[]) {
    std::jthread thread_r(thread_read,  nullptr);
    std::jthread thread_w0(thread_write, nullptr);
    std::jthread thread_w1(thread_write, nullptr);
    std::jthread thread_w2(thread_write, nullptr);
    std::jthread thread_w3(thread_write, nullptr);
    return 0;
}
```

Trong trường hợp sử dụng biến atomic, mỗi quá trình đọc trả ra một giá trị ví dụ như là:

```text
<1518><1672><1681><1689><1698><1709><1719><1730><1739><1749><1762><1773><1781><1791><1797><1802><1811><1817><1823><1831><1839><1848><1855><1867><1881><1888><1898><1905><1916><1925><1932><1943><1949><1953><1959><1967><1978><1984><1991><2000><2008><2016><2026><2034><2043><2048><2052><2057><2067><2073><2081><2091><2102><2112><2121><2128><2135><2143><2150><2157><2167><2178><2188><2206><2217><2224><2233><2241><2247><2253><2258><2262><2270><2276><2290><2295><2303><2311><2319><2329><2338><2350><2366><2375><2384><2390><2402><2419><2428><2435><2445><2457><2466><2474><2486><2495><2499><2509><2527><2539><2552><2565><2580><2594><2610><2628><2653><2675><2687><2705><2719><2736><2751><2766><2780><2797><2812><2836><2850><2871><2889><2896><2908><2922><2939><2953><2974><2991><3005><3031><3042><3053><3067><3095><3120><3137><3162><3172><3185><3200><3219><3243><3271><3287><3319><3328><3340><3362><3375><3394><3420><3438><3456><3479><3509><3538><3575><3601><3631><3649><3662><3673><3700><3720><3751><3770><3797><3831><3857><3882><3912><4421><4442><4451><4468><4497><4528><4555><4578><4596><4628><4655><4679><4702><4731><4754><4789><4828><4853><4873><4894><4922><4949><4974><4989><5010><5037><5062><5093><5134><5149><5171><5196><5216><5240><5281><5309><5326><5358><5367><5393><5411><5433><5455><5481><5506><5524><5550><5577><5592><5626><5651><5663><5682><5710><5724><5754><5764><5792><5804><5818><5839><5873><5897><5918><5939><5961><5985><6003><6028><6055><6081><6101><6116><6133><6156><6171><6203><6231><6251><6281><6308><6334><6353><6384><6405><6431><6447><6463><6493><6514><6536><6548><6575><6597><6619><6631><6652><6671><6691><6709><6728><6748><6775><6792><6816><6834><6847><6869><6891><6916><6932><6953><6981><7010><7030><7055><7068><7102><7123><7150><7177><7198><7218><7229><7259><7283><7298><7315><7328><7349><7369><7392><7417><7438><7452><7472><7496><7524><7548><7568><7594><7623><7643><7668><7701><7716><7737><7767><7786><7812><7829><7870><7897><7926><7950><7964><7987><8000><8025><8055><8090><8111><8133><8147><8175><8198><8222><8234><8253><8271><8291><8530><8539><8560><8588><8632><8645><8665><8685><8707><8733><8744><8767><8788><8808><8829><8845><8881><8902><8925><8952><8972><8988><9006><9036><9065><9090><9123><9149><9171><9191><9225><9246><9273><9286><9306><9329><9352><9386><9407><9429><9451><9478><9495><9516><9535><9567><9583><9611><9643><9660><9674><9692><9724><9758><9773><9792><9820><9857><9889><9903><9922><9941><9964><9994>
```

Nhưng nếu sử dụng biến thông thường, luồng write bị khóa và kết quả chỉ có:

```text
<10000>
```