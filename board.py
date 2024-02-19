from utility import board_dimensions, get_board_data


class Board():
    """Display the board as a matrix. """
    
    def __init__(self,file_content:str) -> None:
        self.file_content = file_content
        self.dimensions = board_dimensions(self.file_content)
        self.board_data = get_board_data(self.file_content)
        self.board_current_state = []
    
    def get_board_current_state(self) -> list:
        if len(self.board_current_state) == 0:       
            self.board_current_state = self.board_state()
            return self.board_current_state
        else:
            return self.board_current_state          

    def set_board_current_state(self,state):
        self.board_current_state = state    

    def board_state(self) -> list:
        """Get the current board state from the file read. Excluding dimensions"""

        board_matrix = []
    
        i = 0
        # dimensions[1] -> height
        for _ in range(self.dimensions[1]):
            a = []
            #dimension[0] -> width 
            for _ in range(self.dimensions[0]):   
                a.append(self.board_data[i + 2])
                i += 1
            board_matrix.append(a)
        self.board_current_state = board_matrix      
        return self.board_current_state    
    
    def display_state(self):
        """Display the board state """

        for dimension in self.dimensions:
            print(f"{dimension:2}", end=", ")
        print('')    

        for row in self.get_board_current_state():
            for num in row:
                print(f"{num:2}", end=", ")
            print('') 
    
    def clone_board(self) ->list:
         """ Clones the board of the matrix"""
         return self.get_board_current_state().copy()
    
    def swap_Idx(self,matrix, idx1 ,idx2):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if(matrix[i][j] == idx1):
                    matrix[i][j] = idx2
                elif(matrix[i][j] == idx2):
                    matrix[i][j] = idx1

    def normalize_matrix(self,matrix):
        nextIdx = 3
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (matrix[i][j] == nextIdx):
                    nextIdx += 1
                elif(matrix[i][j] > nextIdx): 
                    self.swap_Idx(matrix, nextIdx, matrix[i][j])
                    nextIdx += 1
        return matrix
                    
        
        
                    
                                                                  
                               
          