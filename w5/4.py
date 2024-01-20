def shell_sort(list):
    step = len(list)//2
    while step > 0:
        for i in range(step, len(list)):
            j = i
            while j >= step and list[j] < list[j-step]:
                list[j], list[j-step] = list[j-step], list[j]
                j -= step
        
        step //= 2
        
if __name__ == "__main__":
    list = [1, 4, 3, 5, 2]
    shell_sort(list)
    print(list)
    
## 时间复杂度：
## 最坏情况时间复杂度：O(n^2)
## 最好情况时间复杂度：根据步长序列的选择而定，通常是 O(n log^2 n) 到 O(n^(4/3)) 之间。
## 平均情况时间复杂度：取决于步长序列的选择，一般为 O(n log n) 到 O(n^(3/2)) 之间。
## 空间复杂度：
## 希尔排序是一种原地排序算法，不需要额外的空间，空间复杂度为 O(1)。