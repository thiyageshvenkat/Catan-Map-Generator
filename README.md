# Catan Map Generator

A Catan map generator.

## Catan Games and Expansions Supported
- Base Game
- Cities and Knights
- Seafarers
- Base Game 5-6 Player _Expansion_
- Seafarers 5-6 Player _Expansion_
### What the emojis mean:
🌵 = Desert 
🌊 = Sea 
🪙 = Gold Field
🌾 = Field 
🧱 = Hills 
🗻 = Ore 
🌳 = Wood 
🐑 = Pastures 
⚓ = Harbor

### Catan Main Game Sample Output
```
Catan Main Game Board: 

     🌳 🌳 🧱
    🗻 🐑 🌾 🌾
   🗻 🐑 🐑 🌵 🌾
    🗻 🧱 🧱 🐑
     🌾 🌳 🌳



Numbers:

     10  11  12
      5   4  11   9
  6   8   2   🌵   4
      8   9   3  10
      3   6   5


Harbors starting from the 2:1 Clay Harbor:
⚓ 3:1  ⚓ 2:1 Ore  ⚓ 3:1  ⚓ 3:1  ⚓ 3:1  ⚓ 2:1 Wool  ⚓ 2:1 Grain  ⚓ 2:1 Clay  ⚓ 2:1 Wood  ⚓ 2:1 Pasture
```
### Catan Seafarers Sample Output
```
The top-most row of the map displayed represents the longer edge of the Seafarers map.
The middle row of the map displayed contains only 6 tiles, because the first and last two tiles of the eight tiles of that row must be ocean.
Catan Seafarers Board:

     🐑 🌊 🌊 🗻 🌳
    🌊 🌾 🌾 🌊 🧱 🌳
   🌊 🌊 🌳 🌊 🌊 🐑 🌳
    🐑 🌳 🧱 🌾 🌊 🗻
   🌊 🗻 🌊 🗻 🌊 🌊 🧱
    🌊 🐑 🌊 🌾 🌊 🐑
     🌊 🌊 🧱 🌾 🌊


Numbers:

   4  ~  ~  4  12
   ~  10 9  ~  8  10
~  ~  10 ~  ~  2  5
   11 4  9  5  ~  5
~  9  ~  3  ~  ~  3
   ~  6  ~  6  ~  11
   ~  ~  3  8  ~
```

### Catan Main Game 5-6 Expansion

```
Catan Main Game 5-6 Player Board: 

       🌳 🐑 🐑
      🗻 🐑 🌾 🌳
     🌳 🌳 🗻 🌵 🌾
    🌾 🗻 🌵 🌳 🧱 🌾
     🗻 🧱 🐑 🌾 🧱
      🐑 🐑 🗻 🌳
       🧱 🌾 🧱


Numbers:

                5      6     10
                3     11      3     10
         9     11      5      🌵      4
        12      8      🌵      4      6      3
         4      9      8      2     12
                5      2      8      6
               11     10      9

Harbors starting from the 2:1 Clay Harbor:
⚓ 2:1 Grain  ⚓ 2:1 Pasture  ⚓ 2:1 Pasture  ⚓ 3:1  ⚓ 2:1 Clay  ⚓ 3:1  ⚓ 2:1 Ore  ⚓ 3:1  ⚓ 3:1  ⚓ 3:1  ⚓ 2:1 Wood  ⚓ 2:1 Wool
```

### Catan Seafarers 5-6 Expansion
```

The top-most row of the map displayed represents the longer edge of the Seafarers map.
The middle row of the map displayed contains only 9 tiles, because the first and last two tiles of the eight tiles of that row must be ocean.
Catan Seafarers 5-6 Player Board:

     🌊 🐑 🌊 🌊 🌳 🌊 🧱 🌊
    🐑 🐑 🐑 🌾 🌊 🌵 🌊 🗻 🧱
   🌊 🪙 🌊 🌊 🌵 🗻 🌾 🌵 🌊 🐑
    🧱 🐑 🧱 🌳 🌳 🌳 🌊 🗻 🌳
   🌳 🌾 🗻 🗻 🌊 🌊 🧱 🌊 🌾 🌾
    🪙 🌊 🧱 🗻 🌾 🌊 🪙 🪙 🌊
     🌊 🌊 🌾 🌊 🌳 🗻 🐑 🧱





Numbers:

   ~  9  ~  ~  6  ~  12 ~
   11 3  9  2  ~  🌵  ~  4  5
~  6  ~  ~  🌵  4  12 🌵  ~  9
   12 11 5  6  9  8  ~  5  10
11 10 2  3  ~  ~  5  ~  6  9
   10 ~  4  8  8  ~  11 5  ~
   ~  ~  8  ~  10 8  3  4

```
