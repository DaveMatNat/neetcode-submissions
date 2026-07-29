class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Iterative DFS approach
        seen = set()
        directions = [(-1,0),(0,-1),(1,0),(0,1)]
        rows, cols = len(grid), len(grid[0])

        def dfs(block:tuple, area=0):
            seen.add(block)
            area = 1
            for dx,dy in directions:
                r,c = block
                neigh_r, neigh_c = r+dx, c+dy
                if (0 <= neigh_r and neigh_r < rows) and (0 <= neigh_c and neigh_c < cols) and grid[neigh_r][neigh_c] == 1 and (neigh_r, neigh_c) not in seen:
                    area += dfs((neigh_r, neigh_c))
            return area

        maxA = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in seen:
                    # Basic Stack template
                    stack = [(r,c)]
                    seen.add((r,c))
                    total_area = 0
                    while stack:
                        popped_r,popped_c = stack.pop()
                        total_area += 1
                        for dx,dy in directions:
                            neigh_r, neigh_c = popped_r+dx, popped_c+dy
                            if (0 <= neigh_r and neigh_r < rows) and (0 <= neigh_c and neigh_c < cols) and grid[neigh_r][neigh_c] == 1 and (neigh_r, neigh_c) not in seen:
                                seen.add((neigh_r,neigh_c))
                                stack.append((neigh_r,neigh_c))
                    maxA = max(maxA, total_area)
        return maxA