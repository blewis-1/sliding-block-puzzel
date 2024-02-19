import random
from a_star import A_Star
from bfs import BFS
from board import Board
from dfs import DFS
from ids import IDS
from movement import Movement
from puzzle import Puzzle
from read_file import Read_Rile
import sys
from utility import compare_states, display_clean_state

def main() :
    args = sys.argv[1:]
    if len(args) < 1:
        print("This command-line arguments are needed!")
        exit(1)

    else: 
        file_name = args[1]
        file_content = Read_Rile(file_name).read_file()
        board = Board(file_content)
        puzzle =  Puzzle(board)  
        movement = Movement(board)
        moves = puzzle.available_moves(board.board_state())
         
        if args[0] == 'print':
            board.display_state()   

        elif args[0] == 'done':
            print(puzzle.is_goal(board.board_state()))
        
        elif args[0] == 'applyMove':
            try: 
                move = args[2]
                display_clean_state(board.dimensions,movement.apply_moves(move))
            except IndexError:
                print("Move not available, Index Error")    

        elif args[0] == 'availableMoves':
            print(puzzle.available_moves(board.board_state()))
        
        elif args[0] == 'compare':
            board_1 = board.board_state()
            file_name = args[2]
            file_content = Read_Rile(file_name).read_file()
            board_2 = Board(file_content)
            board_2 = board_2.board_state() 
            print(compare_states(board_1,board_2))
        
        elif args[0] == 'norm':
            display_clean_state(board.dimensions, board.normalize_matrix(board.board_state())) 
            
        elif args[0] == "random":
            positive_integer = int(args[2])
            display_clean_state(board.dimensions,board.get_board_current_state())
            print('')
            number_of_plays = 0
            while number_of_plays <= positive_integer:
                moves = puzzle.available_moves(board.get_board_current_state())
                random_move = random.choice(moves)
                piece = str(random_move[0])
                random_move = f"({piece},{random_move[1]})"
            
                state = movement.apply_moves(str(random_move))
                
                normalized_state = board.normalize_matrix(state)
                if puzzle.is_goal(normalized_state): 
                    display_clean_state(board.dimensions,state)
                    print("goal")
                    return
                else:
                    number_of_plays += 1 
                    board.set_board_current_state(state)
                    print(random_move)
                    display_clean_state(board.dimensions,board.board_current_state)   
                    print('')
        
        elif args[0] == "bfs":
            bfs_solver = BFS(puzzle,board.board_current_state,movement,board)
            bfs_solver.bfs()       
        elif args[0] == "dfs":
            dfs_solver = DFS(puzzle,board.board_current_state,movement,board)
            dfs_solver.dfs()
        elif args[0] == "ids":
            ids_solver = IDS(puzzle,board.board_current_state,movement,board)
            ids_solver.ids(board.board_current_state)
        elif args[0] == "astar":
            a_start = A_Star(puzzle,board.board_current_state,movement,board)
            a_start.a_star()
        
            
main()