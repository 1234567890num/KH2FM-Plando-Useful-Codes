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

