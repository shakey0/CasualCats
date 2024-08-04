import subprocess
import os
import sys

def start_flask():
  """Start the Flask server."""
  print("Starting Flask server...")
  flask_process = subprocess.Popen([sys.executable, 'run.py'])
  return flask_process

def start_react():
  """Start the React development server."""
  print("Starting React server...")
  os.chdir('frontend')
  react_process = subprocess.Popen(['npm', 'start'])
  return react_process

if __name__ == "__main__":
  flask_process = start_flask()
  react_process = start_react()

  try:
    flask_process.wait()
    react_process.wait()
  except KeyboardInterrupt:
    print("Shutting down servers...")
    flask_process.terminate()
    react_process.terminate()
