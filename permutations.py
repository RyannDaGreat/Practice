def permutations(s:set):
    if not s:yield ()
    for e in s:
        for p in permutations(s-{e}):
            yield (e,*p)
for x in permutations(set(range(4))):
    print(x)