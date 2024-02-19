
def board_dimensions(content: str) -> list:
    """Get the board dimensions from the file read."""
    dimensions = []
    for s in content:
        if str.isdigit(s):
            dimensions.append(int(s))
        if s == '\n':
            return dimensions
    return dimensions

def get_board_data(content: str) -> list:
    """Get the board data from the file read."""
    board_data = []
    current_number = ''
    
    for s in content:
        if s.isdigit() or (s == '-' and not current_number):
            current_number += s
        elif current_number:
            board_data.append(int(current_number))
            current_number = ''

    if current_number:
        board_data.append(int(current_number))

    return board_data

def display_clean_state(dimensions,state) -> list:
        """Display the current board state """

        for dimension in dimensions:
            print(f"{dimension:2}", end=", ")
        print('')    

        for row in state:
            for num in row:
                print(f"{num:2}", end=", ")
            print('') 
        return state 

def brick_side(current_piece:int,state:list,row:int,col:int,sides):
    
    same_up = current_piece == state[row - 1][col] 
    same_down = current_piece == state[row +1][col]
    same_right = current_piece == state[row][col +1]
    same_left = current_piece == state[row][col - 1]
    
    if same_up:
        sides = sides + 1
    elif same_down:
        sides = sides + 1 
    elif same_right:
        sides = sides + 1
    elif same_left: 
        sides = sides + 1
    if sides == 0:
       sides += 1                                                 
    return sides   

def compare_states(state_1, state_2): 
    if len(state_1) != len(state_2) or len(state_1[0]) != len(state_2[0]):
        return False

    for row in range(len(state_1)):
        for col in range(len(state_1[0])):
            if state_1[row][col] != state_2[row][col]:
                return False  

    return True  


def side_positions(current_piece:int,state:list,row:int,col:int, side_position:list):
    
    same_up = current_piece == state[row - 1][col] 
    same_down = current_piece == state[row +1][col]
    same_right = current_piece == state[row][col +1]
    same_left = current_piece == state[row][col + 1]
    
    if same_up:
        side_position.append("UP")
    elif same_down:
        side_position.append("DOWN")
    elif same_right:
        side_position.append("RIGHT")
    elif same_left: 
        side_position.append("LEFT")
                                       
    return side_position