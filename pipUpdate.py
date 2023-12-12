from sys import platform
import sys
import os
# from os import path
import subprocess
import pkg_resources
sys.stdout.reconfigure(encoding='utf-8')

file_name = 'requirements.bat'
f_req = 'requirements.txt'
f_req_rewrite = True

if platform == "linux" or platform == "linux2":
    pass
elif platform == "darwin":
    pass
elif platform == "win32":
    if (os.path.exists(file_name)) != True:
        print("no file= ")
        with open(file_name, "w") as req_file:
            req_file.write(".\venv\scripts\pip freeze >  "+f_req)
    if f_req_rewrite:
        output = subprocess.run(file_name).stdout
        try:
            print("Output is {} ".format(str(output)))
        except:
            print("error= ")
    else:
        print("rewrite=OFF")
    my_file = open(f_req, 'r')
    data = my_file.read()
    data = (data.split())

    # print(data)


"""
required = {'mutagen', 'aiogram', 'rtt'}
installed = {pkg.key for pkg in pkg_resources.working_set}

missing = required - installed
for ii in missing:
    print("ii=", ii)

if missing:
    python = sys.executable
    subprocess.check_call(
        # [python, '-m', 'pip', 'install', '--ignore-installed', *missing],  stdout=subprocess.DEVNULL)
        [python, '-m', 'pip', 'install', '--ignore-installed', *missing])
    subprocess.check_call(
        [python, '-m', 'pip', 'install', '--upgrade', 'pip'])
else:
    print('no to update')

# output = subprocess.run(['ping'])
# try:
#    print("Output is {} bytes long.".format(len(output)))
# except:
    print("error")
"""
