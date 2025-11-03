import os
import subprocess

result = subprocess.run(
    ["ls","-l","/"],
    check=True,
    capture_output=True,
    text=True,
    timeout=5,
)

print("stdout:", result.stdout)
print("stderr:", result.stderr)
print("return code:", result.returncode)