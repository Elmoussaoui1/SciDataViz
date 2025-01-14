# SciDataViz

SciDataViz is a Python application for interactive data analysis and visualization.  It combines a rich graphical user interface (GUI) with a command-line interface (CLI) for a complete data science workflow.

## Features

* **Data Import:** Import data from CSV and Excel files into pandas DataFrames.  DataFrames are stored in memory, and the application keeps track of them for later use.
* **DataFrame Editing:**  Open a DataFrame in a dedicated editor window for detailed modifications, updating the underlying DataFrame in memory.  Provides an intuitive way to alter data before analysis or visualization.
* **Interactive Plotting:** Create various plots using Seaborn, a powerful visualization library for Python.  A range of plot types are available, each with customizable options like titles, labels, colors, bin sizes, and more.
* **Dashboard Creation:** Store and organize visualizations in a dashboard view.  Create a PDF export of the dashboard, compiling all selected plots for easy sharing and report generation.
* **Interactive Terminal:**  Run Python code (including custom SciDataViz commands) directly in an interactive terminal window.  A history of commands is available, with features like `ls` for listing variables, `clear` for clearing the terminal, and `quit` to exit the application.
* **Error Handling:** The application includes robust error handling during parsing and execution. Error messages are displayed in the terminal, providing users with informative feedback on any issues that occur.


## Getting Started

**Prerequisites:**

* Python 3.10 or higher
* Required packages: Install the necessary packages listed in `requirements_pip.txt` or `requirements_conda.txt` (depending on your preferred package manager).  This ensures compatibility with the visualization and data manipulation libraries.

