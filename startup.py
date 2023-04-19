import subprocess
import time
import os
from datetime import datetime

today = str(datetime.now())[:-7]
timeout = 1
user = os.getlogin()

with open('log.txt', 'a') as f:
    f.write('\n{}, User:{}\n'.format(today, user))
    for curr_path in open("proccessList.txt", "r").readlines():
        head, tail = os.path.split(curr_path)
        file_name, file_extension = os.path.splitext(curr_path)
        if(os.path.isfile(curr_path.strip()) == True):
            if file_extension == '.bat':
                os.chdir(head)
                subprocess.Popen(tail, creationflags=subprocess.CREATE_NEW_CONSOLE)
            else:
                try:
                    subprocess.Popen(curr_path.strip())
                    f.write('---{}--- process was called\n'.format(tail.rstrip()))
                except Exception as e: 
                    f.write('---ERROR---{}\n'.format(e))
            time.sleep(timeout)
        else:
            f.write('---{}--- don\'t exist\n'.format(tail.rstrip()))

exit()