import subprocess

def run_command(command_list):
        try:
            subprocess.run(command_list, check=True)
            print(f"{' '.join(command_list)}")
        except Exception as e:
            print(f"Error running command: {e}")

def change_profile(profile):
    run_command(["asusctl", "profile", "--profile-set", profile])

def change_color(mode, color):
    run_command(["asusctl", "aura", mode, "-c", color])