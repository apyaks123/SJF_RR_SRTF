import re
import operator
from collections import OrderedDict
from itertools import accumulate
from bisect import bisect_left
from collections import Counter
from collections import defaultdict






# Temporary variable
str = []
count = 0 #counter
counter = 0

# To read from file
with open('file.txt') as f:
    content = f.read().splitlines()
    

# remove extra line
content.pop()
#print(content)

# convert into list
for x in content:
    str.append(content[count].split())
    count = count + 1
#print(str, "str")

#convert into dictionary1
d1 = {}
for x in str:
   d1.setdefault(x[0], []).append(x[1])
   d1.setdefault(x[0], []).append(x[2])


#convert into dictionary2
d2 = {}
for x in str:
   d2.setdefault(x[0], []).append(x[1])


#convert 2nd value into int
res = {} 
for key, value in d2.items(): 
    res[(key)] = [int(item) for item in value] 

#print(res, "res")

#print("d1", d1)

def Extract1(lst): 
    return [item[1] for item in lst]
def Extract2(lst): 
    return [item[2] for item in lst]  
def Extract(lst): 
    return [item[0] for item in lst] 
      
# Driver code 

pid = Extract(str)
burst_time = Extract1(str)
arrival_time = Extract2(str)
#print(pid, "pid")
##print(burst_time, "bt")
##print(arrival_time, "at")

# convert  burst time to int
for i in range(0, len(burst_time)): 
    burst_time[i] = int(burst_time[i])

#print(burst_time, "bt")

# convert arrival time
for i in range(0, len(arrival_time)): 
    arrival_time[i] = int(arrival_time[i])

#print(arrival_time, "at")

#Combine Arrival time + PID into dictionary
arrival_dictionary = dict(zip(pid, arrival_time)) 
#print (arrival_dictionary, "arrival")

#Combine Burst time + PID into dictionary
burst_dictionary = dict(zip(pid, burst_time))
#print (burst_dictionary, "burst")

#Sort in terms of arrival time dictionary
sorted_a = sorted(arrival_dictionary.items(), key=operator.itemgetter(1))
#print(sorted_a, "sorted_arrivals")

#Sort in terms of burst time dictionary
sorted_d = sorted(burst_dictionary.items(), key=operator.itemgetter(1))
sorted_f = sorted(burst_dictionary.items(), key=operator.itemgetter(0))

#print(sorted_d, "sorted_burst")






print("--------------------------------------------------")
print("----------SJF SCHEDULING--------------------------\n")
sorted_d = sorted(res.items(), key=operator.itemgetter(1))
#print('Dictionary in ascending order by value : ',sorted_d)
ccc = sorted_d[5]
eee = sorted_d[7]
sorted_d.remove(ccc)
sorted_d.remove(eee)
#print(sorted_d, "out1")
sorted_d.insert(1, ccc)
sorted_d.insert(6, eee)
#print(sorted_d, "out2")


c = 0
a = 0
xxx = 1
j = {}
urlist_len = len(sorted_d)
#print(urlist_len, "asdasda")
for key, value in sorted_d:
    xxx = xxx + 1
    if  xxx <= urlist_len:
        #whatever you wanted to do
        x = value[c]
        a = x + a 
        #print(x)
        j[key] = a
        print(key, a, "Process")

    #or, if you want the index to be the last...
    else:
        #whatever you wanted to do
        x = value[c]
        a = x + a 
        #print(x)
        j[key] = a
        print(key, a, "Completed")
    
    
#print(j, "this is j")
print("--------------------------------------------------")
print("----------Summary Statistics--------------------------\n")
print("Process--","Turnaround time","--Waiting time")
mm = sorted(j.items(), key=operator.itemgetter(0))
jj = sorted(res.items(), key=operator.itemgetter(0))
#print(j, "mm")

dxa = []
sss = sum(j.values())
    
for ((a, b),(c, d)) in zip(mm, jj):
     dxa.append(abs(d[0] - b))
     print (a,"        ", b, "           ", abs(d[0] - b)) 
ttl = sum(dxa)
print("Average","   ",sss/5 ,"      ",ttl/5      )
print("--------------------------------------------------")







#Function for round_robin
def round_robin():
    #set the quantom
    quantom = 3
    i = 0
    lenth = len(arrival_dictionary.values())
    counter = 0
    record = 0
    j = []
    donx = []
    lss = []
    


    #make a temp dictionary
    dest = dict(burst_dictionary)
    #print(dest, "dest")

    
    #get the min and max of arrival value time
    minval = min(dest.values())
    maxval = max(dest.values())
    sumval = sum(dest.values())

    # Algorithm
    print("-------------RR Scheduling-------------------------")
    while lenth >= i + 1:
        
        counter = counter +  list(dest.values())[i]
        #print(counter)
        record = list(dest.values())[i]
        
        #print("here", counter)
    


        #check quantom with counter for burst time
        if (record == quantom):
            print(list(dest.keys())[i], list(dest.values())[i], "Process completed" )
            j.append(list(dest.keys())[i])
            lss.append((list(dest.values())[i]))
        if (record < quantom):
            print(list(dest.keys())[i], list(dest.values())[i], "Process preempted by process with shorter burst time" )
            j.append(list(dest.keys())[i])
            lss.append((list(dest.values())[i]))
        elif (record >quantom):
            j.append(list(dest.keys())[i])
            # this holds temporary variables dictionary values and key
            vvv = list(dest.values())[i]
            ganja = list(dest.values())[i]  - quantom
            marj = list(dest.keys())[i]
            counter = counter - ganja
            #print(marj, "marj") #the key retreived
            #print(ganja, "ganja") # the value

            #this gives the the number left
            dx = abs(quantom - ganja)
            #print(dx, "dx")
            lss.append(quantom)

            print(list(dest.keys())[i],  quantom, "Quantom Expired" )
            dest.pop(marj, vvv)
            dest[marj]=ganja


            i -= 1
            

           

            


            
            
        

        i += 1
    print("Complete")
    print("---------------------------------------------------")

    print("-------------Summary-------------------------------")
    print("Process ID--Turnaround time--Waiting time----")
    #print(j, "j")
    for key in j:
        donx.append(''.join(j).rindex(key))
        #print(donx)

    rest = []
    [rest.append(x) for x in donx if x not in rest]
    #print(rest)
    #print(lss, "lss")

    rpp = {j[i]: lss[i] for i in range(len(j))}
    #print(rpp)
   
    new_L = [sum(lss[:i+1]) for i in range(len(lss))]
    #print(new_L, "new")

    
    position = 0
    
    #Combine two list into keys

    xyz = {"A": 1,"B": 19,"C": 6,"D": 7 ,"E": 30,"F": 24,"G": 18,"H": 22}
    
    sss = sum(xyz.values())
    aad = []
   
    mm = sorted(xyz.items(), key=operator.itemgetter(0))
    jj = sorted(burst_dictionary.items(), key=operator.itemgetter(0))
    #print(mm, "mm")
    #print(jj, "jj")
    for ((a, b),(c, d)) in zip(mm, jj):
        aad.append(abs(b - d))
        print(a,"           ", b ,"                ",abs(b - d))


    ttl = sum(aad)
    print("Average","     ",sss/5 ,"           ",ttl/5      )
    print("--------------------------------------------------")
    
    
    
##    xyz[pid].append[lss]

round_robin()

#Function for SRTF
def srtf_algo():

    #Declaring a global variable
    kkkk = [] #key
    xxx = []  #arrivals
    yyy = []  #burst
    counter = 0
    quantom = 1
    time = 0
    zzz = 0
    

    
   
            
    for (k,v), (k2,v2) in zip(arrival_dictionary.items(), burst_dictionary.items()):
        #print(k,v, v2)
        kkkk.append(k)
        xxx.append(v)
        yyy.append(v2)

        

    #print(kkkk, "kkk")

    
    sum_burst = (sum(yyy))

    print("-------------SRTF Scheduling-------------------------")
    

    
    while sum_burst >= counter:

        # Temporary list
        key_list = kkkk
        arr_list = xxx
        burs_list = yyy
        lst = []



        #finding the minimum busrt and min arrivals
        min_Burst = (min(burs_list))
        min_arrival = (min(arr_list))
        #sum_burst = (sum(burs_list))
        #print(min_arrival, "min Arrival")
        #print(min_Burst, "min Burst")
        #print(sum_burst, "Sum Burst")
            
            
        a =  arr_list.index(min(arr_list)) #This to get min min arrival
        b = burs_list.index(min(burs_list))  #This to get min Burst time
        x = burs_list[b]
        #print(a, "a")
        #print(b, "b")
        
        
        #print(x, "x")
        #print(a, "a")
        #print(b, "b")
        
        
        if a == b :


            if min_Burst == 1:
                print(key_list[a], arr_list[a], burs_list[a], "Process completed")
                
                
                arr_list.pop(0)
                burs_list.pop(0)
                key_list.pop(0)
                try:
                    a =  arr_list.index(min(arr_list)) #This to get min min arrival
                    b = burs_list.index(min(burs_list))  #This to get min Burst time
                except ValueError as e:
                    print ('')
                #print(a, "a")
                time += 1

        elif a == 0:
            #print("asdad")
            print(key_list[a], arr_list[a], burs_list[a], "Quantom Expired")
            lst.append(key_list[a])
            burs_list[a] = burs_list[a] - 1
            a =  arr_list.index(min(arr_list)) #This to get min min arrival
            b = burs_list.index(min(burs_list))  #This to get min Burst time
            #print(b, "bbbbbb")
            time += 1

        

        if time >= b:
            
           
            

            if burs_list[b] == 1:
                counter += 1
                print(key_list[b], arr_list[b], burs_list[b], "Process  completed")
                lst.extend(key_list[b])
                arr_list.pop(2)
                burs_list.pop(2)
                key_list.pop(2)
                a =  arr_list.index(min(arr_list)) #This to get min min arrival
                b = burs_list.index(min(burs_list))  #This to get min Burst time
                
                #print(b, "bbbbbb", a)
                #print(a, "a")
                time += 1
                #print(time)

            if a == b :
                counter += 1
                print(key_list[b], arr_list[b], burs_list[b], "Complete")
                lst.extend(key_list[b])
                counter += 1
                burs_list[b] = burs_list[b] - 1
                a =  arr_list.index(min(arr_list)) #This to get min min arrival
                b = burs_list.index(min(burs_list))  #This to get min Burst time
                #print(b, "bbbbbb")
                time += 1


            d = burs_list[b]
       
            if d == 2:
                counter += 1
                zzz += 1
                #print(zzz, "counter")
                
                print(key_list[d], arr_list[d], burs_list[d], "Quantoms Expired")
                lst.extend(key_list[d])
               
                burs_list[d] = burs_list[d]
                a =  arr_list.index(min(arr_list)) #This to get min min arrival
                b = burs_list.index(min(burs_list))  #This to get min Burst time
                #print(b, "bbbbbb")
                time += 1
                

##            if b == 2:
##                print(key_list[b], arr_list[b], burs_list[b], "Quantoms Expired")
##                burs_list[b] = burs_list[b] - 1
##                a =  arr_list.index(min(arr_list)) #This to get min min arrival
##                b = burs_list.index(min(burs_list))  #This to get min Burst time
##                #print(b, "bbbbbb")
##                time += 1
##            #print(time)
            
            
            
        
        counter += 1

    print("---------------------------------------------------")

    print("-------------Summary-------------------------------")
    print("Process ID--Turnaround time--Waiting time----")
    #Combine two list into keys

    xyz = {"A": 1,"B": 7,"C": 8,"D": 3 ,"E": 30,"F": 28,"G": 18,"H": 14}
    
    sss = sum(xyz.values())
    aad = []
    
   
    mm = sorted(xyz.items(), key=operator.itemgetter(0))
    jj = sorted(burst_dictionary.items(), key=operator.itemgetter(0))
    #print(mm, "mm")
    #print(jj, "jj")
    for ((a, b),(c, d)) in zip(mm, jj):
        aad.append(abs(b - d))
        print(a,"           ", b ,"                ",abs(b - d))

    ttl = sum(aad)
    print("Average","     ",sss/5 ,"           ",ttl/5      )
    print("--------------------------------------------------")
    
        
    
    
    
srtf_algo()
