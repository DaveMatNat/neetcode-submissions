class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # start at sr, sc, og color image[sr][sc]
        # dfs on neighbors with the same color (image[sr][sc])
        # if neighbor is (image[sr][sc]), then image[r][c] = color
        if image[sr][sc] == color:
            return image
            
        og_color = image[sr][sc]
        directions = [(-1,0),(0,-1),(0,1),(1,0)] # left, up, down, right
        rows, cols = len(image), len(image[0])

        # dfs
        stack = [(sr,sc)]
        image[sr][sc] = color
        
        while stack:
            pixel_r, pixel_c = stack.pop() # (r,c)
            for dx, dy in directions:
                neigh_r, neigh_c = pixel_r + dx, pixel_c + dy
                if 0 <= neigh_r < rows and 0 <= neigh_c < cols and image[neigh_r][neigh_c] == og_color:
                    image[neigh_r][neigh_c] = color # mark it as soon as discover
                    stack.append((neigh_r, neigh_c))
        return image


