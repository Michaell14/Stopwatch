input()
alice=list(map(int, input().split(" ")))
bob=list(map(int, input().split(" ")))
alice1=alice[:]
bob1=bob[:]

print((min(alice[0], bob[1])+min(alice[1], bob[2])+min(alice[2], bob[0])))
