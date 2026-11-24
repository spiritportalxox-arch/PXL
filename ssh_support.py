import subprocess

def setup_ssh_key(key):
    subprocess.run(["ssh-add", "-k", key])
    print("SSH key added.")
