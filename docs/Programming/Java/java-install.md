# \[Java\] Install

## Windows

- Download JRE: [https://www.java.com/download/ie_manual.jsp](https://www.java.com/download/ie_manual.jsp)
- Download JDK: 
    - [_General_](https://www.oracle.com/java/technologies/downloads/).
    - [Java 25](https://www.oracle.com/java/technologies/downloads/#java25)
    - [Java 21](https://www.oracle.com/java/technologies/downloads/#java21)
    - [Java 17](https://www.oracle.com/java/technologies/downloads/#java17)
    - [Java 11](https://www.oracle.com/java/technologies/downloads/#java11)
    - [Java 8](https://www.oracle.com/java/technologies/downloads/#java8)
    - [Java 8 Enterprise Performance Pack](https://www.oracle.com/java/technologies/downloads/#jepp)

## Linux

=== "openjdk-25"
    ```text
    sudo apt update && sudo apt upgrade -y
    sudo apt install default-jre -y
    sudo apt install default-jdk -y
    sudo apt install openjdk-25-jdk -y
    ```
=== "openjdk-21"
    ```text
    sudo apt update && sudo apt upgrade -y
    sudo apt install default-jre -y
    sudo apt install default-jdk -y
    sudo apt install openjdk-21-jdk -y
    ```

### Verify the Installation

```text
java -version
```
```text
sudo nano /etc/environment
```
```text
echo $JAVA_HOME
```