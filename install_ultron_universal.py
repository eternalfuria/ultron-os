import os, platform, subprocess
GITHUB_REPO = "https://github.com/EternalFuria/ultron-os.git"
def run_cmd(cmd): subprocess.run(cmd, shell=True, check=True)
def install_linux(path): run_cmd(f"chmod +x {path}/install_ultron.sh"); run_cmd(f"{path}/install_ultron.sh")
def install_windows(path): run_cmd(f"start {path}\\install_ultron.bat")
def main():
    home = os.getcwd(); clone_path = os.path.join(home, "ultron-os")
    if not os.path.exists(clone_path): run_cmd(f"git clone {GITHUB_REPO}")
    os.chdir(clone_path)
    os_name = platform.system(); print(f"Sistema detectado: {os_name}")
    if os_name == "Linux": install_linux(clone_path)
    elif os_name == "Windows": install_windows(clone_path)
    else: print("SO no soportado automáticamente")
if __name__ == "__main__": main()
