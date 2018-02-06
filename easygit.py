# -*- coding: utf-8 -*-
import os
repo_status = os.popen("git status --short").read()

#A  .gitignore
# M command_spike.py
# M easygit.py
# ?? concepto.txt
# ?? git_status_output.log
# ?? spec.py


text = repo_status.split('\n')

print (text)



# from blessings import Terminal
# from pick import pick

# title = 'Please choose the files you want to add (press SPACE to mark, ENTER to continue): '
# options = ['README.MD', 'aFile.js', 'a_python_file.py', 'index.html']
# selected = pick(options, title, multi_select=True, min_selection_count=1)
# print(selected)




