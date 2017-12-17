def isPrime(n):
  if n <= 1:
      return False
  elif n <= 3:
      return True
  elif n % 2 == 0 or n % 3 == 0:
      return False
  i = 5
  while i * i <= n:
      if n % i == 0 or n % (i+2) == 0:
          return False
      i = i + 6
  return True

class SparseColumnMatrix:
  def __init__(self, rowCount):
    self.matrix = []
    self.sorted = False

    for i in range(0,rowCount):
      self.matrix.append([])

  def getRowCount(self):
    return len(self.matrix)

  def set(self, row, col, val):
    self.matrix[row].append((col, val))
    self.sorted = False

  def listRow(self, row):
    return self.matrix[row]

  def get(self, row, col, matrixStartCol, defaultValue):
    if self.sorted == False:
      for i in range(0, len(self.matrix)):
        self.matrix[i].sort(key=lambda v : v[0])
      self.sorted = True

    result = (-1,defaultValue)

    if len(self.matrix[row]) < 1:
      return result

    start = max(0, matrixStartCol)
    end = min(col,len(self.matrix[row])-1)

    while start <= end:
      mid = start + int((end-start)/2)
      if self.matrix[row][mid][0] == col:
        result = (mid, self.matrix[row][mid][1])
        break
        
      if self.matrix[row][mid][0] > col:
        end = mid - 1
      else:
        start = mid + 1

    #print((start, mid, end))
    return result

  def getNeighbors(self, rowIndex, colIndex):
    neighbors = []

    # Left
    result = self.get(rowIndex, colIndex-1, 0, None)
    if result[0] > -1:
        neighbors.append((rowIndex, colIndex-1, result[0], result[1]))

    if rowIndex > 0:
      # Top Left
      result = self.get(rowIndex-1, colIndex-1, 0, None)
      if result[0] > -1:
        neighbors.append((rowIndex-1, colIndex-1, result[0], result[1]))

      # Top
      matrixGuessCol = min(0, result[0])
      result = self.get(rowIndex-1, colIndex, matrixGuessCol, None)
      if result[0] > -1:
        neighbors.append((rowIndex-1, colIndex, result[0], result[1]))

      # Top Right
      matrixGuessCol = min(0, result[0])
      result = self.get(rowIndex-1, colIndex+1, matrixGuessCol, None)
      if result[0] > -1:
        neighbors.append((rowIndex-1, colIndex+1, result[0], result[1]))

    # Right
    result = self.get(rowIndex, colIndex+1, 0, None)
    if result[0] > -1:
        neighbors.append((rowIndex, colIndex+1, result[0], result[1]))

    if rowIndex+1 < len(self.matrix):
      # Bottom Left
      result = self.get(rowIndex+1, colIndex-1, 0, None)
      if result[0] > -1:
        neighbors.append((rowIndex+1, colIndex-1, result[0], result[1]))

      # Bottom
      matrixGuessCol = min(0, result[0])
      result = self.get(rowIndex+1, colIndex, matrixGuessCol, None)
      if result[0] > -1:
        neighbors.append((rowIndex+1, colIndex, result[0], result[1]))

      # Bottom Right
      matrixGuessCol = min(0, result[0])
      result = self.get(rowIndex+1, colIndex+1, matrixGuessCol, None)
      if result[0] > -1:
        neighbors.append((rowIndex+1, colIndex+1, result[0], result[1]))

    return neighbors

def getTripletsSum(n):
  if n < 1:
    return 0

  if n == 1:
    return 0

  if n == 2:
    return 5

  if n == 3:
    return 5

  if n == 4:
    return 7

  startRowIndex = n-2
  matrix = SparseColumnMatrix(5)

  N = 1

  for i in range(1,startRowIndex):
    N += i

  rows = []

  for matrixRowIndex in range(0, 5):
    for colIndex in range(0, startRowIndex+matrixRowIndex):
      if isPrime(N):
        matrix.set(matrixRowIndex,colIndex,N)
      N += 1

  total = 0

  for prime in matrix.listRow(2):
    neighbors = matrix.getNeighbors(2, prime[0])
    if len(neighbors) > 1:
      total += prime[1]
      continue

    for neighbor in neighbors:
      if len(matrix.getNeighbors(neighbor[0], neighbor[1])) > 1:
        total += prime[1]
        break

  return total

ab = [int(v) for v in input().split(" ")]

sumA = getTripletsSum(ab[0])
sumB = getTripletsSum(ab[1])

print(sumA+sumB)  


























