import commands
print commands.getstatusoutput('git status')

from blessings import Terminal

t = Terminal()
print t.red('This is red.')
print t.bold_bright_red_on_black('Bright red on black')

# PYTHON 3
#import subprocess

#output = subprocess.run("git status", shell=True, stdout=subprocess.PIPE,
#                        universal_newlines=True)
#print('UEEEEEEE', output.stdout,'<<<<<<<')
