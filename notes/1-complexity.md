# Complexity
How much **time** and **space** does an algorithm need?

## Big-O
Big-O Notation gives an upper bound of the complexity in the **worst case**, helping to quantify performance as the input size becomes **arbitrarily large**.

`n` is the size of the input:
- Constant time: O(1)
- Linear time: O(n)
- Quadric time: O(n^2)
- Cubic time: O(n^3)

The time complexity is the n that is the biggest/most dominant term. For example,

```
f(n) = n^3 + n^2 +7  
# n^3 is the largest value for n

O(f(n)) = O(n^3)
```

### Examples
#### Constant (O(1))
```
a = 1
b = 1
```

```
i = 0
while i < 10:
  i++
```

For both of the above, **even if the input size gets arbitrarily large**, the program is still executed in the same amount of time.

#### Linear (O(n))

```
i = 0
while i < n:
  i++

#    f(n) = n
# O(f(n)) = O(n)
```

```
i = 0
while i < n:
  i = i + 3

#    f(n) = n/3  <-- need to confirm
# O(f(n)) = O(n)
```

#### Quadric (O(n^2))
```
for i in range(n):
  for j in range(n):
    print(n)

#    f(n) = n^2
# O(f(n)) = O(n^2)
```

```
for i in range(n):  <-- need to confirm
  for j in range(i, n):
    print(n)

# (n) + (n-1) + (n-2) + .. + 2 + 1
# => n(n+1)/2
#O(n(n+1)/2) = O(n^2)
```

#### Logarithm (O(log n))

Binary search produced a time complexity of O(log n):
```
low = 0
high = n-1

  while low <= high:
    mid = int( (low+high) / 2 )
    if array[mid] == value: return mid
    elif array[mid] < value: low = mid + 1
    elif array[mid] > value : high = mid -1

return -1
```