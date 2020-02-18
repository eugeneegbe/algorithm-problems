def solution(A):
  '''
  Finds the positions where there is a rise 
  in an array of numbers sort of the form
  /\___/\___/\ solved using divide and conquer
  '''
  middle = int(len(A)/2)
  peaks = []
  if A[middle] <= A[ middle - 1 ]:
    for i in range(middle):
      if A[ i + 1 ] >= A[ i ]:
        peaks.append( i + 1 )
  if A[middle + 1] >= A[ middle ]:
    for j in range(middle, len(A) - 1):
      if A[j + 1] >= A[j]:
        peaks.append(j + 1)
  else:
      return -1
  return peaks

# Example
print(solution([7,2,4,3,0,7,2,20]))