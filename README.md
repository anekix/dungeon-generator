# dungeon-generator
a random dungeon generator
```bash
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ▓ ▓ ▓ ▓ ▓ . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ▓ ▓ ▓ ▓ ▓ x ▓ ▓ ▓ ▓ ▓ ▓ ▓ . . . . .
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ▓ ▓ ▓ ▓ ▓ . ▓ ▓ ▓ ▓ ▓ ▓ ▓ . . . . .
. . . . . . . . . . . . . . . . . . ▓ ▓ ▓ ▓ ▓ ▓ . . . . . . . . . . . . . . . . . . ▓ ▓ ▓ ▓ ▓ . ▓ ▓ ▓ ▓ ▓ ▓ ▓ . . . . .
. . . . . . . . . . . . . . . . . . ▓ ▓ ▓ ▓ ▓ ▓ . . . . . . . . . . . . . . . . . . ▓ ▓ ▓ ▓ ▓ . ▓ ▓ ▓ ▓ ▓ ▓ ▓ . . . . .
. . . . . . . . . . ▓ ▓ ▓ ▓ ▓ ▓ ▓ . ▓ ▓ ▓ ▓ ▓ ▓ . . . . . . . . . . . . . . . . . . x . . . x . ▓ ▓ ▓ ▓ ▓ ▓ ▓ . . . . .
. . . ▓ ▓ ▓ ▓ ▓ ▓ . ▓ ▓ ▓ ▓ ▓ ▓ ▓ x ▓ ▓ ▓ ▓ ▓ ▓ x x ▓ ▓ ▓ ▓ ▓ ▓ ▓ x x ▓ ▓ ▓ ▓ ▓ ▓ ▓ x . . . x . ▓ ▓ ▓ ▓ ▓ ▓ ▓ . . . . .
. . . ▓ ▓ ▓ ▓ ▓ ▓ . ▓ ▓ ▓ ▓ ▓ ▓ ▓ . ▓ ▓ ▓ ▓ ▓ ▓ . . ▓ ▓ ▓ ▓ ▓ ▓ ▓ . . ▓ ▓ ▓ ▓ ▓ ▓ ▓ x . . . x . ▓ ▓ ▓ ▓ ▓ ▓ ▓ . . . . .
. . . ▓ ▓ ▓ ▓ ▓ ▓ . ▓ ▓ ▓ ▓ ▓ ▓ ▓ . . . . . x x x x ▓ ▓ ▓ ▓ ▓ ▓ ▓ x x ▓ ▓ ▓ ▓ ▓ ▓ ▓ x x x . x . ▓ ▓ ▓ ▓ ▓ ▓ ▓ . . . . .
. . . ▓ ▓ ▓ ▓ ▓ ▓ . ▓ ▓ ▓ ▓ ▓ ▓ ▓ . . . . . . . . . ▓ ▓ ▓ ▓ ▓ ▓ ▓ . . ▓ ▓ ▓ ▓ ▓ ▓ ▓ x . x . x . . . . . . . . . . . . .
. . . ▓ ▓ ▓ ▓ ▓ ▓ . ▓ ▓ ▓ ▓ ▓ ▓ ▓ . . . . . . . . . ▓ ▓ ▓ ▓ ▓ ▓ ▓ . . ▓ ▓ ▓ ▓ ▓ ▓ ▓ x . x . x . . . . . . . . . . . . .
. . . ▓ ▓ ▓ ▓ ▓ ▓ . ▓ ▓ ▓ ▓ ▓ ▓ ▓ . . . . . . . . . ▓ ▓ ▓ ▓ ▓ ▓ ▓ . . ▓ ▓ ▓ ▓ ▓ ▓ ▓ x x x x ▓ ▓ ▓ ▓ ▓ ▓ ▓ . . . . . . .
. . . ▓ ▓ ▓ ▓ ▓ ▓ . ▓ ▓ ▓ ▓ ▓ ▓ ▓ . . . . . . . . . ▓ ▓ ▓ ▓ ▓ ▓ ▓ . . ▓ ▓ ▓ ▓ ▓ ▓ ▓ x . x x ▓ ▓ ▓ ▓ ▓ ▓ ▓ . . . . . . .
. . . ▓ ▓ ▓ ▓ ▓ ▓ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . x x . x x ▓ ▓ ▓ ▓ ▓ ▓ ▓ . . . . . . .
. . . . . . x x x x x x x x x x x x x x x x x x x x x x x x x x ▓ ▓ ▓ ▓ ▓ ▓ ▓ x x x x x x x ▓ ▓ ▓ ▓ ▓ ▓ ▓ x . . . . . .
. . . . . . . . . . . . . . . . . . . . ▓ ▓ ▓ ▓ ▓ ▓ ▓ . . . . . ▓ ▓ ▓ ▓ ▓ ▓ ▓ . . x x . x x ▓ ▓ ▓ ▓ ▓ ▓ ▓ . . . . . . .
. . . . . . . . . . . . . . . . . . . . ▓ ▓ ▓ ▓ ▓ ▓ ▓ x x x x x ▓ ▓ ▓ ▓ ▓ ▓ ▓ x x x x x x x ▓ ▓ ▓ ▓ ▓ ▓ ▓ . . . . . . .
. . . . . . . . . . . . . . . . . . . . ▓ ▓ ▓ ▓ ▓ ▓ ▓ . . . . . ▓ ▓ ▓ ▓ ▓ ▓ ▓ . . x x x x x ▓ ▓ ▓ ▓ ▓ ▓ ▓ . . . . . . .
. . . . . . . . . . . . . . . . . . . . ▓ ▓ ▓ ▓ ▓ ▓ ▓ . . . . . ▓ ▓ ▓ ▓ ▓ ▓ ▓ . . x x x x x x . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . . ▓ ▓ ▓ ▓ ▓ ▓ ▓ . . . . . ▓ ▓ ▓ ▓ ▓ ▓ ▓ x x x x x x x x . . . . . . . . . . . . .
. . ▓ ▓ ▓ ▓ ▓ . . . . . . . . . . . . . . . . . . . . . . . . . ▓ ▓ ▓ ▓ ▓ ▓ ▓ . ▓ ▓ ▓ ▓ ▓ ▓ x . . . . . . . . . . . . .
. . ▓ ▓ ▓ ▓ ▓ . . . . . . . . . ▓ ▓ ▓ ▓ ▓ ▓ ▓ . . . . . . . . . . . . . . . . . ▓ ▓ ▓ ▓ ▓ ▓ x . . . . . . . . . . . . .
. . ▓ ▓ ▓ ▓ ▓ . . . ▓ ▓ ▓ ▓ ▓ . ▓ ▓ ▓ ▓ ▓ ▓ ▓ . . . . . . . . . . ▓ ▓ ▓ ▓ ▓ ▓ . ▓ ▓ ▓ ▓ ▓ ▓ x . . . . . . . . . . . . .
. . ▓ ▓ ▓ ▓ ▓ . . . ▓ ▓ ▓ ▓ ▓ . ▓ ▓ ▓ ▓ ▓ ▓ ▓ x x x x x x x x x x ▓ ▓ ▓ ▓ ▓ ▓ x ▓ ▓ ▓ ▓ ▓ ▓ x . . . . . . . . . . . . .
. . ▓ ▓ ▓ ▓ ▓ . . . ▓ ▓ ▓ ▓ ▓ . ▓ ▓ ▓ ▓ ▓ ▓ ▓ . . . . . . . . . . ▓ ▓ ▓ ▓ ▓ ▓ x ▓ ▓ ▓ ▓ ▓ ▓ x . . . ▓ ▓ ▓ ▓ ▓ . . . . .
. . ▓ ▓ ▓ ▓ ▓ . . . ▓ ▓ ▓ ▓ ▓ . ▓ ▓ ▓ ▓ ▓ ▓ ▓ . . . . . . . . . . ▓ ▓ ▓ ▓ ▓ ▓ x ▓ ▓ ▓ ▓ ▓ ▓ x x x x ▓ ▓ ▓ ▓ ▓ . . . . .
. . ▓ ▓ ▓ ▓ ▓ x x x ▓ ▓ ▓ ▓ ▓ x ▓ ▓ ▓ ▓ ▓ ▓ ▓ x x x x x x x x x x ▓ ▓ ▓ ▓ ▓ ▓ x ▓ ▓ ▓ ▓ ▓ ▓ x . . . ▓ ▓ ▓ ▓ ▓ . . . . .
. . ▓ ▓ ▓ ▓ ▓ . . . ▓ ▓ ▓ ▓ ▓ . ▓ ▓ ▓ ▓ ▓ ▓ ▓ . . ▓ ▓ ▓ ▓ ▓ . . . ▓ ▓ ▓ ▓ ▓ ▓ x ▓ ▓ ▓ ▓ ▓ ▓ x . . . ▓ ▓ ▓ ▓ ▓ . . . . .
. . ▓ ▓ ▓ ▓ ▓ . . . ▓ ▓ ▓ ▓ ▓ . ▓ ▓ ▓ ▓ ▓ ▓ ▓ . . ▓ ▓ ▓ ▓ ▓ . . . ▓ ▓ ▓ ▓ ▓ ▓ x ▓ ▓ ▓ ▓ ▓ ▓ x . . . ▓ ▓ ▓ ▓ ▓ . . . . .
. . . . . . . . . . ▓ ▓ ▓ ▓ ▓ . . . . . . . . . . ▓ ▓ ▓ ▓ ▓ x x x ▓ ▓ ▓ ▓ ▓ ▓ x x x x . x x x . . . ▓ ▓ ▓ ▓ ▓ . . . . .
. . . . . . . . . . . . . . . . . . . . . . . . . ▓ ▓ ▓ ▓ ▓ . . . . . . . . . x x x . . x x x . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . . . . . . . ▓ ▓ ▓ ▓ ▓ . . . . . . . . . x x x . . x x x . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . ▓ ▓ ▓ ▓ ▓ . . . . . . . . . . . . . . . x x x . . x x x . . . . . . . . . . . . .
. . . . . . . . . . . . ▓ ▓ ▓ ▓ ▓ x x ▓ ▓ ▓ ▓ ▓ x x x x x x x x x x x x x x x x x x x x x x x . . ▓ ▓ ▓ ▓ ▓ ▓ ▓ . . . .
. . . . . . . . . . . . ▓ ▓ ▓ ▓ ▓ . . ▓ ▓ ▓ ▓ ▓ . . . . . . . . . . . . . . . x x x . . x x x . . ▓ ▓ ▓ ▓ ▓ ▓ ▓ . . . .
. . . . . . . . . . . . ▓ ▓ ▓ ▓ ▓ . . ▓ ▓ ▓ ▓ ▓ . . . . . . . . . . . . . . . x x x . . x x x x x ▓ ▓ ▓ ▓ ▓ ▓ ▓ . . . .
. . . . . . . . . . . . ▓ ▓ ▓ ▓ ▓ . . ▓ ▓ ▓ ▓ ▓ . . . . . . . . . . . . . . . x x x . . x x x . . ▓ ▓ ▓ ▓ ▓ ▓ ▓ . . . .
. . . . . . . . . . . . ▓ ▓ ▓ ▓ ▓ . . ▓ ▓ ▓ ▓ ▓ x x x ▓ ▓ ▓ ▓ ▓ ▓ x ▓ ▓ ▓ ▓ ▓ ▓ ▓ x x x x x x . . ▓ ▓ ▓ ▓ ▓ ▓ ▓ . . . .
. . . . ▓ ▓ ▓ ▓ ▓ ▓ ▓ . . . . . . . . . . . . . . . . ▓ ▓ ▓ ▓ ▓ ▓ . ▓ ▓ ▓ ▓ ▓ ▓ ▓ x . . x x x . . ▓ ▓ ▓ ▓ ▓ ▓ ▓ . . . .
. . . . ▓ ▓ ▓ ▓ ▓ ▓ ▓ . ▓ ▓ ▓ ▓ ▓ ▓ . . . . . . . . . ▓ ▓ ▓ ▓ ▓ ▓ . ▓ ▓ ▓ ▓ ▓ ▓ ▓ x x x x x x . . ▓ ▓ ▓ ▓ ▓ ▓ ▓ . . . .
. . . . ▓ ▓ ▓ ▓ ▓ ▓ ▓ . ▓ ▓ ▓ ▓ ▓ ▓ . . . . . . . . . ▓ ▓ ▓ ▓ ▓ ▓ . ▓ ▓ ▓ ▓ ▓ ▓ ▓ x . . x x x . . ▓ ▓ ▓ ▓ ▓ ▓ ▓ . . . .
. . . . ▓ ▓ ▓ ▓ ▓ ▓ ▓ . ▓ ▓ ▓ ▓ ▓ ▓ . . . . . . . . . ▓ ▓ ▓ ▓ ▓ ▓ . ▓ ▓ ▓ ▓ ▓ ▓ ▓ x . . x x x . . ▓ ▓ ▓ ▓ ▓ ▓ ▓ . . . .
. . . . ▓ ▓ ▓ ▓ ▓ ▓ ▓ . ▓ ▓ ▓ ▓ ▓ ▓ . ▓ ▓ ▓ ▓ ▓ . . . ▓ ▓ ▓ ▓ ▓ ▓ x x x x x x x x x . . x x x . . . . . . . . . . . . .
. . . . ▓ ▓ ▓ ▓ ▓ ▓ ▓ . ▓ ▓ ▓ ▓ ▓ ▓ x ▓ ▓ ▓ ▓ ▓ x x x x x x x x x x x ▓ ▓ ▓ ▓ ▓ ▓ x x x x x x . . . . . . . . . . . . .
. . . . ▓ ▓ ▓ ▓ ▓ ▓ ▓ . ▓ ▓ ▓ ▓ ▓ ▓ . ▓ ▓ ▓ ▓ ▓ x x x x x x x x x x x ▓ ▓ ▓ ▓ ▓ ▓ x . . x x x . . . . . . . . . . . . .
. . . . ▓ ▓ ▓ ▓ ▓ ▓ ▓ . ▓ ▓ ▓ ▓ ▓ ▓ . ▓ ▓ ▓ ▓ ▓ . . . . . . . . . . . ▓ ▓ ▓ ▓ ▓ ▓ . . . x x x . . . . . . . . . . . . .
. . . . . . . x x x x x ▓ ▓ ▓ ▓ ▓ ▓ x ▓ ▓ ▓ ▓ ▓ x x x x x x x x x x x ▓ ▓ ▓ ▓ ▓ ▓ . . . x x x . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . ▓ ▓ ▓ ▓ ▓ . . ▓ ▓ ▓ ▓ ▓ ▓ . . . ▓ ▓ ▓ ▓ ▓ ▓ . . ▓ ▓ ▓ ▓ ▓ ▓ . . . . . . . . . . .
. . . . . . . . . ▓ ▓ ▓ ▓ ▓ ▓ ▓ . . . . . . . . . . ▓ ▓ ▓ ▓ ▓ ▓ . . . ▓ ▓ ▓ ▓ ▓ ▓ . . ▓ ▓ ▓ ▓ ▓ ▓ . . . . . . . . . . .
. . . . . . . . . ▓ ▓ ▓ ▓ ▓ ▓ ▓ . ▓ ▓ ▓ ▓ ▓ ▓ . . . ▓ ▓ ▓ ▓ ▓ ▓ . . . ▓ ▓ ▓ ▓ ▓ ▓ . . ▓ ▓ ▓ ▓ ▓ ▓ . . . . . . . . . . .
. . . . . . . . . ▓ ▓ ▓ ▓ ▓ ▓ ▓ . ▓ ▓ ▓ ▓ ▓ ▓ . . . ▓ ▓ ▓ ▓ ▓ ▓ . . . ▓ ▓ ▓ ▓ ▓ ▓ . . ▓ ▓ ▓ ▓ ▓ ▓ . . . . . . . . . . .
. . . . . . . . . ▓ ▓ ▓ ▓ ▓ ▓ ▓ . ▓ ▓ ▓ ▓ ▓ ▓ . . . ▓ ▓ ▓ ▓ ▓ ▓ . . . . . . . . x . . ▓ ▓ ▓ ▓ ▓ ▓ . . . . . . . . . . .
. . . . . . . . . ▓ ▓ ▓ ▓ ▓ ▓ ▓ . ▓ ▓ ▓ ▓ ▓ ▓ . . . ▓ ▓ ▓ ▓ ▓ ▓ x x x x x x x x x x x x x x . . . . . . . . . . . . . .
. . . . . . . . . ▓ ▓ ▓ ▓ ▓ ▓ ▓ x ▓ ▓ ▓ ▓ ▓ ▓ x x x x x x x x x x x x x x x x x x x x x x . . . . . . . . . . . . . . .
. . . . . . . . . ▓ ▓ ▓ ▓ ▓ ▓ ▓ . ▓ ▓ ▓ ▓ ▓ ▓ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . ▓ ▓ ▓ ▓ ▓ ▓ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . ▓ ▓ ▓ ▓ ▓ ▓ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . ▓ ▓ ▓ ▓ ▓ ▓ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

```
