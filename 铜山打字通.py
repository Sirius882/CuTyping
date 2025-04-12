from random import randint as rd
import os
import pandas as pd

def creat(dic): #生成要求的字符串
    result = ""
    for i in range(8):
        r = rd(1,sum(dic.values()))
        for j in range(34):
            if r > dic[list(dic.keys())[j]]:
                r -= dic[list(dic.keys())[j]]
            else:
                chra = list(dic.keys())[j]
                break
        result += str(chra)
    return result

print("程序地址：",end= "")
print(os.getcwd()) 
if "data.xlsx" in os.listdir(os.getcwd()): #检查有没有存档
    df = pd.read_excel(os.getcwd() + "\\" + "data.xlsx")
    lis = {}
    lis = df.set_index(df.columns[0]).to_dict()[df.columns[1]]
else:
    lis1 = "\\qwertyuiop[]asdfghjkl;'zxcvbnm,."
    lis = {}
    for i in range(len(lis1)):
        lis[lis1[i]] = 10 #初始化字典lis，保存各个字符的权重
#主体
while True:
    require = creat(lis)
    print(require)
    ans = input()
    if ans == "shut":
        break
    if ans == "check":
        print(lis)
        continue
    for i in range(8):
        if ans[i] == require[i]:
            lis[require[i]] -= 1
            if lis[require[i]] < 0:
                lis[require[i]] = 0
        else:
            lis[require[i]] += 1
df = pd.DataFrame(list(lis.items()), columns=['Key', 'Value'])
df.to_excel("data.xlsx", index=False)
input("已将练习数据保存到 data.xlsx")