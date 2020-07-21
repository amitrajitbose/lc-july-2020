class Solution:
    def find(self, i, j, idx):
        # DFS
        if idx == len(self.word):
            return True
        self.board[i][j] = ord(self.board[i][j]) # mark visited
        if i>0 and self.board[i-1][j] == self.word[idx] and self.find(i-1,j,idx+1): return True
        if j>0 and self.board[i][j-1] == self.word[idx] and self.find(i,j-1,idx+1): return True
        if i<len(self.board)-1 and self.board[i+1][j] == self.word[idx] and self.find(i+1,j,idx+1): return True
        if j<len(self.board[0])-1 and self.board[i][j+1] == self.word[idx] and self.find(i,j+1,idx+1): return True
        self.board[i][j] = chr(self.board[i][j]) # mark unvisited, if not found a match
        return False
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        r,c = len(board), len(board[0])
        self.board = board
        self.word = word
        for i in range(r):
            for j in range(c):
                if word[0] == board[i][j] and self.find(i,j,1):
                    return True
        return False

"""
In this algorithm, we are marking the visited nodes by altering the input matrix.
This might not be the right approach in a real life scenario, we can use a set
of stringified(i,j). But this is a space optimization trick that has been used.
Another similar trick instead of converting to ASCII is to convert to equivalent
character by decreasing or increasing ASCII by 65. Other tricks can also be done
based on the language you're on.
"""

