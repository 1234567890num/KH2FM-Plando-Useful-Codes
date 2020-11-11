```
//Starting Max HP. Max Value is 255 without breaking it.
patch=1,EE,E0052002,extended,0032BAE0
patch=1,EE,E0040001,extended,0032BAE4
patch=1,EE,E0030001,extended,0032BAE6
patch=1,EE,E0020001,extended,0032BAE8
patch=1,EE,01C6C750,extended,000000XX// Current HP
patch=1,EE,01C6C754,extended,000000XX// Max HP

//Starting Max MP. Max Value is 255 without breaking it.
patch=1,EE,E0052002,extended,0032BAE0
patch=1,EE,E0040001,extended,0032BAE4
patch=1,EE,E0030001,extended,0032BAE6
patch=1,EE,E0020001,extended,0032BAE8
patch=1,EE,01C6C8D0,extended,000000XX// Current MP
patch=1,EE,01C6C8D4,extended,000000XX// Max MP

//Starting Drive Gauges (Critical) Place This in the GOA Pnach if you aren't merging.
patch=1,EE,E0042002,extended,0032BAE0
patch=1,EE,E0030001,extended,0032BAE4
patch=1,EE,E0020001,extended,0032BAE6
patch=1,EE,E0010001,extended,0032BAE8
patch=1,EE,11C6C901,extended,00000X0X// 101 is 1 Drive, 505 is 5, etc.

//Starting AP. Going above 255 (FF) causes bugs. Default value is 50 for Crit, 2 for other difficulties
patch=1,EE,E0042002,extended,0032BAE0
patch=1,EE,E0030001,extended,0032BAE4
patch=1,EE,E0020001,extended,0032BAE6
patch=1,EE,E0010001,extended,0032BAE8
patch=1,EE,0032E028,extended,000000XX// Base AP

//Starting Munny
patch=1,EE,E0042002,extended,0032BAE0
patch=1,EE,E0030001,extended,0032BAE4
patch=1,EE,E0020001,extended,0032BAE6
patch=1,EE,E0010001,extended,0032BAE8
patch=1,EE,2032DF70,extended,XXXXXXXX// Starting Munny

//------Starting Gear------
//Starting Keyblade
patch=1,EE,E0042002,extended,0032BAE0
patch=1,EE,E0030001,extended,0032BAE4
patch=1,EE,E0020001,extended,0032BAE6
patch=1,EE,E0010001,extended,0032BAE8
patch=1,EE,1032E020,extended,0000XXXX

//Starting Armor
patch=1,EE,E0042002,extended,0032BAE0
patch=1,EE,E0030001,extended,0032BAE4
patch=1,EE,E0020001,extended,0032BAE6
patch=1,EE,E0010001,extended,0032BAE8
patch=1,EE,1032E034,extended,0000XXXX

//Starting Accessory
patch=1,EE,E0042002,extended,0032BAE0
patch=1,EE,E0030001,extended,0032BAE4
patch=1,EE,E0020001,extended,0032BAE6
patch=1,EE,E0010001,extended,0032BAE8
patch=1,EE,1032E044,extended,0000XXXX
```

Conditionals Explanation:
```
patch=1,EE,E0050003,extended,0032DFC8// Difficulty Determiner. 0=Beginner, 1=Standard, 2=Proud, 3=Critical. This is optional.
patch=1,EE,E0042002,extended,0032BAE0// Location at Station of Serenity
patch=1,EE,E0030001,extended,0032BAE4// Event is selecting dream weapon
patch=1,EE,E0020001,extended,0032BAE6
patch=1,EE,E0010001,extended,0032BAE8
```
Since every code in this file uses the same conditionals, it is possible to combine them all together in one section. 
Be careful not to forget to edit the number of lines affected by the conditionals.
