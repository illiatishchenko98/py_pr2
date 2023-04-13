# h = 'hello'
# w = 'world'

# # com = hello + ' ' + world
# # com = f"{hello} {world}"
# com = f"{str.title(h)} {str.title(w)}"

# print(com)


# def mult(a, b):
#     return a * b


# def mult(a, b): return a * b


# print(mult(5, 10))

def greeting(greet):
    return lambda name: f"{greet}, {name}!"


morning_greeting = greeting('Good morning')

print(morning_greeting('Illia'))

evening_greeting = greeting('Good evening')

print(evening_greeting("Illia"))
