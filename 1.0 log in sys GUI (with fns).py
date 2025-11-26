import tkinter as tk
from tkinter import ttk, messagebox
import time

class LoginSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Secure Login System")
        self.root.geometry("500x600")
        self.root.configure(bg='#2c3e50')
        self.root.resizable(False, False)
        
        # Variables
        self.username = ""
        self.password = ""
        self.attempts = 0
        self.max_attempts = 5
        
        # Set style
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#2c3e50')
        self.style.configure('TLabel', background='#2c3e50', foreground='white', font=('Arial', 10))
        self.style.configure('TButton', font=('Arial', 10))
        self.style.configure('Header.TLabel', font=('Arial', 18, 'bold'), foreground='#ecf0f1')
        
        self.create_setup_screen()
        
    def create_setup_screen(self):
        # Clear existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()
            
        # Header
        header_frame = ttk.Frame(self.root)
        header_frame.pack(pady=30)
        
        ttk.Label(header_frame, text="🔐 Account Setup", style='Header.TLabel').pack()
        ttk.Label(header_frame, text="Create your login credentials", font=('Arial', 11)).pack(pady=5)
        
        # Setup Form Frame
        form_frame = ttk.Frame(self.root)
        form_frame.pack(pady=30)
        
        # Username
        ttk.Label(form_frame, text="Set Username:", font=('Arial', 11, 'bold')).grid(row=0, column=0, padx=10, pady=15, sticky='w')
        self.setup_user_entry = ttk.Entry(form_frame, font=('Arial', 11), width=20)
        self.setup_user_entry.grid(row=0, column=1, padx=10, pady=15)
        
        # Password
        ttk.Label(form_frame, text="Set Password:", font=('Arial', 11, 'bold')).grid(row=1, column=0, padx=10, pady=15, sticky='w')
        self.setup_pass_entry = ttk.Entry(form_frame, font=('Arial', 11), width=20, show="•")
        self.setup_pass_entry.grid(row=1, column=1, padx=10, pady=15)
        
        # Show Password Checkbutton
        self.show_pass_var = tk.BooleanVar()
        show_pass_cb = ttk.Checkbutton(form_frame, text="Show Password", variable=self.show_pass_var, 
                                      command=self.toggle_password_visibility)
        show_pass_cb.grid(row=2, column=0, columnspan=2, pady=10)
        
        # Button Frame
        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=20)
        
        ttk.Button(button_frame, text="Create Account", command=self.create_account).pack(pady=10)
        
        # Requirements Frame
        req_frame = ttk.LabelFrame(self.root, text="Security Requirements", padding=10)
        req_frame.pack(pady=20, padx=20, fill='x')
        
        requirements = """• Username: 3+ characters
• Password: 4+ characters
• Maximum 5 login attempts
• Case-sensitive credentials"""
        
        ttk.Label(req_frame, text=requirements, justify='left').pack()
        
    def toggle_password_visibility(self):
        if self.show_pass_var.get():
            self.setup_pass_entry.config(show="")
        else:
            self.setup_pass_entry.config(show="•")
            
    def create_account(self):
        username = self.setup_user_entry.get().strip()
        password = self.setup_pass_entry.get().strip()
        
        if len(username) < 3:
            messagebox.showerror("Invalid Username", "Username must be at least 3 characters long!")
            return
            
        if len(password) < 4:
            messagebox.showerror("Invalid Password", "Password must be at least 4 characters long!")
            return
            
        self.username = username
        self.password = password
        self.attempts = 0
        
        messagebox.showinfo("Account Created", "Account created successfully!\n\nNow please login with your credentials.")
        self.create_login_screen()
        
    def create_login_screen(self):
        # Clear existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()
            
        # Header
        header_frame = ttk.Frame(self.root)
        header_frame.pack(pady=30)
        
        ttk.Label(header_frame, text="🔐 Secure Login", style='Header.TLabel').pack()
        ttk.Label(header_frame, text="Enter your credentials to continue", font=('Arial', 11)).pack(pady=5)
        
        # Login Form Frame
        form_frame = ttk.Frame(self.root)
        form_frame.pack(pady=30)
        
        # Username
        ttk.Label(form_frame, text="Username:", font=('Arial', 11, 'bold')).grid(row=0, column=0, padx=10, pady=15, sticky='w')
        self.login_user_entry = ttk.Entry(form_frame, font=('Arial', 11), width=20)
        self.login_user_entry.grid(row=0, column=1, padx=10, pady=15)
        self.login_user_entry.focus()
        
        # Password
        ttk.Label(form_frame, text="Password:", font=('Arial', 11, 'bold')).grid(row=1, column=0, padx=10, pady=15, sticky='w')
        self.login_pass_entry = ttk.Entry(form_frame, font=('Arial', 11), width=20, show="•")
        self.login_pass_entry.grid(row=1, column=1, padx=10, pady=15)
        
        # Show Password Checkbutton
        self.login_show_pass_var = tk.BooleanVar()
        show_pass_cb = ttk.Checkbutton(form_frame, text="Show Password", variable=self.login_show_pass_var, 
                                      command=self.toggle_login_password)
        show_pass_cb.grid(row=2, column=0, columnspan=2, pady=10)
        
        # Button Frame
        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=20)
        
        ttk.Button(button_frame, text="Login", command=self.attempt_login).pack(pady=5)
        ttk.Button(button_frame, text="Reset Account", command=self.reset_system).pack(pady=5)
        
        # Attempts Frame
        self.attempts_frame = ttk.LabelFrame(self.root, text="Login Status", padding=10)
        self.attempts_frame.pack(pady=20, padx=20, fill='x')
        
        self.attempts_label = ttk.Label(self.attempts_frame, text=f"Attempts: {self.attempts}/{self.max_attempts}", 
                                       font=('Arial', 10, 'bold'))
        self.attempts_label.pack()
        
        self.status_label = ttk.Label(self.attempts_frame, text="Please enter your credentials", 
                                     foreground='#f39c12')
        self.status_label.pack()
        
        # Bind Enter key to login
        self.root.bind('<Return>', lambda event: self.attempt_login())
        
    def toggle_login_password(self):
        if self.login_show_pass_var.get():
            self.login_pass_entry.config(show="")
        else:
            self.login_pass_entry.config(show="•")
            
    def attempt_login(self):
        if self.attempts >= self.max_attempts:
            messagebox.showerror("Account Locked", "Maximum attempts reached! System locked.")
            self.root.quit()
            return
            
        username_attempt = self.login_user_entry.get().strip()
        password_attempt = self.login_pass_entry.get().strip()
        
        self.attempts += 1
        
        if username_attempt == self.username and password_attempt == self.password:
            self.login_success()
        else:
            self.login_failed(username_attempt, password_attempt)
            
    def login_success(self):
        self.status_label.config(text="✅ Login successful! Welcome!", foreground='#27ae60')
        self.attempts_label.config(text=f"Attempts: {self.attempts}/{self.max_attempts} - SUCCESS!")
        
        # Show success message
        success_window = tk.Toplevel(self.root)
        success_window.title("Login Successful")
        success_window.geometry("300x200")
        success_window.configure(bg='#27ae60')
        
        ttk.Label(success_window, text="🎉 LOGIN SUCCESSFUL!", 
                 font=('Arial', 14, 'bold'), background='#27ae60', 
                 foreground='white').pack(pady=30)
                 
        ttk.Label(success_window, text="User logged in", 
                 font=('Arial', 12), background='#27ae60', 
                 foreground='white').pack(pady=10)
        
        ttk.Button(success_window, text="Continue", 
                  command=lambda: [success_window.destroy(), self.root.quit()]).pack(pady=20)
        
    def login_failed(self, username_attempt, password_attempt):
        error_msg = ""
        
        if username_attempt != self.username:
            error_msg = "❌ Incorrect username"
            self.log_activity("wrong username")
        elif password_attempt != self.password:
            error_msg = "❌ Incorrect password"
            self.log_activity("wrong password")
            
        self.status_label.config(text=error_msg, foreground='#e74c3c')
        self.attempts_label.config(text=f"Attempts: {self.attempts}/{self.max_attempts}")
        
        # Clear password field
        self.login_pass_entry.delete(0, tk.END)
        
        if self.attempts >= self.max_attempts:
            self.status_label.config(text="🔒 Account locked! Too many failed attempts.", foreground='#e74c3c')
            messagebox.showerror("Security Lock", "Maximum login attempts reached!\nThe system will now exit.")
            self.root.after(2000, self.root.quit)
            
    def log_activity(self, action):
        # Simulate logging activity
        print(f"Security log: {action} at attempt {self.attempts}")
        
    def reset_system(self):
        if messagebox.askyesno("Reset System", "Are you sure you want to reset the system?\nThis will clear all credentials."):
            self.username = ""
            self.password = ""
            self.attempts = 0
            self.create_setup_screen()

def main():
    root = tk.Tk()
    app = LoginSystem(root)
    root.mainloop()

if __name__ == "__main__":
    main()