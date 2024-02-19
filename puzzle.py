from board import Board

class Puzzle: 
    """ Game engine  for sbp puzzle"""

    def __init__(self, board: Board) -> None:
        self.board = board

    def is_goal(self,state:list):
        """ Identify is goal state"""
        for item in state:
            for piece in item:
                if piece == -1:
                    return False
                
        return  True

    def __move_up(self,row,col,state) -> bool:
        current_piece = state[row][col]
        if row >= 1:
            if current_piece == 2:
            # is the piece to the right or left that is two
                if state[row][col + 1] == 2:
                    if state[row-1][col] == state[row-1][col + 1]:
                        if state[row-1][col] == 0 or state[row-1][col] == -1:
                            return True
                        
                elif state[row][col - 1] == 2:  
                    if state[row+1][col] == state[row + 1][col - 1]:
                        if state[row+1][col] == 0 or state[row+1][col-1] == -1:
                            return True 
            
            if state[row -1 ][col] == 0:
                if state[row][col + 1] == state[row][col] and state[row+1][col + 1] == 0 :
                    if state[row][col - 1] == state[row][col] and state[row+1][col - 1] == 0:
                        return True
                    
        return False
    
    def __move_left(self,row,col,state) ->bool:  
        if  col >= 1:
            left_element = state[row][col-1]
            if state[row][col] == 2:
                if left_element == 0 or left_element == -1:
                   return True
            if left_element == 0:
                return True
        return False
    
    def __move_right(self,row,col,state) -> bool:
        if col >= 1:
            right_element = state[row][col+1]
            if state[row][col] == 2:
                if right_element == 0 or right_element == -1:
                    return True
                    
            if right_element == 0:
                return True
        return False
    
    def __move_down(self,row,col,state) -> bool:
        if row >= 1 :
            bottom_element = state[row + 1 ][col ]
            if state[row][col] == 2:
               if bottom_element == 0 or bottom_element == -1:
                   return True
               
            if bottom_element == 0:
                return True
            elif state[row][col+1] == state[row][col] and state[row+1][col + 1] == 0:
                    if state[row][col-1] == state[row][col] and state[row+1][col - 1] == 0:
                        return True
        return False
    
    def available_moves(self,state:list)-> list:
        """Gets the available moves from the index"""

        moves = []
        for row in range(len(state)):
            for col in range(len(state[row])):
                try:
                   current_piece = state[row][col]
                   if current_piece != 1 and current_piece != -1:
                        if current_piece != 0:           
                            if self.__move_up(row,col,state):
                                moves.append((current_piece,"up"))
                            if self.__move_left(row,col,state):
                                moves.append((current_piece,"left"))
                            if self.__move_right(row,col,state):
                                moves.append((current_piece,"right"))
                            if self.__move_down(row,col,state):
                                moves.append((current_piece,"down"))  
                except IndexError:
                    print(row,col,"Error here!!")               
        return moves                   

   
        
    
                                
             
                                    
                                
                                                         
                                

    
                                                  
                                               



    

                   
          


       