#1 667个3
#2 1)由于2(x-2)>x在x>4时成立，所以大于4的整数总能被进一步拆分为2和x-2
#  2)由题目可知4可以被拆分为2和2
#  3)由常理可得当n>=4时，拆分出1并不划算
#  综上所述，n>=4时，只会拆分出2和3
#  因为3+3=2+2+2，3*3>2*2*2
#  所以最多出现两个2
#  综上所述，n>=4时正整数列是 n%3=0时，n/3个3；n%3=1时，n/3-1个3和2个2；n%2=2时，n/3个3和1个2。n<=3时为n-1和1。
#3
import numpy as np

n = input()
n = int(n)

if n <= 3:
    print(n-1, 1)
else:
    m = int(n/3)
    if n % 3 == 0:
        print('%d个3' % m)
    elif n % 3 == 1:
        print('%d个3和2个2' % int(m-1))
    else:
        print('%d个3和1个2' % m)
        
#参考：https://leetcode.cn/problems/integer-break/solutions/352875/zheng-shu-chai-fen-by-leetcode-solution/