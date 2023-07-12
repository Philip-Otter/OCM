# Otter Cheat Manager or OCM

## What is it?
***

OCM is a Python driven, browser based, framework for video game cheat files.

## How does it work?
***
Cheat menus are built into modules (Oysters) and are then interpreted by OCM.

## Oysters and 5H3LLf15H
***
Each Oyster file is composed of a set of instructions that is used to build out your cheat menu for a particular game. The "language" of Oysters is 5H3LLf15H. Each default line in 5H3LLf15H is used to build a singular interactive cheat. In general each line is prefixed by a "shell" and its "meat". Combined they make a unique shellfish.
```
{} <- This is a shell
# <- This is a comment meat
```
### Below is a table of Shellfish and their meat

| shellfish + meat | Use                                                                                       |
|------------------|-------------------------------------------------------------------------------------------|
| {}               | The default shellfish. This is where you put your one line - one cheat information.       |
| {#}              | A comment shellfish. This will get ignored by the interpreter.                            |
| {@}              | The Modder shellfish. This is where we provide the modder's name.                         |
| {V}              | The version shellfish. This is where we provide the game version the cheat was made with. |
| {X}              | The architecture shellfish. This is where we define if the application is 64 or 32 bit    |
| {APP}            | The application shellfish. This defines our application file. Generally an .exe file.     |
| {T}              | The target shellfish. Use this if all your mods base off the same .exe or .dll            |
| {C}              | The theme shellfish. Use this to select a non standard theme.                             |
| {H5}             | An HTML shellfish. This will allow HTML to be inserted into the cheat menu.               |
| {JS}             | A JavaScript shellfish. This will allow Javascript to be inserted into the cheat menu.    |
| {P3}             | A Python 3 shellfish. This will allow Python to be inserted into the generated cheat file.|
| {END}            | An end shellfish. This is used to mark the end of an Oyster makers custom shellfish       |


In 5H3LLf15H the order of the following shellfish does not matter `{#} {@} {V} {T} {C} {X} {APP}`. All other Shellfish will be interpreted from top to bottom.

### The Default Shellfish

This is the bread and butter of an oyster file. Here the default shellfish is used. The line following our default shellfish is organized in the following manner:

#### <b>Without</b> {T} shellfish set:

`{}Interaction:Name|BaseOffset:OffsetsCommaSeperatedList>Value<TargetModule`

Example:
`{}Toggle:Infinite Ammo|0x040830C8:0x10, 0xA8, 0x98, 0x300, 0x10, 0x3A8, 0x2E8>999<CrabChampions-Win64-Shipping.exe`

#### <b>With</b> {T} shellfish set:

`{}Interaction:Name|BaseOffset:OffsetsCommaSeperatedList>Value`

Example:
`{}Toggle:Infinite Ammo|0x040830C8:0x10, 0xA8, 0x98, 0x300, 0x10, 0x3A8, 0x2E8>999`

### The Comment Shellfish

The comment shellfish can be used to add comments inside of an oyster file. Any line that is preceded by a comment shellfish will be ignored by the interpreter. With the exception of lines sandwiched between an {H5}, {JS}, {P3} shellfish and an {END} shellfish.

Syntax:
`{#} Otters Love 5H3LLf15H`

Example:
`{#} The following mod will only work while inside of combat`

***
***
## Copyright 2023 Philip Otter