def count(a):
  print(a)
  if a == 10:
      return
  count(a+1)
count(0)

def countd(a):
  while a !=11:
      print(a)
      a+=1
countd(0)