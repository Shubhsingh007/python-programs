import os
import csv
phones=[ ]
name_pos=0
phone_pos=1
phone_header=['name','number']

def proper_choice(which):
    if not which.isdigit():
        print(""+which+"need to be number")
        return False
    which=int(which)
    if which <1 or which >len(phones):
       print(""+ str(which) +"needs to be in range" )
       return False
    return True

def delete(which):
    if not proper_choice(which):
        return
    which=int(which)
    del phones[which-1]
    print("delete phone",which)
    
      
def save_phone_list():
    f = open("myphones.csv", 'w', newline='')
    for item in phones:
        csv.writer(f).writerow(item)
    f.close()


def load_phone_list():
    if os.access("myphones.csv", os.F_OK):
        f = open("myphones.csv")
        for row in csv.reader(f):
            phones.append(row)
        f.close()


def show_phones():                                             #youse of it
    show_phone(phone_header,"")
    index=1
    for phone in phones :
        show_phone(phone,index)
        index=index+1
        print()
def show_phone(phone,index):
    outputstr="{0;>3}  {1:<20}  {2:16}"
    print(outputstr.format(index,phone[name_pos],phone[phone_header])) #phone
def new():
    print("enter the data to be added")
    newname=input("enter name")
    newphone=input("enter the no")
    phone=[newname,newphone]
    phones.append(phone)
    print()

        
      

def mainchoice():
    print("chose one of the following options")
    print("d-delete")
    print("s-show")
    print("d-delete")
    print("q-quit")
    print("n-add new")
    choice=input ("choice:")                        #input function
    if choice.lower in ['s','n','d','e','q']:
        return choice.lower()
    else:
        print(choice+"?")
        print("wrong choice")                    #?
        return None

def mainloop():
   load_phone_list()
   while True:
      choice=mainchoice()
      if choice==None :
          continue
      if choice=='q':
          print("existing")
          break
      elif choice=='n':
           new()
      elif choice=='d':
           delete()
      elif choice=='s':
           show_phones()
   save_phone_list()


# The following makes this program start running at main_loop()
# when executed as a stand-alone program.
if __name__ == '__main__':
    mainloop()

           
    