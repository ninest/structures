# Searching


## Sequential search


```
LIST = [2, 3, 5, 1, 5, 10, 13, 8]
SEARCH = 2
FOUND = false

loop I from 0 to LIST.length()
  if LIST[I] == SEARCH then
    FOUND = true
    output SEARCH, "found at position", I
  end if
end loop

if FOUND == false then
  output "not found"
```



## Binary search


```
LIST = [1, 2, 4, 7, 10, 54, 55, 64, 345, 777, 787]
SEARCH = 2
START = 0
END = LIST.length()

while START <= END
//this is the recursive function
  MID = (START + END) div 2
  if LIST[MID] == SEARCH
    output SEARCH, "found at position", MID
  else
    if SEARCH < LIST[MID]
      END = MID - 1 //discarding middle element and everything after
    else
      START = MID + 1 //discarding middle element and everything before
    end if
  end if
end loop
```

<table>
  <tr>
   <td>Binary search
   </td>
   <td>Sequential search
   </td>
  </tr>
  <tr>
   <td>
    <ul>
      <li>Requires a sorted algorithm
      <li>More efficient for larger arrays
      <li>Time complexity = O(log n)
    </ul>
   </td>
   <td>
    <ul>
      <li>Simplest search strategy; does not require array to be sorted
      <li>Relies on brute force strategy
      <li>Time complexity = O(n)
    </ul>
   </td>
  </tr>
</table>