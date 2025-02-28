import tkinter as tk
from tkinter import filedialog, scrolledtext
import json
import ast

class StaticAnalyzer:
    def __init__(self, code):
        self.code = code

    def analyze(self): 
        tree = ast.parse(self.code)
        issues = []

        # Traverse the AST to detect issues
        for node in ast.walk(tree):
            # Check for function definitions without docstrings
            if isinstance(node, ast.FunctionDef) and ast.get_docstring(node) is None:
                issues.append({"line": node.lineno, "issue": f"Function '{node.name}' is missing a docstring."})
            
            # Check for assignments of magic methods
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id in ["__init__", "__del__", "__str__"]:
                        issues.append({"line": node.lineno, "issue": f"Magic method '{target.id}' is assigned a value."})
            
            # Check for improper identity comparisons
            if isinstance(node, ast.Compare):
                if isinstance(node.ops[0], ast.Is) or isinstance(node.ops[0], ast.IsNot):
                    issues.append({"line": node.lineno, "issue": "Comparison using 'is' or 'is not' instead of '==' or '!='."})

        return json.dumps(issues, indent=4)  # Convert issues to JSON format

class AnalyzerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Static Code Analyzer")

        # Upload button to load Python file
        self.upload_button = tk.Button(root, text="Upload Python File", command=self.load_file)
        self.upload_button.pack(pady=10)

        # Scrolled text widget to display results
        self.result_area = scrolledtext.ScrolledText(root, width=80, height=20)
        self.result_area.pack(pady=10)

    def load_file(self):
        # Open a file dialog to select a Python file
        filepath = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
        if filepath:
            with open(filepath, "r") as file:
                code = file.read()
                analyzer = StaticAnalyzer(code)
                results = analyzer.analyze()  # Perform static analysis
                print(f"Analysis Results: {results}")  # Debugging output
                self.display_results(results)  # Display the analysis results

    def display_results(self, results):
        # Clear previous results from the display area
        self.result_area.delete(1.0, tk.END)
        
        # Parse the analysis results, which should be in JSON format
        try:
            parsed_results = json.loads(results)
            if parsed_results:
                for issue in parsed_results:
                    self.result_area.insert(tk.END, f"Line {issue['line']}: {issue['issue']}\n")
            else:
                self.result_area.insert(tk.END, "No issues detected.\n")
        except json.JSONDecodeError:
            self.result_area.insert(tk.END, "Error: Unable to parse analysis results.\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = AnalyzerGUI(root)
    root.mainloop()