#!usr/bin/env python3
from termux import start, print_menu, Exception_Message, exit_program 


IS_RUNNING = True
while(IS_RUNNING):
    try:
        print_menu()
        choice = int(input("[+] Command > "))
        start(choice)
        check = input('[+] Press Any Key to continue, to exit enter 6:')
        if check == '6':
            IS_RUNNING = False

    except Exception as e:
        Exception_Message(e)
    

print('[+] Exiting... Please be patient...')
exit_program()
