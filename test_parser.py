import first
f = open("/home/akarsh/Documents/tmp/config.conf","r")
first.parse("blocks",f.read()+"\0")