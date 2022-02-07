S = input();
ss = input();
count = 0;
for i in range(0, len(S)):
    count += S.count(ss,i,i+len(ss));
print(count);

#input->shubhshinghsh
        #sh
        #output-> 3
     
#prog will be the no of occerence of 'sh' in above string
