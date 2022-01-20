# snail coordinate function
def snail_coordinate(num):
    # required numbers up to x and y
    req_num_up_x = num // 2
    req_num_up_y = (num-1) // 2
    # coordinate function
    def coord(n):
        # output
        coord = (((2*n)+1) * ((n%2)-((n-1)%2)) + 1) // 4
        # return
        return coord
    # output
    coord_x, coord_y = coord(req_num_up_x), coord(req_num_up_y)
    # return
    return coord_x, coord_y
# user input
usr_num = int(input())
# unpack
usr_coord_x, usr_coord_y = snail_coordinate(usr_num)
# print
print(usr_coord_x, usr_coord_y)
