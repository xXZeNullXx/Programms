import PySimpleGUI as sg
import subprocess

# Define the programs to install
programs = {
    "7Zip": "7zip.7zip",
    "Brave": "Brave.Brave",
    "VSCode": "Microsoft.VisualStudioCode",
    "Discord": "Discord.Discord",
    "TeraCopy": "CodeSector.TeraCopy",
    "GitHub Desktop": "GitHub.GitHubDesktop",
    "Logitech G HUB": "Logitech.GHUB",
    "CurseForge": "Overwolf.CurseForge",
    "MobaXterm": "Mobatek.MobaXterm",
    "Playnite": "Playnite.Playnite",
    "Acrobat Reader": "Adobe.Acrobat.Reader.64-bit",
    "Elgato StreamDeck": "Elgato.StreamDeck",
    "Flow-Launcher": "Flow-Launcher.Flow-Launcher",
    "EpicGames": "EpicGames.EpicGamesLauncher",
    "PowerToys": "Microsoft.PowerToys",
    "EADesktop": "ElectronicArts.EADesktop",
    "GOG Galaxy": "GOG.Galaxy",
    "Teams": "Microsoft.Teams",
    "GIMP": "GIMP.GIMP",
    "Bitwarden": "Bitwarden.Bitwarden",
    "Notepad++": "Notepad++.Notepad++",
    "IrfanView": "IrfanSkiljan.IrfanView",
    "HWiNFO": "REALiX.HWiNFO",
    "ONLYOFFICE": "ONLYOFFICE.DesktopEditors",
    "Nilesoft Shell": "Nilesoft.Shell",
    "VLC": "VideoLAN.VLC",
    "Rufus": "Rufus.Rufus",
    "Everything": "voidtools.Everything",
    "Espanso": "Espanso.Espanso",
    "snaketail": "snakefoot.snaketail",
    "Rainmeter": "Rainmeter.Rainmeter",
    "Greenshot": "Greenshot.Greenshot",
    "flux": "flux.flux",
}

# Check if the programs are already installed and remove them from the dictionary
installed_programs = (
    subprocess.check_output(["winget", "list"]).decode().lower().splitlines()
)
for program_name in list(programs.keys()):
    if any(program_name.lower() in program.lower() for program in installed_programs):
        del programs[program_name]

# Create the layout
layout = [[sg.Text("Select Program to install")]]
for program_name in programs.keys():
    layout.append([sg.Button(f"Install {program_name}", key=program_name)])

# Create the window
window = sg.Window("Program", layout)

# Create an event loop
while True:
    event, values = window.read()
    if event in programs.keys():
        # Run the PowerShell command to install the selected program
        program_id = programs[event]
        ps_command = f"winget install --id={program_id} -e"
        subprocess.call(["powershell", "-Command", ps_command])

        # Remove the program from the dictionary
        del programs[event]

        # Update the button status
        for element in window.all_elements():
            if element.key in programs:
                element.update(visible=True)
            else:
                element.update(visible=False)

    if event == sg.WINDOW_CLOSED:
        break

window.close()
