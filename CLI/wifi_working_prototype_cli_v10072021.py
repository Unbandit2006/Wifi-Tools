import os, re
import time

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

def get_profiles():
    # Finding Names of your wifi profiles saved on ypur computer
    wifi_profiles_command = 'netsh wlan show profiles'
    wifi_profiles = os.popen(wifi_profiles_command).read()
    wifi_profile_names = re.findall(string=wifi_profiles, pattern="All User Profile     : (.*)")

    return wifi_profile_names

def get_pass(profile_name):
    # Gets the Password For the Profile Specified
    password_command = 'netsh wlan show profile '+profile_name+' key=clear'
    password_text = os.popen(password_command).read()
    password = re.findall('Key Content            : (.*)', password_text)

    return password[0]





# Main Code
def intro_sequence():
    print('******************************')
    print('WELCOME TO STARGATE WIFI TOOLS')
    print('******************************\n\n')

def wifi_pass():
    names = get_profiles()

    for count, val in enumerate(names):
        print(f'[{count}]: {val}')

    choice = input('\n\nPLEASE ENTER A NUMBER CORRELATING TO THE WIFI NAME YOU WANT THE PASSWORD TO: ')\

    try:
        if int(choice) in range(len(names)):
            password = get_pass(names[int(choice)])
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
            print('Please Try Again.')
            time.sleep(1)
            os.system('cls')
            intro_sequence()
            wifi_pass()

    except Exception as e:
        print('YOU CAN ONLY ENTER A NUMBER CORRELATTING TO THE WIFI NAME')
        time.sleep(2)
        os.system('cls')
        intro_sequence()
        wifi_pass()


if __name__ == '__main__':
    intro_sequence()
    wifi_pass()