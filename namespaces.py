scopes = {'global': {'parent': None, 'variables': set()}}


def create(namespace, parent):
    global scopes
    scopes[namespace] = {'parent': None, 'variables': set()}
    scopes[namespace]['parent'] = parent


def add(namespace, var):
    global scopes
    scopes[namespace]['variables'].add(var)

def get(namespace,var):
    global scopes
    if var in scopes[namespace]['variables']:
        return namespace
    if scopes[namespace]['parent'] is None:
        return "None"
    return get(scopes[namespace]['parent'], var)

n = int(input())
for i in range(n):
    request = input().split()
    if request[0] == 'create':
        create(request[1], request[2])
    if request[0] == 'add':
        add(request[1], request[2])
    if request[0] == 'get':
        print(get(request[1], request[2]))



