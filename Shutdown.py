import os

print('\033c')

shutdown = input('Do you want to shutdown your OS? (yes / no) : ')

if shutdown == 'yes':
    os.system('shutdown /s /t 1')

else:
    exit()