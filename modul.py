li = [i for i in range(0,1000)]
print([i for i in range(0,1000)])


#0.33 abstand
def adddevide(el):
    return(el + 2)/3

x = map(adddevide,li)
print(x)

print(list(x))



#0.66 abstand
y = map(lambda el:(el/3)*2, li)

print(list(y))

def morethanone(*args):
    return[i for i in args]

print(morethanone(1,2,3,4,5,6,7))