class Solution:
    def knightDialer(self, n: int) -> int:
        ph=[[0 for row in range(n+1)] for col in range(10)]
        
        for r in range (n+1):
             print (ph[r])
        
        for c in range (10):
            ph[c][0]=1
            
        for i in range(1,n+1):
            ph[0][i]=ph[4][i-1]+ph[6][i-1]
            ph[1][i]=ph[6][i-1]+ph[8][i-1]
            ph[2][i]=ph[7][i-1]+ph[9][i-1]
            ph[3][i]=ph[4][i-1]+ph[8][i-1]
            ph[4][i]=ph[0][i-1]+ph[9][i-1]+ph[3][i-1]
            ph[5][i]=0
            ph[6][i]=ph[1][i-1]+ph[7][i-1]+ph[0][i-1]
            ph[7][i]=ph[2][i-1]+ph[6][i-1]
            ph[8][i]=ph[1][i-1]+ph[3][i-1]
            ph[9][i]=ph[2][i-1]+ph[4][i-1]
        for r in range (n+1):
             print (ph[r])
            
        return sum(ph[n])%(10**9+7)    
            
                
