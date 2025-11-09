# \[PlantUml\] WBS Diagram

## Mode

=== "OrgMode"
    <div style="display: flex; gap: 20px;">
      <div style="flex: 1;">
        ```text
        @startwbs
        * File
        ** File 1
        *** File 1.1
        ** File 2
        *** File 2.1
        **** File 2.1.1
        @endwbs
        ```
      </div>
      <div style="flex: 1;">
        ```puml
        @startwbs
        * File
        ** File 1
        *** File 1.1
        ** File 2
        *** File 2.1
        **** File 2.1.1
        @endwbs
        ```
      </div>
    </div>
=== "Direction"
    <div style="display: flex; gap: 20px;">
      <div style="flex: 1;">
        ```text
        @startwbs
        * File
        ** File 1
        ***< File 1.1
        ***> File 1.2
        ** File 2
        ***> File 2.1
        ***< File 2.2
        @endwbs
        ```
      </div>
      <div style="flex: 1;">
        ```puml
        @startwbs
        * File
        ** File 1
        ***< File 1.1
        ***> File 1.2
        ** File 2
        ***> File 2.1
        ***< File 2.2
        @endwbs
        ```
      </div>
    </div>
=== "Multilines"
    <div style="display: flex; gap: 20px;">
      <div style="flex: 1;">
        ```text
        @startwbs
        * File
        **: File 1
        Description 1
        Description 2
        Description 3;
        **: File 2
        Description 1
        Description 2
        Description 3;
        @endwbs
        ```
      </div>
      <div style="flex: 1;">
        ```puml
        @startwbs
        * File
        **: File 1
Description 1
Description 2
Description 3;
        **: File 2
Description 1
Description 2
Description 3;
        @endwbs
        ```
      </div>
    </div>
=== "Boxless"
    <div style="display: flex; gap: 20px;">
      <div style="flex: 1;">
        ```text
        @startwbs
        *_ File
        **_ File 1
        ***_ File 1.1
        **_ File 2
        ***_ File 2.1
        ****_ File 2.1.1
        @endwbs
        ```
      </div>
      <div style="flex: 1;">
        ```puml
        @startwbs
        *_ File
        **_ File 1
        ***_ File 1.1
        **_ File 2
        ***_ File 2.1
        ****_ File 2.1.1
        @endwbs
        ```
      </div>
    </div>
=== "Color Box"
    <div style="display: flex; gap: 20px;">
      <div style="flex: 1;">
        ```text
        @startwbs
        *[#tomato] File
        **[#lightblue] File 1
        **[#lightgreen]: File 2
        Description 1
        Description 2
        Description 3;
        @endwbs
        ```
      </div>
      <div style="flex: 1;">
        ```puml
        @startwbs
        *[#tomato] File
        **[#lightblue] File 1
        **[#lightgreen]: File 2
Description 1
Description 2
Description 3;
        @endwbs
        ```
      </div>
    </div>

## Arrows

=== "Arrows"
    <div style="display: flex; gap: 20px;">
      <div style="flex: 1;">
        ```text
        @startwbs
        * File
        ** "File 1" as AA
        *** "File 1.1" as AB
        ** "File 2" as BA
        *** "File 2.1" as BB

        AA -> BA
        BA -> AB
        AB -> BB
        BB -> AA
        @endwbs
        ```
      </div>
      <div style="flex: 1;">
        ```puml
        @startwbs
        * File
        ** "File 1" as AA
        *** "File 1.1" as AB
        ** "File 2" as BA
        *** "File 2.1" as BB

        AA -> BA
        BA -> AB
        AB -> BB
        BB -> AA
        @endwbs
        ```
      </div>
    </div>
=== "Color Arrows"
    <div style="display: flex; gap: 20px;">
      <div style="flex: 1;">
        ```text
        @startwbs
        * File
        ** "File 1" as AA
        *** "File 1.1" as AB
        ** "File 2" as BA
        *** "File 2.1" as BB

        AA -> BA #red
        BA -> AB #green
        AB -> BB #blue
        BB -> AA #gray
        @endwbs
        ```
      </div>
      <div style="flex: 1;">
        ```puml
        @startwbs
        * File
        ** "File 1" as AA
        *** "File 1.1" as AB
        ** "File 2" as BA
        *** "File 2.1" as BB

        AA -> BA #red
        BA -> AB #green
        AB -> BB #blue
        BB -> AA #gray
        @endwbs
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
