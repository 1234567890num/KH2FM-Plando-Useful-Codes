# Battle Level

The game originally have static values pointed by the bitmask. The bitmask is the values changed by the game as you progress, and it's the one changed by the GoA mod. The values themselves are static.

It doesn't work on some fights (like OC Cups, Sephiroth, Lingering Will, AS, Data). It also might conflict with GoA pnach, so it's safer to delete them if you plan on using this.

```
patch=1,EE,2032F254,extended,00000001 //This is the bitmask that's changed by the game as you progress
patch=1,EE,01D112XX,extended,000000YY
YY: The new battle level
XX: The world code + 90
91 = World of Darkness
92 = Twilight Town
93 = Destiny Islands
94 = Hollow Bastion/Radiant Garden
95 = Beast's Castle
96 = Olympus Coliseum
97 = Agrabah
98 = The Land of Dragons
99 = 100 Acre Wood
9A = Pride Lands
9B = Atlantica
9C = Disney Castle
9D = Timeless River
9E = Halloween Town
9F = World Map (With Gummi Ship, not GoA)
A0 = Port Royal
A1 = Space Paranoids
A2 = The World That Never Was
```

# Party Modifier

Doesn't work on some forced fights (like Bailey Nobodies, Ravine Heartless, Riku, Xemnas 2, etc).

```
patch=1,EE,2032F0XX,extended,DDCCBBAA

XX: Depending on world
68 = World of Darkness
6C = Twilight Town
70 = Destiny Islands
74 = Hollow Bastion/Radiant Garden
78 = Beast's Castle
7C = Olympus Coliseum
80 = Agrabah
84 = The Land of Dragons
88 = 100 Acre Wood
8C = Pride Lands
90 = Atlantica
94 = Disney Castle
98 = Timeless River
9C = Halloween Town
A0 = World Map (With Gummi Ship, not GoA)
A4 = Port Royal
A8 = Space Paranoids
AC = The World That Never Was

AA/BB/CC/DD: Party Members
00 = Sora
01 = Donald
02 = Goofy
03 = Guest
83 = Forced Guest
04 = Valor Form
05 = Wisdom Form
06 = Limit Form
07 = Master Form
08 = Final Form
09 = Anti Form
12 = None
```

