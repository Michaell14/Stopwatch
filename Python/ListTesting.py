classmates=["bob", "sarah", "rob", "joe", "steven", "patty", "ross", "ricky"]
grades=[4,6,2,7,4,8,11,12]
mul=[2,3,4,5,6,7,8,1]

print([x*y for (x,y) in zip(grades, mul)])
