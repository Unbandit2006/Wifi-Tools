import os, re
import platform

class wifi:
    def get_profilenames() -> list:
        # Find Profile Names of that are saved on your computer

        if platform.system().lower() == 'windows':
            wifi_profiles_cmd = 'netsh wlan show profiles'
            wifi_profiles = os.popen(wifi_profiles_cmd).read()
            wifi_profile_names = re.findall(string=wifi_profiles, pattern="All User Profile     : (.*)")

            return wifi_profile_names

    
    def get_pass(profile_name) -> str:
        # Gets the Password For the Profile Specified

        if platform.system().lower() == 'windows':
            password_command = 'netsh wlan show profile '+profile_name+' key=clear'
            password_text = os.popen(password_command).read()
            password = re.findall('Key Content            : (.*)', password_text)

            return password[0]