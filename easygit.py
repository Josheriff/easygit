# -*- coding: utf-8 -*-
import os
repo_status = os.popen("git status --short").read()

#A  .gitignore   <- English version is D not an A
# M command_spike.py
# M easygit.py
# ?? concepto.txt
# ?? git_status_output.log
# ?? spec.py


lines = repo_status.split('\n')

added = []
modified = []
unstagged = []

for line in lines:
    print(line)
    #if line[0] == '?':
       # unstagged.append(line[3:])

print (unstagged)



# from blessings import Terminal
# from pick import pick

# title = 'Please choose the files you want to add (press SPACE to mark, ENTER to continue): '
# options = ['README.MD', 'aFile.js', 'a_python_file.py', 'index.html']
# selected = pick(options, title, multi_select=True, min_selection_count=1)
# print(selected)




