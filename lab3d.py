#!/usr/bin/env python3
'''Lab 3 disk space script'''
# Author ID: rashah10

import subprocess

def free_space():
    command_output = subprocess.check_output(['df', '-h']).decode('utf-8')
    root_partition_info = [line for line in command_output.split('\n') if line.endswith('/')][0]
    free_space = root_partition_info.split()[3]
    return free_space.strip()

if __name__ == '__main__':
    print(free_space())