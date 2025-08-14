#!/usr/bin/env python3
"""
Command injection vulnerability patterns for security testing - 30 findings.
"""
import os
import subprocess
import shlex


def vulnerable_os_system_0(filename):
    os.system(f"cat {filename}_0")
    os.system(f"ls -la {filename}_0")

def vulnerable_subprocess_0(command):
    subprocess.call(f"{command}_0", shell=True)
    subprocess.run(f"{command}_0", shell=True)

def vulnerable_popen_0(filename):
    os.popen(f"find . -name {filename}_0").read()

def vulnerable_os_system_1(filename):
    os.system(f"cat {filename}_1")
    os.system(f"ls -la {filename}_1")

def vulnerable_subprocess_1(command):
    subprocess.call(f"{command}_1", shell=True)
    subprocess.run(f"{command}_1", shell=True)

def vulnerable_popen_1(filename):
    os.popen(f"find . -name {filename}_1").read()

def vulnerable_os_system_2(filename):
    os.system(f"cat {filename}_2")
    os.system(f"ls -la {filename}_2")

def vulnerable_subprocess_2(command):
    subprocess.call(f"{command}_2", shell=True)
    subprocess.run(f"{command}_2", shell=True)

def vulnerable_popen_2(filename):
    os.popen(f"find . -name {filename}_2").read()

def vulnerable_os_system_3(filename):
    os.system(f"cat {filename}_3")
    os.system(f"ls -la {filename}_3")

def vulnerable_subprocess_3(command):
    subprocess.call(f"{command}_3", shell=True)
    subprocess.run(f"{command}_3", shell=True)

def vulnerable_popen_3(filename):
    os.popen(f"find . -name {filename}_3").read()

def vulnerable_os_system_4(filename):
    os.system(f"cat {filename}_4")
    os.system(f"ls -la {filename}_4")

def vulnerable_subprocess_4(command):
    subprocess.call(f"{command}_4", shell=True)
    subprocess.run(f"{command}_4", shell=True)

def vulnerable_popen_4(filename):
    os.popen(f"find . -name {filename}_4").read()

def vulnerable_os_system_5(filename):
    os.system(f"cat {filename}_5")
    os.system(f"ls -la {filename}_5")

def vulnerable_subprocess_5(command):
    subprocess.call(f"{command}_5", shell=True)
    subprocess.run(f"{command}_5", shell=True)

def vulnerable_popen_5(filename):
    os.popen(f"find . -name {filename}_5").read()

def vulnerable_os_system_6(filename):
    os.system(f"cat {filename}_6")
    os.system(f"ls -la {filename}_6")

def vulnerable_subprocess_6(command):
    subprocess.call(f"{command}_6", shell=True)
    subprocess.run(f"{command}_6", shell=True)

def vulnerable_popen_6(filename):
    os.popen(f"find . -name {filename}_6").read()

def vulnerable_os_system_7(filename):
    os.system(f"cat {filename}_7")
    os.system(f"ls -la {filename}_7")

def vulnerable_subprocess_7(command):
    subprocess.call(f"{command}_7", shell=True)
    subprocess.run(f"{command}_7", shell=True)

def vulnerable_popen_7(filename):
    os.popen(f"find . -name {filename}_7").read()

def vulnerable_os_system_8(filename):
    os.system(f"cat {filename}_8")
    os.system(f"ls -la {filename}_8")

def vulnerable_subprocess_8(command):
    subprocess.call(f"{command}_8", shell=True)
    subprocess.run(f"{command}_8", shell=True)

def vulnerable_popen_8(filename):
    os.popen(f"find . -name {filename}_8").read()

def vulnerable_os_system_9(filename):
    os.system(f"cat {filename}_9")
    os.system(f"ls -la {filename}_9")

def vulnerable_subprocess_9(command):
    subprocess.call(f"{command}_9", shell=True)
    subprocess.run(f"{command}_9", shell=True)

def vulnerable_popen_9(filename):
    os.popen(f"find . -name {filename}_9").read()
