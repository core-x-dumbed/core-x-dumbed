import sys
import Todo
import datetime
import manager
from termcolor import colored


def read_input():
    manager.view_lists()
    while True:
        print()
        response = input("Enter command: ").rstrip()
        
        if response:

            command = response[0:response.index(":")]
            
            match command:
                case 'q': manager.quit_app()
                case 'vl' : manager.view_lists()
                case 'mkl' : manager.make_list(response)
                case 'r': manager.rename_list(response)
                case 'a': manager.add_todo(response)
                case 'vt': manager.view_todos()
                case 'o': manager.open_list(response)
                # a: something title dl: 20 p: high
                case _: print("Enter a valid command")

                




    