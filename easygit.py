from pick import pick

title = 'Please choose the files you want to add (press SPACE to mark, ENTER to continue): '
options = ['README.MD', 'aFile.js', 'a_python_file.py', 'index.html']
selected = pick(options, title, multi_select=True, min_selection_count=1)
print(selected)
