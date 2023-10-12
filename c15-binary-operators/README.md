# C15. Binary Operators

> TODO: Add all chapter notes

- Binary operators provide Prometheus with deeper analysis capabilities than other metrics systems.

## Working with Scalars

- Use scalars directly with instant vectors

### Arithmetic Operators

+ addition
- substraction
* multiplication
/ division
% modulo
    - floating-point modulo that can return noninteger results
^ exponentiation

### Trigonometric Operator

`atan2` - returns the arc tangent of the division fo two vectors
    - the signs of the two vectors determine the quadrant

### Comparison Operators

== equals
!= not equals
> greater than
< less than
>= greater than or equal to
<= less than or equal to

> NOTE: Comparison vectors in PromQL are filtering

`bool modifier` -  comparison without filtering
    - returns 1 for true and 0 for false

## Vector Matching

### One-to-One

### Many-to-One and group_left

### Many-to-Many and Logical Operators

## Operator Precedence