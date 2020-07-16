from queue import LifoQueue
import numpy as np 
import matplotlib.pyplot as plt 
#Cell of a Cell
class Cell:
    def __str__(self):
        return "Maze Cell instance"
    def __init__(self):
        self.Cell_State = {"Visited" :False,
               "Up_Wall": True,
               "Down_Wall":True,
               "Right_Wall": True,
               "Left_Wall" : True
               }
        
    #find cell index in maze list     
    def find_cell_index_in_maze(self,maze,cell): #Get the current cell index
        for i in range(len(maze)):
            for j in range(len(maze[0])):
                if (cell is maze[i][j]):
                    return (i,j)
    #return the list containing this cell neighbors
    def get_cell_neighbors(self,maze,cell,cell_index):
        neighbors = [] 
        if(cell_index[0] < len(maze)-1): #Row is not out of bound 
            up = maze[cell_index[0]+1][cell_index[1]]
            neighbors.append(["Up_Wall",up])
        if(cell_index[0] > 0): #Row is not out of bound
           down = maze[cell_index[0]-1][cell_index[1]]
           neighbors.append(["Down_Wall",down])
        if(cell_index[1] < len(maze[0]) -1 ): #Column is not out of bound 
            right = maze[cell_index[0]][cell_index[1]+1]
            neighbors.append(["Right_Wall",right])
        if(cell_index[1] > 0): #Row is not out of bound
           left = maze[cell_index[0]][cell_index[1]-1]
           neighbors.append(["Left_Wall",left])
        return neighbors

class Stack:
    Stack = None
    
    def __init__(self,row,column):
        self.Row = row
        self.Column = Column 
        self.Stack = LifoQueue(maxsize=self.Row*self.Column)
        print("stack initialized successfully!")
    
    def pop(self):
        if self.Stack.empty():
            print("Stack is Empty!")
        else:
            return self.Stack.get()
        
    def push(self,item):
        if self.Stack.qsize() > self.Row*self.Column:
            print("Error pushing!")
        else:
            return self.Stack.put(item)
        
    def empty(self):
        return self.Stack.empty()
    
    def size(self):
        return self.Stack.qsize()
    


Row = 10
Column = 10
stack = Stack(Row,Column)
Maze = []

#Initial the Maze with Cell Instances
for i in range(Row):
    maze = []
    for j in range(Column):
        maze.append(Cell())
    Maze.append(maze)
        


""" Recursive backtracker Algorithm for maze generation """
#Choose the initial cell, mark it as visited and push it to the stack
Initial_Cell = Maze[0][0]
Maze[0][0].Cell_State['Visited'] = True
stack.push(Initial_Cell)

board = np.zeros(shape=(len(Maze),len(Maze[0])))
def visualize_maze(maze,current_cell_index):
    board[current_cell_index[0],current_cell_index[1]] = 1
    plt.imshow(np.asarray(board,dtype="float32"))  
    plt.show()


#while the stack is not empty 
while not stack.empty():
    #pop a cell from the stack and make it a current cell 
    current_cell = stack.pop()
    
    #Get the current cell index
    current_cell_index = current_cell.find_cell_index_in_maze(Maze,current_cell) 
    #Visualizing the movement of the algorithm
    print("\033[H\033[J") 
    visualize_maze(Maze,current_cell_index)
    
    #if the current cell has any neightbours which have not been visited 
    cell_neighbors = current_cell.get_cell_neighbors(Maze,current_cell,current_cell_index)
    
    #Choose the first neighbor that hasnt been visited ( try using a random value here to test the performance)
    for neighbor in cell_neighbors:
        #choose one of the unvisited neighbors 
        if(neighbor[1].Cell_State["Visited"] == False):        
            #push the current cell to the stack 
            stack.push(neighbor[1])
            #remove the wall between the current cell and the chosen cell 
            neighbor[1].Cell_State[neighbor[0]] = False
            #mark the chosen cell as visited and push it to the stack
            neighbor[1].Cell_State["Visited"] = True
        
            








