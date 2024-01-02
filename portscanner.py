import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import socket
import threading

class PortScannerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Port Scanner")
        
        self.create_widgets()

    def create_widgets(self):
        self.label_host = ttk.Label(self.root, text="Target Host:")
        self.label_host.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        
        self.entry_host = ttk.Entry(self.root)
        self.entry_host.grid(row=0, column=1, padx=10, pady=5, sticky="ew")
        self.entry_host.insert(0, "localhost")

        self.label_start_port = ttk.Label(self.root, text="Start Port:")
        self.label_start_port.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        self.entry_start_port = ttk.Entry(self.root)
        self.entry_start_port.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
        self.entry_start_port.insert(0, "1")

        self.label_end_port = ttk.Label(self.root, text="End Port:")
        self.label_end_port.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        self.entry_end_port = ttk.Entry(self.root)
        self.entry_end_port.grid(row=2, column=1, padx=10, pady=5, sticky="ew")
        self.entry_end_port.insert(0, "1024")

        self.scan_button = ttk.Button(self.root, text="Scan Ports", command=self.start_scanning)
        self.scan_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.result_text = tk.Text(self.root, height=10, width=40)
        self.result_text.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="ew")
        self.result_text.insert(tk.END, "Scan results will be displayed here.")

    def start_scanning(self):
        target_host = self.entry_host.get()
        start_port = int(self.entry_start_port.get())
        end_port = int(self.entry_end_port.get())

        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f"Scanning {target_host} from port {start_port} to {end_port}...\n")

        
        scan_thread = threading.Thread(target=self.scan_ports, args=(target_host, start_port, end_port))
        scan_thread.start()

    def scan_ports(self, target, start_port, end_port):
        for port in range(start_port, end_port + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
        
            try:
                
                sock.connect((target, port))
                result = f"Port {port} is open.\n"
                self.result_text.insert(tk.END, result)
            except (socket.timeout, socket.error):
                pass
            finally:
                sock.close()

        self.result_text.insert(tk.END, "Scan completed.\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = PortScannerGUI(root)
    root.mainloop()
