import numpy as np
import time

#选择排序
def selectionSort(list):
    n = len(list)
    if n <= 1:
        return list
    else:
        for i in range(n):
            for j in range(i+1, n):
                if list[i] > list[j]:
                   list[i], list[j] = list[j], list[i]
                
        return list
    
#归并排序
def mergeSort(list):
    if len(list) == 1:
        return list
    
    #拆分列表
    mid = len(list)//2    
    left_list = mergeSort(list[:mid])
    right_list = mergeSort(list[mid:])
    return merge(left_list, right_list)
 
 
def merge(left_list, right_list):
    left_index, right_index, merge_list = 0, 0, list()
     
    #合并
    while left_index < len(left_list) and right_index < len(right_list):
        if left_list[left_index] <= right_list[right_index]:
            merge_list.append(left_list[left_index])
            left_index += 1
        else:
            merge_list.append(right_list[right_index])
            right_index += 1
    merge_list = merge_list + left_list[left_index:] + right_list[right_index:]
    return merge_list

if __name__ == "__main__":
    #随机生成多组长度递增的随机数列
    
    for i in range(2, 5):
        a = np.random.randn(10**i)
        time_start = time.time() #开始计时
        mergeSort(a)
        time_end = time.time()    #结束计时
        time_c= time_end - time_start   #运行所花时间
        print('merge sort time cost', time_c, 's')
        
        time_start = time.time() #开始计时
        selectionSort(a)
        time_end = time.time()    #结束计时
        time_c= time_end - time_start   #运行所花时间
        print('selection sort time cost', time_c, 's')
        i += 1
        
#不同长度：随着列表长度的递增，两种排序时长均递增
#不同算法：列表长度相同的情况下，归并排序所用时间均明显少于选择排序
    
    