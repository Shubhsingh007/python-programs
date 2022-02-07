#%%
def problem1_1():
    print("Problem Set 1")
    #%%
def problem1_2(x,y):
    print(x+y)
    print(x*y)  
    #%%
def problem1_3(n):
    sum=0
    while n>0:
        sum=sum+n
        n=n-1
        
    print(sum)
    #%%
def problem1_4(miles):
    feet=miles*5280
    print("There are",feet,"feet in",miles,"miles.") 
    #%%
def problem1_5(age):
    if age<7:
        print("Have a glass of milk.")
    elif age<21:
        print("Have a coke.")
    else:
            print("Have a martini.")
    #%%
def problem1_6():
    i=-1
    while i<99:
     i=i+2
     print(i,end=" ")