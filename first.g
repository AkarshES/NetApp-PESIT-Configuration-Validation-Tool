global_vars = {}
def lookup(map, name):
    for x,v in map: 
        if x==name: return v
        return global_vars[name]
%%
parser Test:
    ignore: "[ \n\t]"
    token OB: "{"
    token CB: "}"
    #token data1: "[a-zA-Z]+"
    token name: "[^\n\t \{\}\0]+"
    token key: "[^\n\t \{\}]+"
    token value: "[^\n\t\{\}]+"
    token eof: "\0"
    token sp: "[ ]"
    #rule line<N>>:   data2 {{print data1,data2;return (N,data2)}}
    rule blocks:(block|comment)* eof {{return global_vars}}
    rule block: (name
                OB {{i = []}} 
                (key {{key = key}}
                    (
                    (OB subblock<<{}>> CB{{i.append({key:subblock})}})
                    |
                    (value {{i.append((key,value.lstrip()))}})
                    )
                )*
                CB {{global_vars[name] = i;#print i}})
    rule subblock<<V>>: (name value{{V[name] = value.lstrip()}})* {{return (V)}}
    
    rule comment: "##.+"