import tkinter as tk
import pygubu
import subprocess
import time
import threading
import sys

class Showstopper:
    def __init__(self):
        super().__init__()
        self.abort_shutdown = False
        self.thread = None
        self.window = tk.Tk()
        self.window.title("Showstopper")

    def prepare_gui_elements(self):
        # GUI Components definiton
        self.top_label = tk.Label(text="Shutdown")
        self.countdown_lable = tk.Label(text="No shutdown initiated")
        self.button_now = tk.Button(text="Now", width=10, height=1)
        self.button_1h = tk.Button(text="1h", width=10, height=1)
        self.button_2h = tk.Button(text="2h", width=10, height=1)
        self.button_3h = tk.Button(text="3h", width=10, height=1)
        self.button_abort = tk.Button(text="Abort", width=10, height=1)

        self.button_1h.bind("<Button-1>", self.on_b1h_click)
        self.button_abort.bind("<Button-1>", self.abort_shutdown)

        self.gui_elements = [
            self.top_label,
            self.button_now,
            self.button_1h,
            self.button_2h,
            self.button_3h,
            self.button_abort,
            self.countdown_lable
            ]

    def pack_gui_elements(self):
        for element in self.gui_elements:
            element.pack()

    def run(self):
        self.window.mainloop()

    def shutdown_now(self):
        self.spawnThreadWithDelay(0)

    def on_b1h_click(self, event):
        print('countdown started')
        self.spawnThreadWithDelay(3600)

    def on_b2h_click(self):
        self.spawnThreadWithDelay(7200)

    def on_b3h_click(self):
        self.spawnThreadWithDelay(10800)

    def abort_shutdown(self, event):
        if(self.thread is not None):
            self.abort_shutdown = True
            if(self.thread.is_alive()):
                self.thread.join()
                self.thread = None
            print('\nShutdown aborted')
        #else print label no shutdown to abort

    def shutdown(self, delay):
        while delay > 0:
            while(not self.abort_shutdown):
                time.sleep(1)
                delay -= 1
                printMessage = 'Shutting down in ' + str(delay) + ' seconds'
                print(printMessage, end='\r', flush=True)
        self.abort_shutdown = False
        print('thread stopped')
        # subprocess.Popen(['shutdown.exe', '-s', '-f', '-t', '0'])

    def spawnThreadWithDelay(self, delay):
        if(self.thrpppppead is None):
            self.thread = threading.Thread(target=self.shutdown, args=(delay,))
            self.thread.start()
        #else print error in label


if __name__ == '__main__':
    showstopper = Showstopper()
    showstopper.prepare_gui_elements()
    showstopper.pack_gui_elements()
    showstopper.run()