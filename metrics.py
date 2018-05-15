#!/usr/bin/env python3
 
from sys import argv
import psutil
 
def proc_metric(tab = ''):
	print(tab + 'system.cpu.idle ', psutil.cpu_times().idle)
	print(tab + 'system.cpu.user ', psutil.cpu_times().user)
	print(tab + 'system.cpu.guest ', psutil.cpu_times().guest)
	print(tab + 'system.cpu.iowait ', psutil.cpu_times().iowait)
	print(tab + 'system.cpu.stolen ', psutil.cpu_times().steal)
	print(tab + 'system.cpu.system ', psutil.cpu_times().system)

def mem_metric(tab = ''):
	print(tab + 'virtual total ', psutil.virtual_memory().total)
	print(tab + 'virtual used ', psutil.virtual_memory().used)
	print(tab + 'virtual free ', psutil.virtual_memory().free)
	print(tab + 'virtual shared ', psutil.virtual_memory().shared)
	print(tab + 'swap total ', psutil.swap_memory().total)
	print(tab + 'swap used ', psutil.swap_memory().used)
	print(tab + 'swap free ', psutil.swap_memory().free)

def all_metric():
	print('CPU Metrics:')
	proc_metric('   ')
	print('Memory Metrics:')
	mem_metric('    ')

def help():
	print("This script display CPU and Memory metrics\n")
	print("Syntax:")
	print(".\metric [cpu\mem\\all]")
	print("	cpu - Display CPU metrics")
	print("	mem - Display Memory metrics")
	print("	all - Display CPU and Memory metrics\n")
	print("Example:")
	print("	.\metric cpu")

try:
	if argv[1] == "cpu":
		proc_metric()
	elif argv[1] == "mem":
		mem_metric()
	elif argv[1] == "all":
		all_metric()
	else:
		help()
except:
	help()
