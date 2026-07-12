# main.py 

# Import
import tkinter as tk
from installers import vm1
from installers import vm2
from installers import vm3
from installers import vm4

# Main Window
main = tk.Tk()
main.title("vminstaller")
main.geometry('215x210')
main.configure(bg="#474747") # Other variants => ab633a 6b6b6b

# Hover Window
 class Tooltip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.window = None
        widget.bind("<Enter>", self.show)
        widget.bind("<Leave>", self.hide)
    
    def show(self, event=None):
        self.window = tk.Toplevel(self.widget)
        self.window.overrideredirect(True)
        x = self.widget.winfo_rootx() + 20
        y = self.widget.winfo_rooty() + self.widget.winfo_height() + 5
        self.window.geometry(f"+{x}+{y}")
        label = tk.Label(self.window, text=self.text, bg="black", fg="white", padx=10, pady=5, font=("Arial", 10, "bold"))
        label.pack()

    def hide(self, event=None):
        if self.window:
            self.window.destroy()
            self.window = None

# VM Scripts
# vm-slot-1
def start_vm1():
    vm1.install()

# vm-slot-2
def start_vm2():
    vm2.install()

# vm-slot-3
def start_vm3():
    vm3.install()

# vm-slot-4
def start_vm4():
    vm4.install()


# Connections
# vm-slot-1
deploy_vs1 = tk.Button(main, command=start_vm1, bg="white", borderwidth=0, relief="flat", text="vm1 virt-std", fg="black", font=("Arial", 12))
deploy_vs1.grid(row=0, column=0, pady=10, padx=15) # This Padx changes the rest of deploy_vsx aswell 
hoverinfo_vs1 = tk.Label(main, text="info", width=5, height=1, bg="white", fg="black", font=("Arial", 12))
hoverinfo_vs1.grid(row=0, column=1, pady=10, padx=10)
tooltip_vs1 = Tooltip(hoverinfo_vs1, "Name: Passwort:")

# vm-slot-2
deploy_vs2 = tk.Button(main, command=start_vm2, bg="white", borderwidth=0, relief="flat", text="vm2 virt-std", fg="black", font=("Arial", 12))
deploy_vs2.grid(row=1, column=0, pady=10)
hoverinfo_vs2 = tk.Label(main, text="info", width=5, height=1, bg="white", fg="black", font=("Arial", 12))
hoverinfo_vs2.grid(row=1, column=1, pady=10, padx=10)
tooltip_vs2 = Tooltip(hoverinfo_vs2, "Name: Passwort:")

# vm-slot-3
deploy_vs3 = tk.Button(main, command=start_vm3, bg="white", borderwidth=0, relief="flat", text="vm3 virt-std", fg="black", font=("Arial", 12))
deploy_vs3.grid(row=2, column=0, pady=10)
hoverinfo_vs3 = tk.Label(main, text="info", width=5, height=1, bg="white", fg="black", font=("Arial", 12))
hoverinfo_vs3.grid(row=2, column=1, pady=10, padx=10)
tooltip_vs3 = Tooltip(hoverinfo_vs3, "Name: Passwort:")

# vm-slot-4
deploy_vs4 = tk.Button(main, command=start_vm4, bg="white", borderwidth=0, relief="flat", text="vm4 virt-std", fg="black", font=("Arial", 12))
deploy_vs4.grid(row=3, column=0, pady=10)
hoverinfo_vs4 = tk.Label(main, text="info", width=5, height=1, bg="white", fg="black", font=("Arial", 12))
hoverinfo_vs4.grid(row=3, column=1, pady=10, padx=10)
tooltip_vs4 = Tooltip(hoverinfo_vs4, "Name: Passwort:")

main.mainloop()
