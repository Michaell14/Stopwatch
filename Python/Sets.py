#s={1,2,3}
#s2={2,3,4}
#s3={3,4,5}

#s.add(55)
#s.discard(88)
#s4=s.intersection(s2, s3)
#s4=s3.difference(s,s2)
#s4=s.symmetric_difference(s2)

#l1=[1,2,3,4,1,2,3,4]
#l2=list(set(l1))

employees=["mike", "bob", "joe", "chris", "steve", "matt"]
gymmembers=["mike", "joe", "chris"]
developers=["matt", "bob", "mike", "steve"]

print(set(gymmembers).intersection(employees))
