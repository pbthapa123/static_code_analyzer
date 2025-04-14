import tkinter as tk
from tkinter import filedialog, scrolledtext
import json
import ast

class StaticAnalyzer:
    def __init__(self, code):
        self.code = code
        self.tree = ast.parse(code)
        self.issues = []

    def detect_memory_issues(self):
        for node in ast.walk(self.tree):
            if isinstance(node, ast.ListComp):
                self.issues.append({
                    "issue": "Inefficient memory usage detected (List comprehension)",
                    "line": node.lineno
                })
            elif isinstance(node, ast.SetComp):
                self.issues.append({
                    "issue": "Inefficient memory usage detected (Set comprehension)",
                    "line": node.lineno
                })

    def detect_blocking_operations(self):
        for node in ast.walk(self.tree):
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Attribute) and isinstance(node.func.value, ast.Name):
                    if node.func.value.id == "time" and node.func.attr == "sleep":
                        self.issues.append({
                            "issue": "Blocking operation detected (sleep call)",
                            "line": node.lineno
                        })

    def detect_variable_type_reassignment(self):
        variable_types = {}
        for node in ast.walk(self.tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        var_name = target.id
                        new_type = type(node.value).__name__
                        if var_name in variable_types and variable_types[var_name] != new_type:
                            self.issues.append({
                                "issue": f"Variable '{var_name}' reassigned with different types ({variable_types[var_name]} -> {new_type})",
                                "line": node.lineno
                            })
                        variable_types[var_name] = new_type

    def detect_large_loops(self):
        for node in ast.walk(self.tree):
            if isinstance(node, ast.For):
                if isinstance(node.iter, ast.Call) and isinstance(node.iter.func, ast.Name) and node.iter.func.id == 'range':
                    args = node.iter.args
                    if len(args) == 1 and isinstance(args[0], ast.Constant):
                        if args[0].value > 100000:
                            self.issues.append({
                                "issue": f"Large loop detected with {args[0].value} iterations",
                                "line": node.lineno
                            })
                    elif len(args) == 2 and isinstance(args[0], ast.Constant) and isinstance(args[1], ast.Constant):
                        if args[1].value - args[0].value > 100000:
                            self.issues.append({
                                "issue": f"Large loop detected with {args[1].value - args[0].value} iterations",
                                "line": node.lineno
                            })

    def detect_unreachable_code(self):
        unreachable = False
        for node in ast.walk(self.tree):
            if isinstance(node, (ast.Return, ast.Break, ast.Continue)):
                unreachable = True
            elif unreachable and isinstance(node, ast.Expr):
                self.issues.append({
                    "issue": "Unreachable code detected after return/break/continue",
                    "line": node.lineno
                })

    def detect_unnecessary_try_except(self):
        for node in ast.walk(self.tree):
            if isinstance(node, ast.Try):
                if not node.body and node.handlers:
                    self.issues.append({
                        "issue": "Unnecessary try-except block with no body",
                        "line": node.lineno
                    })

    def detect_missing_docstrings(self):
        for node in ast.walk(self.tree):
            if isinstance(node, ast.FunctionDef) and ast.get_docstring(node) is None:
                self.issues.append({
                    "line": node.lineno,
                    "issue": f"Function '{node.name}' is missing a docstring."
                })

    def detect_magic_method_assignment(self):
        for node in ast.walk(self.tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id in ["__init__", "__del__", "__str__"]:
                        self.issues.append({
                            "line": node.lineno,
                            "issue": f"Magic method '{target.id}' is assigned a value."
                        })

    def detect_identity_comparison(self):
        for node in ast.walk(self.tree):
            if isinstance(node, ast.Compare):
                if isinstance(node.ops[0], (ast.Is, ast.IsNot)):
                    self.issues.append({
                        "line": node.lineno,
                        "issue": "Comparison using 'is' or 'is not' instead of '==' or '!='."
                    })

    def analyze(self):
        self.detect_memory_issues()
        self.detect_blocking_operations()
        self.detect_variable_type_reassignment()
        self.detect_large_loops()
        self.detect_unreachable_code()
        self.detect_unnecessary_try_except()
        self.detect_missing_docstrings()
        self.detect_magic_method_assignment()
        self.detect_identity_comparison()
        return json.dumps(self.issues, indent=4)


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
