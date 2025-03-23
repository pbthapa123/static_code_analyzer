import ast
import json

class StaticAnalyzer:
    def __init__(self, code):
        self.tree = ast.parse(code)
        self.issues = []

    def detect_memory_issues(self):
        """Detect inefficient memory allocations (e.g., list comprehensions)."""
        for node in ast.walk(self.tree):
            # Detect list comprehension
            if isinstance(node, ast.ListComp):
                self.issues.append({
                    "issue": "Inefficient memory usage detected (List comprehension)",
                    "line": node.lineno
                })
            # Detect set comprehension
            elif isinstance(node, ast.SetComp):
                self.issues.append({
                    "issue": "Inefficient memory usage detected (Set comprehension)",
                    "line": node.lineno
                })

    def detect_blocking_operations(self):
        """Detect potential real-time constraint violations (e.g., sleep calls)."""
        for node in ast.walk(self.tree):
            # Detect 'sleep' call that could cause blocking
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Attribute) and isinstance(node.func.value, ast.Name):
                    if node.func.value.id == "time" and node.func.attr == "sleep":
                        self.issues.append({
                            "issue": "Blocking operation detected (sleep call)",
                            "line": node.lineno
                        })

    def detect_variable_type_reassignment(self):
        """Detect variables being reassigned with different types."""
        variable_types = {}  # Keeps track of variable types
        for node in ast.walk(self.tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        var_name = target.id
                        if var_name in variable_types:
                            old_type = variable_types[var_name]
                            # Check if the type is changing
                            new_type = type(node.value).__name__
                            if old_type != new_type:
                                self.issues.append({
                                    "issue": f"Variable '{var_name}' reassigned with different types ({old_type} -> {new_type})",
                                    "line": node.lineno
                                })
                        variable_types[var_name] = type(node.value).__name__

    def detect_large_loops(self):
        """Detect large loops that may cause performance issues."""
        for node in ast.walk(self.tree):
            if isinstance(node, ast.For):
                # Check for loop ranges with a large number of iterations
                if isinstance(node.iter, ast.Call) and isinstance(node.iter.func, ast.Name) and node.iter.func.id == 'range':
                    start = node.iter.args[0] if len(node.iter.args) > 0 else None
                    stop = node.iter.args[1] if len(node.iter.args) > 1 else None
                    if isinstance(stop, ast.Constant) and isinstance(start, ast.Constant):
                        if stop.value - start.value > 100000:  # Arbitrary large threshold
                            self.issues.append({
                                "issue": f"Large loop detected with {stop.value - start.value} iterations",
                                "line": node.lineno
                            })

    def detect_unreachable_code(self):
        """Detect unreachable code (e.g., after return, break, or continue)."""
        unreachable = False
        for node in ast.walk(self.tree):
            if isinstance(node, ast.Return) or isinstance(node, ast.Break) or isinstance(node, ast.Continue):
                unreachable = True
            if unreachable and isinstance(node, ast.Expr):
                self.issues.append({
                    "issue": "Unreachable code detected after return/break/continue",
                    "line": node.lineno
                })

    def detect_unnecessary_try_except(self):
        """Detect unnecessary try-except blocks."""
        for node in ast.walk(self.tree):
            if isinstance(node, ast.Try):
                if not node.body and node.handlers:
                    self.issues.append({
                        "issue": "Unnecessary try-except block with no body",
                        "line": node.lineno
                    })

    def analyze(self):
        """Run all analysis checks."""
        self.detect_memory_issues()
        self.detect_blocking_operations()
        self.detect_variable_type_reassignment()
        self.detect_large_loops()
        self.detect_unreachable_code()
        self.detect_unnecessary_try_except()
        return json.dumps(self.issues, indent=4)

if __name__ == "__main__":
    test_code = """
# Example code with various issues

import time

# Inefficient memory usage (list comprehension inside a loop)
x = [i for i in range(100)]

# Blocking operation
time.sleep(5)

# Variable reassigned with different types
y = 5
y = "hello"

# Large loop with constant operations
for i in range(1000000):
    pass

# Unreachable code after return
def example():
    return
    print("This will never be reached")

# Unnecessary try-except block
try:
    pass
except:
    pass
    """
    analyzer = StaticAnalyzer(test_code)
    print(analyzer.analyze())
