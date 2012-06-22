import first
def parse(path = "/home/akarsh/Documents/tmp/config2.conf"):
    f = open(path,"r")
    blocks = first.parse("blocks",f.read()+"\0")
    return blocks
#    for key in blocks:
#	print key,blocks[key],"\n"
