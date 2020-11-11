So if you aren't already aware pnach cheats are basically just differently formatted, RAW GameShark Codes.

This means 2 things:

1. What you may assume at first glance is an entire address actually isn't. It's <img src="https://render.githubusercontent.com/render/math?math=\frac{7}{8}">ths of an address because the first digit is inherent to the code.

2. Codes follow a set number of defined formats.

To get into the technical stuff, Gameshark codes (and thus pnach codes) only address a portion of the game’s memory. If you're looking into memory from Cheat Engine you should be able to limit your search to the 20000000 - 2FFFFFFF range to find whatever you're looking for.

The formatting for codes works as follows:

# Constant Write Commands:

## 8-bit (1 byte) Constant Write:
```
patch=1,EE,0AAAAAAA,extended,000000XX
```

This command will constantly write the value XX to the address specified by AAAAAAA.

## 16-bit (2 byte) Constant Write:
```
patch=1,EE,1AAAAAAA,extended,0000XXXX
```

This command will constantly write the value XXXX to the address specified by AAAAAAA.

## 32-bit (4 byte) Constant Write:
```
patch=1,EE,2AAAAAAA,extended,XXXXXXXX
```

This command will constantly write the value XXXXXXXX to the address specified by AAAAAAA.

# Single-line Conditional Commands:

## 16-bit (2 byte) Equal:
```
patch=1,EE,DAAAAAAA,extended,0000XXXX
```

This command will run the next one (1) line IF AND ONLY IF the value of the address specified by AAAAAAA is *EQUAL TO* XXXX. Otherwise the next one (1) line is skipped.

## 16-bit (2 byte) Not Equal:
```
patch=1,EE,DAAAAAAA,extended,0010XXXX
```

This command will run the next one (1) line IF AND ONLY IF the value of the address specified by AAAAAAA is *NOT EQUAL TO* XXXX. Otherwise the next one (1) line is skipped.

## 16-bit (2 byte) Less Than:
```
patch=1,EE,DAAAAAAA,extended,0020XXXX
```

This command will run the next one (1) line IF AND ONLY IF the value of the address specified by AAAAAAA is *LESS THAN* XXXX. Otherwise the next one (1) line is skipped.

## 16-bit (2 byte) Greater Than:
```
patch=1,EE,DAAAAAAA,extended,0030XXXX
```

This command will run the next one (1) line IF AND ONLY IF the value of the address specified by AAAAAAA is *GREATER THAN* XXXX. Otherwise the next one (1) line is skipped.

# Multi-line Conditional Commands:

## 16-bit (2 byte) Equal:
```
patch=1,EE,ENNNXXXX,extended,0AAAAAAA
```

This command will run the next NNN line(s) IF AND ONLY IF the value of the address specified by AAAAAAA is *EQUAL TO* XXXX. Otherwise the next NNN line(s) are skipped.

## 16-bit (2 byte) Not Equal:
```
patch=1,EE,ENNNXXXX,extended,1AAAAAAA
```

This command will run the next NNN line(s) IF AND ONLY IF the value of the address specified by AAAAAAA is *NOT EQUAL TO* XXXX. Otherwise the next NNN line(s) are skipped.

## 16-bit (2 byte) Less Than:
```
patch=1,EE,ENNNXXXX,extended,2AAAAAAA
```

This command will run the next NNN line(s) IF AND ONLY IF the value of the address specified by AAAAAAA is *LESS THAN* XXXX. Otherwise the next NNN line(s) are skipped.

## 16-bit (2 byte) Greater Than:
```
patch=1,EE,ENNNXXXX,extended,3AAAAAAA
```

This command will run the next NNN line(s) IF AND ONLY IF the value of the address specified by AAAAAAA is *GREATER THAN* XXXX. Otherwise the next NNN line(s) are skipped.

# Additions and Subtractions:

## 8-bit (1 byte) Increment:
```
patch=1,EE,301000XX,extended,0AAAAAAA
```

This command will add XX to the value of the address specified by AAAAAAA.

## 8-bit (1 byte) Decrement:
```
patch=1,EE,302000XX,extended,0AAAAAAA
```

This command will subtract XX from the value of the address specified by AAAAAAA.

## 16-bit (2 byte) Increment:
```
patch=1,EE,3030XXXX,extended,0AAAAAAA
```

This command will add XXXX to the value of the address specified by AAAAAAA.

## 16-bit (2 byte) Decrement:
```
patch=1,EE,3040XXXX,extended,0AAAAAAA
```

This command will subtract XXXX from the value of the address specified by AAAAAAA.

## 32-bit (4 byte) Increment:
```
patch=1,EE,30500000,extended,0AAAAAAA
patch=1,EE,XXXXXXXX,extended,00000000
```

This command will add XXXXXXXX to the value of the address specified by AAAAAAA.

## 32-bit (4 byte) Decrement:
```
patch=1,EE,30600000,extended,0AAAAAAA
patch=1,EE,XXXXXXXX,extended,00000000
```

This command will subtract XXXXXXXX from the value of the address specified by AAAAAAA.

# Miscellaneous:

## Copy-Bytes:
```
patch=1,EE,5AAAAAAA,extended,000000NN
patch=1,EE,0BBBBBBB,extended,00000000
```

This command copies NN bytes from the address specified by AAAAAAA to the address specified by BBBBBBB.

## 32-bit (4 byte) Multi-Address Write:
```
patch=1,EE,4AAAAAAA,extended,XXXXYYYY
patch=1,EE,DDDDDDDD,extended,00000000
```

Also referred to as a "patch code"

This command writes the value DDDDDDDD to XXXX addresses starting with the address specified by AAAAAAA and determining the next address by incrementing AAAAAAA by (YYYY * 4)

# Example Code:
As an example, this block of code:
```
patch=1,EE,E0041A04,extended,0032BAE0
patch=1,EE,E0030001,extended,0032BAE4
patch=1,EE,E0020001,extended,0032BAE8
patch=1,EE,01C6C754,extended,00000001
patch=1,EE,01C6C750,extended,00000001
```

Translates to:
IF the value of 2032BAE0 is equal to 1A04 run the next 4 lines.\
Then IF the value of 2032BAE4 is equal to 0001 run the next 3 lines.\
Then IF the value of 2032BAE8 is equal to 0001 run the next 2 lines.\
Then set the byte at 21C6C754 to 01.\
Then set the byte at 21C6C750 to 01.

If at any point one of those conditions is not true the last 2 lines do nothing.
