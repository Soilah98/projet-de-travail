class Truc:
  def __init__(self, a):
    self.a = a

  def __mul__(self, autre):
    return Truc(a=self.a * autre.a)

  def __repr__(self):
    return f"Truc({self.a})"

x = Truc(1)
y = Truc(6)
print(x * y)

print('i like git')
print('hello')

for i in range (5):
  print(i^2)