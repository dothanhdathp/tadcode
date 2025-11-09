# \[PlantUml\] Local Server

## Cho máy Ubuntu

- Install Java:
    ```text
    sudo apt update
    sudo apt install openjdk-11-jre -y
    ```
- Download PlantUML Server WAR File
    ```text
    wget https://github.com/plantuml/plantuml-server/releases/latest/download/plantuml.war
    ```
- Install Jetty (Lightweight Servlet Container)
    ```text
    sudo apt install jetty9 -y
    ```
- Deploy PlantUML WAR to Jetty:
    ```text
    sudo mv plantuml.war /var/lib/jetty9/webapps/
    ```
- Start Jetty Server
    ```text
    sudo systemctl restart jetty9
    ```
- Access the PlantUML Server
    ```text
    http://<your-ubuntu-PC-IP>:8080/plantuml
    ```
- ⚠️ Optional: Make It Accessible Remotely
    - Open port 8080 in your firewall:
        ```text
        sudo ufw allow 8080
        ```
    - Ensure your router allows traffic to that PC if you're accessing it from outside your local network.

## Test your uml

```puml
@startuml
Alice -> Bob: Authentication Request
Bob --> Alice: Authentication Response

Alice -> Bob: Another authentication Request
Alice <-- Bob: Another authentication Response
@enduml
```