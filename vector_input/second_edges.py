import vector_input as vi
"""After white face is solved, solve all the second layer edges: B4/R4, B3/O4, R4/G5, O3/G3 """
import white_corners as wc
import white_cross as we
def check_sec_edge(cube):
    if not (cube.vec_list['blue'][4] == 'B4' and cube.vec_list['red'][3] == 'R3'):
        cube.tmp_queue.append(['B4','R3'])
    if not (cube.vec_list['blue'][3] == 'B3' and cube.vec_list['orange'][4] == 'O4'):
        cube.tmp_queue.append(['B3','O4'])
    if not (cube.vec_list['red'][4] == 'R4' and cube.vec_list['green'][4] == 'G4'):
        cube.tmp_queue.append(['R4','G4'])
    if not (cube.vec_list['orange'][3] == 'O3' and cube.vec_list['green'][3] == 'G3'):
        cube.tmp_queue.append(['O3','G3'])
    return
def white_check(face):
    for x in face:
        if 'W' in x:
            return True
    return False
def sec_edge(cube, edge):
    if (cube.tmp_queue == []):
        return
    first_col = vi.get_piece_color(edge[0])
    sec_col = vi.get_piece_color(edge[1])
    if (edge[1] in cube.vec_list[sec_col] and edge[0] in cube.vec_list[first_col]):
        cube.tmp_queue.remove(edge)
        return
    # bad case, force edge out then fix the corner
    if (edge[1] not in cube.vec_list['yellow'] and edge[0] not in cube.vec_list['yellow']):
        tmp_move = cube.sig[vi.get_color(cube, edge[0])]
        count = 0
        while (edge[1] not in cube.vec_list['yellow']):
            getattr(cube, tmp_move)()
            count += 1
        cube.up()
        cube.up()
        while count > 0:
            getattr(cube, tmp_move+'_prime')()
            count -= 1
        wc.check_corner(cube)
        for x in cube.tmp_queue:
            #as corner objects have 3 elements
            if len(x) == 3:
                corner = x
                break
        wc.white_corners(cube, corner)
    if (edge[0] in cube.vec_list['yellow']):
        good_edge = edge[1]
        bad_edge = edge[0]
        first_col = vi.get_piece_color(edge[1])
        sec_col = vi.get_piece_color(edge[0])
    else:
        good_edge = edge[0]
        bad_edge = edge[1]
        first_col = vi.get_piece_color(edge[0])
        sec_col = vi.get_piece_color(edge[1])
    while (good_edge not in cube.vec_list[sec_col]):
        cube.up()
    cube.up()
    cube.up()
    tmp_move = cube.sig[vi.get_piece_color(bad_edge)]
    tmp_move2 = cube.sig[vi.get_piece_color(good_edge)]
    count = 0
    while (not white_check(cube.vec_list[first_col])):
        getattr(cube, tmp_move)()
        count += 1
    while (good_edge not in cube.vec_list[first_col]):
        cube.up()
    while count > 0:
        getattr(cube, tmp_move+'_prime')()
        count -= 1
    while (good_edge not in cube.vec_list[sec_col]):
        cube.up()
    count = 0
    while (not white_check(cube.vec_list[sec_col])):
        getattr(cube, tmp_move2)()
        count+=1
    while (good_edge not in cube.vec_list[first_col]):
        cube.up()
    while count > 0:
        getattr(cube, tmp_move2+'_prime')()
        count -= 1
    cube.tmp_queue.remove(edge)
    return



def check_end_edges(cube):
    if not (cube.vec_list['blue'][4] == 'B4' and cube.vec_list['red'][3] == 'R3'):
        return False
    if not (cube.vec_list['blue'][3] == 'B3' and cube.vec_list['orange'][4] == 'O4'):
        return False
    if not (cube.vec_list['red'][4] == 'R4' and cube.vec_list['green'][4] == 'G4'):
        return False
    if not (cube.vec_list['orange'][3] == 'O3' and cube.vec_list['green'][3] == 'G3'):
        return False
    return wc.check_end(cube)

def solve_sec_edges(cube):
    new_copy = cube.tmp_queue.copy()
    for x in new_copy:
        sec_edge(cube, x)
    return
#testing

if __name__ == '__main__':
    new = vi.cube(vi.cube_dict)
    vi.random_move(new, 5, vi.colors)

    we.solve_white_cross(new)
    wc.solve_white_corners(new)
    check_sec_edge(new)
    new_copy = new.tmp_queue.copy()
    for x in new_copy:
        sec_edge(new, x)
    print(new.moves)
    print(check_end_edges(new))