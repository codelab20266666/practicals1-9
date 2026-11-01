# Practical 7: Paper Prototype of a Game Idea

**Aim:** Create a paper prototype of a game idea, focusing on core gameplay mechanics and level layout. Draw the game's interface, levels and key interactions on paper so the design can be iterated and tested quickly.

**Course link:** 418243 Game Design and Development, Unit II (Game Prototyping) and Unit V (Playtesting)

---

## 1. Game Concept

**Title:** Sky Hopper

**Genre:** 2D side-view platformer (single player)

**One-line pitch:** A small robot hops across floating platforms, collects energy cells and reaches the exit portal before the platforms run out.

**Goal:** Collect all energy cells in a level and reach the portal.

**Player motivation:** Clear short levels, collect every cell, finish with the fewest moves.

---

## 2. Core Gameplay Mechanics

| Mechanic | Description | Paper version |
|---|---|---|
| Move | Robot moves one tile left or right per turn | Move the paper token one square |
| Jump | Jumps up 1 tile and across up to 2 tiles | Move the token in an L-shape (up 1, across 1-2) |
| Collect | Landing on a cell tile picks it up | Remove the cell card and add it to the score box |
| Crumbling platform | Platform marked "C" disappears after one landing | Flip the tile face down after the token leaves |
| Hazard (spikes) | Touching spikes costs 1 life | Lose a life token (3 lives total) |
| Win / Lose | Win at portal with all cells; lose at 0 lives | Check the win/lose box on the interface sheet |

**Turn order:** Player moves, then hazards update (crumbling platforms flip), then check win/lose.

---

## 3. Interface Layout (draw this on a sheet of paper)

```
+--------------------------------------------------+
|  LIVES: [♥][♥][♥]    CELLS: 0 / 3    LEVEL: 1    |
+--------------------------------------------------+
|                                                  |
|                  GAME BOARD                      |
|             (grid of 8 columns x 5 rows)         |
|                                                  |
+--------------------------------------------------+
|  [ < LEFT ]   [ JUMP ]   [ RIGHT > ]   [ RESET ] |
+--------------------------------------------------+
```

Elements to draw: lives row, cell counter, level number, game board grid, and the control buttons (use sticky notes or paper flaps for the buttons).

---

## 4. Level Layouts (8 x 5 grid)

Legend: `R` robot start, `=` solid platform, `C` crumbling platform, `*` energy cell, `^` spikes, `P` portal, `.` empty

**Level 1: Tutorial (teaches move, jump, collect)**
```
. . . . . . . P
. . . . . . = =
. . . * . . . .
R . = = = . . .
= = . . . . . .
```

**Level 2: Crumbling platforms (teaches planning ahead)**
```
. . . . . . . P
. * . . . C C =
. C . . . . . .
R = . * C . . .
= . . . . ^ ^ .
```

**Level 3: Hazards and timing (combines everything)**
```
. . . . * . . P
. . C C . C . =
. * . . . . . .
R = . C * . ^ .
= . . . . = . .
```

Draw each level on its own sheet of grid paper with coloured pens for each symbol.

---

## 5. Key Interactions (draw as storyboard panels)

1. **Jump and land:** Robot on tile (2,3) jumps to tile (3,3). Show an arrow arcing between tiles.
2. **Collect a cell:** Robot lands on `*`. Cell card is removed and the counter goes up by 1.
3. **Crumbling platform:** Robot leaves a `C` tile and the tile is flipped face down. It cannot be used again.
4. **Hazard hit:** Robot lands on `^`. Remove one heart from the lives row and return the robot to the last safe tile.
5. **Win condition:** Robot reaches `P` with all cells collected. Show the "LEVEL COMPLETE" screen sketch.

---

## 6. Materials Needed

- A4 sheets and grid paper
- Coloured pens or pencils
- Sticky notes (for buttons and tiles)
- Paper token for the robot
- Scissors and a small box for lives and cells

---

## 7. Playtest Log (fill in after testing)

| Test # | Tester | Level | What happened | Problem found | Change made |
|---|---|---|---|---|---|
| 1 | Friend 1 | 1 | | | |
| 2 | Friend 2 | 2 | | | |
| 3 | Friend 3 | 3 | | | |

**Sample iterations to record:**
- Jump distance of 3 tiles made Level 1 too easy, so it was reduced to 2.
- Crumbling platforms were confusing without a visible marking, so a crack pattern was added to the `C` tiles.
- Three lives felt too punishing in Level 3, so a checkpoint tile was added.

(Replace these with what actually happens in your own playtests.)

---

## 8. Conclusion

The paper prototype let the core mechanics (move, jump, collect, crumbling platforms and hazards) and the level layouts be tested without any code. Playtesting with friends exposed balance problems early, and the design was refined over several quick iterations before any programming effort was spent.
