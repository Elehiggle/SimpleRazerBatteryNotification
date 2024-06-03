import re
import ctypes
import time
import winsound
import os
import logging
from file_read_backwards import FileReadBackwards
from windows_toasts import Toast, WindowsToaster

log_level_root = os.getenv("LOG_LEVEL_ROOT", "INFO").upper()
logging.basicConfig(level=log_level_root)

log_level = os.getenv("LOG_LEVEL", "INFO").upper()
logger = logging.getLogger(__name__)
logger.setLevel(log_level)

battery_level_alert_threshold = int(os.getenv("BATTERY_LEVEL_ALERT_THRESHOLD", "5"))
battery_level_alert_threshold_locked = int(
    os.getenv("BATTERY_LEVEL_ALERT_THRESHOLD_LOCKED", "30")
)

log_path = os.path.join(
    os.getenv("LOCALAPPDATA"), "Razer", "Synapse3", "Log", "Razer Synapse 3.log"
)


def get_foreground_window():
    return ctypes.windll.user32.GetForegroundWindow()


def send_alert(battery_level):
    toast = Toast()
    toast.text_fields = [f"Battery: {battery_level}%"]
    WindowsToaster("Simple Razer Battery").show_toast(toast)
    winsound.Beep(200, 200)
    winsound.Beep(200, 200)
    winsound.Beep(200, 200)


def find_last_entries(log_file_path):
    battery_percentage = None
    battery_state = None

    with FileReadBackwards(log_file_path, encoding="utf-8") as frb:
        for line in frb:
            if battery_state is None:
                state_match = re.search(r"Battery State: (\w+)", line)
                if state_match:
                    battery_state = state_match.group(1)

            if battery_percentage is None:
                percentage_match = re.search(r"Battery Percentage: (\d+)", line)
                if percentage_match:
                    battery_percentage = int(percentage_match.group(1))
                    break  # Both variables should now be found already

    return battery_percentage, battery_state


def check_battery_is_low(battery_alert_threshold):
    battery_percentage, battery_state = find_last_entries(log_path)

    if battery_percentage is None or battery_state is None:
        logger.error("Battery percentage or state not found in log file")
        return

    if battery_state == "NotCharging" and battery_percentage is not None:
        logger.debug(
            f"Battery: {battery_state} {battery_percentage}%, threshold: {battery_alert_threshold}"
        )
        if battery_percentage < battery_alert_threshold:
            logger.info("Warning: Battery level is below threshold and not charging!")
            send_alert(battery_percentage)
        else:
            logger.info("Battery is not charging, but the battery level is sufficient")
    else:
        logger.info("Battery state is charging or above the threshold")


def main():
    last_time_windows_was_unlocked = 0
    last_check = 0

    logger.debug(f"Log file path: {log_path}")

    while True:
        is_pc_locked = get_foreground_window() == 0
        time.sleep(2)  # Sleep for 2 seconds
        is_pc_locked = (
            is_pc_locked and get_foreground_window() == 0
        )  # Recheck, as this method is not perfect

        if is_pc_locked:
            if (
                time.time() - last_time_windows_was_unlocked < 10
            ):  # Check if we just locked windows within last 10 seconds
                logger.debug("PC is locked, time to check")
                check_battery_is_low(battery_level_alert_threshold_locked)
        else:
            last_time_windows_was_unlocked = time.time()
            if time.time() - last_check > 60 * 20:  # Check every 20 minutes
                last_check = time.time()
                last_time_windows_was_unlocked = time.time()
                check_battery_is_low(battery_level_alert_threshold)

        time.sleep(5)


if __name__ == "__main__":
    main()
