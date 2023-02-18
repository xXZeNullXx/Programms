import PySimpleGUI as sg
import subprocess

# Define the programs to install
programs = {
    "7Zip": "7zip.7zip",
    "Brave": "Brave.Brave"
}

# Check if the programs are already installed
ps_command = 'winget list'
installed_programs = subprocess.check_output(['powershell', '-Command', ps_command]).decode().splitlines()
for program_name in programs.keys():
    if any(program_name.lower() in program.lower() for program in installed_programs):
        programs[program_name] = None  # Set to None to hide the button

# Create the layout
layout = [[sg.Text("Select Program to install")]]
for program_name, program_id in programs.items():
    if program_id is not None:
        layout.append([sg.Button(f"Install {program_name}", key=program_name)])

# Create the window
window = sg.Window("Program", layout)

# Create an event loop
while True:
    event, values = window.read()
    if event in programs.keys() and programs[event] is not None:
        # Run the PowerShell command to install the selected program
        program_id = programs[event]
        ps_command = f'winget install --id={program_id} -e'
        subprocess.call(['powershell', '-Command', ps_command])
        
        # Re-check if the installed program to update the button status
        ps_command = 'winget list'
        installed_programs = subprocess.check_output(['powershell', '-Command', ps_command]).decode().splitlines()
        for program_name in programs.keys():
            if any(program_name.lower() in program.lower() for program in installed_programs):
                programs[program_name] = None
            else:
                programs[program_name] = f"{program_name}"

        # Update the button status
        for program_name, program_id in programs.items():
            if program_id is not None:
                window[program_name].update(visible=True)
            else:
                window[program_name].update(visible=False)

    if event == sg.WIN_CLOSED:
        break

window.close()