# import tkinter as tk
# from tkinter import messagebox
# from enum import IntEnum
# import pygubu
# import subprocess
import time
import threading
# import sys
import tkinter as tk

# #maybe try to repack the label to refresh

# class Duration(IntEnum):
#     zero = 0
#     oneHour = 3600
#     twoHours = 7200
#     threeHours = 10800

# class MyApplication(pygubu.TkApplication):
#     def _create_ui(self):
#         self.stop = False

#         #1: Create a builder
#         self.builder = builder = pygubu.Builder()

#         #2: Load an ui file
#         self.builder.add_from_file('gui.ui')

#         #3: Create the widget using a master as parent
#         self.mainwindow = builder.get_object('App_Frame', self.master)

#         #4 connect callbacks to buttons
#         self.builder.connect_callbacks(self)

#     def shutdown_now(self):
#         self.spawnThreadWithDelay(Duration.zero)

#     def on_b1h_click(self):
#         self.spawnThreadWithDelay(Duration.oneHour)

#     def on_b2h_click(self):
#         self.spawnThreadWithDelay(Duration.twoHours)

#     def on_b3h_click(self):
#         self.spawnThreadWithDelay(Duration.threeHours)

#     def abort_shutdown(self):
#         self.stop = True
#         if hasattr(self, 'thread'):
#             if(self.thread.is_alive()):
#                 self.thread.join()
#                 del self.thread
#                 print('\nThread stopped')
#         print('\nShutdown aborted')

#     def shutdown(self, delay):
#         self.stop = False
#         while delay > 0:
#             if(self.stop):
#                 return
#             time.sleep(1)
#             delay -= 1
#             printMessage = 'Shutting down in ' + str(delay) + ' seconds'
#         subprocess.Popen(['shutdown.exe', '-s', '-f', '-t', '0'])

#     def spawnThreadWithDelay(self, delay):
#         self.thread = threading.Thread(target=self.shutdown, args=(delay,))
#         self.thread.start()

global stop
global testLabel
global tkStringVar

def shutdown(delay):
    while delay > 0:
        print(f"delay is {delay}")
        if stop:
            print("start thread stopped")
            return
        time.sleep(1)
        delay-=1
    print("time ran out")

# def stop():
#     stop = True
#     print("stop thread stopped")

def changeLabel(text):
    tkStringVar.set(text)

if __name__ == '__main__':
    # stop = False
    # start_t = threading.Thread(target=shutdown, args=(10,))
    # stop_t = threading.Thread(target=stop)
    # start_t.start()
    # stop_t.start()
    # time.sleep(5)
    # stop = True
    mainWindow = tk.Tk()
    mainWindow.title('Counting Seconds')

    startButton = tk.Button(mainWindow, text='Start', width=25, command=mainWindow.destroy)
    startButton.pack()

    stopButton = tk.Button(mainWindow, text='Stop', width=25, command=mainWindow.destroy)
    stopButton.pack()

    tkStringVar = tk.StringVar()
    tkStringVar.set("start up the rotos")

    testLabel = tk.Label(mainWindow, textvariable = tkStringVar).pack()
    # testLabel.pack()

    mainWindow.mainloop()

    changeText = threading.Thread(target=changeLabel, args=("pack the commie scum",))
    time.sleep(5)
    changeText.start()





    # root = tk.Tk()
    # app = MyApplication(root)
    # app.run()