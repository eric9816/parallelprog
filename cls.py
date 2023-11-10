class A:
    def __a(self):
        print(1)

a = A()
print(hash(a))
a.g = 5
print(hash(a))
# print(a._A__a())