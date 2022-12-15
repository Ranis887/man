def robot_hello():
    s = ['Азат','Рома','Ильдар']
    imya = input()
    if imya in s:
        print(f"Привет, {imya}!")
    elif imya != s:
        s.append(imya)
        print(f"Привет, {imya}! Рад знакомству!")
        print(s)
robot_hello()