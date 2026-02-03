# \[PlantUml\] Sequence Diagram

## Mục đích

__Sequence Diagram__ được sử dụng để mô tả luồng hoạt động giữa các lớp, tiến trình

Tham khảo chi tiết tại: [https://plantuml.com/sequence-diagram](https://plantuml.com/sequence-diagram)

## Participant

=== "Types"
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
        skinparam backgroundcolor transparent
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
=== "Participant Color"
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
        skinparam backgroundcolor transparent
        participant Red #red
        participant Green #green
        participant Blue #blue
        @enduml
        ```
      </div>
    </div>
=== "Detail"
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
        skinparam backgroundcolor transparent
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

## Message

=== "Arror Style"
    <div style="display: flex; gap: 20px;">
      <div style="flex: 1;">
        ```text
        @startuml
        Alice ->     Bob : ""->   ""
        Alice ->>    Bob : ""->>  ""
        Alice -\     Bob : ""-\   ""
        Alice -\\    Bob : ""-\\\\""
        Alice -/     Bob : ""-/   ""
        Alice -//    Bob : ""-//  ""
        Alice ->x    Bob : ""->x  ""
        Alice x->    Bob : ""x->  ""
        Alice o->    Bob : ""o->  ""
        Alice ->o    Bob : ""->o  ""
        Alice o->o   Bob : ""o->o ""
        Alice <->    Bob : ""<->  ""
        Alice o<->o  Bob : ""o<->o""
        Alice x<->x  Bob : ""x<->x""
        Alice ->>o   Bob : ""->>o ""
        Alice -\o    Bob : ""-\o  ""
        Alice -\\o   Bob : ""-\\\\o""
        Alice -/o    Bob : ""-/o  ""
        Alice -//o   Bob : ""-//o ""
        Alice x->o   Bob : ""x->o ""
        @enduml
        ```
      </div>
      <div style="flex: 1;">
        ```puml
        @startuml
        skinparam backgroundcolor transparent
        Alice ->     Bob : ""->   ""
        Alice ->>    Bob : ""->>  ""
        Alice -\     Bob : ""-\   ""
        Alice -\\    Bob : ""-\\\\""
        Alice -/     Bob : ""-/   ""
        Alice -//    Bob : ""-//  ""
        Alice ->x    Bob : ""->x  ""
        Alice x->    Bob : ""x->  ""
        Alice o->    Bob : ""o->  ""
        Alice ->o    Bob : ""->o  ""
        Alice o->o   Bob : ""o->o ""
        Alice <->    Bob : ""<->  ""
        Alice o<->o  Bob : ""o<->o""
        Alice x<->x  Bob : ""x<->x""
        Alice ->>o   Bob : ""->>o ""
        Alice -\o    Bob : ""-\o  ""
        Alice -\\o   Bob : ""-\\\\o""
        Alice -/o    Bob : ""-/o  ""
        Alice -//o   Bob : ""-//o ""
        Alice x->o   Bob : ""x->o ""
        @enduml
        ```
      </div>
    </div>
=== "Arror Color"
    <div style="display: flex; gap: 20px;">
      <div style="flex: 1;">
        ```text
        @startuml
        Bob -[#red]> Alice : hello
        Alice -[#0000FF]->Bob : ok
        @enduml
        ```
      </div>
      <div style="flex: 1;">
        ```puml
        @startuml
        skinparam backgroundcolor transparent
        Bob -[#red]> Alice : hello
        Alice -[#0000FF]->Bob : ok
        @enduml
        ```
      </div>
    </div>
=== "In/Out"
    <div style="display: flex; gap: 20px;">
      <div style="flex: 1;">
        ```text
        @startuml
        participant Alice
        participant Bob

        -> Alice : Incommimg message
        Alice -> : Outgoing message

        ?-> Alice : short line
        Alice ->? : short line

        [-> Alice : From Begin
        Alice ->] : To the End
        @enduml
        ```
      </div>
      <div style="flex: 1;">
        ```puml
        @startuml
        skinparam backgroundcolor transparent
        participant Alice
        participant Bob

        -> Alice : Incommimg message
        Alice -> : Outgoing message

        ?-> Alice : short line
        Alice ->? : short line

        [-> Alice : From Begin
        Alice ->] : To the End
        @enduml
        ```
      </div>
    </div>
=== "Duration"
    <div style="display: flex; gap: 20px;">
      <div style="flex: 1;">
        ```text
        @startuml
        !pragma teoz true

        {start} Alice -> Bob : start the process
        Bob -> Cindy: do something start
        Bob -> Cindy: do something ...
        Bob -> Cindy: do something end
        {end} Bob --> Alice: End the process

        {start} <-> {end} : duration\nfor\nsomething

        @enduml
        ```
      </div>
      <div style="flex: 1;">
        ```puml
        @startuml
        skinparam backgroundcolor transparent
        !pragma teoz true

        {start} Alice -> Bob : start the process
        Bob -> Cindy: do something start
        Bob -> Cindy: do something ...
        Bob -> Cindy: do something end
        {end} Bob --> Alice: End the process

        {start} <-> {end} : duration\nfor\nsomething

        @enduml
        ```
      </div>
    </div>

    !!! danger "Danger"
        - Yêu cầu sử dụng `!pragma teoz true`
        - `{start} <-> {end}` là cấu trúc mặc định không thể sửa đổi.
=== "Slanted Arrows"
    <div style="display: flex; gap: 20px;">
      <div style="flex: 1;">
        ```text
        @startuml
        A ->(10) B: text 10
        B ->(10) A: text 10

        A ->(10) B: text 10
        A (10)<- B: text 10
        @enduml
        ```
      </div>
      <div style="flex: 1;">
        ```puml
        @startuml
        skinparam backgroundcolor transparent
        A ->(10) B: text 10
        B ->(10) A: text 10

        A ->(10) B: text 10
        A (10)<- B: text 10
        @enduml
        ```
      </div>
    </div>
=== "Parallel"
    <div style="display: flex; gap: 20px;">
      <div style="flex: 1;">
        ```text
        @startuml
        !pragma teoz true

        A -> B: //<<by pass>>//
        & B -> C: //<<by pass>>//

        A ->(20) B:
        & B ->(20) A:
        & B ->(20) C:
        & C ->(20) B:

        A -> B: "normal message"
        B -> C: "normal message"

        @enduml
        ```
      </div>
      <div style="flex: 1;">
        ```puml
        @startuml
        skinparam backgroundcolor transparent
        !pragma teoz true

        A -> B: //<<by pass>>//
        & B -> C: //<<by pass>>//

        A ->(20) B:
        & B ->(20) A:
        & B ->(20) C:
        & C ->(20) B:

        A -> B: "normal message"
        B -> C: "normal message"

        @enduml
        ```
      </div>
    </div>
    !!! danger "Danger"
        - Yêu cầu sử dụng `!pragma teoz true`
        - Các tiến trình trên một dòng sử dụng `&`

## Activation

=== "Activation"
    Keyword: `activate`, `deactivate`, `destroy`

    <div style="display: flex; gap: 20px;">
      <div style="flex: 1;">
        ```text
        @startuml
        participant User
        User -> A: DoWork
        activate A
        A -> B: << createRequest >>
        activate B
        B -> C: DoWork
        activate C
        C --> B: WorkDone
        destroy C
        B --> A: RequestCreated
        deactivate B
        A -> User: Done
        deactivate A
        @enduml
        ```
      </div>
      <div style="flex: 1;">
        ```puml
        @startuml
        skinparam backgroundcolor transparent
        participant User
        User -> A: DoWork
        activate A
        A -> B: << createRequest >>
        activate B
        B -> C: DoWork
        activate C
        C --> B: WorkDone
        destroy C
        B --> A: RequestCreated
        deactivate B
        A -> User: Done
        deactivate A
        @enduml
        ```
      </div>
    </div>
=== "Activation Color"
    <div style="display: flex; gap: 20px;">
      <div style="flex: 1;">
        ```text
        @startuml
        participant User

        User -> A: DoWork
        activate A #FFBBBB

        A -> A: Internal call
        activate A #DarkSalmon

        A -> B: << createRequest >>
        activate B

        B --> A: RequestCreated
        deactivate B
        deactivate A
        A -> User: Done
        deactivate A
        @enduml
        ```
      </div>
      <div style="flex: 1;">
        ```puml
        @startuml
        skinparam backgroundcolor transparent
        participant User

        User -> A: DoWork
        activate A #FFBBBB

        A -> A: Internal call
        activate A #DarkSalmon

        A -> B: << createRequest >>
        activate B

        B --> A: RequestCreated
        deactivate B
        deactivate A
        A -> User: Done
        deactivate A
        @enduml
        ```
      </div>
    </div>


## Contents And Decore

=== "Title, Header and Footer"
    Keyword: `title`, `header`, `footer`.

    <div style="display: flex; gap: 20px;">
      <div style="flex: 1;">
        ```text
        @startuml
        header Page Header
        footer Page %page% of %lastpage%
        title Example Title
        Alice -> Bob : message 1
        Alice -> Bob : message 2
        @enduml
        ```
      </div>
      <div style="flex: 1;">
        ```puml
        @startuml
        skinparam backgroundcolor transparent
        header Page Header
        footer Page %page% of %lastpage%
        title Example Title
        Alice -> Bob : message 1
        Alice -> Bob : message 2
        @enduml
        ```
      </div>
    </div>
=== "Divider or separator"
    <div style="display: flex; gap: 20px;">
      <div style="flex: 1;">
        ```text
        @startuml
        == Initialization ==
        Alice -> Bob: Authentication Request
        Bob --> Alice: Authentication Response
        == Repetition ==
        Alice -> Bob: Another authentication Request
        Alice <-- Bob: another authentication Response
        @enduml
        ```
      </div>
      <div style="flex: 1;">
        ```puml
        == Initialization ==
        skinparam backgroundcolor transparent
        Alice -> Bob: Authentication Request
        Bob --> Alice: Authentication Response
        == Repetition ==
        Alice -> Bob: Another authentication Request
        Alice <-- Bob: another authentication Response
        @enduml
        ```
      </div>
    </div>

## Note

=== "Shape"
    <div style="display: flex; gap: 20px;">
      <div style="flex: 1;">
        ```text
        @startuml

        participant Alice as A

        note right of A: Normal Shape
        rnote right of A: Rectangle Shape
        hnote right of A: Hexagon Shape

        @enduml
        ```
      </div>
      <div style="flex: 1;">
        ```puml
        @startuml
        skinparam backgroundcolor transparent

        participant Alice as A

        note right of A: right text
        rnote right of A: Rectangle Shape
        hnote right of A: Hexagon Shape

        @enduml
        ```
      </div>
    </div>
=== "Multilines"
    <div style="display: flex; gap: 20px;">
      <div style="flex: 1;">
        ```text
        @startuml

        participant Alice as A

        note over of A
        If this is long text
        need to be display, or
        multilline need
        display/show
        in the page!
        end note

        @enduml
        ```
      </div>
      <div style="flex: 1;">
        ```puml
        @startuml
        skinparam backgroundcolor transparent

        participant Alice as A

        note over of A
        If this is long text
        need to be display, or
        multilline need
        display/show
        in the page!
        end note

        @enduml
        ```
      </div>
    </div>
=== "Aligned"
    <div style="display: flex; gap: 20px;">
      <div style="flex: 1;">
        ```text
        @startuml

        participant Alice as A
        participant Bob as B
        participant Charlin as C
        participant Daisy as D
        participant Emily as E

        note right of A: note right
        note left of A: note left
        note over of A: note over
        note over A, B: note over multi participant

        note across: Note across all part.

        @enduml
        ```
      </div>
      <div style="flex: 1;">
        ```puml
        @startuml
        skinparam backgroundcolor transparent

        participant Alice as A
        participant Bob as B
        participant Charlin as C
        participant Daisy as D
        participant Emily as E

        note right of A: note right
        note left of A: note left
        note over of A: note over
        note over A, B: note over multi participant

        note across: Note across all part.

        @enduml
        ```
      </div>
    </div>
=== "Note Color"
    <div style="display: flex; gap: 20px;">
      <div style="flex: 1;">
        ```text
        @startuml

        participant Alice as A

        note right of A #tomato: right text
        note right of A #lightblue: right text
        note right of A #lightgreen: over text

        @enduml
        ```
      </div>
      <div style="flex: 1;">
        ```puml
        @startuml
        skinparam backgroundcolor transparent

        participant Alice as A

        note right of A #tomato: color tomato
        note right of A #lightblue: color lightblue
        note right of A #lightgreen: color lightgreen

        @enduml
        ```
      </div>
    </div>
=== "Text Style"
    <div style="display: flex; gap: 20px;">
      <div style="flex: 1;">
        ```text
        @startuml
        participant Alice as A

        note over A
          This is **bold**
          This is //italics//
          This is ""monospaced""
          This is --stroked--
          This is __underlined__
          This is ~~waved~~
        end note
        @enduml
        ```
      </div>
      <div style="flex: 1;">
        ```puml
        @startuml
        skinparam backgroundcolor transparent
        participant Alice as A

        note over A
          This is **bold**
          This is //italics//
          This is ""monospaced""
          This is --stroked--
          This is __underlined__
          This is ~~waved~~
        end note
        @enduml
        ```
      </div>
    </div>
=== "Reference"
    Nó gần giống một dạng _note_, dùng để gợi ý đến một phần kiến thức nào đó khác.

    <div style="display: flex; gap: 20px;">
      <div style="flex: 1;">
        ```text
          
        @startuml
        participant Alice
        participant Bob

        ref over Alice, Bob : init
        Alice -> Bob : hello
        ref over Bob
          This can be on
          several lines
        end ref
        @enduml
        ```
      </div>
      <div style="flex: 1;">
        ```puml
          
          skinparam backgroundcolor transparent
        @startuml
        participant Alice
        participant Bob

        ref over Alice, Bob : init
        Alice -> Bob : hello
        ref over Bob
          This can be on
          several lines
        end ref
        @enduml
        ```
      </div>
    </div>

## Group

=== "Group"
    <div style="display: flex; gap: 20px;">
      <div style="flex: 1;">
        ```text
        @startuml
        group Name of Group [The label]
          Alice -> Bob: Authentication Request
          Bob -> Alice: Request Responded
        end
        @enduml
        ```
      </div>
      <div style="flex: 1;">
        ```puml
        @startuml
        skinparam backgroundcolor transparent
        group Name of Group [The label]
          Alice -> Bob: Authentication Request
          Bob -> Alice: Request Responded
        end
        @enduml
        ```
      </div>
    </div>
=== "Alt/Else"
    <div style="display: flex; gap: 20px;">
      <div style="flex: 1;">
        ```text
        @startuml
        Alice -> Bob: Authentication Request
        alt successful case
            Bob -> Alice: Authentication Accepted
        else some kind of failure
            Bob -> Alice: Authentication Failure
        else Another type of failure
          Bob -> Alice: Please repeat
        end
        @enduml
        ```
      </div>
      <div style="flex: 1;">
        ```puml
        @startuml
        skinparam backgroundcolor transparent
        Alice -> Bob: Authentication Request
        alt successful case
            Bob -> Alice: Authentication Accepted
        else some kind of failure
            Bob -> Alice: Authentication Failure
        else Another type of failure
          Bob -> Alice: Please repeat
        end
        @enduml
        ```
      </div>
    </div>
=== "Another Types"
    <div style="display: flex; gap: 20px;">
      <div style="flex: 1;">
        ```text
        @startuml
        loop 1000 times
          Alice -> Bob: Example message
        end
        par The par
          Alice -> Bob: Example message
        end
        break The break
          Alice -> Bob: Example message
        end
        critical The critical
          Alice -> Bob: Example message
        end
        @enduml
        ```
      </div>
      <div style="flex: 1;">
        ```puml
        @startuml
        skinparam backgroundcolor transparent
        loop 1000 times
          Alice -> Bob: Example message
        end
        par The par
          Alice -> Bob: Example message
        end
        break The break
          Alice -> Bob: Example message
        end
        critical The critical
          Alice -> Bob: Example message
        end
        @enduml
        ```
      </div>
    </div>
=== "Group in Group"
    <div style="display: flex; gap: 20px;">
      <div style="flex: 1;">
        ```text
        @startuml
        group Looper [looper ]
          Alice -> Bob: Authentication Request
          group Looper [repeat]
            Alice -> Bob: Authentication Request
          end
          Bob -> Alice: Request Responded
        end
        @enduml
        ```
      </div>
      <div style="flex: 1;">
        ```puml
        group Looper [looper ]
        skinparam backgroundcolor transparent
          Alice -> Bob: Authentication Request
          group Looper [repeat]
            Alice -> Bob: Authentication Request
          end
          Bob -> Alice: Request Responded
        end
        @enduml
        ```
      </div>
    </div>
=== "Group Color"
    <div style="display: flex; gap: 20px;">
      <div style="flex: 1;">
      ```text
      @startuml
      Alice -> Bob: Authentication Request
      alt#Gold #LightBlue Successful case
          Bob -> Alice: Authentication Accepted
      else #Pink Failure
          Bob -> Alice: Authentication Rejected
      end

      group#Gold #LightBlue The Group [Process]
        Alice -> Bob: Authentication Request
        Bob -> Alice: Authentication Accepted
      end

      loop#Gold #LightBlue Process
        Alice -> Bob: Authentication Request
        Bob -> Alice: Authentication Accepted
      end
      @enduml
      ```
      </div>
      <div style="flex: 1;">
      ```puml
      @startuml
      skinparam backgroundcolor transparent
      Alice -> Bob: Authentication Request
      alt#Gold #LightBlue Successful case
          Bob -> Alice: Authentication Accepted
      else #Pink Failure
          Bob -> Alice: Authentication Rejected
      end

      group#Gold #LightBlue The Group [Process]
        Alice -> Bob: Authentication Request
        Bob -> Alice: Authentication Accepted
      end

      loop#Gold #LightBlue Process
        Alice -> Bob: Authentication Request
        Bob -> Alice: Authentication Accepted
      end
      @enduml
      ```
      </div>
    </div>

## Box

=== "Box"
    <div style="display: flex; gap: 20px;">
      <div style="flex: 1;">
      ```text
      @startuml

      box "Internal Service"
      participant Bob
      participant Alice
      end box

      participant Other
      Bob -> Alice : hello
      Alice -> Other : hello
      @enduml
      ```
      </div>
      <div style="flex: 1;">
      ```puml
      @startuml
      skinparam backgroundcolor transparent

      box "Internal Service"
      participant Bob
      participant Alice
      end box

      participant Other
      Bob -> Alice : hello
      Alice -> Other : hello
      @enduml
      ```
      </div>
    </div>
=== "Box Color"
    <div style="display: flex; gap: 20px;">
      <div style="flex: 1;">
      ```text
      @startuml

      box "Internal Service" #LightBlue
      participant Bob
      participant Alice
      end box

      participant Other
      Bob -> Alice : hello
      Alice -> Other : hello
      @enduml
      ```
      </div>
      <div style="flex: 1;">
      ```puml
      @startuml
      skinparam backgroundcolor transparent

      box "Internal Service" #LightBlue
      participant Bob
      participant Alice
      end box

      participant Other
      Bob -> Alice : hello
      Alice -> Other : hello
      @enduml
      ```
      </div>
    </div>
=== "Nest Boxes"
    <div style="display: flex; gap: 20px;">
      <div style="flex: 1;">
      ```text
      @startuml
      !pragma teoz true

      box "Internal Service" #LightBlue
      participant Bob
      box "Subteam"
      participant Alice
      participant John
      end box

      end box
      participant Other

      Bob -> Alice : hello
      Alice -> John : hello
      John -> Other: Hello

      @enduml
      ```
      </div>
      <div style="flex: 1;">
      ```puml
      @startuml
      skinparam backgroundcolor transparent
      !pragma teoz true

      box "Internal Service" #LightBlue
      participant Bob
      box "Subteam"
      participant Alice
      participant John
      end box

      end box
      participant Other

      Bob -> Alice : hello
      Alice -> John : hello
      John -> Other: Hello

      @enduml
      ```
      </div>
    </div>

    !!! danger "Danger"
        - Yêu cầu sử dụng `!pragma teoz true`