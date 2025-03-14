import subprocess
from subprocess import Popen

#C:\\DATA\\Python_GUI\\scripts_for_running\\


# Jabber functions
#W10
def jabber_script_func():
    jabber_script_location = "C:\\DATA\\Python_GUI\\scripts_for_running\\Jabber_Script_W10.ps1"
    run_jabber_script = subprocess.run([r'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe', jabber_script_location ], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    print(run_jabber_script)


#W11
def jabber_w11():
    agent_logs_bat_loc = "C:\\DATA\\Python_GUI\\scripts_for_running\\Jabber_Script_W11.bat"
    run_W11_bat = subprocess.Popen(agent_logs_bat_loc, shell=True, stdout = subprocess.PIPE)
    stdout, stderr = run_W11_bat.communicate()
    print(run_W11_bat)
# End Jabber functions


#FortiNAC agent logs function    
def agent_logs_func():
    agent_logs_bat_loc = "C:\\DATA\\Python_GUI\\scripts_for_running\\Pull_FortiClient_Agent_Logs.bat"
    run_agent_bat = subprocess.Popen(agent_logs_bat_loc, shell=True, stdout = subprocess.PIPE)
    stdout, stderr = run_agent_bat.communicate()
    print(run_agent_bat)
#End FortiNAC agent logs function    


#Group of printer/label printer functions
def list_label_printers():
    lp_bat_location = "C:\\DATA\\Python_GUI\\scripts_for_running\\List_Label_Printers_For_a_Location.bat"
    run_lp_script = subprocess.Popen(lp_bat_location, shell=True, stdout = subprocess.PIPE)
    stdout, stderr = run_lp_script.communicate()
    print(run_lp_script)
    
    
def list_printers():
    printer_bat_location = "C:\\DATA\\Python_GUI\\scripts_for_running\\List_Printers_For_a_Location.bat"
    run_printer_script = subprocess.Popen(printer_bat_location, shell=True, stdout = subprocess.PIPE)
    stdout, stderr = run_printer_script.communicate()
    print(run_printer_script)
    

def add_printer():
    add_printer_bat_location = "C:\\DATA\\Python_GUI\\scripts_for_running\\Printer_Quick_Add.bat"
    run_add_printer_script = subprocess.Popen(add_printer_bat_location, shell=True, stdout = subprocess.PIPE)
    stdout, stderr = run_add_printer_script.communicate()
    print(run_add_printer_script) 
# End printer functions


#Data Transfer Script Function
def data_transfer():
    transfer_bat_location = "C:\\DATA\\Python_GUI\scripts_for_running\\data-transfer-v2.bat"
    run_transfer_script = subprocess.Popen(transfer_bat_location, shell=True, stdout = subprocess.PIPE)
    stdout, stderr = run_transfer_script.communicate()
    print(run_transfer_script)
#End Data Transfer Script Function


#Network Related Functions
def net_drivers():
    drivers_bat_location = "C:\\DATA\\Python_GUI\scripts_for_running\\Get_net_drivers.bat"
    run_drivers_script = subprocess.Popen(drivers_bat_location, shell=True, stdout = subprocess.PIPE)
    stdout, stderr = run_drivers_script.communicate()
    print(run_drivers_script)
    

def net_events():
    events_bat_location = "C:\\DATA\\Python_GUI\scripts_for_running\\Get_Network_Events.bat"
    run_events_script = subprocess.Popen(events_bat_location, shell=True, stdout = subprocess.PIPE)
    stdout, stderr = run_events_script.communicate()
    print(run_events_script)
    

def ping_count():
    ping_bat_location = "C:\\DATA\\Python_GUI\scripts_for_running\\ping_count_select_file.bat"
    run_ping_script = subprocess.Popen(ping_bat_location, shell=True, stdout = subprocess.PIPE)
    stdout, stderr = run_ping_script.communicate()
    print(run_ping_script)
#End Network Related Functions