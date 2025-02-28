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
            # Debugging output
            print(f"Checking node: {ast.dump(node)}")

            # Detect 'sleep' call that could cause blocking
            if isinstance(node, ast.Call):
                # Check if the function is a 'sleep' call from the 'time' module
                if isinstance(node.func, ast.Attribute) and isinstance(node.func.value, ast.Name):
                    if node.func.value.id == "time" and node.func.attr == "sleep":
                        self.issues.append({
                            "issue": "Blocking operation detected (sleep call)",
                            "line": node.lineno
                        })

    def detect_division_by_zero(self):
        """Detect potential division by zero errors."""
        for node in ast.walk(self.tree):
            # Look for division operations
            if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div):
                # Check if the right side of division is a zero literal
                if isinstance(node.right, ast.Constant) and node.right.value == 0:
                    self.issues.append({
                        "issue": "Division by zero detected",
                        "line": node.lineno
                    })

    def detect_invalid_addition(self):
        """Detect invalid addition between incompatible types (e.g., int + str)."""
        for node in ast.walk(self.tree):
            # Look for addition operations
            if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
                # Check the types of the left and right operands
                if isinstance(node.left, ast.Constant) and isinstance(node.right, ast.Constant):
                    if isinstance(node.left.value, int) and isinstance(node.right.value, str):
                        self.issues.append({
                            "issue": "Potential type error: adding int and str",
                            "line": node.lineno
                        })

    def analyze(self):
        """Run all analysis checks."""
        self.detect_memory_issues()
        self.detect_blocking_operations()
        self.detect_division_by_zero()
        self.detect_invalid_addition()
        return json.dumps(self.issues, indent=4)

if __name__ == "__main__":
    test_code = """
x = 10
y = 0  # Division by zero will occur here
result = x / y

a = 5
b = "10"  # Invalid addition of int and string
result2 = a + b
    """
    analyzer = StaticAnalyzer(test_code)
    print(analyzer.analyze())
