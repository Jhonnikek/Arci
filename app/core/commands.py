import subprocess

def run_command(command_list):
        try:
            subprocess.run(command_list, check=True)
            print(f"{' '.join(command_list)}")
        except Exception as e:
            print(f"Error running command: {e}")

def change_power_profile(profile):
    run_command(["asusctl", "profile", "--profile-set", profile])

def change_aura_mode(mode):
    run_command(["asusctl", "aura", mode])

def change_rgb_lvl(brightness):
    run_command(["asusctl", "-k", brightness])

def change_color(mode, color):
    run_command(["asusctl", "aura", mode, "-c", color])

def change_battery_limit(limit):
    run_command(["asusctl", "-c", limit])