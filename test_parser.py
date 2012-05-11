import first
def parse():
    f = open("/home/akarsh/Documents/tmp/config2.conf","r")
    blocks = first.parse("blocks",f.read()+"\0")
    return blocks
#    for key in blocks:
#	print key,blocks[key],"\n"
