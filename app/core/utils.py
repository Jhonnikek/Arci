import os

PLATFORM_PROFILE = "/sys/firmware/acpi/platform_profile"
BATTERY_PATHS = [
    "/sys/class/power_supply/BAT0/charge_control_end_threshold",
    "/sys/class/power_supply/BAT1/charge_control_end_threshold",
]

def get_energy_mode():
    if os.path.exists(PLATFORM_PROFILE):
        with open(PLATFORM_PROFILE, "r") as f:
            return f.read().strip()
    return "Desconocido"

def get_battery_limit():
    for path in BATTERY_PATHS:
        if os.path.exists(path):
            with open(path, "r") as f:
                return f.read().strip()
    return "unknown"


def get_keyboard_brightness():
    if os.path.exists("/sys/class/leds/asus::kbd_backlight/brightness"):
        with open("/sys/class/leds/asus::kbd_backlight/brightness", "r") as f:
            return f.read().strip()
    return "0"