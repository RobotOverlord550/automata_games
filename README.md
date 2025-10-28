# Data Reference
## Character Meaning
| Character | Meaning                   |
| --------- | ------------------------- |
| g         | Generic (including empty) |
| #         | Empty                     |
| e         | Generic (excluding empty) |
| w         | Water                     |
| l         | Lava                      |
| o         | Obsidian                  |
## LHS Operators
| Operator | Description                               | Usage                | Order           | Parameters     |
| -------- | ----------------------------------------- | -------------------- | --------------- | -------------- |
| `/`      | When two `g` are right next to each other | Unspecified          | Does Not Matter | `["g", "g"]`   |
| `-`      | When two `g` are one tile apart           | Unspecified          | Does Not Matter | `["g", "g"]`   |
| `_`      | When `e` is above `g`                     | Gravity, Unspecified | Matters         | 1: `g`, 2: `e` |
## RHS Operators
| Operator | Meaning                                              |                               |     |
| -------- | ---------------------------------------------------- | ----------------------------- | --- |
| (space)  | Spacing for code to distinguish arguments            |                               |     |
| `><`     | Elements are swapped                                 |                               |     |
| `\|`     |                                                      | Separates results when needed |     |
| `>`      | What both elements turn into                         |                               |     |
| `>>`     | What specific operand from left-hand side turns into |                               |     |
