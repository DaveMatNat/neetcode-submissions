class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [(-1,0),(0,-1),(1,0),(0,1)]

        numIsland = 0
        seen = set()

        stack = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r,c) not in seen:
                    stack.append((r,c))
                    seen.add((r,c))
                    while stack:
                        x,y = stack.pop()
                        for dx, dy in dirs:
                            nx, ny = x+dx, y+dy
                            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == "1" and (nx,ny) not in seen:
                                seen.add((nx,ny))
                                stack.append((nx,ny))
                            
                    numIsland += 1
        return numIsland
