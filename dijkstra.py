def dijkstra(verts,edges,start,end):
    from numbers import Number
    assert isinstance(edges,dict)
    assert all(isinstance(x,tuple)  for x in edges.keys())
    assert all(isinstance(x,Number) for x in edges.values())
    assert all(len(x)==2 for x in edges)
    assert all(x in verts and y in verts for x,y in edges)
    assert start in verts
    assert end   in verts
    #
    graph={vert:{} for vert in verts} # a dict of verts to dicts of verts to distances
    for (x,y),dist in edges.items():
        graph[x][y]=\
        graph[y][x]=dist
    heap =[]       # min-heap of verts with respect to their dists
    def pop():
        from heapq import heappop
        return heappop(heap)[1]
    dists={start:0}# verts dists from start
    def push(vert):
        from heapq import heappush
        assert vert in dists
        heappush(heap,(dists[vert],vert))
    push(start)
    while True:
        print('heap',heap)
        vert=pop()
        for neighbor in graph[vert]:
            vdist=dists[vert]
            ndist=vdist+graph[vert][neighbor]
            if vert==end:
                # walk backwards from end to start and return reversed path
                out=[]
                cursor=end
                while cursor!=start:
                    print('cursor',cursor)
                    out.append(cursor)
                    cursor=min(graph[cursor],key=lambda x:dists[x]+graph[cursor][x])
                print('out',out)
                print('dists',dists)
                return out[::-1]
            if neighbor not in dists or ndist<dists[neighbor]:
                # not being in dists is like having a dist of infinity
                dists[neighbor]=ndist
                push(neighbor)

#Example Usage: (Picture of graph: imgur.com/59y1VBp)
print(dijkstra(verts={'a','b','c','d','e'},
               edges={('a','b'):7,
                      ('a','c'):3,
                      ('b','c'):1,
                      ('b','d'):2,
                      ('b','e'):6,
                      ('c','d'):2,
                      ('d','e'):4},
               start='a',
               end  ='e'))
#The above prints: ['c', 'd', 'e']
