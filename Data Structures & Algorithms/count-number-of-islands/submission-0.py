class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        count = 0
        m,n = len(grid), len(grid[0])
        def recursion(v):
            seen.add(v)
            x,y = v
            # moves
            moves = [(-1,0),(0,-1),(1,0),(0,1)]
            for dx,dy in moves:
                new_v = (x + dx, y + dy)
                if new_v[0] in range(0,m) and new_v[1] in range(0,n) and new_v not in seen and grid[new_v[0]][new_v[1]] == "1":
                    recursion(new_v)
        
        for i in range(m):
            for j in range(n):
                v = (i,j)
                if grid[i][j] == "1" and v not in seen:
                    recursion(v)
                    count += 1
        print(seen)
        return count