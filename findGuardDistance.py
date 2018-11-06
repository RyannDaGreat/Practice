#From https://www.careercup.com/question?id=4716965625069568

# Given a 2-D matrix represents the room, obstacle and guard like the following (0 is room, B->obstacle, G-> Guard): 
# 0 0 0 
# B G G 
# B 0 0 
# 
# calculate the steps from a room to nearest Guard and set the matrix, like this 
# 2 1 1 
# B G G 
# B 1 1 
# Write the algorithm, with optimal solution.

def f(s):
    grid=string_to_coord_dict(s)
    guard_coords={key for key,value in grid.items() if value=='G'}
    def neighbors(coords):
        def neighbors(coord):
            x,y=coord
            coords={(x+1,y),(x-1,y),(x,y+1),(x,y-1)}
            coords={coord for coord in coords if coord in grid}
            return coords
        from functools import reduce
        return reduce(set.union,map(neighbors,coords),set())
    front=guard_coords.copy()
    dist=0
    while front:
        front={coord for coord in neighbors(front) if grid[coord]=='0'}
        dist+=1
        for coord in front:
            grid[coord]=str(dist)
    output=list(map(list,s.split('\n')))
    for coord,tile in grid.items():
        x,y=coord
        output[y][x]=tile
    for row in output:
        print(''.join(row))

f('000\nBGG\nB00')

#Prints:
# 211
# BGG
# B11