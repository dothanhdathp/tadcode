# \[PlantUml\] Sequence Diagram

## Mục đích

__Sequence Diagram__ được sử dụng để vẻ và mô tả luồng hoạt động

## Examples

<div style="display: flex; gap: 20px;">
  <div style="flex: 1;">
    ```text
    @startuml
    Alice -> Bob: Authentication Request
    Bob --> Alice: Authentication Response

    Alice -> Bob: Another authentication Request
    Alice <-- Bob: Another authentication Response
    @enduml
    ```
  </div>
  <div style="flex: 1;">
    ```puml
    @startuml
    Alice -> Bob: Authentication Request
    Bob --> Alice: Authentication Response

    Alice -> Bob: Another authentication Request
    Alice <-- Bob: Another authentication Response
    @enduml
    ```
  </div>
</div>

## Participant

### Các loại

<div style="display: flex; gap: 20px;">
  <div style="flex: 1;">
    ```text
    @startuml
    participant Participant as Foo
    actor       Actor       as Foo1
    boundary    Boundary    as Foo2
    control     Control     as Foo3
    entity      Entity      as Foo4
    database    Database    as Foo5
    collections Collections as Foo6
    queue       Queue       as Foo7
    @enduml
    ```
  </div>
  <div style="flex: 1;">
    ```puml
    @startuml
    participant Participant as Foo
    actor       Actor       as Foo1
    boundary    Boundary    as Foo2
    control     Control     as Foo3
    entity      Entity      as Foo4
    database    Database    as Foo5
    collections Collections as Foo6
    queue       Queue       as Foo7
    @enduml
    ```
  </div>
</div>

### Color

<div style="display: flex; gap: 20px;">
  <div style="flex: 1;">
    ```text
    @startuml
    participant Red #red
    participant Green #green
    participant Blue #blue
    @enduml
    ```
  </div>
  <div style="flex: 1;">
    ```puml
    @startuml
    participant Red #red
    participant Green #green
    participant Blue #blue
    @enduml
    ```
  </div>
</div>

### Multiline

<div style="display: flex; gap: 20px;">
  <div style="flex: 1;">
    ```text
    @startuml
    participant Multiline [
        =Title
        ----
        ""SubTitle""
        **SubTitle**
        //SubTitle//
    ]
    @enduml
    ```
  </div>
  <div style="flex: 1;">
    ```puml
    @startuml
    participant Multiline [
        =Title
        ----
        ""SubTitle""
        **SubTitle**
        //SubTitle//
    ]
    @enduml
    ```
  </div>
</div>

### 