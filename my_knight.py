
import time


class knight_tour:
    def __init__(self,start=(0,0),N=5):
        self.size=N
        self.step_count=1
        self.moves_x=[2, 1, -1, -2, -2, -1, 1, 2]
        self.moves_y=[1, 2, 2, 1, -1, -2, -2, -1]
        self.start=start
        #initailizing solution
        self.solution=[[-1 for _ in range(self.size)] for _ in range(self.size)]

    def knight_tour(self,i,j,step_count):
        if step_count==(self.size**2+1):
            return True
        
        for k in range(8):
            next_i= i+self.moves_x[k]
            next_j= j+self.moves_y[k]

            if(self.is_valid(next_i,next_j)):
                self.solution[next_i][next_j]=step_count
                if(self.knight_tour(next_i,next_j, step_count+1)):
                    return True
                self.solution[next_i][next_j]= -1
        return False
    
    def is_valid(self,next_i, next_j):
        if(next_i>=0 and next_i<=self.size-1 and next_j>=0 and next_j<=self.size-1):
            if(self.solution[next_i][next_j]==-1):
                return True
        return False
    
    def start_tour(self):
        i,j=self.start
        self.solution[i][j]=self.step_count
        if(self.knight_tour(i,j,2)):
            for i in range(self.size):
                print(self.solution[i])
            return True
        return False

if __name__=='__main__':
    coordinate=input("Enter the first position where you want to place your knight at first: ")
    points=tuple(int(x) for x in coordinate.split())
    size=int(input("Enter the size of N*N chessboard: "))
    knight=knight_tour(points,size)
    start_time=time.time()
    print(knight.start_tour())
    end_time=time.time()
    difference_time=(end_time-start_time)
    print('Required time for solution: ', difference_time)
