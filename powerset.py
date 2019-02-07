def powerset(s):
    if s:
        e=s.pop()
        for _ in powerset(s):
            yield _
            yield _|{e}
    else:    
        yield set()
        
ans=list(powerset({1,2,3,4}))

