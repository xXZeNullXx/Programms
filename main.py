import PySimpleGUI as sg
import subprocess

layout = [[sg.Text("Select Program to install")]]
if subprocess.call(['powershell', 'Get-WindowsPackage -Name 7zip']) != 0:
    layout.append([sg.Button("Install 7Zip", key="7Zip")])
if subprocess.call(['powershell', 'Get-WindowsPackage -Name Brave']) != 0:
    layout.append([sg.Button("Install Brave", key="Brave")])

# Create the window
window = sg.Window("Program", layout)

# Create an event loop
while True:
    event, values = window.read()
    if event == "7Zip":
        # Run the PowerShell command to install 7Zip
        ps_command = 'winget install --id=7zip.7zip  -e'
        subprocess.call(['powershell', '-Command', ps_command])
        layout.pop(1)
    if event == "Brave":
        # Run the PowerShell command to install Brave
        ps_command = 'winget install --id=Brave.Brave  -e'
        subprocess.call(['powershell', '-Command', ps_command])
        layout.pop(1)
    if event == sg.WIN_CLOSED:
        break

window.close()