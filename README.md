# ***CURRENTLY NOT FUNCTIONAL***
# Current Version: Pre-Alpha
# Description
Little game I'm working on in python using [Pygame Community Edition](https://github.com/pygame-community/pygame-ce).  It is called Random Game because I didn't really know what I wanted to make when I initiated the repository.  I am planning on posting the first Alpha release on itch.io.  (If you really want to play it now the source code is here for your usage)
## Data Reference

### Description
Use this as a reference guide for modifying the file to your hearts content without needing to read my poorly commented source code.  I may add more extensive modding support in the future.
### Character Meaning
| Character | Meaning                   |
| --------- | ------------------------- |
| `g`       | Generic (including empty) |
| `e`       | Generic (excluding empty) |
| `#`       | Empty                     |
| `w`       | Water                     |
| `l`       | Lava                      |
| `o`       | Obsidian                  |
### LHS Operators
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
