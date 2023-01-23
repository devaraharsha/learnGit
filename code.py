'''
from csv import*
with open("Book1.csv") as f1:
    Book= list(reader(f1))
    for d in Book[1:]:
        print(d[-1] )
'''



from csv import*
college=()
with open("Book1.csv") as f1:
    Book1= list(reader(f1))
    for d in Book1[1:]:
        coll=d[-1].upper()
        b=d[-2].upper()
        if coll not in college:
            college[coll]=[b]
        else:
            if b not in college[coll]:
                college[coll].append(b)
for k,v in college.items():
    print(k,v)        
        
        
