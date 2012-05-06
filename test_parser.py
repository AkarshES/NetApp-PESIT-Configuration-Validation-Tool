import first
f = open("/home/akarsh/Documents/tmp/config2.conf","r")
first.parse("blocks",f.read()+"\0")
