import vector_input.vector_input as vi
from vector_input.vector_input import cube_dict
""" Important edges: W1/B6, W3/O6, W4/R6, W6/G1
Care about: white = [junk, W1, junk, W3, W4, junk, W6, junk],
 blue = [junk, junk, junk, junk, junk, junk, B6, junk], 
 orange = [junk, junk, junk, O6, junk, junk, B6, junk], 
 red = [junk, junk, junk, junk, R6, junk, B6, junk], 
 green = [junk, G1, junk, junk, junk, junk, junk, junk]"""

def check_cross(cube):
    if not (cube.vec_list['white'][1] == 'W1' and cube.vec_list['blue'][6] == 'B6'):
         cube.tmp_queue.append(['W1','B6', 'blue'])
    if not (cube.vec_list['white'][3] == 'W3' and cube.vec_list['orange'][6] == 'O6'):
        cube.tmp_queue.append(['W3','O6', 'orange'])
    if not (cube.vec_list['white'][4] == 'W4' and cube.vec_list['red'][6] == 'R6'):
        cube.tmp_queue.append(['W4','R6', 'red'])
    if not (cube.vec_list['white'][6] == 'W6' and cube.vec_list['green'][1] == 'G1'):
        cube.tmp_queue.append(['W6','G1', 'green'])
    return
    
new = vi.cube(cube_dict)

def first_edge(cube, edge):
    #3n   k base cases: if white edge is on white face in wrong spot, if white edge 
    #is on its opposite face, if the opposite edge is in the right spot but white part is not
    # RISKY EDGE CASE ONLY WORKS FOR FIRST EDGE
    if edge[0] in cube.vec_list['white']:
        while (edge[1] not in cube.vec_list[edge[2]]):
            cube.down()
    #works for any case
    if edge[1] in cube.vec_list[edge[2]]:
        while (edge[0] not in cube.vec_list['white']):
            if edge[2] == 'blue':
                cube.front()
            elif edge[2] == 'orange':
                cube.left()
            elif edge[2] == 'red':
                cube.right()
            elif edge[2] == 'green':
                cube.back()
    # works for any case
    if edge[0] in cube.vec_list[edge[2]]:
        while (edge[1] not in cube.vec_list['white']):
            if edge[2] == 'red':
                cube.right()
            elif edge[2] == 'green':
                cube.back()
            elif edge[2] == 'blue':
                cube.front()
            elif edge[2] == 'orange':
                cube.left()
        if (edge[2] == 'red'):
            cube.right()
            cube.down_prime()
            cube.front()
            cube.down()
        elif (edge[2] == 'green'):
            cube.back()
            cube.down()
            cube.left_prime()
            cube.down_prime()
        elif (edge[2] == 'blue'):
            cube.front()
            cube.down_prime()
            cube.left_prime()
            cube.down()
        elif (edge[2] == 'orange'):
            cube.left()
            cube.down_prime()
            cube.back_prime()
            cube.down()

def white_cross(cube):
    check_cross(cube)