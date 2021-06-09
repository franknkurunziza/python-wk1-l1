import random
def randInt(max=100,min=0):
    num=max-min
    return round(random.random() * num+ min)
print(randInt())
print(randInt(max=50))
print(randInt(min=50))
print(randInt(min=50,max=500))
