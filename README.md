[![GitHub Repo stars](https://img.shields.io/github/stars/Elehiggle/SimpleRazerBatteryNotification?style=flat-square)](https://github.com/Elehiggle/SimpleRazerBatteryNotification/stargazers)
[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/Elehiggle/SimpleRazerBatteryNotification/publish.yml?branch=master&label=build&logo=github&style=flat-square)](https://github.com/Elehiggle/SimpleRazerBatteryNotification/actions/workflows/publish.yml)
[![GitHub last commit](https://img.shields.io/github/last-commit/Elehiggle/SimpleRazerBatteryNotification?style=flat-square)](https://github.com/Elehiggle/SimpleRazerBatteryNotification/commits/master)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/78d52e5d61e145fc89bfa39743eafe76)](https://app.codacy.com/gh/Elehiggle/SimpleRazerBatteryNotification/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)
[![GitHub License](https://img.shields.io/github/license/Elehiggle/SimpleRazerBatteryNotification?style=flat-square)](https://github.com/Elehiggle/SimpleRazerBatteryNotification/blob/master/LICENSE)

# Simple Razer Battery Notification

This is a very simple tool that runs in the background and notifies you when your Razer mouse/keyboard battery is low (and possibly other devices that are listed via Razer Synapse 3).

## Features

- Checks battery level of the Razer device and notifies you when it is low
- If you lock your PC, it will notify you at a higher battery percentage so you can prepare earlier

## Prerequisites

- Python 3.12 or just download the precompiled Windows executable file
- It uses the Razer Synapse 3 tool which always runs in the background and writes log files. This simple tool watches the log files for battery status changes.

## Installation

### SIMPLE USAGE: Skip to the [Usage via Windows binary](#usage-via-windows-binary) section if you want to use the precompiled Windows executable file

1. Clone the repository:

    ```bash
    git clone https://github.com/Elehiggle/SimpleRazerBatteryNotification.git
    cd SimpleRazerBatteryNotification
    ```

2. Install the required dependencies:

    ```bash
    pip3 install -r requirements.txt
    ```
   _or alternatively:_
    ```bash
    python3 -m pip install Windows-Toasts file-read-backwards
    ```

3. Set the following environment variables with your own values:

| Parameter                                      | Description                                                                         |
|------------------------------------------------|-------------------------------------------------------------------------------------|
| `BATTERY_LEVEL_ALERT_THRESHOLD`                | Battery % where you would like to get notified. Default: "5"                        |
| `BATTERY_LEVEL_ALERT_THRESHOLD_LOCKED`         | Battery % where you would like to get notified when you lock your PC. Default: "30" |

## Usage via script

Run the script:

```bash
python3 main.py
```

## Usage via Windows binary

Simply run the executable file which you can download [here](https://github.com/Elehiggle/SimpleRazerBatteryNotification/releases) (attention: Windows SmartScreen defender may raise an alert, this is normal since this is an unknown tool). It will silently run in the background and notify you when your Razer device battery is low via notifications and beeps at certain thresholds. 
Copy the file into your startup folder at %APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup to run it automatically on startup. It will use the default variables (5% and 30% for when the PC is locked)

## Known Issues

This tool was only meant for private use for my Razer Viper V2 Pro wireless mouse. It may not work if you have multiple wireless Razer devices. In this case, let me know, and I may fix it

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
