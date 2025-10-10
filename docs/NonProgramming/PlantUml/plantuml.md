# \[PlantUml\]

## Giới thiệu

PlantUML là một công cụ rất linh hoạt tạo điều kiện tạo ra sự tạo ra nhanh chóng và đơn giản của một loạt các sơ đồ.

## Supported UML Diagrams


### [Sequence Diagram](./plantuml-sequence-diagram.md)

```puml
@startuml
Alice -> Bob: Authentication Request
Bob --> Alice: Authentication Response

Alice -> Bob: Another authentication Request
Alice <-- Bob: Another authentication Response
@enduml
```

<div style="text-align: center; font-style: italic;">
Sequence Diagram Example
</div>


### [Usecase diagram](./plantuml-usecase-diagram.md)

```puml
@startuml
:Main Admin: as Admin
(Use the application) as (Use)

User -> (Start)
User --> (Use)

Admin ---> (Use)

note right of Admin : This is an example.

note right of (Use)
  A note can also
  be on several lines
end note

note "This note is connected\nto several objects." as N2
(Start) .. N2
N2 .. (Use)
@enduml
```

<div style="text-align: center; font-style: italic;">
Usecase Diagram Example
</div>

### [Class diagram](./plantuml-class-diagram.md)

```puml
@startuml

abstract class AbstractList
abstract AbstractCollection
interface List
interface Collection

List <|-- AbstractList
Collection <|-- AbstractCollection

Collection <|- List
AbstractCollection <|- AbstractList
AbstractList <|-- ArrayList

class ArrayList {
    Object[] elementData
    size()
}
@enduml
```

<div style="text-align: center; font-style: italic;">
Class diagram Example
</div>

### [Object diagram](./plantuml-object-diagram.md)



### [Activity diagram](./plantuml-activity-diagram.md)

```puml
@startuml
start
:Hello world;
:This is defined on
several **lines**;
stop
@enduml
```

<div style="text-align: center; font-style: italic;">
Activity Diagram Example
</div>

### [Component diagram](./plantuml-component-diagram.md)



### [Deployment diagram](./plantuml-deployment-diagram.md)



### [State diagram](./plantuml-state-diagram.md)



### [Timing diagram](./plantuml-timing-diagram.md)