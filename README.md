# Project: Static Code Analyzer

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Version](https://img.shields.io/badge/version-1.0.0-green.svg)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)

## Description
The **Static Code Analyzer** is a Python-based tool designed to analyze source code and detect code smells, inefficiencies, and potential issues. It helps developers improve code quality by providing structured insights based on predefined analysis rules.

## Purpose & Value
- **Ensure high-quality code** by detecting code smells and highlighting problematic areas.
- **Assist developers** in maintaining clean, efficient, and readable code.
- **Supports AI-assisted code reviews** (planned) by integrating machine learning for deeper analysis.

## Primary Functionalities
- **GUI Interface:** `gui.py` handles the user interface, allowing users to upload Python files easily.
- **Static Analysis Engine:** `static_analyzer.py` examines the uploaded code, identifying memory inefficiencies and blocking operations.
- **Smooth Workflow:** The GUI seamlessly integrates with the analysis engine, displaying results in an intuitive interface.

## Technologies Used
- **Python** – Core programming language
- **Tkinter** – For a user-friendly GUI
- **Machine Learning** *(optional)* – For advanced code smell detection (if time allows)

## Setup Instructions

To get started with the Static Code Analyzer, follow these steps:

1. **Clone the Repository**
   git clone https://github.com/pbthapa123/static_code_analyzer.git
   cd static_code_analyzer

2. **Install the Dependencies**
    pip install -r requirements.txt

3. **Run the application**
    python gui.py


## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
