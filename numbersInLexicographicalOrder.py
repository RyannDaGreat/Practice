#https://www.careercup.com/question?id=5680043955060736
#Output top N positive integer in string comparison order. For example, let's say N=1000, then you need to output in string comparison order as below: 
#1, 10, 100, 1000, 101, 102, ... 109, 11, 110, ...
#O(1) space, O(n) time
def f(n,s=''):
    if not s or int(s)<=n:
        print(s)
        for i in range(not s,10):
            f(n,s+str(i))