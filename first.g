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
    token name: "[^\n\t \{\}\0]+"
    token key: "[^\n\t \{\}]+"
    token value: "[^\n\t\{\}]+"
    token eof: "\0"
    token sp: "[ ]"
    rule blocks:(block<<{}>>|comment)* eof {{return global_vars}}
    rule block<<D>>: (name
                OB  
                (key {{key = key}}
                    (
                    (OB subblock<<{}>> CB{{D[key] = subblock}})
                    |
                    (value {{D[key] = value.lstrip()}})
                    )
                )*
                CB {{global_vars[name] = D;#print i}})
    rule subblock<<V>>: (name value{{V[name] = value.lstrip()}})* {{return (V)}}
    
    rule comment: "##.+"
