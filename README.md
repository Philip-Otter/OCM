# Otter Cheat Manager or OCM

## What is it?
***

OCM is a Python driven, browser based, framework for video game cheat files.

## How does it work?
***
Cheat menus are built into modules (Oysters) and are then interpreted by OCM.

## Oysters and 5H3LLf15H
***
Each Oyster file is composed of a set of instructions that is used to build out your cheat menu for a particular game. The "language" of Oysters is 5H3LLf15H. Each default line in 5H3LLf15H is used to build a singular interactive cheat. Each line after the header is defined by a "shell" and its "meat". Combined they make a unique shellfish.
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
| {v}              | The version shellfish. This is where we provide the game version the cheat was made with. |
| {T}              | The target shellfish. Use this if all your mods base off the same .exe or .dll            |
| {H5}             | An HTML shellfish. This will allow HTML to be inserted into the cheat menu.               |
| {JS}             | A JavaScript shellfish. This will allow Javascript to be inserted into the cheat menu.    |
| {P3}             | A Python 3 shellfish. This will allow Python to be inserted into the generated cheat file.|
