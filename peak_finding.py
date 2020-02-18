def solution_1(A):
  '''
  Finding a peak if it exists in an array of integers.
  A peak is is an element which is not smaller than its two neighbors
  '''
  peak = None
  for i in range(1, len(A) - 1):
    if A[ i ] >= A[ i - 1 ] and A[ i ] >= A[ i + 1 ]:
      peak = i
  if A[len(A) - 1 ] >= A[ len(A) - 2]:
    peak = len(A) - 1 
  return peak

print(solution_1([1, 3, 20, 4, 1, 0]))

def solution(A):
  middle = int(len(A)/2)
  peak = None
  # the left could have a peak
  if A[ middle - 1 ] >= A[middle]:
    for i in range( 1, middle):
      if A[i] > A[middle]:
        peak = i
  elif A[ middle + 1 ] >= A[middle]:
    for j in range(middle, len(A)):
      if A[j] > A[middle]:
        peak = j
  else:
    peak = middle
  return peak

print(solution([1, 3, 20, 4, 1, 0]))