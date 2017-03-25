# DuckyKiller
Short Python script that attempts to neuter USB Rubber Duckies.

### To run this file on Debian or Ubuntu,
* `sudo apt-get install python libusb-1.0-01`
* `sudo apt-get install python-pygame`
* `sudo apt-get install python-usb`
* Navigate to the folder where you've downloaded DuckyKiller.py and wordlist.py, 
* `python DuckyKiller.py`

When a keyboard is plugged in, the script will prompt the user to 
type a set of words. Press enter to confirm your input. Press backspace
to clear your input.

### Before using this in vital locations,
Please note that this is a work in progress, and likey has issues
which could possibly allow people to circumvent it. I've been unable
to find no other alternatives to the vulnerability that is unauthorized
USB keyboard input. Also, on my measily $100 laptop's crappy CPU, this
script hits about five percent while being run from the python interpreter.
