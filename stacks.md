# Stacks

*   LIFO: last in, first out
*   Top pointer points to first element: `PEEK() => STACK[TOP]`
*   Two methods:
    *   `PUSH()`
    *   `POP()`


## Applications



*   Reversing a string
*   Convert an infix expression to postfix


## Methods


### Push


```
TOP = -1  // stack is empty
input item

if (TOP == N-1) then
  print "OVERFLOW"
else
  top = TOP + 1
  STACK[TOP] = item
end if
```


**Overflow** is when the stack is full and an element is being pushed.


### Pop


```
TOP = 0  // no value for top as stack is empty
if (TOP < 1) then
  print "UNDERFLOW"
else
  print STACK[TOP]
  TOP = TOP -1
  // return value and remove index
end if
```


**Underflow** is when the stack is empty but an element is being popped.


### Peek


```
begin procedure PEEK
  return stack[TOP]
end procedure
```