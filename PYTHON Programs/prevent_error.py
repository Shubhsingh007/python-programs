#%%
def s():# always put"()" after program name IMPORTAT 
    numb=input("enter a number")# take input from use
    print(type(numb))#type will tell the type ex str int of numb
    try:
        num=float(numb) #try to convert to float if possible else wil show error
        print(num)
    except Exception as e:#exception will not work but Exception case matters
        #e and E are different when there is error type e in program it will
        # show erroe mesege so that program does not stop
        print("exception was:,e")