import PySimpleGUI as sg
import subprocess

layout = [[sg.Text("Select Program to install")], [sg.Button("Install 7Zip", key="7Zip")], [sg.Button("Install Brave", key="Brave")]]

# Create the window
window = sg.Window("Program", layout)

# Create an event loop
while True:
    event, values = window.read()
    if event == "7Zip":
        # Run the PowerShell command to install 7Zip
        ps_command = 'winget install --id=7zip.7zip  -e'
        subprocess.call(['powershell', '-Command', ps_command])
    if event == "Brave":
        # Run the PowerShell command to install Brave
        ps_command = 'winget install --id=Brave.Brave  -e'
        subprocess.call(['powershell', '-Command', ps_command])
    if event == sg.WIN_CLOSED:
        break

window.close()