# Main imports
import time
import ctypes
from datetime import datetime

# Set start time
code_start_time = time.time()

# Set intervals (in seconds)
work_interval = 1800 
idle_time_threshold = 300  

# Break message
def remind_break():
    message = "Time to take a break!"
    ctypes.windll.user32.MessageBoxW(0, message, "Break Reminder", 0x40 | 0x1)

# Back from break message
def back_from_inactivity():
    message = "Welcome back! Are you ready to get back to work?"
    ctypes.windll.user32.MessageBoxW(0, message, "Break Reminder", 0x40 | 0x1)

# Idle time by tracking keyboard and mouse activity
def inactivity_time():
    class last_active_time(ctypes.Structure):
        _last_active_time_ = [("cbSize", ctypes.c_uint), ("dwTime", ctypes.c_uint)]

    last_input_info = last_active_time()
    last_input_info.cbSize = ctypes.sizeof(last_active_time)
    
    ctypes.windll.user32.GetLastInputInfo(ctypes.byref(last_input_info))
    last_input = (ctypes.windll.kernel32.GetTickCount() - last_input_info.dwTime) // 1000
    
    return last_input

# Loop
while True:
    idle_time = inactivity_time()
    time_spent = time.time() - code_start_time

    if idle_time >= idle_time_threshold:
        back_from_inactivity()
        code_start_time = time.time()
    
    elif time_spent >= work_interval:
        remind_break()
        code_start_time = time.time()
        with open("break_log.txt", "a") as log_file:
                        log_file.write(f"Break taken at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    time.sleep(1)