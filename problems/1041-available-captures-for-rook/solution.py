class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        def findwhite():
            for i in range (8):
                for j in range(8):
                    if board[i][j]=='R':
                        return (i,j)

        x,y = findwhite()
        ans = 0
        directions = [(0,1),(1,0),(-1,0),(0,-1)] 
        for i,j in directions :
            f1,f2 = i,j
            while 0<=f1+x<8 and 0<=y+f2<8:
                if board[f1+x][f2+y]=='p':
                    ans += 1 
                    break
                if board[f1+x][f2+y]=='B':
                    break
                f1+=i
                f2+=j
        return ans
