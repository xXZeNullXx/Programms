# Define colors for console output
$GREEN = [ConsoleColor]::Green
$RED = [ConsoleColor]::Red
$YELLOW = [ConsoleColor]::Yellow

if (!(Get-Command winget -ErrorAction SilentlyContinue)) {
    # Install winget from Microsoft's official package repository
    Write-Host "Installing winget..." -ForegroundColor $YELLOW
    Invoke-WebRequest -Uri https://github.com/microsoft/winget-cli/releases/download/v1.0.11692/Microsoft.DesktopAppInstaller_8wekyb3d8bbwe.appxbundle -OutFile winget.appxbundle
    Add-AppxPackage .\winget.appxbundle

    # Verify that winget is installed
    if (Get-Command winget -ErrorAction SilentlyContinue) {
        Write-Host "winget installed successfully" -ForegroundColor $GREEN
    } else {
        Write-Host "Failed to install winget" -ForegroundColor $RED
    }

    # Remove the temporary appxbundle file
    Remove-Item .\winget.appxbundle
} else {
    Write-Host "winget is already installed" -ForegroundColor $YELLOW
}

# Run main.py
python .\main.py