def edit_distance(start,end):
    @lru_cache(None,None)
    def helper(start,end,dist):
        if not(start or end):return dist
        if bool(start)!=bool(end):return len(start or end)+dist
        if start[0]==end[0]:return helper(start[1:],end[1:],dist+0)
        else:return min(helper(start[1:],end    ,dist+1),#Delete
                        helper(start    ,end[1:],dist+1),#Insert
                        helper(start[1:],end[1:],dist+1))#Replace
    return helper(start,end,0)
print(edit_distance('kitt','mitt'))#1
print(edit_distance('1234','abcd'))#4
print(edit_distance('abab','acac'))#2
