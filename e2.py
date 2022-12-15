import re

lst = ['анТОн', 'НАТАЛЬЯ', 'никита', 'МаРиЯ', '!СЕРГЕЙ!', 'Владимир747', 'Павел+100500']
def proverka(new):
  for i in new:
      print(re.sub("[$|@|&|!|+|1234567890|]","",i.lower().title()))
proverka(lst)