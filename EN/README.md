# **SkyLoCkeR**

Winlocker on python

Based on [hellolocker](https://github.com/restanse/HELLOCKER)





Winlocker written in Python.
DO NOT USE FOR EVIL PURPOSES!





##### **Functional:**

1.Banner in full screen on top of all windows

2. Complete blocking of the keyboard (the password can be entered by clicking on the graphic buttons)
3. Creating a bat file to add to startup
4. Call bsod when password attempts expire
5. frightening animation before opening the main window (000000.gif in resources)
6. if you restart your computer, winlocker will start instead of the desktop.

##### 

##### **Detections (VirusTotal):**

 [https://www.virustotal.com/gui/file/2644c5e41beabdd467e0aec3f7f9586c8683312180dbb4fb381a32df0173e8bc/detection](https://www.virustotal.com/gui/file/2644c5e41beabdd467e0aec3f7f9586c8683312180dbb4fb381a32df0173e8bc/detection)





##### **Using:**

open the file Builder.exe , and follow the instructions in it.



##### **Error fixing:**

When building your application, you may encounter an error related to pyinstaller. It looks like this:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

 ***X*** **Unhandled exception in script**



 ***X*** Failed to execute script 'lock' due to unhandled exception: No

 module named 'tkinter'



 Traceback (most recent call last):

 File "lock.py", line 1, in <module>

 ModuleNotFoundError: No module named 'tkinter'

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_



This happens most often if you compile several files in a row, and Pyinstaller has

a cache problem, and it loses important libraries for the code. You can fix this by

* Restarting your PC.;
* Reinstalling the PyInstaller component;
* Reinstalling the entire Python.

One of these methods will most likely help you solve the problem.

Also, if you have antivirus software, the program may not start, or it may start with limited functionality.

This applies to both the compiler and the final program. I don't think it's worth explaining why this happens.

