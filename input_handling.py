class cube:
    # create cube instance with int list
    def __init__(self, pos_list):
        self.pos_list = pos_list
        
    def right(self):
        new = self.pos_list.copy()
        self.pos_list[2] = new[7]
        self.pos_list[4] = new[10]
        self.pos_list[7] = new[19]
        self.pos_list[9] = new[4]
        self.pos_list[10]= new[16]
        self.pos_list[14]= new[2]
        self.pos_list[16]= new[9]
        self.pos_list[19]= new[14]
        return new

    




pos_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
new_cube = cube(pos_list)
print(new_cube.pos_list)
new_cube.right()
print(new_cube.pos_list)