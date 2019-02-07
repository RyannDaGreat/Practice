#From https://www.dailycodingproblem.com/blog/an-introduction-to-backtracking/
def nqueens(n,l=[]):
    def legal(l):
        coords=[(x,y,x+y,x-y)for x,y in enumerate(l)]
        out=all(len(l)==i for i in map(len,map(set,(zip(*coords)))))
        #if out:
            #fansi_print(l,'yellow')
        #else:
            #fansi_print(l,'green')
        return out
    if legal(l):
        if n==0:
            #fansi_print(l,'cyan')
            return 1
        else:
            #print('n=%i'%n,l)
            return sum(nqueens(n-1,l+[i])for i in range(n+len(l)))
    else:
        #fansi_print(l,'red')
        return 0
for _ in range(100):
    print(_,nqueens(_))
