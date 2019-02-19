# Queue



*   FIFO: first in, first out
    *   All **insertions** take place at the **rear**, and all **deletions** take place at the **front**
*   Two pointers:
    *   `FRONT` returns the first value
    *   `REAR` returns the last value
*   Top pointer points to first element: `PEEK() => QUEUE[FRONT]`
*   Two methods:
    *   `ENQUEUE()`
    *   `DEQUE()`
*   When a value is dequeued, the value of `FRONT()` changes, and there is a _vacant_ space left (and the value is returned)


## Methods


### Enqueue


```
begin procedure ENQUEUE(DATA)
  if QUEUE.isFull() then
    return "OVERFLOW"
    exit
  end if
  REAR = REAR + 1
  QUEUE[REAR] = DATA
end procedure
```



### Dequeue


```
begin procedure DEQUEUE
  if QUEUE.isEmpty() then
    return "UNDERFLOW"
    exit
  end if
  DATA = QUEUE[FRONT]
  FRONT = FRONT + 1  
  // the front value is changed
  // although the data still exists in the memory, it is not in the queue
  return DATA
end procedure
```



### isFull


```
begin procedure isFull
  if (REAR == MAXSIZE) then  // max size is N - 1
    return true
  else
    return false
  end if
end procedure
```



### isEmpty


```
begin procedure isEmpty
  if (FONT < MINSIZE) OR (FRONT > REAR) then
    return true
  else
    return false
  end if
end procedure
```



### Peek


```
begin procedure PEEK
  return QUEUE[FRONT]
end procedure
```



<!-- Docs to Markdown version 1.0β15 -->
