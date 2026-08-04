class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # start at sr, sc, og color image[sr][sc]
        # dfs on neighbors with the same color (image[sr][sc])
        # if neighbor is (image[sr][sc]), then image[r][c] = color

        og_color = image[sr][sc]
        directions = [(-1,0),(0,-1),(0,1),(1,0)] # left, up, down, right
        rows, cols = len(image), len(image[0])
        # dfs
        seen = set()
        stack = [(sr,sc)]
        while stack:
            pixel_r, pixel_c = stack.pop() # (r,c)
            seen.add((pixel_r, pixel_c))
            image[pixel_r][pixel_c] = color
            for dx, dy in directions:
                neigh_r, neigh_c = pixel_r + dx, pixel_c + dy
                # in range, og color
                if neigh_r in range(rows) and neigh_c in range(cols) and image[neigh_r][neigh_c] == og_color and (neigh_r, neigh_c) not in seen:
                    stack.append((neigh_r, neigh_c))
                    image[neigh_r][neigh_c] = color
        return image


