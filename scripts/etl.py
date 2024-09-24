import subprocess
import sys
import os

python_executable = sys.executable

def run_script(script_name):
    result = subprocess.run([python_executable, f'{script_name}'], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running {script_name}: {result.stderr}")
    else:
        print(f"Successfully ran {script_name}")

if __name__ == "__main__":
    run_script(os.path.join('scripts', 'extract.py'))
    run_script(os.path.join('scripts', 'transform.py'))
    run_script(os.path.join('scripts', 'load.py'))
