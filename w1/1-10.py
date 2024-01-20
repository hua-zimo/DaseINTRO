S = input()
i = 0
flag = 0
while i < len(S)-1:
    if S[i] == S[i+1]:
        flag = 1
        break
    i += 1

if flag == 1:
    print('是')
else:
    print('否')