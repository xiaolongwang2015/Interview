import time

eggs = [lambda a: i * a for i in range(3)]
for egg in eggs:
    print(egg(5))
