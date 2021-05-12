import webbrowser
from urllib.parse import urlencode
import subprocess

url = 'https://docs.google.com/forms/d/e/1FAIpQLSf-BfD6zSQ-7WiorOXU26OQXXukicWBgPRzRQNo5tUwJQ40QA/viewform'
doctor_result = subprocess.run(["tilt", "doctor"], capture_output=True)
params = {}
if doctor_result.returncode == 0:
  params['entry.828517829'] = doctor_result.stdout.decode('utf-8')
else:
  params['entry.828517829'] = doctor_result.stderr.decode('utf-8')

# TODO(nick): Ideally this wouls use the UISession API
session_result = subprocess.run(["tilt", "get", "session", "Tiltfile", "-o=yaml"], capture_output=True)
if session_result.returncode == 0:
  params['entry.1953852310'] = session_result.stdout.decode('utf-8')
else:
  params['entry.1953852310'] = session_result.stderr.decode('utf-8')

webbrowser.open('%s?%s' % (url, urlencode(params)))
