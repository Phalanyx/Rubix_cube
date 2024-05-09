# solving the final layer

import vector_input as vi
import copy
#import solver as so
def matching_corners(cube):
    colours = {'B':'blue', 'R':'red', 'G':'green', 'O':'orange'}
    solved_edges = []
    for x in range(4):
        if (cube.vec_list['blue'][0][0] == cube.vec_list['blue'][2][0]):
            solved_edges.append(colours[cube.vec_list['blue'][0][0]])
        cube.up()
    return solved_edges
def corner_counter(cube, face):
    corners = [0,2,5,7]
    counter = 0
    color = face[0].upper()
    for x in corners:
        if cube.vec_list[face][x][0] == color:
            counter+=1
    return counter
def solve_corners(cube):
    corners = matching_corners(cube)
    if (len(corners) == 4):
       return
    if corners != []:
        sol_col = vi.get_piece_color(corners[0].upper())
        for x in range(4):
            if (corner_counter(cube, sol_col) == 4):
                break
            cube.up()
    # this implementation is so bad :(
    if (corners == [] or corners[0] == 'blue'):
        cube.left_prime()
        cube.back_prime()
        cube.left_prime()
        cube.front_prime()
        cube.front_prime()
        cube.left()
        cube.back()
        cube.left_prime()
        cube.front()
        cube.front()
        cube.left_prime()
        cube.left_prime()
        if corners == []:
            solve_corners(cube)
    elif (corners[0] == 'red'):
        cube.front_prime()
        cube.left()
        cube.front_prime()
        cube.right_prime()
        cube.right_prime()
        cube.front()
        cube.left_prime()
        cube.front_prime()
        cube.right()
        cube.right()
        cube.front_prime()
        cube.front_prime()
    elif (corners[0] == 'green'):
        cube.right_prime()
        cube.front()
        cube.right_prime()
        cube.back()
        cube.back()
        cube.right()
        cube.front_prime()
        cube.right_prime()
        cube.back()
        cube.back()
        cube.right()
        cube.right()
    elif (corners[0] == 'orange'):
        cube.back()
        cube.right()
        cube.back()
        cube.left_prime()
        cube.left_prime()
        cube.back_prime()
        cube.right_prime()
        cube.back()
        cube.left()
        cube.left()
        cube.back_prime()
        cube.back_prime()

    return    


#finally solving the last edges


def final_solve(cube):
    while (cube.vec_list['blue'][0][0] != 'B'):
        cube.up()
    colors = ['blue', 'red', 'green', 'orange']
    count = 0
    for x in colors:
        if (cube.vec_list[x][1][0] != x[0].upper()):
            count+=1
    if count == 0:
        return
    # correspond faces to moves in order: R R'
    faces = {'blue':['right', 'right_prime'], 'red':['back_prime', 'back'],
              'green':['left', 'left_prime'], 'orange':['front', 'front_prime']}        
    # brute force (too lazy to do all cases)
    for x in colors:
            if (cube.vec_list[x][1][0] == x[0].upper()):
                solved_face = x
                break
    opposite_faces = {'blue':'green', 'green':'blue', 'red':'orange', 'orange':'red'}
    new_face = opposite_faces[solved_face]
    #moves  R U' R U R U R U' R' U' R2
    getattr(cube, faces[new_face][0])()
    cube.up_prime()
    getattr(cube, faces[new_face][0])()
    cube.up()
    getattr(cube, faces[new_face][0])()
    cube.up()
    getattr(cube, faces[new_face][0])()
    cube.up_prime()
    getattr(cube, faces[new_face][1])() 
    cube.up_prime()
    getattr(cube, faces[new_face][0])()
    getattr(cube, faces[new_face][0])()
    final_solve(cube)
        

            

            

 #testing



if __name__ == '__main__':
    new = vi.cube(vi.cube_dict)
    vi.random_move(new, 5, vi.colors)
    #so.solve(new)
    solve_corners(new)
    final_solve(new)
    print(new.vec_list)
    print(len(new.moves))
