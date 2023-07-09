# Otter Cheat Manager or OCM

## What is it?
***

OCM is a Python driven, browser based, framework for video game cheat files.

## How does it work?
***
Cheat menus are built into modules (Oysters) and are then interpreted by OCM.

## Oysters and Shellfish
***
Each Oyster file is composed of a set of instructions that is used to build out your cheat menu for a particular game. The "language" of Oysters is Shellfish. Each default line in Shellfish is used to build a singular interactive cheat. Each line of Shellfish after the header is defined by a "shellfish" and its "meat".
```
{} <- This is a Shellfish
# <- This is a comment meat
```
