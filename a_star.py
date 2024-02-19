import heapq
from board import Board
from movement import Movement
from puzzle import Puzzle
import time
from utility import display_clean_state


class A_Star():
    """Class to perform A* search on the matrix"""
    
    def __init__(self, puzzle: Puzzle, state: list, movement: Movement, board: Board) -> None:
        self.puzzle = puzzle
        self.state = state
        self.movement = movement
        self.board = board
    
    def clone_state(self, state) -> list:
        """Function to clone the given state."""
        state_copy = [row[:] for row in state]
        return state_copy
    
    def swap_Idx(self, matrix, idx1, idx2):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == idx1:
                    matrix[i][j] = idx2
                elif matrix[i][j] == idx2:
                    matrix[i][j] = idx1

    def normalize_matrix(self, matrix):
        nextIdx = 3
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == nextIdx:
                    nextIdx += 1
                elif matrix[i][j] > nextIdx: 
                    self.swap_Idx(matrix, nextIdx, matrix[i][j])
                    nextIdx += 1
        return matrix
    
    def heuristic(self, state) -> int:
        """Manhattan distance heuristic: sum of the distances of each tile from its goal position."""
        total_distance = 0
        for i in range(len(state)):
            for j in range(len(state[0])):
                if state[i][j] != 0: 
                    goal_row, goal_col = divmod(state[i][j] - 1, len(state[0]))
                    total_distance += abs(i - goal_row) + abs(j - goal_col)
        return total_distance
    
    def a_star(self):
        start = time.time()
        current_state = self.state
        queue = [(self.heuristic(current_state), current_state, [])]  
        
        visited_states = set() 
        
        while queue:
            _, node, path = heapq.heappop(queue)  
            
            if self.puzzle.is_goal(node):
                end = time.time()
                totalTime = end - start
                
                for i in range(len(path)):
                    print(path[i])
                    
                print('')
                display_clean_state(self.board.dimensions, node)
                print('')
                print(len(visited_states))
                print(round(totalTime, 2))
                print(len(path))
                
                return 
            
            visited_states.add(tuple(map(tuple, node)))
            
            moves = self.puzzle.available_moves(node)
            
            for move in moves:
                piece = str(move[0])
                move_string = f"({piece},{move[1]})"
                cloned_state = self.clone_state(node)
                new_state = self.movement.apply_moves(move_string, cloned_state)
                new_normalized_state = self.normalize_matrix(new_state)
                
                if tuple(map(tuple, new_normalized_state)) not in visited_states:
                    g_n = len(path) + 1 
                    h_n = self.heuristic(new_normalized_state)
                    heapq.heappush(queue, (g_n + h_n, new_normalized_state, path + [move]))

