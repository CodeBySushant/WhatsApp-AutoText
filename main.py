import pywhatkit as pwk
import pyautogui
import time

phone_number = "+916204653603"
message = "Hello World!"

# Send message instantly
pwk.sendwhatmsg_instantly(phone_number, message, wait_time=10, tab_close=False)

# Short wait: Give the browser time to type the message (experiment with this)
time.sleep(3)  # You can try 2 if it's fast enough

# Instantly press Enter
pyautogui.press("enter")

print("Done! Message sent instantly.")
