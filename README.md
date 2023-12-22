# Photo Recovery Tool

## Overview
This Python script interfaces with the PhotoRec tool to assist in recovering deleted photos from a specified device. It lists mounted drives and allows the user to select a drive for recovery.

## Prerequisites
- Python 3.x
- PhotoRec installed and accessible in the system's PATH

## Installation
1. Ensure Python 3.x is installed on your system.
2. Install PhotoRec from [PhotoRec's official website](https://www.cgsecurity.org/wiki/PhotoRec).

## Usage
To run the script, follow these steps:
1. Open a terminal or command prompt.
2. Navigate to the directory containing the script.
3. Run the script with the command `python photo_recovery.py`.
4. Follow the on-screen instructions to select a drive and start the recovery process.

## Caution
- Use this tool at your own risk. Incorrect use may lead to permanent data loss.
- It is recommended to consult with a data recovery professional if unsure.

## License
[MIT License](LICENSE)

#Installing PhotoRec and adding it to your system's PATH involves several steps. PhotoRec is part of the TestDisk package, and you'll need to download and install it from the official website. Here's a step-by-step guide:

### For Windows Users:

1. **Download TestDisk & PhotoRec**:
   - Visit the official website: [CGSecurity - TestDisk Download](https://www.cgsecurity.org/wiki/TestDisk_Download).
   - Download the appropriate version for your Windows (32-bit or 64-bit).

2. **Extract the Downloaded File**:
   - Extract the downloaded ZIP file to a location on your computer (e.g., `C:\Program Files\TestDisk`).

3. **Add to System PATH**:
   - Right-click on 'This PC' or 'My Computer' and select 'Properties'.
   - Click on 'Advanced system settings' and then 'Environment Variables'.
   - Under 'System Variables', find and select the 'Path' variable, then click 'Edit'.
   - Click 'New' and add the path where you extracted TestDisk (e.g., `C:\Program Files\TestDisk`).
   - Click 'OK' to close all dialogs.

4. **Verify Installation**:
   - Open a new Command Prompt.
   - Type `photorec` and press Enter. If the installation was successful, you should see the PhotoRec interface.

### For macOS Users:

1. **Download TestDisk & PhotoRec**:
   - Visit [CGSecurity - TestDisk Download](https://www.cgsecurity.org/wiki/TestDisk_Download).
   - Download the version for macOS.

2. **Extract and Move to Applications**:
   - Extract the downloaded file.
   - It’s recommended to move the TestDisk folder to your Applications directory for ease of use.

3. **Add to PATH (Optional)**:
   - Open Terminal.
   - Edit your shell profile file (e.g., `~/.bash_profile` for bash or `~/.zshrc` for zsh) using a text editor like nano: `nano ~/.bash_profile`.
   - Add the following line (modify the path if you didn't place it in Applications): `export PATH="/Applications/testdisk-7.1/:$PATH"`.
   - Save and exit (in nano, it's Ctrl+O, Enter, and then Ctrl+X).
   - Apply the changes: `source ~/.bash_profile`.

4. **Verify Installation**:
   - Open a new Terminal window.
   - Type `photorec` and press Enter.

### For Linux Users:

PhotoRec is usually available in the official repositories of most Linux distributions.

1. **Install via Package Manager** (e.g., for Debian/Ubuntu):
   - Open Terminal.
   - Run `sudo apt-get install testdisk`.
   - Enter your password and confirm the installation.

2. **Verify Installation**:
   - In Terminal, type `photorec` and press Enter.

### Notes:
- Always ensure you download software from official or trusted sources to avoid security risks.
- The installation process may require administrative privileges.
- After adding PhotoRec to your PATH, you might need to restart your terminal or command prompt for the changes to take effect.


For installing TestDisk and PhotoRec on a MacBook Pro with an M1 chip, you'll need to follow a slightly different approach compared to Intel-based Macs due to the difference in architecture. The M1 chip uses ARM architecture, and many applications, including TestDisk, are primarily designed for Intel (x86_64) architecture. However, macOS Big Sur and later versions on M1 Macs include Rosetta 2, which allows you to run applications built for Intel-based Macs.

Given this information, here's how you should proceed:

Installing TestDisk and PhotoRec on MacBook Pro M1
Using Homebrew:
Homebrew is a popular package manager for macOS, which simplifies the installation of software.
First, ensure that you have Homebrew installed. If not, you can install it by following the instructions on Homebrew's official website.
Once Homebrew is installed, open the Terminal and run the following command:
Copy code
brew install testdisk
This command will download and install TestDisk (which includes PhotoRec) compatible with your M1 Mac. Homebrew automatically handles the architecture compatibility.
Downloading from Official Website:
Alternatively, you can manually download TestDisk & PhotoRec from the CGSecurity website.
For M1 Macs, you can still try the Mac OS X Intel / OS X / macOS version. With Rosetta 2, your M1 Mac should be able to run it.
After downloading, extract the files and move them to a preferred directory.
Running TestDisk and PhotoRec:
After installation, you can run PhotoRec or TestDisk from the Terminal.
If you installed via Homebrew, simply typing photorec or testdisk in the Terminal should work.
If you downloaded it manually, navigate to the directory where you extracted the files and run them from there. For example:
bash
Copy code
cd /path/to/testdisk-folder
./photorec
Note on Compatibility:
While Rosetta 2 allows running Intel-based applications on M1 Macs, there might be some performance impacts or occasional compatibility issues.
Always ensure that your macOS is up-to-date to have the latest version of Rosetta 2 for better compatibility.
Conclusion
For a MacBook Pro with an M1 chip, using Homebrew is the recommended way to install TestDisk and PhotoRec due to its simplicity and automatic handling of compatibility issues. Alternatively, downloading from the official website and running the software under Rosetta 2 is also an option. Remember to regularly check for any updates from the software developers for native ARM support in the future.
