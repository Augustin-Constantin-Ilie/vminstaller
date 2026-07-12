# vm2.py

#Import
import subprocess

# X = Placeholder => Chance to preference 
def install():
    ova = "XX" 
    vm_name = "XX"
    subprocess.run(["VBoxManage", "import", ova, "--vmname", vm_name])
    subprocess.run(["VBoxManage", "modifyvm", vm_name, "--memory", "X"])
    subprocess.run(["VBoxManage", "modifyvm", vm_name, "--macadres1", "auto"]) # I recomend to leave it on auto as it sets a new Mac-Adress 
    subprocess.run(["VBoxManage", "modifyvm", vm_name, "--nic1", "xxx"])
    subprocess.run(["VBoxManage", "modifyvm", vm_name, "--cpus", "x"])
    # subprocess.run(["VBoxManage", "modifyvm", vm_name, "--name", "x"]) Optional

    # Test Output
    if result.returncode == 0:
        print("Success")
    else:
        print("ERROR")