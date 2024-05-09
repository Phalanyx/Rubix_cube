import white_cross as wc
import vector_input as vi
import white_corners as we
import second_edges as se
import yellow_face as yf
import final_layer as fl
import copy
def solve(cube):
    wc.check_cross(cube)
    wc.solve_white_cross(cube)
    we.check_corner(cube)
    we.solve_white_corners(cube)
    se.check_sec_edge(cube)
    se.solve_sec_edges(cube)
    yf.yellow_cross(cube)
    yf.yellow_corners(cube)
    fl.solve_corners(cube)
    fl.final_solve(cube)
    return


if __name__ == "__main__":
    new = vi.cube(vi.cube_dict)
    count = 0
    for x in range(100):
        new_copy = copy.deepcopy(new)
        vi.random_move(new_copy, 20, vi.colors)
        solve(new_copy)
        if (new.vec_list != new_copy.vec_list):
            print("Failed")
        count += (len(new_copy.moves))
    print(count/100)

