class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        start_color = image[sr][sc]
        
        # The Trap: If the pixel is already the target color, do nothing.
        if start_color == color:
            return image
            
        ROWS = len(image)
        COLS = len(image[0])
        
        # The Paint Spiller
        def dfs(r, c):
            # 1. Base Case: Stop if we hit a boundary wall, or a pixel that isn't the original color
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or image[r][c] != start_color:
                return
                
            # 2. Paint the current pixel!
            image[r][c] = color
            
            # 3. Spill the paint recursively in all 4 directions
            dfs(r + 1, c) # Down
            dfs(r - 1, c) # Up
            dfs(r, c + 1) # Right
            dfs(r, c - 1) # Left
            
        # Drop the very first drop of paint
        dfs(sr, sc)
        
        return image