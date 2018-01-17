from blessings import Terminal

import commands

repo_status_tuple = commands.getstatusoutput('git status')
repo_status = repo_status_tuple[1]

#start = '/t'
#end = ':'
#result= repo_status[1].split(start)[1].split(end)[0]

#print (result)





#t = Terminal()
#print t.red('This is red.')
#print t.bold_bright_red_on_black('Bright red on black')
