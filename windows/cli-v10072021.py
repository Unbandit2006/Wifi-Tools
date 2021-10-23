import SharedCode_v10142021 as code
import os, time

'''
CODE OF CONDUCT:
----------------
funtions will be in snake_case, with a descriptive name.
variables will be also in snake_case again with a descriptive name
class names could be either camel_Case or snake_case again with a descriptive name
WE USE SPACES NO TABS
single quotes for strings

THIS CODE IS THE CLI VERSION OF THE APPLICATION
'''

# Main Code
def intro_sequence():
    print('******************************')
    print('WELCOME TO STARGATE WIFI TOOLS')
    print('******************************\n\n')

def wifi_pass():
    names = code.wifi.get_profilenames()

    for count, val in enumerate(names):
        print(f'[{count}]: {val}')

    print('[Q]: To Quit')

    choice = input('\n\nPLEASE ENTER A NUMBER CORRELATING TO THE WIFI NAME YOU WANT THE PASSWORD TO OR TYPE Q TO QUIT: ')

    try:

        if choice.lower() == 'q':
            print('THANK YOU FOR USING STARGATE WIFI TOOLS')
            time.sleep(2)
            quit()
        
        elif int(choice) in range(len(names)):
            password = code.wifi.get_pass(names[int(choice)])
            print(f'PASSWORD: {password}')
            

            def continue_():
                contine_choice = input('Do YOU WANT TO CONTINUE? Y or N: ')

                if contine_choice.lower() == 'y':
                    os.system('cls')
                    wifi_pass()

                elif contine_choice.lower() == 'n':
                    print('THANK YOU FOR USING STARGATE WIFI TOOLS')
                    quit()

                else:
                    print('PLEASE TYPE EITHER: Y or N')
                    time.sleep(1)
                    os.system('cls')
                    continue_()

            continue_()

        else:
            print('YOU CAN ONLY ENTER A NUMBER CORRELATTING TO THE WIFI NAME OR Q TO QUIT.')
            time.sleep(1)
            os.system('cls')
            intro_sequence()
            wifi_pass()

    except Exception as e:
        print('YOU CAN ONLY ENTER A NUMBER CORRELATTING TO THE WIFI NAME OR Q TO QUIT')
        time.sleep(2)
        os.system('cls')
        intro_sequence()
        wifi_pass()


if __name__ == '__main__':
    intro_sequence()
    wifi_pass()
