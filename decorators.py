def vehicle(function):

    def wrapper(*args, **kwargs):
        rvalue = function(*args, **kwargs)
        print('I have a chevy')
        return rvalue
    
    return wrapper

@vehicle
def color(truck):
    print(f'The type of vehicle is a {truck}. ')
    return f'The type of vehicle is a {truck}. '

print(color('truck'))

print()

def tv(function):
    def wrapper(*args, **kwargs):
        tvalue = function(*args, **kwargs)
        with open('notebook.txt', 'b+') as f:
              aname = function.__name__
              print(f'{aname} returned value {tvalue}')
              f.write(f'{aname} returned value {tvalue}')
        return tvalue
    return wrapper

@tv
def add(x, y):
    return x + y

print(add(20, 50))
    
