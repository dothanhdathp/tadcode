# Marvin

## Tải Về

```bash
sudo apt install maven -y
```

## Tạo Dự Án

```bash
mvn archetype:generate -DgroupId=com.app -DartifactId=my-first-app -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
```

- `-DgroupId=com.app`: Tên gói là **com.app**
- `-DartifactId=my-first-app`: Tên ứng dụng **my-first-app**

Sau khi xong sẽ tạo thành cấu trúc thư mục như này:

```text
.
├── pom.xml
├── src
│   ├── main
│   │   └── java
│   │       └── com
│   │           └── app
│   │               └── App.java
│   └── test
│       └── java
│           └── com
│               └── app
│                   └── AppTest.java
└── target
    ├── classes
    │   └── com
    │       └── app
    │           └── App.class
    └── test-classes
        └── com
            └── app
                └── AppTest.class
```

- **App.java** / **App.class**: Tệp nguồn, mã nguồn gốc của ứng dụng.
- **AppTest.java** / **AppTest.class**: Mã kiểm thử.

## Build

```bash
mvn package
```

## Test

```bash
java -cp target/my-first-app-1.0-SNAPSHOT.jar com.app.App
```
```text title="Kết Quả"
Hello World!
```

## Các Lệnh Khác

```bash
mvn clean	# Xóa thư mục target (dọn dẹp các file đã biên dịch cũ).
mvn compile	# Chỉ biên dịch mã nguồn (không chạy test hay đóng gói).
mvn test	# Chạy các unit test có trong dự án.
mvn install	# Đóng gói dự án và đưa vào kho lưu trữ cục bộ (~/.m2) để các dự án khác có thể dùng chung.
```

## Xử Lý Lỗi

### Mã 1

```bash
[ERROR] Failed to execute goal org.apache.maven.plugins:maven-compiler-plugin:3.1:compile (default-compile) on project my-first-app: Compilation failure: Compilation failure: 
[ERROR] Source option 5 is no longer supported. Use 8 or later.
[ERROR] Target option 5 is no longer supported. Use 8 or later.
```

Hoặc

```text
[ERROR] Failed to execute goal org.apache.maven.plugins:maven-compiler-plugin:3.1:testCompile (default-testCompile) on project my-first-app: Fatal error compiling: error: specified target release 1.5 is too old for the specified source release 1.8
[ERROR]   --release 1.5 is recommended when compiling code to run on JDK 1.5
```

Lỗi này do bla bla ...

Thêm thẻ này vào project là được, tệp `pom.xml`.

```xml
<project>
    <properties>
        <maven.compiler.source>1.5</maven.compiler.source>
    </properties>
</project>
```