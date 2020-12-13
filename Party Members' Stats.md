# Levels

Each character's level has 16 (0x10) bytes. Bytes 00-03 are the EXP required to level up (cumulative). Bytes 04-07 are stats at that particular level. Bytes 08-09, 0A-0B, and 0C-0D are rewards for sword, shield, and staff respectively.

## Explanation for Level's Stats

```
//---------- Level Up Stats ----------
//AA: AP, BB: Defense, CC: Magic, DD: Strength
patch=1,EE,2XXXXXXX,extended,AABBCCDD
//AP gives 1.5x rounded down for Critical mode.
```

You can put stats that the character is supposed to have at that level. Those stats are then added with base AP, boosts, and equipment bonuses to give the final stats. For example:

```
patch=1,EE,21D0B6BC,extended,08162861
patch=1,EE,21D0B6CC,extended,01869284
```

These codes will give Sora base 97 Str, 40 Mag, 22 Def, 8 AP for Level 2 before changing them to 132 Str, 146 Mag, 134 Def, 1 AP for Level 3. The stats CAN decrease, so make sure to fill up every single level's stats.

## Dream Weapon Conditionals

```
//Conditionals to apply only if a certain Dream Weapon is picked
patch=1,EE,E0620X00,extended,0032E02D
X = 0 for Dream Sword, 1 for Dream Shield, 2 for Dream Staff

//Optional Conditionals to apply only at the beginning of the game:
patch=1,EE,E0041A04,extended,0032BAE0 //Location at Garden of Assemblage in Hollow Bastion
patch=1,EE,E0020001,extended,0032BAE8 //Condition is Computer have never been interacted
```

As always with conditionals, don't forget to adjust for the number of lines affected.

## Addresses

Addresses shown below are for the start of the blocks for lv 1 (aka required EXP for lv2). Next level's blocks come immediately after.

```
patch=1,EE,21D0B6A8,extended,XXXXXXXX //Sora
patch=1,EE,21D0BCDC,extended,XXXXXXXX //Donald
patch=1,EE,21D0C310,extended,XXXXXXXX //Goofy
patch=1,EE,21D0C944,extended,XXXXXXXX //Mickey
patch=1,EE,21D0CF78,extended,XXXXXXXX //Auron
patch=1,EE,21D0D5AC,extended,XXXXXXXX //Mulan
patch=1,EE,21D0DBE0,extended,XXXXXXXX //Aladdin
patch=1,EE,21D0E214,extended,XXXXXXXX //Jack Sparrow
patch=1,EE,21D0E848,extended,XXXXXXXX //Beast
patch=1,EE,21D0EE7C,extended,XXXXXXXX //Jack Skellington
patch=1,EE,21D0F4B0,extended,XXXXXXXX //Simba
patch=1,EE,21D0FAE4,extended,XXXXXXXX //Tron
patch=1,EE,21D10118,extended,XXXXXXXX //Riku
```

# Boosts

Sora has a default AP Boost of 50 at Critical and 2 at other difficulties. The rest are all automatic.

```
//AA: Defense, BB: Magic, CC: Power, DD: AP
patch=1,EE,2032E028,extended,AABBCCDD //Sora
patch=1,EE,2032E13C,extended,AABBCCDD //Donald
patch=1,EE,2032E250,extended,AABBCCDD //Goofy
patch=1,EE,2032E364,extended,AABBCCDD //Mickey
patch=1,EE,2032E478,extended,AABBCCDD //Auron
patch=1,EE,2032E58C,extended,AABBCCDD //Mulan
patch=1,EE,2032E6A0,extended,AABBCCDD //Aladdin
patch=1,EE,2032E7B4,extended,AABBCCDD //Jack Sparrow
patch=1,EE,2032E8C8,extended,AABBCCDD //Beast
patch=1,EE,2032E9DC,extended,AABBCCDD //Jack Skellington
patch=1,EE,2032EAF0,extended,AABBCCDD //Simba
patch=1,EE,2032EC04,extended,AABBCCDD //Tron
patch=1,EE,2032ED18,extended,AABBCCDD //Riku
```

# Slots

Make sure to have a total slots of 20 or less. If you trawl through cheat engine, you can see that there's 1 junk byte with each 2-bytes pairs right after showing what are equipped in those slots.

Stats in levels might go down, but the levels themselves won't. So you can jack up the levels without worrying about it reverting. The reverse isn't true, though; it'll go up if you have too much EXP.

```
//AA: Item Slot, BB: Accessory Slot, CC: Armor Slot, DD: Level
patch=1,EE,2032E02F,extended,AABBCCDD //Sora
patch=1,EE,2032E143,extended,AABBCCDD //Donald
patch=1,EE,2032E257,extended,AABBCCDD //Goofy
patch=1,EE,2032E36B,extended,AABBCCDD //Mickey
patch=1,EE,2032E47F,extended,AABBCCDD //Auron
patch=1,EE,2032E593,extended,AABBCCDD //Mulan
patch=1,EE,2032E6A7,extended,AABBCCDD //Aladdin
patch=1,EE,2032E7BB,extended,AABBCCDD //Jack Sparrow
patch=1,EE,2032E8CF,extended,AABBCCDD //Beast
patch=1,EE,2032E9E3,extended,AABBCCDD //Jack Skellington
patch=1,EE,2032EAF7,extended,AABBCCDD //Simba
patch=1,EE,2032EC0B,extended,AABBCCDD //Tron
patch=1,EE,2032ED1F,extended,AABBCCDD //Riku
```

# Abilities

Each ability block is 2-byte long, with the next ability coming right after. If the ability is equipped, it has the value of 0x8000 added to it (so Guard has id 0x0052 while unequipped and 0x8052 while equipped).

Make sure to have a maximum of 80 visible abilities per person (which includes abilities from weapons but not armors or accessories). Depending on how it works, GoA might break this.

```
patch=1,EE,1032E074,extended,0000YXXX //Sora
patch=1,EE,1032E188,extended,0000YXXX //Donald
patch=1,EE,1032E29C,extended,0000YXXX //Goofy
patch=1,EE,1032E3B0,extended,0000YXXX //Mickey (Default Air Combo Plus and Scan)
patch=1,EE,1032E4C4,extended,0000YXXX //Auron
patch=1,EE,1032E5D8,extended,0000YXXX //Mulan
patch=1,EE,1032E6EC,extended,0000YXXX //Aladdin
patch=1,EE,1032E800,extended,0000YXXX //Jack Sparrow
patch=1,EE,1032E914,extended,0000YXXX //Beast
patch=1,EE,1032EA28,extended,0000YXXX //Jack Skellington
patch=1,EE,1032EB3C,extended,0000YXXX //Simba
patch=1,EE,1032EC50,extended,0000YXXX //Tron
patch=1,EE,1032ED64,extended,0000YXXX //Riku
```
