"""
Starting at the top left corner of an N x M grid and facing towards the right,
you keep walking one square at a time in the direction you are facing. If you 
reach the boundary of the grid or if the next square you are about to visit has
already been visited, you turn right. You stop when all the squares in the grid 
have been visited. What direction will you be facing when you stop? For example: 
Consider the case with N = 3, M = 3. The path followed will be (0,0) -> (0,1) -> 
(0,2) -> (1,2) -> (2,2) -> (2,1) -> (2,0) -> (1,0) -> (1,1). At this point, all 
squares have been visited, and you are facing right.

Input:
The first line contains T the number of test cases. Each of the next T lines 
contain two integers N and M, denoting the number of rows and columns respectively.
Output:
Output T lines, one for each test case, containing the required direction you will}
be facing at the end. Output L for left, R for right, U for up, and D for down.
1 <= T <= 5000, 1 <= N,M <= 10^9.

Proposed Solution By Luis Mex
12/6/2020
"""


def create_matrix(n,m): 
# This function create a matrix that represent the board
    zero =0 
    matrix = [[zero for i in range(0,n)] for j in range(0,m)]
    return matrix


class Peon():
    #class called Peon where initialize the movements at 0,0 
    def __init__(self,initial_x,initial_y,m,n) :
    # m  : columns
    # n  ; rows
    # x : position x at the board
    # y : position y at the board
        self.x = initial_x
        self.y = initial_y
        self.n = n
        self.m = m
        self.matrix = create_matrix(self.n,self.m)
        self.matrix[self.x][self.y] = 1
        self.moves =  []
        self.moves.append([self.x,self.y])
        self.directions =['R','D','L','U']
        self.facing =[]
        self.facing.append(self.directions[0])
    #method that returns the output of the statement problem
    def face(self):
        return (self.facing[-1])
    
    def is_safe(self,x,y):
    #method to determine if a following step is allowed    
        if (x >= 0 and x < self.m and y >= 0 and y < self.n and self.matrix[x][y] == 0 ):
            return True
        return False
                    
    def possible_moves(self,current_x,current_y):
    # Recursive method where all the moves are called according to the statement problem                
        # print("matrix")
        # for i in self.matrix:
        #      print(i)
        
               
        if len(self.moves)-1 >= self.n*self.m :
            return self.moves
    #here we state where last step is reached
        temp = self.moves[-1]
       
        if (self.is_safe(temp[0],temp[1]+1) and [temp[0],temp[1]+1] not in self.moves ):
            self.matrix[temp[0]][temp[1]+1] = 1
            self.moves.append([temp[0],temp[1]+1])
            self.facing.append(self.directions[0])
            temp = self.moves[-1]
            self.possible_moves(temp[0],temp[1])
        else:
            
            if(self.is_safe(temp[0]+1,temp[1])and [temp[0]+1,temp[1]] not in self.moves):
                self.matrix[temp[0]+1][temp[1]] = 1
                self.moves.append([temp[0]+1,temp[1]])
                self.facing.append(self.directions[1])
                temp = self.moves[-1]
                self.possible_moves(temp[0],temp[1])
                
            else:
                
                if(self.is_safe(temp[0],temp[1]-1) and [temp[0],temp[1]-1] not in self.moves):
                    self.matrix[temp[0]][temp[1]-1] = 1
                    self.moves.append([temp[0],temp[1]-1])
                    self.facing.append(self.directions[2])
                    temp = self.moves[-1]
                    self.possible_moves(temp[0],temp[1])
                    
                else:
                  
                    if(self.is_safe(temp[0]-1,temp[1]) and [temp[0]-1,temp[1]] not in self.moves):
                        self.matrix[temp[0]-1][temp[1]] = 1
                        self.moves.append([temp[0]-1,temp[1]])
                        self.facing.append(self.directions[3])
                        temp = self.moves[-1]
                        self.possible_moves(temp[0],temp[1])
                      
            return self.facing
           


if __name__ == '__main__':
    lista = []
    st = input()
    
    for i in range(0,int(st)):
        mn_values = (input().split())
        m = int(mn_values[0])
        n = int(mn_values[1])
        lista.append([m,n])
    
    for j in lista:
        My_peon = Peon(0,0,j[0],j[1])
        My_peon.possible_moves(0,0)
        print(My_peon.face())