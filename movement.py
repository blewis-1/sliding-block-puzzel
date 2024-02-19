from board import Board
from utility import brick_side, side_positions

class Movement():
    """Take a piece and apply a move."""
    def __init__(self, board: Board) -> None:
            self.board = board
        
    def swap_right_double_move(self, state, row, col, current_piece):
        state[row + 1][col] = current_piece
        state[row][col] = 0  
                                                        
        state[row+1][col+1] = current_piece
        state[row ][col+1] = 0                                                                             
                                    
    def __move_1_block(self, state, direction, row, col, current_piece):
        if direction == "up":
            if state[row -1][col] == 0:
                state[row -1][col] = current_piece
                state[row][col] = 0
        if direction == "down" :
            if state[row + 1][col] == 0:
                state[row + 1][col] = current_piece
                state[row][col] = 0 
        if direction == "right":
            if state[row][col + 1] == 0:
                state[row][col + 1] = current_piece
                state[row][col] = 0  
        if direction == "left":
            if state[row][col - 1] == 0:
                state[row][col - 1] = current_piece
                state[row][col] = 0   
                
    def __move_2_block(self,state,direction,row,col,current_piece,side_position:list):
            two_moves = 0
            if direction == "right":
                if len(side_position) >= 1:
                    if side_position[0] == "DOWN":
                        if current_piece == 2 and state[row][col +1] == -1 :
                            state[row][col + 1] = current_piece
                            state[row][col] = 0
                            
                            state[row +1][col] = 0
                            state[row +1][col + 1] = current_piece   
                            
                        if state[row][col + 1] == 0:
                            state[row][col + 1] = current_piece
                            state[row][col] = 0 
                        if state[row+ 1][col + 1] == 0:    
                            state[row + 1][col + 1] = current_piece
                            state[row + 1][col] = 0 
                                
                    if side_position[0] == "RIGHT":
                        if (col + 2) <= len(state[row]) - 1: 
                            if current_piece == 2 and state[row][col + 2] == -1:
                                 state[row][col + 2] = current_piece
                                 state[row][col] = 0  
                                
                            if state[row][col + 2] == 0:
                                state[row][col + 2] = current_piece
                                state[row][col] = 0  
                                return                 

            elif direction == "left":
                if len(side_position) >= 1:
                    if side_position[0] == "DOWN":
                        if current_piece == 2 and state[row][col - 1] == -1:
                            state[row][col] = 0
                            state[row][col -1] = current_piece
                        
                        if state[row][col - 1] == 0:
                            state[row][col - 1] = current_piece
                            state[row][col] = 0 
                                
                        if state[row+ 1][col - 1] == 0:    
                                state[row + 1][col - 1] = current_piece
                                state[row + 1][col] = 0
                                
                    if side_position[0] == "RIGHT":
                        if current_piece == 2 and state[row][col - 1] == -1:
                            state[row][col -1] = current_piece
                            state[row][col] = 0
                            
                            state[row][col +1] = 0 
                            state[row][col] = current_piece  
                                                       
                        if state[row][col - 2] == 0:
                            state[row][col - 2] = current_piece
                            state[row][col] = 0 

            elif direction == "down":
                if row != len(state) - 1:
                    if len(side_position) >= 1:
                        if side_position[0] == "DOWN":
                            if row + 2 <= len(state) - 1:
                                if current_piece == 2 and state[row + 2][col] == -1:
                                    state[row][col] = 0
                                    state[row + 2][col] = current_piece
                                    return
                                
                                if state[row + 2][col] == 0: 
                                    state[row + 2][col] = current_piece
                                    state[row][col] = 0 
                                    
                        if side_position[0] == "RIGHT":
                            if two_moves <= 1:
                                if current_piece == 2 and state[row + 1][col] == -1:
                                    if state[row + 1][col] == -1 and state[row+1][col + 1] == -1:
                                        self.swap_right_double_move(state, row, col, current_piece)
                                        two_moves += 1
                                        
                                if state[row + 1][col] == 0 and state[row+1][col + 1] == 0:
                                        self.swap_right_double_move(state, row, col, current_piece)
                                        two_moves += 1
                                      
            elif direction == "up":
                if len(side_position) >= 1:
                    if side_position[0] == "DOWN":
                        if current_piece == 2 and state[row - 1][col] == -1:
                            state[row + 1][col] = 0
                            state[row -1][col] = current_piece
                            
                        if state[row - 2][col] == 0:
                            # first right
                            state[row - 2][col] = current_piece
                            state[row][col] = 0 
                    
                    if side_position[0] == "RIGHT":
                        if current_piece == 2 and state[row - 1][col] == -1:
                            if state[row - 1][col] == -1 and state[row-1][col + 1] == -1:
                                state[row - 1][col] = current_piece
                                state[row][col] = 0  
                                state[row - 1][col+ 1] = current_piece
                                state[row][col + 1] = 0  
                                                                    
                        if state[row - 1][col] == 0:
                        # first right
                            state[row - 1][col] = current_piece
                            state[row][col] = 0 
               
    def __move_4_block(self,state,direction,row,col,current_piece,side_position:list):
            four_down_actions = 0 
            down = 0
            up = 0 
            for side_direction in side_position:
                if side_direction == "DOWN":
                    down = down + 1
                if side_direction == "UP":
                    up = up + 1
            if up == 2 and down == 2:
                if direction == "right":
                    if col + 2 <= len(state[row]) - 1:
                        piece_beside = state[row][col + 1]
                        if current_piece == 2 and piece_beside == current_piece:
                            if state[row][col + 2] == -1:
                                state[row][col + 2] = current_piece
                                state[row][col] = 0
                        
                        if current_piece == piece_beside and state[row][col + 2] == 0:
                            state[row][col + 2] = current_piece
                            state[row][col] = 0
                            
                if direction == "left":
                        piece_beside = state[row][col + 1]
                        if current_piece == 2 and piece_beside == current_piece:
                            if state[row][col - 1] == -1:
                                state[row][col - 1] = current_piece
                                state[row][col + 1] = 0 
                        
                        if current_piece == piece_beside and state[row][col - 1] == 0:
                            state[row][col - 1] = current_piece
                            state[row][col + 1] = 0     
                
                if direction == "up":
                    piece_below = state[row+1][col]
                    piece_above = state[row -1][col]
                    if current_piece == 2 and current_piece == piece_below:
                        if piece_above == -1:
                            state[row+1][col] =  0
                            state[row-1][col] = current_piece 
                        
                    
                    if current_piece == piece_below and piece_above == 0:
                        state[row+1][col] =  0
                        state[row-1][col] = current_piece  
                        
                if direction == "down":
                    # checks of the piece below and the current piece are the same and 
                    # the piece below the piece below the current piece is 0
                    if four_down_actions <= 2:
                       
                       if row + 2 <= len(state[row]): 
                            piece_below = state[row+1][col]
                            piece_below_the_piece_below = state[row + 2][col]
                            
                            if current_piece == 2 and piece_below == current_piece:
                                if piece_below_the_piece_below == -1:
                                    state[row + 2][col] = current_piece
                                    state[row][col] = 0
                                    four_down_actions += 1 
                                    
                            if piece_below == current_piece and piece_below_the_piece_below == 0:
                                state[row + 2][col] = current_piece
                                state[row][col] = 0
                                four_down_actions += 1   
                                                              
    def apply_moves(self, move,state):
        """Apply the given move and print the state"""""
        direction = move.lstrip("(").rstrip(")").split(",").pop()
        piece = int(move.lstrip("(").rstrip(")").split(",")[0])      
        self.change_state(state,direction,piece)
        
        return state               
    
    def change_state(self,state,direction,piece):
            "Change the state base on the moves passed down."
            sides = 0
            side_position = []
            
            for row in range(len(state)):
                for col in range(len(state[row])):
                    current_piece = state[row][col]
                    if current_piece != 1 and current_piece != -1:
                        if current_piece != 0 and current_piece == piece:  
                                sides =  brick_side(current_piece,state, row,col,sides)
                                side_position = side_positions(current_piece,state, row,col,side_position)
                           
            for row in range(len(state)):
                for col in range(len(state[row])):
                    current_piece = state[row][col]
                    if current_piece != 1 and current_piece != -1:
                        if current_piece != 0 and current_piece == piece:  
                                if sides == 1:
                                    self.__move_1_block(state, direction, row, col, current_piece)
                                if sides == 2:
                                    self.__move_2_block(state, direction, row,col,current_piece,side_position)  
                                if sides == 4:
                                    self.__move_4_block(state, direction, row,col,current_piece,side_position)
                                          

        