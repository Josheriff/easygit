start = 'asdf=5;'
end = '123jasd'
s = 'asdf=5;Hooray123jasd'
result= s.split(start)[1].split(end)[0]

print result

