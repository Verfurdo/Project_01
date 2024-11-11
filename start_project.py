import os
import subprocess
import sys

# A project.py fájl elérési útjának meghatározása
script_dir = os.path.dirname(os.path.abspath(__file__))  # A jelenlegi fájl könyvtára
project_path = os.path.join(script_dir, 'project', 'project.py')

# A Streamlit alkalmazás indítása
print("Elindítjuk a Streamlit alkalmazást...")
subprocess.run([sys.executable, "-m", "streamlit", "run", project_path])

