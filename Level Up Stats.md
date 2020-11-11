# Explanation
```
//---------- Level Ups ----------
//AA: AP, BB: Def, CC: Mag, DD: Str
//patch=1,EE,2XXXXXXX,extended,AABBCCDD
//AP gives 1.5x rounded down for Critical mode.
//A Short table for ease of use in Critical mode.
//A=15, 9=13, 8=12 7=10, 6=9, 5=7, 4=6, 3=4, 2=3, 1=1, FF=382
```

You can put stats that the character is supposed to have at that level. Those stats are then added with base AP, boosts, and equipment bonuses to give the final stats. For example:

```
patch=1,EE,21D0B6BC,extended,08162861
patch=1,EE,21D0B6CC,extended,01869284
```

These codes will give Sora 97 Str, 40 Mag, 22 Def, 8 AP for Level 2 before changing them to 132 Str, 146 Mag, 134 Def, 1 AP for Level 3. The stats CAN decrease, so make sure to fill up every single level's stats.

# Dream Weapon Conditionals

```
//Conditionals to apply only if a certain Dream Weapon is picked
patch=1,EE,E0620X00,extended,0032E02D
X = 0 for Dream Sword, 1 for Dream Shield, 2 for Dream Staff

//Optional Conditionals to apply only at the beginning of the game:
patch=1,EE,E0041A04,extended,0032BAE0 //Location at Garden of Assemblage in Hollow Bastion
patch=1,EE,E0020001,extended,0032BAE8 //Condition is Computer have never been interacted
```

As always with conditionals, don't forget to adjust for the number of lines affected.

# Addresses

Addresses shown below are for level up stats. You can edit the level EXP (following the same rule as above) at the address-8. You can also edit the given ability from Dream Weapon at the address+2 (Sword), address+4 (Shield), or address+6 (Staff)

## Sora
```
patch=1,EE,21D0B6AC,extended,AABBCCDD //LV 1
patch=1,EE,21D0B6BC,extended,AABBCCDD //LV 2
patch=1,EE,21D0B6CC,extended,AABBCCDD //LV 3
patch=1,EE,21D0B6DC,extended,AABBCCDD //LV 4
patch=1,EE,21D0B6EC,extended,AABBCCDD //LV 5
patch=1,EE,21D0B6FC,extended,AABBCCDD //LV 6
patch=1,EE,21D0B70C,extended,AABBCCDD //LV 7
patch=1,EE,21D0B71C,extended,AABBCCDD //LV 8
patch=1,EE,21D0B72C,extended,AABBCCDD //LV 9
patch=1,EE,21D0B73C,extended,AABBCCDD //LV 10
patch=1,EE,21D0B74C,extended,AABBCCDD //LV 11
patch=1,EE,21D0B75C,extended,AABBCCDD //LV 12
patch=1,EE,21D0B76C,extended,AABBCCDD //LV 13
patch=1,EE,21D0B77C,extended,AABBCCDD //LV 14
patch=1,EE,21D0B78C,extended,AABBCCDD //LV 15
patch=1,EE,21D0B79C,extended,AABBCCDD //LV 16
patch=1,EE,21D0B7AC,extended,AABBCCDD //LV 17
patch=1,EE,21D0B7BC,extended,AABBCCDD //LV 18
patch=1,EE,21D0B7CC,extended,AABBCCDD //LV 19
patch=1,EE,21D0B7DC,extended,AABBCCDD //LV 20
patch=1,EE,21D0B7EC,extended,AABBCCDD //LV 21
patch=1,EE,21D0B7FC,extended,AABBCCDD //LV 22
patch=1,EE,21D0B80C,extended,AABBCCDD //LV 23
patch=1,EE,21D0B81C,extended,AABBCCDD //LV 24
patch=1,EE,21D0B82C,extended,AABBCCDD //LV 25
patch=1,EE,21D0B83C,extended,AABBCCDD //LV 26
patch=1,EE,21D0B84C,extended,AABBCCDD //LV 27
patch=1,EE,21D0B85C,extended,AABBCCDD //LV 28
patch=1,EE,21D0B86C,extended,AABBCCDD //LV 29
patch=1,EE,21D0B87C,extended,AABBCCDD //LV 30
patch=1,EE,21D0B88C,extended,AABBCCDD //LV 31
patch=1,EE,21D0B89C,extended,AABBCCDD //LV 32
patch=1,EE,21D0B8AC,extended,AABBCCDD //LV 33
patch=1,EE,21D0B8BC,extended,AABBCCDD //LV 34
patch=1,EE,21D0B8CC,extended,AABBCCDD //LV 35
patch=1,EE,21D0B8DC,extended,AABBCCDD //LV 36
patch=1,EE,21D0B8EC,extended,AABBCCDD //LV 37
patch=1,EE,21D0B8FC,extended,AABBCCDD //LV 38
patch=1,EE,21D0B90C,extended,AABBCCDD //LV 39
patch=1,EE,21D0B91C,extended,AABBCCDD //LV 40
patch=1,EE,21D0B92C,extended,AABBCCDD //LV 41
patch=1,EE,21D0B93C,extended,AABBCCDD //LV 42
patch=1,EE,21D0B94C,extended,AABBCCDD //LV 43
patch=1,EE,21D0B95C,extended,AABBCCDD //LV 44
patch=1,EE,21D0B96C,extended,AABBCCDD //LV 45
patch=1,EE,21D0B97C,extended,AABBCCDD //LV 46
patch=1,EE,21D0B98C,extended,AABBCCDD //LV 47
patch=1,EE,21D0B99C,extended,AABBCCDD //LV 48
patch=1,EE,21D0B9AC,extended,AABBCCDD //LV 49
patch=1,EE,21D0B9BC,extended,AABBCCDD //LV 50
patch=1,EE,21D0B9CC,extended,AABBCCDD //LV 51
patch=1,EE,21D0B9DC,extended,AABBCCDD //LV 52
patch=1,EE,21D0B9EC,extended,AABBCCDD //LV 53
patch=1,EE,21D0B9FC,extended,AABBCCDD //LV 54
patch=1,EE,21D0BA0C,extended,AABBCCDD //LV 55
patch=1,EE,21D0BA1C,extended,AABBCCDD //LV 56
patch=1,EE,21D0BA2C,extended,AABBCCDD //LV 57
patch=1,EE,21D0BA3C,extended,AABBCCDD //LV 58
patch=1,EE,21D0BA4C,extended,AABBCCDD //LV 59
patch=1,EE,21D0BA5C,extended,AABBCCDD //LV 60
patch=1,EE,21D0BA6C,extended,AABBCCDD //LV 61
patch=1,EE,21D0BA7C,extended,AABBCCDD //LV 62
patch=1,EE,21D0BA8C,extended,AABBCCDD //LV 63
patch=1,EE,21D0BA9C,extended,AABBCCDD //LV 64
patch=1,EE,21D0BAAC,extended,AABBCCDD //LV 65
patch=1,EE,21D0BABC,extended,AABBCCDD //LV 66
patch=1,EE,21D0BACC,extended,AABBCCDD //LV 67
patch=1,EE,21D0BADC,extended,AABBCCDD //LV 68
patch=1,EE,21D0BAEC,extended,AABBCCDD //LV 69
patch=1,EE,21D0BAFC,extended,AABBCCDD //LV 70
patch=1,EE,21D0BB0C,extended,AABBCCDD //LV 71
patch=1,EE,21D0BB1C,extended,AABBCCDD //LV 72
patch=1,EE,21D0BB2C,extended,AABBCCDD //LV 73
patch=1,EE,21D0BB3C,extended,AABBCCDD //LV 74
patch=1,EE,21D0BB4C,extended,AABBCCDD //LV 75
patch=1,EE,21D0BB5C,extended,AABBCCDD //LV 76
patch=1,EE,21D0BB6C,extended,AABBCCDD //LV 77
patch=1,EE,21D0BB7C,extended,AABBCCDD //LV 78
patch=1,EE,21D0BB8C,extended,AABBCCDD //LV 79
patch=1,EE,21D0BB9C,extended,AABBCCDD //LV 80
patch=1,EE,21D0BBAC,extended,AABBCCDD //LV 81
patch=1,EE,21D0BBBC,extended,AABBCCDD //LV 82
patch=1,EE,21D0BBCC,extended,AABBCCDD //LV 83
patch=1,EE,21D0BBDC,extended,AABBCCDD //LV 84
patch=1,EE,21D0BBEC,extended,AABBCCDD //LV 85
patch=1,EE,21D0BBFC,extended,AABBCCDD //LV 86
patch=1,EE,21D0BC0C,extended,AABBCCDD //LV 87
patch=1,EE,21D0BC1C,extended,AABBCCDD //LV 88
patch=1,EE,21D0BC2C,extended,AABBCCDD //LV 89
patch=1,EE,21D0BC3C,extended,AABBCCDD //LV 90
patch=1,EE,21D0BC4C,extended,AABBCCDD //LV 91
patch=1,EE,21D0BC5C,extended,AABBCCDD //LV 92
patch=1,EE,21D0BC6C,extended,AABBCCDD //LV 93
patch=1,EE,21D0BC7C,extended,AABBCCDD //LV 94
patch=1,EE,21D0BC8C,extended,AABBCCDD //LV 95
patch=1,EE,21D0BC9C,extended,AABBCCDD //LV 96
patch=1,EE,21D0BCAC,extended,AABBCCDD //LV 97
patch=1,EE,21D0BCBC,extended,AABBCCDD //LV 98
patch=1,EE,21D0BCCC,extended,AABBCCDD //LV 99
```

## Donald
```
patch=1,EE,21D0BCE0,extended,AABBCCDD //LV 1
patch=1,EE,21D0BCF0,extended,AABBCCDD //LV 2
patch=1,EE,21D0BD00,extended,AABBCCDD //LV 3
patch=1,EE,21D0BD10,extended,AABBCCDD //LV 4
patch=1,EE,21D0BD20,extended,AABBCCDD //LV 5
patch=1,EE,21D0BD30,extended,AABBCCDD //LV 6
patch=1,EE,21D0BD40,extended,AABBCCDD //LV 7
patch=1,EE,21D0BD50,extended,AABBCCDD //LV 8
patch=1,EE,21D0BD60,extended,AABBCCDD //LV 9
patch=1,EE,21D0BD70,extended,AABBCCDD //LV 10
patch=1,EE,21D0BD80,extended,AABBCCDD //LV 11
patch=1,EE,21D0BD90,extended,AABBCCDD //LV 12
patch=1,EE,21D0BDA0,extended,AABBCCDD //LV 13
patch=1,EE,21D0BDB0,extended,AABBCCDD //LV 14
patch=1,EE,21D0BDC0,extended,AABBCCDD //LV 15
patch=1,EE,21D0BDD0,extended,AABBCCDD //LV 16
patch=1,EE,21D0BDE0,extended,AABBCCDD //LV 17
patch=1,EE,21D0BDF0,extended,AABBCCDD //LV 18
patch=1,EE,21D0BE00,extended,AABBCCDD //LV 19
patch=1,EE,21D0BE10,extended,AABBCCDD //LV 20
patch=1,EE,21D0BE20,extended,AABBCCDD //LV 21
patch=1,EE,21D0BE30,extended,AABBCCDD //LV 22
patch=1,EE,21D0BE40,extended,AABBCCDD //LV 23
patch=1,EE,21D0BE50,extended,AABBCCDD //LV 24
patch=1,EE,21D0BE60,extended,AABBCCDD //LV 25
patch=1,EE,21D0BE70,extended,AABBCCDD //LV 26
patch=1,EE,21D0BE80,extended,AABBCCDD //LV 27
patch=1,EE,21D0BE90,extended,AABBCCDD //LV 28
patch=1,EE,21D0BEA0,extended,AABBCCDD //LV 29
patch=1,EE,21D0BEB0,extended,AABBCCDD //LV 30
patch=1,EE,21D0BEC0,extended,AABBCCDD //LV 31
patch=1,EE,21D0BED0,extended,AABBCCDD //LV 32
patch=1,EE,21D0BEE0,extended,AABBCCDD //LV 33
patch=1,EE,21D0BEF0,extended,AABBCCDD //LV 34
patch=1,EE,21D0BF00,extended,AABBCCDD //LV 35
patch=1,EE,21D0BF10,extended,AABBCCDD //LV 36
patch=1,EE,21D0BF20,extended,AABBCCDD //LV 37
patch=1,EE,21D0BF30,extended,AABBCCDD //LV 38
patch=1,EE,21D0BF40,extended,AABBCCDD //LV 39
patch=1,EE,21D0BF50,extended,AABBCCDD //LV 40
patch=1,EE,21D0BF60,extended,AABBCCDD //LV 41
patch=1,EE,21D0BF70,extended,AABBCCDD //LV 42
patch=1,EE,21D0BF80,extended,AABBCCDD //LV 43
patch=1,EE,21D0BF90,extended,AABBCCDD //LV 44
patch=1,EE,21D0BFA0,extended,AABBCCDD //LV 45
patch=1,EE,21D0BFB0,extended,AABBCCDD //LV 46
patch=1,EE,21D0BFC0,extended,AABBCCDD //LV 47
patch=1,EE,21D0BFD0,extended,AABBCCDD //LV 48
patch=1,EE,21D0BFE0,extended,AABBCCDD //LV 49
patch=1,EE,21D0BFF0,extended,AABBCCDD //LV 50
patch=1,EE,21D0C000,extended,AABBCCDD //LV 51
patch=1,EE,21D0C010,extended,AABBCCDD //LV 52
patch=1,EE,21D0C020,extended,AABBCCDD //LV 53
patch=1,EE,21D0C030,extended,AABBCCDD //LV 54
patch=1,EE,21D0C040,extended,AABBCCDD //LV 55
patch=1,EE,21D0C050,extended,AABBCCDD //LV 56
patch=1,EE,21D0C060,extended,AABBCCDD //LV 57
patch=1,EE,21D0C070,extended,AABBCCDD //LV 58
patch=1,EE,21D0C080,extended,AABBCCDD //LV 59
patch=1,EE,21D0C090,extended,AABBCCDD //LV 60
patch=1,EE,21D0C0A0,extended,AABBCCDD //LV 61
patch=1,EE,21D0C0B0,extended,AABBCCDD //LV 62
patch=1,EE,21D0C0C0,extended,AABBCCDD //LV 63
patch=1,EE,21D0C0D0,extended,AABBCCDD //LV 64
patch=1,EE,21D0C0E0,extended,AABBCCDD //LV 65
patch=1,EE,21D0C0F0,extended,AABBCCDD //LV 66
patch=1,EE,21D0C100,extended,AABBCCDD //LV 67
patch=1,EE,21D0C110,extended,AABBCCDD //LV 68
patch=1,EE,21D0C120,extended,AABBCCDD //LV 69
patch=1,EE,21D0C130,extended,AABBCCDD //LV 70
patch=1,EE,21D0C140,extended,AABBCCDD //LV 71
patch=1,EE,21D0C150,extended,AABBCCDD //LV 72
patch=1,EE,21D0C160,extended,AABBCCDD //LV 73
patch=1,EE,21D0C170,extended,AABBCCDD //LV 74
patch=1,EE,21D0C180,extended,AABBCCDD //LV 75
patch=1,EE,21D0C190,extended,AABBCCDD //LV 76
patch=1,EE,21D0C1A0,extended,AABBCCDD //LV 77
patch=1,EE,21D0C1B0,extended,AABBCCDD //LV 78
patch=1,EE,21D0C1C0,extended,AABBCCDD //LV 79
patch=1,EE,21D0C1D0,extended,AABBCCDD //LV 80
patch=1,EE,21D0C1E0,extended,AABBCCDD //LV 81
patch=1,EE,21D0C1F0,extended,AABBCCDD //LV 82
patch=1,EE,21D0C200,extended,AABBCCDD //LV 83
patch=1,EE,21D0C210,extended,AABBCCDD //LV 84
patch=1,EE,21D0C220,extended,AABBCCDD //LV 85
patch=1,EE,21D0C230,extended,AABBCCDD //LV 86
patch=1,EE,21D0C240,extended,AABBCCDD //LV 87
patch=1,EE,21D0C250,extended,AABBCCDD //LV 88
patch=1,EE,21D0C260,extended,AABBCCDD //LV 89
patch=1,EE,21D0C270,extended,AABBCCDD //LV 90
patch=1,EE,21D0C280,extended,AABBCCDD //LV 91
patch=1,EE,21D0C290,extended,AABBCCDD //LV 92
patch=1,EE,21D0C2A0,extended,AABBCCDD //LV 93
patch=1,EE,21D0C2B0,extended,AABBCCDD //LV 94
patch=1,EE,21D0C2C0,extended,AABBCCDD //LV 95
patch=1,EE,21D0C2D0,extended,AABBCCDD //LV 96
patch=1,EE,21D0C2E0,extended,AABBCCDD //LV 97
patch=1,EE,21D0C2F0,extended,AABBCCDD //LV 98
patch=1,EE,21D0C300,extended,AABBCCDD //LV 99
```

## Goofy
```
patch=1,EE,21D0C314,extended,AABBCCDD //LV 1
patch=1,EE,21D0C324,extended,AABBCCDD //LV 2
patch=1,EE,21D0C334,extended,AABBCCDD //LV 3
patch=1,EE,21D0C344,extended,AABBCCDD //LV 4
patch=1,EE,21D0C354,extended,AABBCCDD //LV 5
patch=1,EE,21D0C364,extended,AABBCCDD //LV 6
patch=1,EE,21D0C374,extended,AABBCCDD //LV 7
patch=1,EE,21D0C384,extended,AABBCCDD //LV 8
patch=1,EE,21D0C394,extended,AABBCCDD //LV 9
patch=1,EE,21D0C3A4,extended,AABBCCDD //LV 10
patch=1,EE,21D0C3B4,extended,AABBCCDD //LV 11
patch=1,EE,21D0C3C4,extended,AABBCCDD //LV 12
patch=1,EE,21D0C3D4,extended,AABBCCDD //LV 13
patch=1,EE,21D0C3E4,extended,AABBCCDD //LV 14
patch=1,EE,21D0C3F4,extended,AABBCCDD //LV 15
patch=1,EE,21D0C404,extended,AABBCCDD //LV 16
patch=1,EE,21D0C414,extended,AABBCCDD //LV 17
patch=1,EE,21D0C424,extended,AABBCCDD //LV 18
patch=1,EE,21D0C434,extended,AABBCCDD //LV 19
patch=1,EE,21D0C444,extended,AABBCCDD //LV 20
patch=1,EE,21D0C454,extended,AABBCCDD //LV 21
patch=1,EE,21D0C464,extended,AABBCCDD //LV 22
patch=1,EE,21D0C474,extended,AABBCCDD //LV 23
patch=1,EE,21D0C484,extended,AABBCCDD //LV 24
patch=1,EE,21D0C494,extended,AABBCCDD //LV 25
patch=1,EE,21D0C4A4,extended,AABBCCDD //LV 26
patch=1,EE,21D0C4B4,extended,AABBCCDD //LV 27
patch=1,EE,21D0C4C4,extended,AABBCCDD //LV 28
patch=1,EE,21D0C4D4,extended,AABBCCDD //LV 29
patch=1,EE,21D0C4E4,extended,AABBCCDD //LV 30
patch=1,EE,21D0C4F4,extended,AABBCCDD //LV 31
patch=1,EE,21D0C504,extended,AABBCCDD //LV 32
patch=1,EE,21D0C514,extended,AABBCCDD //LV 33
patch=1,EE,21D0C524,extended,AABBCCDD //LV 34
patch=1,EE,21D0C534,extended,AABBCCDD //LV 35
patch=1,EE,21D0C544,extended,AABBCCDD //LV 36
patch=1,EE,21D0C554,extended,AABBCCDD //LV 37
patch=1,EE,21D0C564,extended,AABBCCDD //LV 38
patch=1,EE,21D0C574,extended,AABBCCDD //LV 39
patch=1,EE,21D0C584,extended,AABBCCDD //LV 40
patch=1,EE,21D0C594,extended,AABBCCDD //LV 41
patch=1,EE,21D0C5A4,extended,AABBCCDD //LV 42
patch=1,EE,21D0C5B4,extended,AABBCCDD //LV 43
patch=1,EE,21D0C5C4,extended,AABBCCDD //LV 44
patch=1,EE,21D0C5D4,extended,AABBCCDD //LV 45
patch=1,EE,21D0C5E4,extended,AABBCCDD //LV 46
patch=1,EE,21D0C5F4,extended,AABBCCDD //LV 47
patch=1,EE,21D0C604,extended,AABBCCDD //LV 48
patch=1,EE,21D0C614,extended,AABBCCDD //LV 49
patch=1,EE,21D0C624,extended,AABBCCDD //LV 50
patch=1,EE,21D0C634,extended,AABBCCDD //LV 51
patch=1,EE,21D0C644,extended,AABBCCDD //LV 52
patch=1,EE,21D0C654,extended,AABBCCDD //LV 53
patch=1,EE,21D0C664,extended,AABBCCDD //LV 54
patch=1,EE,21D0C674,extended,AABBCCDD //LV 55
patch=1,EE,21D0C684,extended,AABBCCDD //LV 56
patch=1,EE,21D0C694,extended,AABBCCDD //LV 57
patch=1,EE,21D0C6A4,extended,AABBCCDD //LV 58
patch=1,EE,21D0C6B4,extended,AABBCCDD //LV 59
patch=1,EE,21D0C6C4,extended,AABBCCDD //LV 60
patch=1,EE,21D0C6D4,extended,AABBCCDD //LV 61
patch=1,EE,21D0C6E4,extended,AABBCCDD //LV 62
patch=1,EE,21D0C6F4,extended,AABBCCDD //LV 63
patch=1,EE,21D0C704,extended,AABBCCDD //LV 64
patch=1,EE,21D0C714,extended,AABBCCDD //LV 65
patch=1,EE,21D0C724,extended,AABBCCDD //LV 66
patch=1,EE,21D0C734,extended,AABBCCDD //LV 67
patch=1,EE,21D0C744,extended,AABBCCDD //LV 68
patch=1,EE,21D0C754,extended,AABBCCDD //LV 69
patch=1,EE,21D0C764,extended,AABBCCDD //LV 70
patch=1,EE,21D0C774,extended,AABBCCDD //LV 71
patch=1,EE,21D0C784,extended,AABBCCDD //LV 72
patch=1,EE,21D0C794,extended,AABBCCDD //LV 73
patch=1,EE,21D0C7A4,extended,AABBCCDD //LV 74
patch=1,EE,21D0C7B4,extended,AABBCCDD //LV 75
patch=1,EE,21D0C7C4,extended,AABBCCDD //LV 76
patch=1,EE,21D0C7D4,extended,AABBCCDD //LV 77
patch=1,EE,21D0C7E4,extended,AABBCCDD //LV 78
patch=1,EE,21D0C7F4,extended,AABBCCDD //LV 79
patch=1,EE,21D0C804,extended,AABBCCDD //LV 80
patch=1,EE,21D0C814,extended,AABBCCDD //LV 81
patch=1,EE,21D0C824,extended,AABBCCDD //LV 82
patch=1,EE,21D0C834,extended,AABBCCDD //LV 83
patch=1,EE,21D0C844,extended,AABBCCDD //LV 84
patch=1,EE,21D0C854,extended,AABBCCDD //LV 85
patch=1,EE,21D0C864,extended,AABBCCDD //LV 86
patch=1,EE,21D0C874,extended,AABBCCDD //LV 87
patch=1,EE,21D0C884,extended,AABBCCDD //LV 88
patch=1,EE,21D0C894,extended,AABBCCDD //LV 89
patch=1,EE,21D0C8A4,extended,AABBCCDD //LV 90
patch=1,EE,21D0C8B4,extended,AABBCCDD //LV 91
patch=1,EE,21D0C8C4,extended,AABBCCDD //LV 92
patch=1,EE,21D0C8D4,extended,AABBCCDD //LV 93
patch=1,EE,21D0C8E4,extended,AABBCCDD //LV 94
patch=1,EE,21D0C8F4,extended,AABBCCDD //LV 95
patch=1,EE,21D0C904,extended,AABBCCDD //LV 96
patch=1,EE,21D0C914,extended,AABBCCDD //LV 97
patch=1,EE,21D0C924,extended,AABBCCDD //LV 98
patch=1,EE,21D0C934,extended,AABBCCDD //LV 99
```

# Guest Party Members

It is also possible to alter the stats of party members, but it is faster to just alter their weapon's stats instead. If you are insistent on changing their levels, here are their Lv1 addresses. You can find the rest following the same patterns as above.
```
patch=1,EE,21D0C948,extended,AABBCCDD //Mickey
patch=1,EE,21D0CF7C,extended,AABBCCDD //Auron
patch=1,EE,21D0D5B0,extended,AABBCCDD //Mulan
patch=1,EE,21D0DBE4,extended,AABBCCDD //Aladdin
patch=1,EE,21D0E218,extended,AABBCCDD //Jack Sparrow
patch=1,EE,21D0E84C,extended,AABBCCDD //Beast
patch=1,EE,21D0EE80,extended,AABBCCDD //Jack Skellington
patch=1,EE,21D0F4B4,extended,AABBCCDD //Simba
patch=1,EE,21D0FAE8,extended,AABBCCDD //Tron
patch=1,EE,21D1011C,extended,AABBCCDD //Riku
```
