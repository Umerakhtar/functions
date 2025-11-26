import tkinter as tk
from tkinter import ttk, messagebox

class GradingSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Grading System")
        self.root.geometry("500x400")
        self.root.configure(bg='#f0f0f0')
        
        # Set style
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('TLabel', background='#f0f0f0', font=('Arial', 11))
        self.style.configure('TButton', font=('Arial', 10))
        self.style.configure('Header.TLabel', font=('Arial', 16, 'bold'), foreground='#2c3e50')
        
        self.create_widgets()
        
    def create_widgets(self):
        # Header
        header_frame = ttk.Frame(self.root)
        header_frame.pack(pady=20)
        
        ttk.Label(header_frame, text="🎓 Student Grading System", style='Header.TLabel').pack()
        
        # Input Frame
        input_frame = ttk.Frame(self.root)
        input_frame.pack(pady=30)
        
        ttk.Label(input_frame, text="Enter your marks (0-100):").grid(row=0, column=0, padx=10, pady=10, sticky='w')
        
        self.marks_entry = ttk.Entry(input_frame, font=('Arial', 12), width=10)
        self.marks_entry.grid(row=0, column=1, padx=10, pady=10)
        self.marks_entry.bind('<Return>', self.calculate_grade)  # Enter key to submit
        
        # Buttons Frame
        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=10)
        
        ttk.Button(button_frame, text="Calculate Grade", command=self.calculate_grade).grid(row=0, column=0, padx=5)
        ttk.Button(button_frame, text="Clear", command=self.clear_fields).grid(row=0, column=1, padx=5)
        ttk.Button(button_frame, text="Exit", command=self.root.quit).grid(row=0, column=2, padx=5)
        
        # Results Frame
        results_frame = ttk.Frame(self.root)
        results_frame.pack(pady=30)
        
        ttk.Label(results_frame, text="Grade Result:", font=('Arial', 12, 'bold')).pack()
        
        self.result_label = ttk.Label(results_frame, text="", font=('Arial', 24, 'bold'), foreground='#2c3e50')
        self.result_label.pack(pady=10)
        
        # Grading Scale Frame
        scale_frame = ttk.LabelFrame(self.root, text="Grading Scale", padding=10)
        scale_frame.pack(pady=20, padx=20, fill='x')
        
        scale_text = """90-100: A+ (Excellent)
80-89:  B+ (Very Good)
70-79:  C+ (Good)
60-69:  D+ (Satisfactory)
0-59:   F  (Fail)"""
        
        scale_label = ttk.Label(scale_frame, text=scale_text, font=('Arial', 10), justify='left')
        scale_label.pack()
        
    def calculate_grade(self, event=None):
        try:
            marks = self.marks_entry.get().strip()
            
            if not marks:
                messagebox.showwarning("Input Error", "Please enter marks!")
                return
                
            mks = float(marks)
            
            if mks < 0 or mks > 100:
                messagebox.showerror("Input Error", "Marks must be between 0 and 100!")
                return
                
            # Grade calculation
            if mks >= 90:
                grade = "A+"
                color = "#27ae60"  # Green
                message = "Excellent! 🎉"
            elif mks >= 80:
                grade = "B+"
                color = "#2980b9"  # Blue
                message = "Very Good! 👍"
            elif mks >= 70:
                grade = "C+"
                color = "#f39c12"  # Orange
                message = "Good! 👌"
            elif mks >= 60:
                grade = "D+"
                color = "#e67e22"  # Dark Orange
                message = "Satisfactory! ✅"
            else:
                grade = "F"
                color = "#e74c3c"  # Red
                message = "Needs Improvement! 📚"
            
            # Display result
            result_text = f"{grade}\n{message}"
            self.result_label.configure(text=result_text, foreground=color)
            
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number!")
            
    def clear_fields(self):
        self.marks_entry.delete(0, tk.END)
        self.result_label.configure(text="")

def main():
    root = tk.Tk()
    app = GradingSystem(root)
    root.mainloop()

if __name__ == "__main__":
    main()