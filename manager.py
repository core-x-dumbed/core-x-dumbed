import os
import sys

current_list = ''

def view_lists():

    print("------------------LISTS---------------------", end = '\n\n')
    dir = os.listdir("lists/")
    if dir: 
        for file in dir:
            if file.lower().endswith(".txt"):
                print(file[:len(file)-4])                
    else:
        print("You don't have any lists yet, use the mkl: command to make a new one.") 


def make_list(title):
    title = title[title.index(" ") + 1:]
    file = open('lists/'+title+'.txt', 'x')


def rename_list(response):
    tokens = response.split(':')
    #[r, old t, new]
    params = ['','']

    for i in range(len(tokens)):
        match tokens[i]:
            case 'r': params[0] = tokens[i+1].strip(' t')
            case _: params[1] = tokens[-1].strip()

    old = 'lists/'+params[0]+'.txt'

    if os.path.exists(old):
        os.rename(old, 'lists/'+params[1]+'.txt')
    
    else:
        print('That list does not exist, you can use the "mkl" command to make a new list')


def open_list(response):
    #o: title
    list_title = response.split(':')[1].strip()
    global current_list
    current_list = 'lists/'+list_title+'.txt'
    view_todos()


def view_todos():
    if os.path.exists(current_list):
        file = open(current_list, 'r')

        while True:
            content = file.readline()
            if not content:
                print('No todos have been added to this list, use the "a" command to add a new one.')
                break
            else:
                print(content)
        
        file.close()
            

    else:
        print('That list does not exist, you can use the "mkl" command to make a new list')


def quit_app():
    #add save on quit
    print('QUITING...')
    sys.exit(0)


#TODO
def delete_list(response):

    if os.path.exists(''):
        os.remove('')
    else:
        print('That list does not exist you can use the "mkl" command to make a new list')

def add_todo(response):
    #[a, something title, dl, 20, p, high]
    tokens = response.split(":")
    params = []

    for i in range(len(tokens)):
        match tokens[i]:
            case 'a': params[0] = tokens[i+1] 
            case 'dl' : params[1] = tokens[i+1]
            case 'p' : params[2] = tokens[i+1]