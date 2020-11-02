"""
ID: your_id_here
LANG: PYTHON3
TASK: Mixing Milk
"""
#fin = open ('test.in', 'r')
#fout = open ('test.out', 'w')
#x,y = map(int, fin.readline().split())
#sum = x+y
#fout.write (str(sum) + '\n')
#fout.close()


b1, c1=map(int, input().split(" "))
b2, c2=map(int, input().split(" "))
b3, c3=map(int, input().split(" "))
def solve(c, c2, b):
    x=min(c, b-c2)
    c2+=x
    c-=x
    return c,c2

for i in range(33):
    c1,c2=solve(c1,c2,b2)
    c2,c3=solve(c2,c3,b3)
    c3,c1=solve(c3,c1,b1)
c1,c2=solve(c1,c2,b2)
print(c1)
print(c2)
print(c3)
