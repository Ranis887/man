file = open("Names.txt", "r")
print(file.read())
#name = input("Введите одно из предоставленных имен - ")
lst_d = []
l = file.readline().split()
while l:
    lst_d.extend(l)
    l = file.readline().split()
print(lst_d)
lst = []
#for a in lst_d:
  #  if name == a:
     #   continue
   # lst.append(a)
file.close()
#file2 = open("Names2.txt", "w")
#b = lst
#file2.write(b)
#file2.close()

#!!!Не пон!!!