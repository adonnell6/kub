# kub
Answers the question: what play do I have given a current state of the board and tiles in your hand. The printed output tells you what to play from your hand and what the final board state should be — you have to figure out how to reorganize the board to get there

```
Best play found:
  Tiles to play: ['⬛️ 4', '🟧 3', '🟥 7', '🟧 4', '🟧 1', '🟥10', '🟧 2']
  Combination on board:
     ['🟥 4', '🟧 4', '⬛️ 4']
     ['🟥 1', '🟥 2', '🟥 3']
     ['🟥 5', '🟥 6', '🟥 7']
     ['🟥 8', '🟥 9', '🟥10', '🌟']
     ['🟧 1', '🟧 2', '🟧 3']
```

- does not handle duplicate tiles correctly
- performance at high tile counts unclear