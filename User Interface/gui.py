import tkinter as tk
from tkinter import filedialog, scrolledtext
import json
from static_analyzer import StaticAnalyzer

class AnalyzerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Static Code Analyzer")

        self.upload_button = tk.Button(root, text="Upload Python File", command=self.load_file)
        self.upload_button.pack(pady=10)

        self.result_area = scrolledtext.ScrolledText(root, width=80, height=20)
        self.result_area.pack(pady=10)

    def load_file(self):
        filepath = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
        if filepath:
            with open(filepath, "r") as file:
                code = file.read()
                analyzer = StaticAnalyzer(code)
                results = analyzer.analyze()
                self.display_results(results)

    def display_results(self, results):
        self.result_area.delete(1.0, tk.END)
        parsed_results = json.loads(results)
        if parsed_results:
            for issue in parsed_results:
                self.result_area.insert(tk.END, f"Line {issue['line']}: {issue['issue']}\n")
        else:
            self.result_area.insert(tk.END, "No issues detected.\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = AnalyzerGUI(root)
    root.mainloop()
