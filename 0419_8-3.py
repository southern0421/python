ss = '---Python---- is---- Easy.---'

outStr=''

for i in range(0,len(ss)):
    if ss[i] != '-':
        outStr +=ss[i]

print(ss)
print(outStr)