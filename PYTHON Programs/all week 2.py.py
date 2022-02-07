#%%
def problem2_1():
    no=list(range(20,30))  #asa list bnta ha
    print(no[3])
    print(no)
    for itm in no:
        print(itm,end=" ")
        
        #%%
alist=["a","e","i","o","u","y"]

def problem2_2(my_list):
    l=len(my_list)
    print(my_list)
    print(my_list[0])
    print(my_list[l-1])
    print(my_list[3:5])
    print(my_list[:3])
    print(my_list[3:])
    print(len(my_list))
    my_list.append('z')
    print(my_list)
    
    #%%
newindia=["delhi","up","tamil"]
def problem2_3(ni):
    for i in ni: #i ka ander ni jo ki outpt ma newindia dala ga vo store hoga
        length=len(i)
        state=i
        print(state,"has",length,"letters.")
        
        #%%

import random #  iska buna koi randome comand work nahi hogi

def problem2_5():
    random.seed(171) #output of randome no will ramain smae by seed function
    for r in range(0,10):  # for function to run program 10 times IMPORTENT
       print(random.randint(1,6))# comand to chose random no between 2 no
       
       #%%

import random #  iska buna koi randome comand work nahi hogi

def problem2_6():
    random.seed(431) #output of randome no will ramain smae by seed function
    for r in range(0,100):  # for function to run program 10 times IMPORTENT
       dis1=random.randint(1,6)# comand to chose random no between 2 no
       dis2=random.randint(1,6)
       print(dis1+dis2)
       
       # %%

def problem2_7():
  a = float(input("Enter length of side one: "))#convert input to float 
  b = float(input("Enter length of side two: "))
  c = float(input("Enter length of side three: "))

  s = (a + b + c)/2

  areas = s*((s-a)*(s-b)*(s-c))


  print("Area of a triangle with sides", a, b, c,"is",areas ** 0.5 )#areas**0.5 means sqr root
  
  #%%
def problem2_8(temp_list):
    sum = 0
    for temp in temp_list:
        sum += temp
    avg = sum/len(temp_list)
    max_temp = max(temp_list)#max command to get the maximem no and min for minimem
    min_temp = min(temp_list)
    print("Average:",avg)
    print("High:",max_temp)
    print("Low:",min_temp)
    
    