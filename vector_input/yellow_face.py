""" Solving the yellow face"""
#import solver as solve
import vector_input as vi
import copy
def yellow_edge_counter(cube):
    counter = 0
    edges = [1,3,4,6]
    for x in edges:
        if cube.vec_list['yellow'][x][0] == 'Y':
            counter+=1
    return counter

# if counter == 4, then done, else must check for line or plus shape


def line_check(cube):
    if ((cube.vec_list['yellow'][1][0] == 'Y' and cube.vec_list['yellow'][6][0] == 'Y')
        or (cube.vec_list['yellow'][3][0] == 'Y' and cube.vec_list['yellow'][4][0] == 'Y')):
        return True
    return False

def yellow_cross(cube):
    first_check = False
    edge_count = yellow_edge_counter(cube)
    if (edge_count) == 4:
        return
    if (edge_count) == 0:
        first_check = True
    if line_check(cube) or first_check:
        while cube.vec_list['yellow'][6][0] == 'Y' and not first_check:
            cube.up()
        cube.front()
        cube.right()
        cube.up()
        cube.right_prime()
        cube.up_prime()
        cube.front_prime()
        if (first_check):
            yellow_cross(cube)
        return
    else:
        while (cube.vec_list['yellow'][1][0] != 'Y' or cube.vec_list['yellow'][3][0] != 'Y'):
            cube.up()
        cube.front()
        cube.up()
        cube.right()
        cube.up_prime()
        cube.right_prime()
        cube.front_prime()
        return


def corner_check(cube):
    corner_idx = [0, 2, 5, 7]
    counter=0
    for idx in corner_idx:
        if cube.vec_list['yellow'][idx][0] == 'Y':
            counter+=1
    return counter

def yellow_algo(cube):
    cube.right()
    cube.up()
    cube.right_prime()
    cube.up()
    cube.right()
    cube.up()   
    cube.up()
    cube.right_prime()
    return

def find_yellow_spot(cube):
    new = copy.deepcopy(cube)
    for x in range(3):
        if (new.vec_list['blue'][0][0] != 'Y' and new.vec_list['blue'][2][0] == 'Y'):
            return True
        new.up()
    return False
    
def yellow_corners(cube):
    count = corner_check(cube)
    if count == 4:
        return
    #bad cases
    elif count == 2:
        while ((cube.vec_list['yellow'][5][0] != 'Y' and cube.vec_list['yellow'][7][0] != 'Y') 
               or (cube.vec_list['yellow'][0][0] != 'Y' and cube.vec_list['yellow'][7][0] != 'Y')):
            cube.up()
        yellow_algo(cube)
    elif count == 0:
        if find_yellow_spot(cube):
            while not (cube.vec_list['blue'][0][0] != 'Y' and cube.vec_list['blue'][2][0] == 'Y'):
                cube.up()
            yellow_algo(cube)
        else:
            while (cube.vec_list['blue'][2][0] == 'Y' or cube.vec_list['blue'][0][0] == 'Y'):
                cube.up()
            yellow_algo(cube)
    #1 case
    elif find_yellow_spot(cube):
        for x in range(3):
            if (cube.vec_list['blue'][0][0] != 'Y' 
                and cube.vec_list['blue'][2][0] == 'Y' 
                and cube.vec_list['yellow'][5][0] == 'Y'):
                break
            cube.up()
        yellow_algo(cube)
    else:
        for x in range(3):
            if (cube.vec_list['blue'][0][0] != 'Y' 
                and cube.vec_list['blue'][2][0] != 'Y'
                and cube.vec_list['yellow'][5][0] == 'Y'):
                break
            cube.up()
        yellow_algo(cube)
    yellow_corners(cube)    
    return
        
#testing

def check_yellow(cube):
    for x in cube.vec_list['yellow']:
        if x[0] != 'Y':
            return False
    return True    



if __name__ == '__main__':
    new = vi.cube(vi.cube_dict)

    vi.random_move(new, 5, vi.colors)
   # solve(new)
    yellow_cross(new)
    yellow_corners(new)
    print(new.vec_list)
    print(check_yellow(new))
