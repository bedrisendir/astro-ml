#!/usr/bin/env python
import sys
import time
import paramiko
import os
import socket
import datetime
import time
def kill(interval,nodelist,thold_cpu,thold_mem):
    counter = 1
    lines = [line.strip() for line in open(nodelist)]
    while(True):
        for line in lines :
            ts = time.time()
            st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            print st," connecting -",line,"-"
            try:
                ssh.connect(line)
            except socket.error:
                print "Cannot ssh to:",line
                continue
            #sshin,sshout,ssherr = ssh.exec_command("uptime")
            sshin,sshout,ssherr = ssh.exec_command("free | grep Mem")
            mem = sshout.readline().split()
            cur_mem = float(mem[2])/float(mem[1])*100*1.0
            print st," Memory percentage: ",cur_mem
            sshin,sshout,ssherr = ssh.exec_command("top -bn2 | grep Cpu")
            cpu1 = sshout.readline()
            cpu1 = cpu1.split(',')[3].split("%id")[0]
            cpu2 = sshout.readline()
            cpu2 = cpu2.split(',')[3].split("%id")[0]
            cur_cpu= (float(cpu1)+float(cpu2)) / 2.0
            cur_cpu = 100.0-cur_cpu
            print st," Cpu Usage Percentage: ",cur_cpu
            if cur_cpu > thold_cpu or cur_mem > thold_mem:
                print "Kill server"
                print "Thold cpu: ",thold_cpu," Cur cpu:",cur_cpu
                print "Thold mem: ",thold_mem," Cur mem:",cur_mem
                print counter, " iteration"
                counter+=1
        time.sleep(int(interval*2))

kill(int(sys.argv[1]),sys.argv[2],sys.argv[3],sys.argv[4])
