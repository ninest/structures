# Sorting


## Bubble sort

```
LIST = [2, 3, 5, 1, 5, 10, 13, 8]

loop K from 0 to LIST.length() - 1
  loop I from 0 to LIST.length() - 2
  //-2 because the last element has no value after
    if LIST[I] > LIST[I+1] then   
      swap(LIST[I], LIST[I+1])
    end if
  end loop
end loop
```

The last two values will already be sorted, so it's no use traversing through them.

## Selection sort

```
LIST = [2, 3, 5, 1, 5, 10, 13, 8]

loop I from 0 to LIST.length()-2  //once done till n-2, n-1 will be sorted already
  MIN = I
  
  loop J from I+1 to LIST.length()-1
    if LIST[I] < LIST[MIN]
      MIN = J
    end if
  end loop

  swap(LIST[I], LIST[MIN])
end loop
```

<table>
  <tr>
   <td>Bubble sort
   </td>
   <td>Selection sort
   </td>
  </tr>
  <tr>
   <td>
    <ul>
      <li>Repeatedly steps through an array then compared and swaps adjacent elements if they are not in correct order
      <li>At the end of each pass, the highest number is bubbled up (end of array)
      <li>Takes multiple passes until no swaps are necessary
      <li>Slow and impractical
      <li>Time complexity = O(n<sup>2</sup>)
    </ul>
   </td>
   <td>
    <ul>
      <li>Runs through the array and swaps the minimum value with the first value of the array
      <li>Time complexity = O(n<sup>2</sup>)
    </ul>
   </td>
  </tr>
</table>
