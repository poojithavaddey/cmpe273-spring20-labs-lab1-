import sys
import os
import time

path = '/Users/poojitha/Desktop/273-Lab1/input/'

def ext_merge_sort(lis):
    if len(lis)<2 :
        return lis
    else:
        midval = len(lis)//2
        l_list = ext_merge_sort(lis[:midval])
        r_list = ext_merge_sort(lis[midval:])
        f_list = merge_lists(l_list,r_list)
        return f_list    

def merge_lists(l_list1,r_list1):
    l_iter,r_iter =0,0
    l_list,r_list= [],[]
    l_list.extend(l_list1)
    r_list.extend(r_list1)
    res=[]
    while l_iter < len(l_list) and r_iter < len(r_list):
        if int(r_list[r_iter]) > int(l_list[l_iter]):
            #print(l_list[l_iter])
            res.append(l_list[l_iter])
            l_iter += 1
        else:
            res.append(r_list[r_iter])
            r_iter += 1
    
    res.extend(l_list[l_iter:])
    res.extend(r_list[r_iter:])
    #print (res)
    return res

def writedata(sorted_data):
    op_file = open('sorted.txt','a')
    for x in sorted_data:
        op_file.write(str(x))
        op_file.write('\n')
    op_file.close()

def sortdata(unsorted_data):
    sorted_data = ext_merge_sort(unsorted_data)
    writedata(sorted_data)   

def readdata(): 
    file_names = ['unsorted_'+str(i)+'.txt' for i in range(1,11)]
    unsorted_data =[]
    time.sleep(1)
    for fi in file_names:
        fpath = os.path.join(path,fi)
        f_read =open(fpath,'r')
        unsorted_data += [int(x.strip()) for x in f_read.readlines()]
    time.sleep(1)
    f_read.close()
    sortdata(unsorted_data)

def main():
    readdata()   

if __name__ ==  "__main__":
    main()


