import tkinter as tk
from tkinter import messagebox
import pygubu
import subprocess

class MyApplication(pygubu.TkApplication):
    def _create_ui(self):

        #1: Create a builder
        self.builder = builder = pygubu.Builder()

        #2: Load an ui file
        builder.add_from_file('gui.ui')

        #3: Create the widget using a master as parent
        self.mainwindow = builder.get_object('App_Frame', self.master)
        builder.connect_callbacks(self)

    def on_b1h_click(self):
        subprocess.Popen(['shutdown.exe', '-s', '-t', '3600'], shell=True)

    def on_b2h_click(self):
        messagebox.showinfo('Message', 'You clicked Button 2')

    def on_b3h_click(self):
        messagebox.showinfo('Message', 'You clicked Button 3')

    def stop_shutdown(self):
        subprocess.Popen(['shutdown.exe', '-a'], shell=True)


if __name__ == '__main__':
    root = tk.Tk()
    app = MyApplication(root)
    app.run()