def max_min(mlist):
 minimum = mlist[0]
 for item in mlist:
    if item<minimum:
        minimum = item
    print(minimum)    
        
def get_value():
    mlist = random.sample(range(20,50),10)
    print(mlist)
    max_min(mlist) 
    
    

mlist =[5,3,4,88,12]
max_min(mlist)