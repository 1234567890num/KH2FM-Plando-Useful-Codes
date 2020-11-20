So if you aren't already aware pnach cheats are basically just differently formatted, RAW GameShark Codes.

This means 2 things:

1. What you may assume at first glance is an entire address actually isn't. It's <img src="https://render.githubusercontent.com/render/math?math=\frac{7}{8}">ths of an address because the first digit is inherent to the code.

2. Codes follow a set number of defined formats.

To get into the technical stuff, Gameshark codes (and thus pnach codes) only address a portion of the game’s memory. If you're looking into memory from Cheat Engine you should be able to limit your search to the 20000000 - 2FFFFFFF range to find whatever you're looking for.

The formatting for codes works as follows:
```
---------------------------------------------------------------
          PCSX2 1.5.0 - Extended PNACH - Cheat Sheet
---------------------------------------------------------------

0AAAAAAA 000000VV -> Writes value V into address A (8-bit Write)

1AAAAAAA 000000VV -> Writes value V into address A (16-bit Write)

2AAAAAAA 000000VV -> Writes value V into address A (32-bit Write)

300000VV 0AAAAAAA -> Increases the value of address A by the value V (8-bit)

301000VV 0AAAAAAA -> Decreases the value of address A by the value V (8-bit)

3020VVVV 0AAAAAAA -> Increases the value of address A by the value V (16-bit)

3030VVVV 0AAAAAAA -> Decreases the value of address A by the value V (16-bit)

30400000 0AAAAAAA |-> Increases the value of address A by the value V (32-bit)
VVVVVVVV 00000000 |

30500000 0AAAAAAA |-> Decreases the value of address A by the value V (32-bit)
VVVVVVVV 00000000 | 

4AAAAAAA TTTTBBBB |-> Writes value V into address A + (B * (4 * T))
VVVVVVVV 00000000 | in a loop T times.

5FFFFFFF NNNNNNNN |-> Copies the N amount of bytes from address F to address T
0TTTTTTT 00000000 |

6AAAAAAA VVVVVVVV |-> Writes value V into the pointed address of A + O, X
000X0000 OOOOOOOO | determines data depth (0 = 8-bit, 1 = 16-bit 2 = 32-bit)

7AAAAAAA 000XVVVV -> Performs a bitwise operation with the value stored at address
A and value V, and writes it back to address A.

Operations (X): 0 = 8-Bit OR, 1 = 16-Bit OR, 2 = 8-Bit AND, 3 = 16-Bit AND, 4 = 8-Bit XOR
5 = 16-Bit XOR

8AAAAAAA OOOOOOOO |-> Copies the value at the pointed address of A + O into
0TTTTTTT 00000000 |  address T

9AAAAAAA 0TTTTTTT -> Copies the value stored at address A to address T
 
ADDDDDDD 00000000 |-> Copies the value stored at address D to the pointed
0PPPPPPP 0IIIIIII |  address of P + I 

BXXSSSSS 00000000 -> Activates X amount of lines every S milliseconds.

CAAAAAAA 00000000 |-> Compares the value at address A with the value at
0TTTTTTT YZXXXXXX |  address T. If true, activates X amount of lines.

Value Type (Y): 0 = 32-Bit, 1 = 16-Bit, 2 = 8-Bit
Operations (Z): 00 = Equal, 10 = Not Equal, 20 = Lesser, 30 = Greater

DAAAAAAA 00XXVVVV -> Checks the value at address A and compares it to value V. If the
condition is true, it activates 1 line of code.

Operations (X): 00 = Equal, 10 = Not Equal, 20 = Lesser, 30 = Greater

EZNNVVVV XAAAAAAA -> Checks the value at address A and compares it to value V. If the
condition is true, it activates N amount of lines.

Value Type (Z): 0 = 16-Bit, 1 = 8-Bit
Operations (X): 0 = Equal , 1 = Not Equal, 2 = Lesser, 3 = Greater
```

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
