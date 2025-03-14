import tkinter as tk   
from tkinter import *
from tkinter import ttk
import sv_ttk
import subprocess
from functions import *
import time
import threading

root = tk.Tk()

try:
    root.iconbitmap("C:\\DATA\\Python_GUI\\temp_files_etc\\service_help_customer_question_communication_information_support_icon_261681.ico")  # Path to your icon file
except tk.TclError:
    print("Icon file not found or incorrect format.")
    
root.title("DP04 LAUNCHPAD")
root.geometry("400x500")


w = Label(root, text ='DP04 Launchpad', font = "100")  
w.pack(pady=10) 


jabber_button = ttk.Button(root, text="Jabber Reset Script W10", command=jabber_script_func)
jabber_button.pack(pady=10)

jabber_w11_button = ttk.Button(root, text="Jabber Reset Script W11", command=jabber_w11)
jabber_w11_button.pack(pady=10)

agent_button = ttk.Button(root, text="Agent Logs Script", command=agent_logs_func)
agent_button.pack(pady=10)


label_print_button = ttk.Button(root, text="List Label Printers For A Location", command=list_label_printers)
label_print_button.pack(pady=10)


printer_list_button = ttk.Button(root, text="List Printers For A Location", command=list_printers)
printer_list_button.pack(pady=10)


add_printer_button = ttk.Button(root, text="Add Printers", command=add_printer)
add_printer_button.pack(pady=10)


transfer_script_button = ttk.Button(root, text="Data Transfer", command=data_transfer)
transfer_script_button.pack(pady=10)


net_drivers_button = ttk.Button(root, text="Get PC Network Drivers", command=net_drivers)
net_drivers_button.pack(pady=10)


net_events_button = ttk.Button(root, text="Get PC Network Events", command=net_events)
net_events_button.pack(pady=10)


ping_button = ttk.Button(root, text="Ping List of PCs", command=ping_count)
ping_button.pack(pady=10)


sv_ttk.set_theme("dark")


root.mainloop()