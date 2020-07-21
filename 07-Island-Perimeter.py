class Solution:
    def isValid(self, x, y, xmax, ymax):
        if x < 0 or x >= xmax or y < 0 or y >= ymax:
            return False
        return True
        
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        peri = 0
        xmax=len(grid)
        ymax=len(grid[0])
        for i in range(xmax):
            for j in range(ymax):
                if grid[i][j] == 1:
                    neighs = [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
                    for x,y in neighs:
                        if not self.isValid(x,y,xmax,ymax):
                            peri += 1
                        elif grid[x][y] == 0:
                            peri += 1
        return peri

"""
Time : O(n^2)
Space: O(1), no extra space
"""
