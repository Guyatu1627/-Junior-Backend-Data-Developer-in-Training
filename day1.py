"""x = 1000
y = 1000

print(id(x))
print(id(y))

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
b = a.copy()

b.append(10)

print(a)
print(b)

ax = [1, 2, 3]
by = [1, 2, 3]

print(ax == by)
print(ax is by)

ya = None
if ya is None:
    print("Correct")"""


'''def f(a):
    b = []

    for i in a:
        if i % 2 == 0:
            b.append(i)
    
    return b'''

def get_even_numbers(numbers: list[int]) -> list[int]:
    return [n for n in numbers if n % 2 == 0]

def add_item(item=[]):
    item.append("new")
    return item

print(add_item())
print(add_item())
print(add_item())
