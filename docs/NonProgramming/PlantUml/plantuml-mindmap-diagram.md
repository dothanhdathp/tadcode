# \[PlantUml\] MindMap Diagram

## Common

=== "Syntax"
    <div style="display: flex; gap: 20px;">
      <div style="flex: 1;">
        ```text
        @startmindmap
        * root node
            * some first level node
                * second level node
                * another second level node
            * another first level node
        @endmindmap
        ```
      </div>
      <div style="flex: 1;">
        ```puml
        @startmindmap
        skinparam backgroundcolor transparent
        * root node
            * some first level node
                * second level node
                * another second level node
            * another first level node
        @endmindmap
        ```
      </div>
    </div>
=== "Arithmetic"
    <div style="display: flex; gap: 20px;">
      <div style="flex: 1;">
        ```text
        @startmindmap
        + OS
        ++ Ubuntu
        +++ Linux Mint
        +++ Kubuntu
        +++ Lubuntu
        +++ KDE Neon
        ++ LMDE
        ++ SolydXK
        ++ SteamOS
        ++ Raspbian
        -- Windows 95
        -- Windows 98
        -- Windows NT
        --- Windows 8
        --- Windows 10
        --- Windows 11
        @endmindmap
        ```
      </div>
      <div style="flex: 1;">
        ```puml
        @startmindmap
* OS
** Ubuntu
*** Linux Mint
*** Kubuntu
*** Lubuntu
*** KDE Neon
** LMDE
** SolydXK
** SteamOS
** Raspbian
-- Windows 95
-- Windows 98
-- Windows NT
--- Windows 8
--- Windows 10
--- Windows 11
        @endmindmap
        ```
      </div>
    </div>
=== "Multilines"
    <div style="display: flex; gap: 20px;">
      <div style="flex: 1;">
        ```text
        @startmindmap
        * Class Templates
        **:Example 1
        <code>
        template <typename T>
        class cname{
        void f1()<U+003B>
        ...
        }
        </code>
        ;
        **:Example 2
        <code>
        other template <typename T>
        class cname{
        ...
        </code>
        ;
        @endmindmap
        ```
      </div>
      <div style="flex: 1;">
        ```puml
        @startmindmap
* Class Templates
**:Example 1
<code>
template <typename T>
class cname{
void f1()<U+003B>
...
}
</code>
;
**:Example 2
<code>
other template <typename T>
class cname{
...
</code>
;
        @endmindmap
        ```
      </div>
    </div>
=== "Multiroot"
    <div style="display: flex; gap: 20px;">
        <div style="flex: 1;">
            ```text
            @startmindmap
            * Root 1
            ** Foo
            ** Bar
            * Root 2
            ** Lorem
            ** Ipsum
            @endmindmap
            ```
        </div>
        <div style="flex: 1;">
            ```puml
            @startmindmap
            * Root 1
            ** Foo
            ** Bar
            * Root 2
            ** Lorem
            ** Ipsum
            @endmindmap
            ```
        </div>
    </div>
=== "Color"
    <div style="display: flex; gap: 20px;">
    <div style="flex: 1;">
        ```text
        @startmindmap
        *[#Orange] Colors
        **[#lightgreen] Green
        **[#FFBBCC] Rose
        **[#lightblue] Blue
        @endmindmap
        ```
    </div>
    <div style="flex: 1;">
        ```puml
        @startmindmap
        *[#Orange] Colors
        **[#lightgreen] Green
        **[#FFBBCC] Rose
        **[#lightblue] Blue
        @endmindmap
        ```
    </div>
    </div>
=== "NoBox"
    <div style="display: flex; gap: 20px;">
    <div style="flex: 1;">
        ```text
        @startmindmap
        *_ root node
        **_ some first level node
        ***_ second level node
        ***_ another second level node
        ***_ foo
        ***_ bar
        ***_ foobar
        **_ another first level node
        @endmindmap
        ```
    </div>
    <div style="flex: 1;">
        ```puml
        @startmindmap
        *_ root node
        **_ some first level node
        ***_ second level node
        ***_ another second level node
        ***_ foo
        ***_ bar
        ***_ foobar
        **_ another first level node
        @endmindmap
        ```
    </div>
    </div>

## Direction

=== "Left to Right (Default)"
    <div style="display: flex; gap: 20px;">
      <div style="flex: 1;">
        ```text
        @startmindmap
        * 1
        ** 2
        *** 4
        *** 5
        ** 3
        *** 6
        *** 7
        @endmindmap
        ```
      </div>
      <div style="flex: 1;">
        ```puml
        @startmindmap
        * 1
        ** 2
        *** 4
        *** 5
        ** 3
        *** 6
        *** 7
        @endmindmap
        ```
      </div>
    </div>
=== "Top to Bottom"
    <div style="display: flex; gap: 20px;">
      <div style="flex: 1;">
        ```text
        @startmindmap
        top to bottom direction
        * 1
        ** 2
        *** 4
        *** 5
        ** 3
        *** 6
        *** 7
        @endmindmap
        ```
      </div>
      <div style="flex: 1;">
        ```puml
        @startmindmap
        top to bottom direction
        * 1
        ** 2
        *** 4
        *** 5
        ** 3
        *** 6
        *** 7
        @endmindmap
        ```
      </div>
    </div>
=== "Right to Left"
    <div style="display: flex; gap: 20px;">
      <div style="flex: 1;">
        ```text
        @startmindmap
        right to left direction
        * 1
        ** 2
        *** 4
        *** 5
        ** 3
        *** 6
        *** 7
        @endmindmap
        ```
      </div>
      <div style="flex: 1;">
        ```puml
        @startmindmap
        right to left direction
        * 1
        ** 2
        *** 4
        *** 5
        ** 3
        *** 6
        *** 7
        @endmindmap
        ```
      </div>
    </div>
=== "Side H"
    <div style="display: flex; gap: 20px;">
      <div style="flex: 1;">
        ```text
        @startmindmap
        * 0
        right side
        ** 1
        ** 2
        *** 3
        *** 4
        left side
        ** -1
        ** -2
        *** -3
        *** -4
        @endmindmap
        ```
      </div>
      <div style="flex: 1;">
        ```puml
        @startmindmap
        * 0
        right side
        ** 1
        ** 2
        *** 3
        *** 4
        left side
        ** -1
        ** -2
        *** -3
        *** -4
        @endmindmap
        ```
      </div>
    </div>
=== "Side V"
    <div style="display: flex; gap: 20px;">
      <div style="flex: 1;">
        ```text
        @startmindmap
        top to bottom direction
        * 0
        right side
        ** 1
        ** 2
        *** 3
        *** 4
        left side
        ** -1
        ** -2
        *** -3
        *** -4
        @endmindmap
        ```
      </div>
      <div style="flex: 1;">
        ```puml
        @startmindmap
        top to bottom direction
        * 0
        right side
        ** 1
        ** 2
        *** 3
        *** 4
        left side
        ** -1
        ** -2
        *** -3
        *** -4
        @endmindmap
        ```
      </div>
    </div>

## Creole

=== "Creole"
    <div style="display: flex; gap: 20px;">
      <div style="flex: 1;">
        ```text
        @startmindmap
        *:==Creole
        This is **bold**
        This is //italics//
        This is ""monospaced""
        This is --stricken-out--
        This is __underlined__
        This is ~~wave-underlined~~
        --test Unicode and icons--
        This is <U+221E> long
        This is a <&code> icon
        Use image : <img:https://plantuml.com/logo3.png>
        ;
        @endmindmap
        ```
      </div>
      <div style="flex: 1;">
        ```puml
        @startmindmap
*:==Creole
This is **bold**
This is //italics//
This is ""monospaced""
This is --stricken-out--
This is __underlined__
This is ~~wave-underlined~~
--test Unicode and icons--
This is <U+221E> long
This is a <&code> icon
Use image : <img:https://plantuml.com/logo3.png>
;
        @endmindmap
        ```
      </div>
    </div>
=== "HTML Creole"
    <div style="display: flex; gap: 20px;">
      <div style="flex: 1;">
        ```text
        @startmindmap
        *: <b>HTML Creole 
        This is <b>bold</b>
        This is <i>italics</i>
        This is <font:monospaced>monospaced</font>
        This is <s>stroked</s>
        This is <u>underlined</u>
        This is <w>waved</w>
        This is <s:green>stroked</s>
        This is <u:red>underlined</u>
        This is <w:#0000FF>waved</w>
        -- other examples --
        This is <color:blue>Blue</color>
        This is <back:orange>Orange background</back>
        This is <size:20>big</size>
        ;
        @endmindmap
        ```
      </div>
      <div style="flex: 1;">
        ```puml
        @startmindmap
*: <b>HTML Creole 
This is <b>bold</b>
This is <i>italics</i>
This is <font:monospaced>monospaced</font>
This is <s>stroked</s>
This is <u>underlined</u>
This is <w>waved</w>
This is <s:green>stroked</s>
This is <u:red>underlined</u>
This is <w:#0000FF>waved</w>
-- other examples --
This is <color:blue>Blue</color>
This is <back:orange>Orange background</back>
This is <size:20>big</size>
;
        @endmindmap
        ```
      </div>
    </div>
=== "Creole line"
    <div style="display: flex; gap: 20px;">
      <div style="flex: 1;">
        ```text
        @startmindmap
        *:==Creole line
        You can have horizontal line
        ----
        Or double line
        ====
        Or strong line
        ____
        Or dotted line
        ..My title..
        Or dotted title
        //and title... //
        ==Title==
        Or double-line title
        --Another title--
        Or single-line title
        Enjoy!
        ;
        @endmindmap
        ```
      </div>
      <div style="flex: 1;">
        ```puml
        @startmindmap
*:==Creole line
You can have horizontal line
----
Or double line
====
Or strong line
____
Or dotted line
..My title..
Or dotted title
//and title... //
==Title==
Or double-line title
--Another title--
Or single-line title
Enjoy!
;
        @endmindmap
        ```
      </div>
    </div>
=== "Creole List Item"
    <div style="display: flex; gap: 20px;">
      <div style="flex: 1;">
        ```text
        @startmindmap
        *:==Creole list item
        **test list 1**
        * Bullet list
        * Second item
        ** Sub item
        *** Sub sub item
        * Third item
        ----
        **test list 2**
        # Numbered list
        # Second item
        ## Sub item
        ## Another sub item
        # Third item
        ;
        @endmindmap
        ```
      </div>
      <div style="flex: 1;">
        ```puml
        @startmindmap
*:==Creole list item
**test list 1**
* Bullet list
* Second item
** Sub item
*** Sub sub item
* Third item
----
**test list 2**
# Numbered list
# Second item
## Sub item
## Another sub item
# Third item
;
        @endmindmap
        ```
      </div>
    </div>
