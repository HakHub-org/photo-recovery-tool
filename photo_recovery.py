import subprocess

def list_mounted_drives():
    print("Available Drives:")
    try:
        result = subprocess.run(["diskutil", "list"], capture_output=True, text=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Failed to list drives: {e}")

def run_photorec(device_path):
    try:
        subprocess.run(["photorec", device_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred during recovery: {e}")
    except FileNotFoundError:
        print("PhotoRec is not installed or not in the PATH.")

def main():
    list_mounted_drives()
    device_path = input("Enter the path to the device for recovery (e.g., /dev/disk2): ")

    if not device_path.startswith("/dev/"):
        print("Invalid device path. Make sure it starts with /dev/")
        return

    run_photorec(device_path)

if __name__ == "__main__":
    main()

