#!/usr/bin/env python3
'''Lab 3 Inv 2 function free_space '''
# Author ID: 112379227

import subprocess

def free_space():
    # Run the command as a new process and capture its output
    p = subprocess.Popen("df -h | grep '/$' | awk '{print $4}'",
                         shell=True,
                         stdout=subprocess.PIPE)
    out = p.communicate()[0]          # out is bytes
    text = out.decode('utf-8')        # convert bytes → str (utf-8)
    return text.strip()               # remove newline at the end

if __name__ == '__main__':
    print(free_space())
