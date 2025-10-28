_functions_to_update=[]
def register(func):
    _functions_to_update.append(func)

def update():
    for f in _functions_to_update:
        f()

