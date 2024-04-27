import vector_input as vi
from vector_input import cube_dict
import copy
""" Important edges: W1/B6, W3/O6, W4/R6, W6/G1
Care about: white = [junk, W1, junk, W3, W4, junk, W6, junk],
 blue = [junk, junk, junk, junk, junk, junk, B6, junk], 
 orange = [junk, junk, junk, O6, junk, junk, B6, junk], 
 red = [junk, junk, junk, junk, R6, junk, B6, junk], 
 green = [junk, G1, junk, junk, junk, junk, junk, junk]
 turning a face, signature: 
 blue: F, orange: L, red: R, green: B"""

def check_cross(cube):
    if not (cube.vec_list['white'][1] == 'W1' and cube.vec_list['blue'][6] == 'B6'):
         cube.tmp_queue.append(['W1','B6', 'blue', 'front'])
    if not (cube.vec_list['white'][3] == 'W3' and cube.vec_list['orange'][6] == 'O6'):
        cube.tmp_queue.append(['W3','O6', 'orange', 'left'])
    if not (cube.vec_list['white'][4] == 'W4' and cube.vec_list['red'][6] == 'R6'):
        cube.tmp_queue.append(['W4','R6', 'red', 'right'])
    if not (cube.vec_list['white'][6] == 'W6' and cube.vec_list['green'][1] == 'G1'):
        cube.tmp_queue.append(['W6','G1', 'green', 'back'])
    return
#returns what centre a certain edge is on
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

new = vi.cube(cube_dict)
def white_cross(cube, edge):
    #trivial case
    if (len(cube.tmp_queue) == 0):
        return
    if (edge[1] in cube.vec_list[edge[2]]):
        while (edge[0] not in cube.vec_list['white']):
            getattr(cube, edge[3])()
        cube.tmp_queue.remove(edge)
        return
    #check if opposite edge is on white, force onto yellow:
    tmp_move = cube.sig[get_color(cube, edge[0])]
    if (edge[1] in cube.vec_list['white']):
        while (edge[1] not in cube.vec_list['yellow']):
            getattr(cube, tmp_move)()
    #force onto yellow:
    tmp_move = cube.sig[get_color(cube, edge[1])]
    count = 0
    while (edge[0] not in cube.vec_list['yellow'] and edge[1] not in cube.vec_list['yellow']):
        print(tmp_move)
        getattr(cube, tmp_move)()
        count += 1
    cube.up()
    while count > 0:
        getattr(cube, tmp_move+'_prime')()
        count -= 1
    if (edge[0] in cube.vec_list['yellow']):
        while (edge[1] not in cube.vec_list[edge[2]]):
            cube.up()
        getattr(cube, edge[3])()
        getattr(cube, edge[3])()
        cube.tmp_queue.remove(edge)
        return
    if (edge[1] in cube.vec_list['yellow']):
        while (edge[0] not in cube.vec_list[edge[2]]):
            cube.up()
        cube.up()
        tmp_move = cube.sig[get_color(cube, edge[0])]
        count = 0
        while (edge[1] not in cube.vec_list[edge[2]]):
            getattr(cube, tmp_move)()
            count += 1
        while (edge[0] not in cube.vec_list['white']):
            getattr(cube, edge[3])()
        while count > 0:
            getattr(cube, tmp_move+'_prime')()
            count -= 1
        cube.tmp_queue.remove(edge)
        return

    
def check_end(cube):
    if (cube.vec_list['white'][1] == 'W1' and cube.vec_list['blue'][6] == 'B6' 
        and cube.vec_list['white'][3] == 'W3' and cube.vec_list['orange'][6] == 'O6' 
        and cube.vec_list['white'][4] == 'W4' and cube.vec_list['red'][6] == 'R6' 
        and cube.vec_list['white'][6] == 'W6' and cube.vec_list['green'][1] == 'G1'):
        return True
    return False
if __name__ == '__main__':
    new = vi.cube(cube_dict)
    vi.random_move(new, 5, vi.colors)

    check_cross(new)
    print(new.tmp_queue)
    new_copy = copy.deepcopy(new)
    for x in new_copy.tmp_queue:
        white_cross(new, x)
        print(new.vec_list)
        print(new.moves)
    print(check_end(new))


