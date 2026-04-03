import os

print("System Monitoring Tool\n")

print("CPU Info:")
os.system("echo %PROCESSOR_IDENTIFIER%")

print("\nMemory Info:")
os.system("systeminfo | findstr /C:\"Total Physical Memory\"")

print("\nDisk Info:")
os.system("dir")