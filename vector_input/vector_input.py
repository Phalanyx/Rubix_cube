
import copy
import random
cube_dict = {'white': ['W0', 'W1', 'W2', 'W3', 'W4', 'W5', 'W6', 'W7'], 'yellow': ['Y0', 'Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6', 'Y7'], 
             'green': ['G0', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7'], 'blue': ['B0', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7'], 
             'red': ['R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7'], 'orange': ['O0', 'O1', 'O2', 'O3', 'O4', 'O5', 'O6', 'O7']}
class cube:
    def __init__(self, vec_list):
        self.vec_list = vec_list
        self.tmp_queue = []
        self.moves = []
        self.sig = {'white': 'down', 'yellow': 'up', 'green': 'back', 'blue': 'front', 'red': 'right', 'orange': 'left'}

    def right(self):
        new = copy.deepcopy(self.vec_list)
        self.vec_list['blue'][2] = new['white'][2]
        self.vec_list['blue'][4] = new['white'][4]
        self.vec_list['blue'][7] = new['white'][7]
        self.vec_list['yellow'][2] = new['blue'][2]
        self.vec_list['yellow'][4] = new['blue'][4]
        self.vec_list['yellow'][7] = new['blue'][7]
        self.vec_list['green'][2] = new['yellow'][2]
        self.vec_list['green'][4] = new['yellow'][4]
        self.vec_list['green'][7] = new['yellow'][7]
        self.vec_list['white'][2] = new['green'][2]
        self.vec_list['white'][4] = new['green'][4]
        self.vec_list['white'][7] = new['green'][7]
        self.vec_list['red'][0] = new['red'][5]
        self.vec_list['red'][1] = new['red'][3]
        self.vec_list['red'][2] = new['red'][0]
        self.vec_list['red'][3] = new['red'][6]
        self.vec_list['red'][4] = new['red'][1]
        self.vec_list['red'][5] = new['red'][7]
        self.vec_list['red'][6] = new['red'][4]
        self.vec_list['red'][7] = new['red'][2]
        self.moves.append('R')
        return
    def right_prime(self):
        new = copy.deepcopy(self.vec_list)
        self.vec_list['blue'][2] = new['yellow'][2]
        self.vec_list['blue'][4] = new['yellow'][4]
        self.vec_list['blue'][7] = new['yellow'][7]
        self.vec_list['yellow'][2] = new['green'][2]
        self.vec_list['yellow'][4] = new['green'][4]
        self.vec_list['yellow'][7] = new['green'][7]
        self.vec_list['green'][2] = new['white'][2]
        self.vec_list['green'][4] = new['white'][4]
        self.vec_list['green'][7] = new['white'][7]
        self.vec_list['white'][2] = new['blue'][2]
        self.vec_list['white'][4] = new['blue'][4]
        self.vec_list['white'][7] = new['blue'][7]
        self.vec_list['red'][0] = new['red'][2]
        self.vec_list['red'][1] = new['red'][4]
        self.vec_list['red'][2] = new['red'][7]
        self.vec_list['red'][3] = new['red'][1]
        self.vec_list['red'][4] = new['red'][6]
        self.vec_list['red'][5] = new['red'][0]
        self.vec_list['red'][6] = new['red'][3]
        self.vec_list['red'][7] = new['red'][5]
        self.moves.append("R'")
        return
    def left(self):
        new = copy.deepcopy(self.vec_list)
        self.vec_list['blue'][0] = new['yellow'][0]
        self.vec_list['blue'][3] = new['yellow'][3]
        self.vec_list['blue'][5] = new['yellow'][5]
        self.vec_list['yellow'][0] = new['green'][0]
        self.vec_list['yellow'][3] = new['green'][3]
        self.vec_list['yellow'][5] = new['green'][5]
        self.vec_list['green'][0] = new['white'][0]
        self.vec_list['green'][3] = new['white'][3]
        self.vec_list['green'][5] = new['white'][5]
        self.vec_list['white'][0] = new['blue'][0]
        self.vec_list['white'][3] = new['blue'][3]
        self.vec_list['white'][5] = new['blue'][5]
        self.vec_list['orange'][0] = new['orange'][5]
        self.vec_list['orange'][1] = new['orange'][3]
        self.vec_list['orange'][2] = new['orange'][0]
        self.vec_list['orange'][3] = new['orange'][6]
        self.vec_list['orange'][4] = new['orange'][1]
        self.vec_list['orange'][5] = new['orange'][7]
        self.vec_list['orange'][6] = new['orange'][4]
        self.vec_list['orange'][7] = new['orange'][2]
        self.moves.append('L')
        return
    def left_prime(self):
        new = copy.deepcopy(self.vec_list)
        self.vec_list['blue'][0] = new['white'][0]
        self.vec_list['blue'][3] = new['white'][3]
        self.vec_list['blue'][5] = new['white'][5]
        self.vec_list['yellow'][0] = new['blue'][0]
        self.vec_list['yellow'][3] = new['blue'][3]
        self.vec_list['yellow'][5] = new['blue'][5]
        self.vec_list['green'][0] = new['yellow'][0]
        self.vec_list['green'][3] = new['yellow'][3]
        self.vec_list['green'][5] = new['yellow'][5]
        self.vec_list['white'][0] = new['green'][0]
        self.vec_list['white'][3] = new['green'][3]
        self.vec_list['white'][5] = new['green'][5]
        self.vec_list['orange'][0] = new['orange'][2]
        self.vec_list['orange'][1] = new['orange'][4]
        self.vec_list['orange'][2] = new['orange'][7]
        self.vec_list['orange'][3] = new['orange'][1]
        self.vec_list['orange'][4] = new['orange'][6]
        self.vec_list['orange'][5] = new['orange'][0]
        self.vec_list['orange'][6] = new['orange'][3]
        self.vec_list['orange'][7] = new['orange'][5]
        self.moves.append("L'")
        return
    def front(self):
        new = copy.deepcopy(self.vec_list)
        self.vec_list['white'][0] = new['red'][5]
        self.vec_list['white'][1] = new['red'][3]
        self.vec_list['white'][2] = new['red'][0]
        self.vec_list['red'][0] = new['yellow'][5]
        self.vec_list['red'][3] = new['yellow'][6]
        self.vec_list['red'][5] = new['yellow'][7]
        self.vec_list['yellow'][5] = new['orange'][7]
        self.vec_list['yellow'][6] = new['orange'][4]
        self.vec_list['yellow'][7] = new['orange'][2]
        self.vec_list['orange'][2] = new['white'][0]
        self.vec_list['orange'][4] = new['white'][1]
        self.vec_list['orange'][7] = new['white'][2]
        self.vec_list['blue'][0] = new['blue'][5]
        self.vec_list['blue'][1] = new['blue'][3]
        self.vec_list['blue'][2] = new['blue'][0]
        self.vec_list['blue'][3] = new['blue'][6]
        self.vec_list['blue'][4] = new['blue'][1]
        self.vec_list['blue'][5] = new['blue'][7]
        self.vec_list['blue'][6] = new['blue'][4]
        self.vec_list['blue'][7] = new['blue'][2]
        self.moves.append('F')
        return
    def front_prime(self):
        new = copy.deepcopy(self.vec_list)
        self.vec_list['white'][0] = new['orange'][2]
        self.vec_list['white'][1] = new['orange'][4]
        self.vec_list['white'][2] = new['orange'][7]
        self.vec_list['red'][0] = new['white'][2]
        self.vec_list['red'][3] = new['white'][1]
        self.vec_list['red'][5] = new['white'][0]
        self.vec_list['yellow'][5] = new['red'][0]
        self.vec_list['yellow'][6] = new['red'][3]
        self.vec_list['yellow'][7] = new['red'][5]
        self.vec_list['orange'][2] = new['yellow'][7]
        self.vec_list['orange'][4] = new['yellow'][6]
        self.vec_list['orange'][7] = new['yellow'][5]
        self.vec_list['blue'][0] = new['blue'][2]
        self.vec_list['blue'][1] = new['blue'][4]
        self.vec_list['blue'][2] = new['blue'][7]
        self.vec_list['blue'][3] = new['blue'][1]
        self.vec_list['blue'][4] = new['blue'][6]
        self.vec_list['blue'][5] = new['blue'][0]
        self.vec_list['blue'][6] = new['blue'][3]
        self.vec_list['blue'][7] = new['blue'][5]
        self.moves.append("F'")
        return
    def up(self):
        new = copy.deepcopy(self.vec_list)
        self.vec_list['blue'][0] = new['red'][0]
        self.vec_list['blue'][1] = new['red'][1]
        self.vec_list['blue'][2] = new['red'][2]
        self.vec_list['red'][0] = new['green'][7]
        self.vec_list['red'][1] = new['green'][6]
        self.vec_list['red'][2] = new['green'][5]
        self.vec_list['green'][5] = new['orange'][2]
        self.vec_list['green'][6] = new['orange'][1]
        self.vec_list['green'][7] = new['orange'][0]
        self.vec_list['orange'][0] = new['blue'][0]
        self.vec_list['orange'][1] = new['blue'][1]
        self.vec_list['orange'][2] = new['blue'][2]
        self.vec_list['yellow'][0] = new['yellow'][5]
        self.vec_list['yellow'][1] = new['yellow'][3]
        self.vec_list['yellow'][2] = new['yellow'][0]
        self.vec_list['yellow'][3] = new['yellow'][6]
        self.vec_list['yellow'][4] = new['yellow'][1]
        self.vec_list['yellow'][5] = new['yellow'][7]
        self.vec_list['yellow'][6] = new['yellow'][4]
        self.vec_list['yellow'][7] = new['yellow'][2]
        self.moves.append('U')
        return
    def up_prime(self):
        new = copy.deepcopy(self.vec_list)
        self.vec_list['blue'][0] = new['orange'][0]
        self.vec_list['blue'][1] = new['orange'][1]
        self.vec_list['blue'][2] = new['orange'][2]
        self.vec_list['red'][0] = new['blue'][0]
        self.vec_list['red'][1] = new['blue'][1]
        self.vec_list['red'][2] = new['blue'][2]
        self.vec_list['green'][5] = new['red'][2]
        self.vec_list['green'][6] = new['red'][1]
        self.vec_list['green'][7] = new['red'][0]
        self.vec_list['orange'][0] = new['green'][7]
        self.vec_list['orange'][1] = new['green'][6]
        self.vec_list['orange'][2] = new['green'][5]
        self.vec_list['yellow'][0] = new['yellow'][2]
        self.vec_list['yellow'][1] = new['yellow'][4]
        self.vec_list['yellow'][2] = new['yellow'][7]
        self.vec_list['yellow'][3] = new['yellow'][1]
        self.vec_list['yellow'][4] = new['yellow'][6]
        self.vec_list['yellow'][5] = new['yellow'][0]
        self.vec_list['yellow'][6] = new['yellow'][3]
        self.vec_list['yellow'][7] = new['yellow'][5]
        self.moves.append("U'")
        return

    def down(self):
        new = copy.deepcopy(self.vec_list)
        self.vec_list['blue'][5] = new['orange'][5]
        self.vec_list['blue'][6] = new['orange'][6]
        self.vec_list['blue'][7] = new['orange'][7]
        self.vec_list['red'][5] = new['blue'][5]
        self.vec_list['red'][6] = new['blue'][6]
        self.vec_list['red'][7] = new['blue'][7]
        self.vec_list['green'][0] = new['red'][7]
        self.vec_list['green'][1] = new['red'][6]
        self.vec_list['green'][2] = new['red'][5]
        self.vec_list['orange'][5] = new['green'][2]
        self.vec_list['orange'][6] = new['green'][1]
        self.vec_list['orange'][7] = new['green'][0]
        self.vec_list['white'][0] = new['white'][5]
        self.vec_list['white'][1] = new['white'][3]
        self.vec_list['white'][2] = new['white'][0]
        self.vec_list['white'][3] = new['white'][6]
        self.vec_list['white'][4] = new['white'][1]
        self.vec_list['white'][5] = new['white'][7]
        self.vec_list['white'][6] = new['white'][4]
        self.vec_list['white'][7] = new['white'][2]
        self.moves.append('D')
        return
    def down_prime(self):
        new = copy.deepcopy(self.vec_list)
        self.vec_list['orange'][5] = new['blue'][5]
        self.vec_list['orange'][6] = new['blue'][6]
        self.vec_list['orange'][7] = new['blue'][7]
        self.vec_list['blue'][5] = new['red'][5]
        self.vec_list['blue'][6] = new['red'][6]
        self.vec_list['blue'][7] = new['red'][7]
        self.vec_list['red'][5] = new['green'][2]
        self.vec_list['red'][6] = new['green'][1]
        self.vec_list['red'][7] = new['green'][0]
        self.vec_list['green'][0] = new['orange'][7]
        self.vec_list['green'][1] = new['orange'][6]
        self.vec_list['green'][2] = new['orange'][5]
        self.vec_list['white'][0] = new['white'][2]
        self.vec_list['white'][1] = new['white'][4]
        self.vec_list['white'][2] = new['white'][7]
        self.vec_list['white'][3] = new['white'][1]
        self.vec_list['white'][4] = new['white'][6]
        self.vec_list['white'][5] = new['white'][0]
        self.vec_list['white'][6] = new['white'][3]
        self.vec_list['white'][7] = new['white'][5]
        self.moves.append("D'")
        return
        
    def back(self):
        new = copy.deepcopy(self.vec_list)
        self.vec_list['white'][5] = new['red'][7]
        self.vec_list['white'][6] = new['red'][4]
        self.vec_list['white'][7] = new['red'][2]
        self.vec_list['red'][2] = new['yellow'][0]
        self.vec_list['red'][4] = new['yellow'][1]
        self.vec_list['red'][7] = new['yellow'][2]
        self.vec_list['yellow'][0] = new['orange'][5]
        self.vec_list['yellow'][1] = new['orange'][3]
        self.vec_list['yellow'][2] = new['orange'][0]
        self.vec_list['orange'][0] = new['white'][5]
        self.vec_list['orange'][3] = new['white'][6]
        self.vec_list['orange'][5] = new['white'][7]
        self.vec_list['green'][0] = new['green'][2]
        self.vec_list['green'][1] = new['green'][4]
        self.vec_list['green'][2] = new['green'][7]
        self.vec_list['green'][3] = new['green'][1]
        self.vec_list['green'][4] = new['green'][6]
        self.vec_list['green'][5] = new['green'][0]
        self.vec_list['green'][6] = new['green'][3]
        self.vec_list['green'][7] = new['green'][5]
        self.moves.append('B')
        return
    
    def back_prime(self):
        new = copy.deepcopy(self.vec_list)
        self.vec_list['white'][5] = new['orange'][0]
        self.vec_list['white'][6] = new['orange'][3]
        self.vec_list['white'][7] = new['orange'][5]
        self.vec_list['red'][2] = new['white'][7]
        self.vec_list['red'][4] = new['white'][6]
        self.vec_list['red'][7] = new['white'][5]
        self.vec_list['yellow'][0] = new['red'][2]
        self.vec_list['yellow'][1] = new['red'][4]
        self.vec_list['yellow'][2] = new['red'][7]
        self.vec_list['orange'][0] = new['yellow'][2]
        self.vec_list['orange'][3] = new['yellow'][1]
        self.vec_list['orange'][5] = new['yellow'][0]
        self.vec_list['green'][0] = new['green'][5]
        self.vec_list['green'][1] = new['green'][3]
        self.vec_list['green'][2] = new['green'][0]
        self.vec_list['green'][3] = new['green'][6]
        self.vec_list['green'][4] = new['green'][1]
        self.vec_list['green'][5] = new['green'][7]
        self.vec_list['green'][6] = new['green'][4]
        self.vec_list['green'][7] = new['green'][2]
        self.moves.append("B'")
        return
    
    def middle(self):
        self.right_prime()
        self.left()
        return

def get_color(cube, edge):
        if edge in cube.vec_list['white']:
            return 'white'
        if edge in cube.vec_list['blue']:
            return 'blue'
        if edge in cube.vec_list['orange']:
            return 'orange'
        if edge in cube.vec_list['red']:
            return 'red'
        if edge in cube.vec_list['green']:
            return 'green'
        if edge in cube.vec_list['yellow']:
            return 'yellow'
        return 'error'

def get_piece_color(piece):
    if piece[0] == 'W':
        return 'white'
    if piece[0] == 'B':
        return 'blue'
    if piece[0] == 'O':
        return 'orange'
    if piece[0] == 'R':
        return 'red'
    if piece[0] == 'G':
        return 'green'
    if piece[0] == 'Y':
        return 'yellow'
    return 'error'
colors = ['white', 'yellow', 'green', 'blue', 'red', 'orange']
new_cube = cube(copy.deepcopy(cube_dict))

def random_move(cube, moves, colors):
    for i in range(moves):
        seed = random.randint(0,5)
        getattr(cube, (cube.sig[colors[seed]]))()

