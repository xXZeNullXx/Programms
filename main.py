import PySimpleGUI as sg
import subprocess

layout = [[sg.Text("Select Program to install")], [sg.Button("7Zip")], [sg.Button("Brave")]]

# Create the window
window = sg.Window("Program", layout)

# Create an event loop
while True:
    event, values = window.read()
    if event == "7Zip":
        # Run the PowerShell command to install 7Zip
        ps_command = 'Write-Host "Installing 7Zip"'
        subprocess.call(['powershell', '-Command', ps_command])
    if event == "Brave":
        # Run the PowerShell command to install Brave
        ps_command = 'Write-Host "Installing Brave"'
        subprocess.call(['powershell', '-Command', ps_command])
    if event == sg.WIN_CLOSED:
        break

window.close()