from PIL import Image

def insertion_sort(list):
    for i in range(1, len(list)):
        tmp = list[i]
        j = i - 1
        while j >= 0 and list[j] > tmp:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = tmp
        
if __name__ == "__main__":
    list = [1, 4, 3, 5, 2]
    insertion_sort(list)
    print(list)
    
    image_path = "C:/Users/15010/Desktop/ECNU/sophomore/daseINTRO/daseINTRO/daseINTRO/assignment/DaSE_INTRO/w4/x st=start 1 4 3 5 2 op1=operation 1 4 op2=operation 1 3 4op3=operation 1 3 4 5op4=operation 1 2 3 4 5st-o.png"  # 替换为你的图片路径
    img = Image.open(image_path)
    img.show()

