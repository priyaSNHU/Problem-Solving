#Hacker Rank Problem: https://www.hackerrank.com/challenges/simple-text-editor/problem
# TIme COmplexity: O(n) 
# Space COmplexity: O(n) - dict length

dic = {0:''}
seq = 0
s = ''
for i in range(int(input())):
  t=input().strip().split()
  if t[0]=='1':
      seq+=1
      s+=t[1]
      dic[seq] = s 
  elif t[0]=='3':
      print(s[int(t[1])-1])
  elif t[0]=='2':
      s=s[:len(s)-int(t[1])]
      seq+=1
      dic[seq]=s
  elif t[0]=='4':
      seq-=1
      s=dic[seq]
