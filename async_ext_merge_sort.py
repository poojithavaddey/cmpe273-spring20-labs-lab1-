import sys
import os
import asyncio

path = '/Users/poojitha/Desktop/273-Lab1/input/'
unsorted_data =[]

def async_ext_merge_sort(lis):
    if len(lis)<2 :
        return lis
    else:
        midval = len(lis)//2
        l_list = async_ext_merge_sort(lis[:midval])
        r_list = async_ext_merge_sort(lis[midval:])
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
    op_file = open('async_sorted.txt','a')
    for x in sorted_data:
        op_file.write(str(x))
        op_file.write('\n')
    op_file.close()

def sortdata(unsorted_data):
    sorted_data = async_ext_merge_sort(unsorted_data)
    writedata(sorted_data)   

async def readdata(fname): 
    fpath = os.path.join(path,fname)
    f_read =open(fpath,'r')
    unsorted_data.extend([int(x.strip()) for x in f_read.readlines()])
    await asyncio.sleep(1)
    f_read.close()
    #sortdata(unsorted_data)
    return unsorted_data

async def main():
    file_names = ['unsorted_'+ str(i)+ '.txt' for i in range(1,11)]
    unsorted_data = await asyncio.gather(readdata(file_names[0]),readdata(file_names[1]),readdata(file_names[2]),readdata(file_names[3]),readdata(file_names[4]),readdata(file_names[5]),readdata(file_names[6]),readdata(file_names[7]),readdata(file_names[8]),readdata(file_names[9]))
    sortdata(unsorted_data[0])

if __name__ ==  "__main__":
    asyncio.run(main())