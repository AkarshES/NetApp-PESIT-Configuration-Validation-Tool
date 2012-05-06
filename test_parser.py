import first
f = open("/home/akarsh/Documents/tmp/config2.conf","r")
blocks = first.parse("blocks",f.read()+"\0")
for key in blocks:
	print key,blocks[key],"\n"
