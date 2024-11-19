# Keylogger_PRODIGY_CS_04

 Keylogger Script

This is a Python-based keylogger script that listens for keyboard events and logs the keys pressed along with a timestamp to a file. The script uses the `pynput` library to capture keyboard input and save the information in a `keylog.txt` file.

## Prerequisites

Before running this script, ensure that you have Python 3.x installed. Additionally, you'll need to install the `pynput` library.

### Install pynput

You can install the `pynput` library using pip:

pip install pynput

**How It Works**

The script listens for keyboard events and logs every keypress to a file (keylog.txt). It captures both regular key presses and special keys (like Enter, Shift, etc.).

The log format includes:

Timestamp: The date and time the key was pressed.

Key: The key that was pressed, including special keys.

Key Features:

Logs regular and special keys.

Saves keystrokes with a timestamp.

Stops logging when Ctrl+C is pressed or an Esc key is detected.

**Running the Script**

To run the script, simply execute it using Python:

python keylogger.py
