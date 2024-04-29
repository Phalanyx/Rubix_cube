import vector_input as vi
from vector_input import cube_dict
import copy
import white_cross as wc
"""Must check 3 colors of edge"""

def check_corner(cube):
    if not (cube.vec_list['white'][0] == 'W0'
             and cube.vec_list['blue'][5] == 'B5' 
             and cube.vec_list['orange'][7] == 'O7'):
        cube.tmp_queue.append(['W0', 'B5', 'O7'])
    if not (cube.vec_list['white'][2] == 'W2'
             and cube.vec_list['blue'][7] == 'B7' 
             and cube.vec_list['red'][5] == 'R5'):
        cube.tmp_queue.append(['W2', 'B7', 'R5'])
    if not (cube.vec_list['white'][5] == 'W5'
             and cube.vec_list['green'][0] == 'G0' 
             and cube.vec_list['orange'][5] == 'O5'):
        cube.tmp_queue.append(['W5', 'G0', 'O5'])
    if not (cube.vec_list['white'][7] == 'W7'
             and cube.vec_list['green'][2] == 'G2' 
             and cube.vec_list['red'][7] == 'R7'):
        cube.tmp_queue.append(['W7', 'G2', 'R7'])
    return

def white_corners(cube, corner):
    if (cube.tmp_queue == []):
        return
    count = 0
    first_check = True
    if (corner[0] in cube.vec_list['white'] 
        and corner[1] in cube.vec_list[vi.get_piece_color(corner[1])] 
        and corner[2] in cube.vec_list[vi.get_piece_color(corner[2])]):
        cube.tmp_queue.remove(corner)
        return
    #pushing white to a nice spot
    if (corner[0] in cube.vec_list['white']):
        tmp_move = cube.sig[vi.get_color(cube, corner[1])]
        while (corner[1] not in cube.vec_list['yellow'] and corner[2] not in cube.vec_list['yellow']):
            getattr(cube, tmp_move)()
            count += 1
        cube.up()
        cube.up()
        while count > 0:
            getattr(cube, tmp_move+'_prime')()
            count -= 1
        first_check = False
    if (corner[1] in cube.vec_list['white'] or corner[2] in cube.vec_list['white'] and first_check):
        if (corner[1] in cube.vec_list['white']):
            nice_corner = corner[2]
            bad_corner = corner[1]
        else:
            nice_corner = corner[1]
            bad_corner = corner[2]
        tmp_move = cube.sig[vi.get_color(cube, corner[0])]
        while (nice_corner not in cube.vec_list['yellow']):
            getattr(cube, tmp_move)()
            count += 1
        cube.up()
        cube.up()
        while count > 0:
            getattr(cube, tmp_move+'_prime')()
            count -= 1
        first_check = False
    # bad case if white on yellow
    sec_col = vi.get_piece_color(corner[2])
    if (corner[0] in cube.vec_list['yellow'] and first_check):
        while (corner[1] not in cube.vec_list[sec_col]):
            cube.up()
        count = 0
        tmp_move = cube.sig[vi.get_color(cube, corner[2])]
        while (corner[1] not in cube.vec_list['yellow']):
            count+=1
            getattr(cube, tmp_move)()
        cube.up()
        cube.up()
        while count > 0:
            getattr(cube, tmp_move+'_prime')()
            count -= 1
    # nice solve
    if (corner[1] in cube.vec_list['yellow']):
        nice_corner = corner[2]
        bad_corner = corner[1]
        bad_centre = cube.vec_list[vi.get_piece_color(bad_corner)]
        nice_centre = cube.vec_list[vi.get_piece_color(nice_corner)]
    else:
        nice_corner = corner[1]
        bad_corner = corner[2]
        bad_centre = cube.vec_list[vi.get_piece_color(bad_corner)]
        nice_centre = cube.vec_list[vi.get_piece_color(nice_corner)]
    while(nice_corner not in nice_centre):
        cube.up()
    count = 0
    tmp_move = cube.sig[vi.get_color(cube, corner[0])]
    while (nice_corner not in cube.vec_list['yellow']):
        count+=1
        getattr(cube, tmp_move)()
    while (bad_corner not in bad_centre):
        cube.up()
    while count > 0:
        getattr(cube, tmp_move+'_prime')()
        count -= 1
    cube.tmp_queue.remove(corner)
    return

def check_end(cube):
    if not (cube.vec_list['white'][0] == 'W0'
             and cube.vec_list['blue'][5] == 'B5' 
             and cube.vec_list['orange'][7] == 'O7'):
        return False
    if not (cube.vec_list['white'][2] == 'W2'
             and cube.vec_list['blue'][7] == 'B7' 
             and cube.vec_list['red'][5] == 'R5'):
        return False
    if not (cube.vec_list['white'][6] == 'W6'
             and cube.vec_list['green'][0] == 'G0' 
             and cube.vec_list['orange'][5] == 'O5'):
        return False
    if not (cube.vec_list['white'][7] == 'W7'
             and cube.vec_list['green'][2] == 'G2' 
             and cube.vec_list['red'][7] == 'R7'):
        return False
    if (cube.vec_list['white'] != ['W0', 'W1', 'W2', 'W3', 'W4', 'W5', 'W6', 'W7']):
        return False
    return True
def solve_white_corners(cube):
    check_corner(cube)
    cube_copy = copy.deepcopy(cube)
    for x in cube_copy.tmp_queue:
        white_corners(cube, x)

#testing
if __name__ == '__main__':
    new = vi.cube(cube_dict)
    vi.random_move(new, 5, vi.colors)
    wc.solve_white_cross(new)
    check_corner(new)
    print(new.moves)
    print(new.tmp_queue)
    print(new.vec_list)
    new_copy = copy.deepcopy(new)
    for x in new_copy.tmp_queue:
        white_corners(new, x)
        print(new.vec_list)
        print(new.moves)
    print(check_end(new))