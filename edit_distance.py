def edit_distance(start,end):
    from functools import lru_cache
    @lru_cache(None,None)
    def helper(start,end,dist):
        if not start and not end   :return                                dist  #Base
        if not start or  not end   :return len(       start or  end)     +dist  #Failure
        if     start[0]  ==  end[0]:return     helper(start[1:],end[1:],  dist) #Skip
        else:                       return min(helper(start[1:],end    ,1+dist),#Delete
                                               helper(start    ,end[1:],1+dist),#Insert
                                               helper(start[1:],end[1:],1+dist))#Replace
    return helper(start,end,0)
print(edit_distance('kitt','mitt'))#1
print(edit_distance('1234','abcd'))#4
print(edit_distance('abab','acac'))#2
