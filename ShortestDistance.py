# You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. 
# You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:

#Each 0 marks an empty land which you can pass by freely.
#Each 1 marks a building which you cannot pass through.
#Each 2 marks an obstacle which you cannot pass through.
#this answer is not mine

import collections
def shortestDistance(grid):
  if not grid or not grid[0]: return -1
  M, N, buildings = len(grid), len(grid[0]), sum(val for line in grid for val in line if val == 1)
  hit, distSum = [[0] * N for i in range(M)], [[0] * N for i in range(M)]
  
  def BFS(start_x, start_y):                   #what will be achieved by this method? 
      visited = [[False] * N for k in range(M)]
      visited[start_x][start_y], count1, queue = True, 1, collections.deque([(start_x, start_y, 0)])
      while queue:
          x, y, dist = queue.popleft()
          for i, j in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
              if 0 <= i < M and 0 <= j < N and not visited[i][j]:
                  visited[i][j] = True
                  if not grid[i][j]:
                      queue.append((i, j, dist + 1))
                      hit[i][j] += 1
                      distSum[i][j] += dist + 1
                  elif grid[i][j] == 1:
                      count1 += 1
      return count1 == buildings               #if this return False,what happpen? find an obstacle ?
  
  for x in range(M):
      for y in range(N):
          if grid[x][y] == 1:
              if not BFS(x, y): return -1
  return min([distSum[i][j] for i in range(M) for j in range(N) if not grid[i][j] and hit[i][j] == buildings] or [-1])


input1 = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
print(shortestDistance(input1)) #this should return 7 