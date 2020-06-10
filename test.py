#!/usr/bin/env python
# coding: utf-8

# In[79]:


import sys


# In[125]:


def fizzBuzz(args):
    f = open(args)
    lines = f.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
    f.close()
    
    #文字を”:”で分割    
    lines2 = list()
    for line in lines:
        line = line.split(":")
        lines2.append(line)

    
    len1 = len(lines2) - 1 #リストの長さを取得
    
    m = lines2.pop(len1)    #mの値を取得、リストから削除
  
    m = m[0].replace("\n","")#改行文字の削除
    m = int(m)              #数値に変換
    
    #文字列を数値に変換
    lines3 = list()
    for line in lines2:
        line[0] = int(line[0])
        line[1] = line[1].replace("\n","")
        lines3.append(line)
        
    #条件分岐
    lines4 = list()
    for line in lines3:
        if int(m) % line[0] == 0:
            lines4.append(line)
    #並び替え
    lines4.sort()
    
    #出力
    if len(lines4) == 0:
        print(m)
    else:
        for line in lines4:
            print(line[1],end='')
    print("\n")
    
if __name__ == '__main__':
    args = sys.argv
    
    if 2 <= len(args):
        fizzBuzz(str(args[1]))
        
    else:
        print('引数として、テキストファイルを指定してください')
    
    
    


# In[ ]:





# In[ ]:




