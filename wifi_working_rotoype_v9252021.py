import os
import re
import tkinter as tk

'''Made file and About in the Menubar then made the nto frame'''

# ========== NEW CODE ===========

def passwords():
    default_frame.pack_forget()

    # Command For Double Clicking on an Wifi name in the Listbox
    def get_wifi_password(event):
        wifi_selection_name = wifi_selection.curselection()[0]

        # Checking If you are Connected to this Wifi Network
        connection = os.popen('netsh wlan show interfaces').read()

        # Using RegEx we will Find the connected Newtwork
        connection = re.findall('Profile                : (.*) ', connection)

        if connection[0] == wifi_names[wifi_selection_name]:
            connection = 'True'

        else:
            connection = 'False'

        # Gets Password From Network
        password = os.popen('netsh wlan show profile ' + wifi_names[wifi_selection_name] + ' key=clear').read()

        # Using Regex we will find the password
        password = re.findall('Key Content            : (.*)', password)

        # Changing the Text in the entry
        wifi_password_entry.config(state='normal')
        wifi_password_entry.delete(0, 'end')
        wifi_password_entry.insert(0, password)
        wifi_password_entry.config(state='disabled')

        wifi_connection_entry.config(state='normal')
        wifi_connection_entry.delete(0, 'end')
        wifi_connection_entry.insert(0, connection)
        wifi_connection_entry.config(state='disabled')

        # Changing the Title
        wifi_name_title['text'] = wifi_names[wifi_selection_name]

    # Getting Profile Names (Wifi Names) From Console
    profiles = os.popen('netsh wlan show profiles').read()

    # Using Regexx: Getting the Name of the Netword Profiles (Wifi Names)
    wifi_names = re.findall(string=profiles, pattern="All User Profile     : (.*)")

    wifi_password_frame = tk.Frame(root, width=1350, height=750)  # 4 (, bg='black')

    wifi_selection = tk.Listbox(wifi_password_frame, height=750, width=50)  # 4 (, bg='blue')
    wifi_selection.place(x=0, y=0)

    # Inserting the Wifi Names into the Listbox
    for name in wifi_names:
        wifi_selection.insert(tk.END, name)

    # Binding Double Click to get_wifi_password in the Listbox
    wifi_selection.bind('<Double-Button>', get_wifi_password)

    wifi_name_title = tk.Label(wifi_password_frame, text='Name Of Network',
                               font=('arial', 59, 'bold'))  # 2 (, bg='green')
    wifi_name_title.place(x=305, y=-12)

    wifi_password = tk.Label(wifi_password_frame, text='Wifi Password: ', font=('arial', 40, 'bold'))  # 2 (, bg='red')
    wifi_password.place(x=305, y=150)

    wifi_password_entry = tk.Entry(wifi_password_frame, width=22, font=('arial', 40, 'bold'), state='disabled')
    wifi_password_entry.place(x=690, y=150)

    wifi_connection = tk.Label(wifi_password_frame, text='Connected: ', font=('arial', 40, 'bold'))  # 2 (, bg='yellow')
    wifi_connection.place(x=305, y=220)

    wifi_connection_entry = tk.Entry(wifi_password_frame, width=22, font=('arial', 40, 'bold'), state='disabled')
    wifi_connection_entry.place(x=690, y=220)

    wifi_password_frame.pack()



def about():
    about_win = tk.Toplevel(root)
    about_win.title('About WIFI Tools')
    about_win.geometry('600x200+5+5')
    about_win.resizable(width=False,height=False)

    about_win.mainloop()










root = tk.Tk()
root.geometry('1350x750+0+0')
root.resizable(width=False, height=False)
root.title('WIFI Tools')

# Setting Up the Menu
menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='Quit', command=quit)

wifi_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label='Wifi', menu=wifi_menu)
wifi_menu.add_command(label='Passwords', command=passwords)

help_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label='Help', menu=help_menu)
help_menu.add_command(label='About', command=about)

default_frame = tk.Frame(root, width=1350, height=750)

intro_label = tk.Label(default_frame, text='Introduction', font=('arial', 60, 'bold'))
intro_label.place(x=0, y=0)

info = tk.StringVar(root)
info_label = tk.Label(default_frame, textvariable=info, font=('arial', 20, 'bold'))
info_label.place(x=0, y=90)
info.set(
    'To get the Wifi Names and their Passwords (To Which You Are Already Connected to)\nClick On the Wifi Menu and then Click on the Passwords.\n'\
        'Double-Click on the Name Of the Wifi You Want the Passwoard to, and tada.\nYou Have the Name and the Password Of the Wifi.\n(HINT: It also shows you if your connected to that WIFI)')

default_frame.pack()

root.mainloop()
