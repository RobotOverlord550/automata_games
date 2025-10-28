# Data Reference
## Character Meaning
| Character | Meaning                   |
| --------- | ------------------------- |
| `g`       | Generic (including empty) |
| `e`       | Generic (excluding empty) |
| `#`       | Empty                     |
| `w`       | Water                     |
| `l`       | Lava                      |
| `o`       | Obsidian                  |
## LHS Operators
| Operator | Meaning                                   |
| -------- | ----------------------------------------- |
| `/`      | When two `g` are right next to each other |
| `-`      | When two `g` are one tile apart           |
| `_`      | When `e` is above `g`                     |
## RHS Operators
| Operator | Meaning                                              |
| -------- | ---------------------------------------------------- |
| ` `      | Spacing for code to distinguish arguments            |
| `><`     | Elements are swapped                                 |
| `\|`     | Separates results when needed                        |
| `>`      | What both elements turn into                         |
| `>>`     | What specific operand from left-hand side turns into |
