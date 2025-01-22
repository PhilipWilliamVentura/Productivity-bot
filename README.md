This code creates a productivity bot
The program tracks idle time (keyboard and mouse inactivity) and reminds you to take breaks at regular intervals.<br/>
If you’ve been idle for more than the set threshold, a welcome-back message will be displayed.<br/>
Each break time is logged in a break_log.txt file with a timestamp.<br/>

Dependencies<br/>

Python<br/>
Version: Python 3.7 or higher.

Libraries
```
pip install datetime
```

Additional Requirements<br/>
Platform: This program relies on the Windows API (ctypes.windll) to monitor user activity and display message boxes. It is designed to work on Windows systems only.<br/>
No additional libraries are needed beyond Python's standard library, except for the optional installation of datetime, which is included in the standard library.
