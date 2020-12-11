# Complexity

How much **time** and **space** does an algorithm need?

## Big-O

Big-O Notation gives an upper bound of the complexity in the **worst case**, helping to quantify performance as the input size becomes **arbitrarily large**.

`n` is the size of the input:

- Constant time: O(1)
- Linear time: O(n)
- Quadric time: O(n^2)
- Cubic time: O(n^3)
- Exponential time: O(b^n), b>1
- Factorial time: O(n!)

The time complexity is the n that is the biggest/most dominant term. For example,

```py
O(n + c) = O(n)
O(cn) = O(n), c > 0

f(n) = n^3 + n^2 +7
# n^3 is the largest value for n
O(f(n)) = O(n^3)
```

### Examples

#### Constant: O(1)

These run in **constant** time:

```py
a = 1
b = 1
c = a + b * 5
```

```py
i = 0
while i < 10:
  i++
  # although we have a loop, it doesn't depend on n
  # the loop always takes the same amount of time
```

For both of the above, **even if the input size gets arbitrarily large**, the program is still executed in the same amount of time.

#### Linear: O(n)

These run in linear time:

```py
i = 0
while i < n:
  i++

#    f(n) = n
# O(f(n)) = O(n)
```

```py
i = 0
while i < n:
  i = i + 3

#    f(n) = n/3  (the loop finishes 3x faster than in the previous example)
# O(f(n)) = O(n)

```

#### Quadric: O(n^2)

```py
for i in range(n):
  for j in range(n):
    print(n)

#    f(n) = n^2
# O(f(n)) = O(n^2)
```

```py
for i in range(n):
  for j in range(i, n): # this one starts loop at i
    print(n)

# (n) + (n-1) + (n-2) + .. + 2 + 1
# => n(n+1)/2
# O(n(n+1)/2) = O(n^2)
```

When `i` is `0`, we do `n` work. When `i` is `1`, we do `n-1` work. When `i` is `2`, we do `n-2` work, and so on.

So we do

```py
n + (n-1) + (n-2) + ... + 3 + 2 + 1 work
n(n + 1)/2 work
```

and

```py
O(n(n+1)/2) = O(n^2/2 + n/2)
O(n^2)
```

#### Logarithm: O(log n)

Binary search produces a time complexity of O(log n):

```py
low = 0
high = n-1

while low <= high:
  mid = int( (low+high) / 2 )
  if array[mid] == value: return mid
  elif array[mid] < value: low = mid + 1
  elif array[mid] > value : high = mid -1

return -1

# O(log2 n) = O(log n)
```

#### More examples

##### Quadric

```py
i = 0

while i < n:  # this loop will happen n times
  j = 0

  while j < 3*n:  # time complexity of 3n
    j = j + 1

  j = 0

  while j < 2*n:  # time complexity of 2n
    j = j + 1

  i = i + 1

# f(n) = n * (3n + 2n) = 5n^2
# O(f(n)) = O(n^2)
```

##### Quartic

```py
i = 0

while i < 3*n:
  j = 10

  while j <= 50:  # constant amount of work done here regardless of input value
    j = j +1

  j = 0

  while j < n*n*n:
    j = j + 2

  i = i + 1

# f(n) = 3n * (50 + n^3/2) = 3n/40 + 3n^4/2
# O(f(n)) = O(n^4)
```

### Big-O examples

- Finding all subsets of a set: O(2^n)
- Finding all permutations of a string: O(n!)
- Sorting using mergesort: O(n log n)
- Iterating over cells in a matrix size `n * m`: O(nm)
