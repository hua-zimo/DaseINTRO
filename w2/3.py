name = ["人", "狼", "羊", "菜"]

finish = False

def is_done(status):
    return status[0] and status[1] and status[2] and status[3] #全为true时返回true

def is_valid_status(status):
    #狼羊同侧人不在
    if status[1] == status[2]:
        if status[0] != status[1]:
            return False
        
    #草羊同侧人不在  
    if status[3] == status[2]:
        if status[0] != status[2]:
            return False 
    
    return True   

def generate_next_status(status):
    next_status_list = []
    
    for i in range(0, 4):
        if status[0] != status[i]: #和农夫不在一侧
            continue
        
        n_status = [status[0], status[1], status[2], status[3]]
        n_status[0] = not n_status[0] #农夫取反
        n_status[i] = n_status[0] #和农夫过河
        
        if is_valid_status(n_status):#判断是否违规
            next_status_list.append(n_status)
            
    return next_status_list

def search(hs_status):
    global finish
    if finish:
        return
    
    cr_status = hs_status[len(hs_status)-1]#当前状态
    next_status_list = generate_next_status(cr_status)#下一状态
    
    for next_status in next_status_list:
        if next_status in hs_status:#防止重复操作
            continue
        
        hs_status.append(next_status)#加入
        
        if is_done(next_status):#进行输出
            finish = True
            print(solution(hs_status))
        else:#继续搜索
            search(hs_status)
        hs_status.pop()
        
    
def cmp_status(pre, now): #根据前后状态对比判断过河对象
    res = []
    for i in range(len(pre)):
        if pre[i] != now[i]:
            res.append(name[i])
    return ''.join(res)

def solution(hs_status):
    result = ''
    hs_len = len(hs_status)
    for i in range(hs_len):
        if i > 0:
            result += cmp_status(hs_status[i-1], hs_status[i])
            if i != hs_len-1:#不是最后一个
                result += ' '
    
    return result

if __name__ == "__main__":
    status = [False, False, False, False]#初始状态
    hs_status = [status]
    
    search(hs_status)
    
#参考：http://t.csdn.cn/zclwS