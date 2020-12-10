# Sora's Starting Stats

```
//Starting Max HP. Max Value is 255 without breaking it.
patch=1,EE,E0032002,extended,0032BAE0
patch=1,EE,E0020001,extended,0032BAE8
patch=1,EE,01C6C750,extended,000000XX// Current HP
patch=1,EE,01C6C754,extended,000000XX// Max HP

//Starting Max MP. Max Value is 255 without breaking it.
patch=1,EE,E0032002,extended,0032BAE0
patch=1,EE,E0020001,extended,0032BAE8
patch=1,EE,01C6C8D0,extended,000000XX// Current MP
patch=1,EE,01C6C8D4,extended,000000XX// Max MP

//Starting Drive Gauges. Place This in the GOA Pnach if you aren't merging.
patch=1,EE,E0022002,extended,0032BAE0
patch=1,EE,E0010001,extended,0032BAE8
patch=1,EE,11C6C901,extended,00000X0X// 101 is 1 Drive, 505 is 5, etc.
//See 'Drive Forms & Summons.md' for details.

//Starting AP. Going above 255 (FF) causes bugs. Default value is 50 for Crit, 2 for other difficulties
patch=1,EE,E0022002,extended,0032BAE0
patch=1,EE,E0010001,extended,0032BAE8
patch=1,EE,0032E028,extended,000000XX// Base AP

//Starting Munny
patch=1,EE,E0022002,extended,0032BAE0
patch=1,EE,E0010001,extended,0032BAE8
patch=1,EE,2032DF70,extended,XXXXXXXX// Starting Munny

//------Starting Gear------
//Starting Keyblade
patch=1,EE,E0022002,extended,0032BAE0
patch=1,EE,E0010001,extended,0032BAE8
patch=1,EE,1032E020,extended,0000XXXX

//Starting Armor
patch=1,EE,E0022002,extended,0032BAE0
patch=1,EE,E0010001,extended,0032BAE8
patch=1,EE,1032E034,extended,0000XXXX

//Starting Accessory
patch=1,EE,E0022002,extended,0032BAE0
patch=1,EE,E0010001,extended,0032BAE8
patch=1,EE,1032E044,extended,0000XXXX
```

# MP Costs

Setting MP Costs without any conditionals will crash the game when starting. They are never overwritten by the game other than during the bootup. To make it last the entire game, we can make said conditional the beginning of the game.

```
//Conditional
patch=1,EE,E0252002,extended,0032BAE0
patch=1,EE,E0240001,extended,0032BAE8
//Spells
patch=1,EE,01CCBCE0,extended,000000XX// Fire// 0C
patch=1,EE,01CCC8E0,extended,000000XX// Fira// 0C
patch=1,EE,01CCC910,extended,000000XX// Firaga// 0C
patch=1,EE,01CCBD40,extended,000000XX// Blizzard// 0F
patch=1,EE,01CCC940,extended,000000XX// Blizzara// 0F
patch=1,EE,01CCC970,extended,000000XX// Blizzaga// 0F
patch=1,EE,01CCBD10,extended,000000XX// Thunder// 12
patch=1,EE,01CCC9A0,extended,000000XX// Thundara// 12
patch=1,EE,01CCC9D0,extended,000000XX// Thundaga// 12
patch=1,EE,01CCBD70,extended,000000XX// Cure// FF
patch=1,EE,01CCCA00,extended,000000XX// Cura// FF
patch=1,EE,01CCCA30,extended,000000XX// Curaga// FF
patch=1,EE,01CCD240,extended,000000XX// Magnet// 1E
patch=1,EE,01CCD270,extended,000000XX// Magnera// 1E
patch=1,EE,01CCD2A0,extended,000000XX// Magnega// 1E
patch=1,EE,01CCD2D0,extended,000000XX// Reflect// 0A
patch=1,EE,01CCD300,extended,000000XX// Reflera// 0A
patch=1,EE,01CCD330,extended,000000XX// Reflega// 0A
//Limit Form Abilities
patch=1,EE,01CD3150,extended,000000XX// Strike Raid// 41
patch=1,EE,01CD3030,extended,000000XX// Sonic Blade// 3C
patch=1,EE,01CD2F10,extended,000000XX// Ragnarok// 50
patch=1,EE,01CD30C0,extended,000000XX// Ars Arcanum// 48
//Limits
patch=1,EE,01CCC130,extended,000000XX// Twin Howl// FF
patch=1,EE,01CCC2B0,extended,000000XX// Bushido// FF
patch=1,EE,01CCCC40,extended,000000XX// Red Rocket//FF 
patch=1,EE,01CCE110,extended,000000XX// Whirli-Goof// FF
patch=1,EE,01CCE620,extended,000000XX// Comet// FF
patch=1,EE,01CCF040,extended,000000XX// Knocksmash// FF
patch=1,EE,01CCF160,extended,000000XX// Duck Flare// FF
patch=1,EE,01CCF280,extended,000000XX// Speedster// FF
patch=1,EE,01CCF3A0,extended,000000XX// Bluff// FF
patch=1,EE,01CCF730,extended,000000XX// WildCat// FF
patch=1,EE,01CCFCA0,extended,000000XX// Dance Call// FF
patch=1,EE,01CCFE80,extended,000000XX// Setup// FF
patch=1,EE,01CD0B40,extended,000000XX// Trinity Limit// FF
patch=1,EE,01CD1AD0,extended,000000XX// Session// FF
```

# Conditionals Explanation

Since every code in this file uses the same conditionals, it is possible to combine them all together in one section. Don't forget to edit the number of lines affected by the conditionals.

```
patch=1,EE,E0030003,extended,0032DFC8// Difficulty Determiner. 0=Beginner, 1=Standard, 2=Proud, 3=Critical. This is optional.
patch=1,EE,E0022002,extended,0032BAE0// Location at Station of Serenity in Twilight Town
patch=1,EE,E0010001,extended,0032BAE8// Event at selecting dream weapon
```
