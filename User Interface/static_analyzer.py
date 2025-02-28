import ast
import json

class StaticAnalyzer:
    def __init__(self, code):
        self.tree = ast.parse(code)
        self.issues = []

    def detect_memory_issues(self):
        """Detect inefficient memory allocations."""
        for node in ast.walk(self.tree):
            if isinstance(node, ast.ListComp) or isinstance(node, ast.SetComp):
                self.issues.append({
                    "issue": "Inefficient memory usage detected",
                    "line": node.lineno
                })

    def detect_blocking_operations(self):
        """Detect potential real-time constraint violations (e.g., sleep calls)."""
        for node in ast.walk(self.tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                if node.func.id == "sleep":
                    self.issues.append({
                        "issue": "Blocking operation detected (sleep call)",
                        "line": node.lineno
                    })

    def analyze(self):
        """Run all analysis checks."""
        self.detect_memory_issues()
        self.detect_blocking_operations()
        return json.dumps(self.issues, indent=4)

if __name__ == "__main__":
    test_code = """
import time
x = [i for i in range(100)]
time.sleep(5)
    """
    analyzer = StaticAnalyzer(test_code)
    print(analyzer.analyze())
