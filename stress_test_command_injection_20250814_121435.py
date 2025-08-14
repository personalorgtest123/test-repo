#!/usr/bin/env python3
"""
Command injection vulnerability patterns for security testing.
"""
import os
import subprocess
import shlex


def vulnerable_os_system_0(filename):
    os.system(f"cat {filename}_0")
    os.system(f"ls -la {filename}_0")
    os.system(f"grep pattern {filename}_0")

def vulnerable_subprocess_0(command):
    subprocess.call(f"{command}_0", shell=True)
    subprocess.run(f"{command}_0", shell=True)
    subprocess.Popen(f"{command}_0", shell=True)

def vulnerable_popen_0(filename):
    os.popen(f"find . -name {filename}_0").read()
    os.popen(f"wc -l {filename}_0").read()
    os.popen(f"head -n 10 {filename}_0").read()

def vulnerable_exec_0(code):
    exec(f"print('{code}_0')")
    eval(f"len('{code}_0')")

def vulnerable_os_system_1(filename):
    os.system(f"cat {filename}_1")
    os.system(f"ls -la {filename}_1")
    os.system(f"grep pattern {filename}_1")

def vulnerable_subprocess_1(command):
    subprocess.call(f"{command}_1", shell=True)
    subprocess.run(f"{command}_1", shell=True)
    subprocess.Popen(f"{command}_1", shell=True)

def vulnerable_popen_1(filename):
    os.popen(f"find . -name {filename}_1").read()
    os.popen(f"wc -l {filename}_1").read()
    os.popen(f"head -n 10 {filename}_1").read()

def vulnerable_exec_1(code):
    exec(f"print('{code}_1')")
    eval(f"len('{code}_1')")

def vulnerable_os_system_2(filename):
    os.system(f"cat {filename}_2")
    os.system(f"ls -la {filename}_2")
    os.system(f"grep pattern {filename}_2")

def vulnerable_subprocess_2(command):
    subprocess.call(f"{command}_2", shell=True)
    subprocess.run(f"{command}_2", shell=True)
    subprocess.Popen(f"{command}_2", shell=True)

def vulnerable_popen_2(filename):
    os.popen(f"find . -name {filename}_2").read()
    os.popen(f"wc -l {filename}_2").read()
    os.popen(f"head -n 10 {filename}_2").read()

def vulnerable_exec_2(code):
    exec(f"print('{code}_2')")
    eval(f"len('{code}_2')")

def vulnerable_os_system_3(filename):
    os.system(f"cat {filename}_3")
    os.system(f"ls -la {filename}_3")
    os.system(f"grep pattern {filename}_3")

def vulnerable_subprocess_3(command):
    subprocess.call(f"{command}_3", shell=True)
    subprocess.run(f"{command}_3", shell=True)
    subprocess.Popen(f"{command}_3", shell=True)

def vulnerable_popen_3(filename):
    os.popen(f"find . -name {filename}_3").read()
    os.popen(f"wc -l {filename}_3").read()
    os.popen(f"head -n 10 {filename}_3").read()

def vulnerable_exec_3(code):
    exec(f"print('{code}_3')")
    eval(f"len('{code}_3')")

def vulnerable_os_system_4(filename):
    os.system(f"cat {filename}_4")
    os.system(f"ls -la {filename}_4")
    os.system(f"grep pattern {filename}_4")

def vulnerable_subprocess_4(command):
    subprocess.call(f"{command}_4", shell=True)
    subprocess.run(f"{command}_4", shell=True)
    subprocess.Popen(f"{command}_4", shell=True)

def vulnerable_popen_4(filename):
    os.popen(f"find . -name {filename}_4").read()
    os.popen(f"wc -l {filename}_4").read()
    os.popen(f"head -n 10 {filename}_4").read()

def vulnerable_exec_4(code):
    exec(f"print('{code}_4')")
    eval(f"len('{code}_4')")

def vulnerable_os_system_5(filename):
    os.system(f"cat {filename}_5")
    os.system(f"ls -la {filename}_5")
    os.system(f"grep pattern {filename}_5")

def vulnerable_subprocess_5(command):
    subprocess.call(f"{command}_5", shell=True)
    subprocess.run(f"{command}_5", shell=True)
    subprocess.Popen(f"{command}_5", shell=True)

def vulnerable_popen_5(filename):
    os.popen(f"find . -name {filename}_5").read()
    os.popen(f"wc -l {filename}_5").read()
    os.popen(f"head -n 10 {filename}_5").read()

def vulnerable_exec_5(code):
    exec(f"print('{code}_5')")
    eval(f"len('{code}_5')")

def vulnerable_os_system_6(filename):
    os.system(f"cat {filename}_6")
    os.system(f"ls -la {filename}_6")
    os.system(f"grep pattern {filename}_6")

def vulnerable_subprocess_6(command):
    subprocess.call(f"{command}_6", shell=True)
    subprocess.run(f"{command}_6", shell=True)
    subprocess.Popen(f"{command}_6", shell=True)

def vulnerable_popen_6(filename):
    os.popen(f"find . -name {filename}_6").read()
    os.popen(f"wc -l {filename}_6").read()
    os.popen(f"head -n 10 {filename}_6").read()

def vulnerable_exec_6(code):
    exec(f"print('{code}_6')")
    eval(f"len('{code}_6')")

def vulnerable_os_system_7(filename):
    os.system(f"cat {filename}_7")
    os.system(f"ls -la {filename}_7")
    os.system(f"grep pattern {filename}_7")

def vulnerable_subprocess_7(command):
    subprocess.call(f"{command}_7", shell=True)
    subprocess.run(f"{command}_7", shell=True)
    subprocess.Popen(f"{command}_7", shell=True)

def vulnerable_popen_7(filename):
    os.popen(f"find . -name {filename}_7").read()
    os.popen(f"wc -l {filename}_7").read()
    os.popen(f"head -n 10 {filename}_7").read()

def vulnerable_exec_7(code):
    exec(f"print('{code}_7')")
    eval(f"len('{code}_7')")

def vulnerable_os_system_8(filename):
    os.system(f"cat {filename}_8")
    os.system(f"ls -la {filename}_8")
    os.system(f"grep pattern {filename}_8")

def vulnerable_subprocess_8(command):
    subprocess.call(f"{command}_8", shell=True)
    subprocess.run(f"{command}_8", shell=True)
    subprocess.Popen(f"{command}_8", shell=True)

def vulnerable_popen_8(filename):
    os.popen(f"find . -name {filename}_8").read()
    os.popen(f"wc -l {filename}_8").read()
    os.popen(f"head -n 10 {filename}_8").read()

def vulnerable_exec_8(code):
    exec(f"print('{code}_8')")
    eval(f"len('{code}_8')")

def vulnerable_os_system_9(filename):
    os.system(f"cat {filename}_9")
    os.system(f"ls -la {filename}_9")
    os.system(f"grep pattern {filename}_9")

def vulnerable_subprocess_9(command):
    subprocess.call(f"{command}_9", shell=True)
    subprocess.run(f"{command}_9", shell=True)
    subprocess.Popen(f"{command}_9", shell=True)

def vulnerable_popen_9(filename):
    os.popen(f"find . -name {filename}_9").read()
    os.popen(f"wc -l {filename}_9").read()
    os.popen(f"head -n 10 {filename}_9").read()

def vulnerable_exec_9(code):
    exec(f"print('{code}_9')")
    eval(f"len('{code}_9')")
