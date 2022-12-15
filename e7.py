def get_name( ):
  name = input('Введите имя - ')
  return name

def hello(res):
  print(f"Привет, {res}!")


hello(get_name())