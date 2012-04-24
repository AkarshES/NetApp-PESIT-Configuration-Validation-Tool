parser Test:
    ignore: "[ \n]"
    token OB: "{"
    token CB: "}"
    token name: "[a-zA-Z]+"
    token data1: "[^\n\t \{\}]+"
    token data2: "[^\n\t\{\}]+"
    token sp: "[ ]"
    rule line:  data1 data2 {{return (data1,data2)}}
    rule block: name  OB {{i = [(name,'')]}} 
                (name OB subblock CB)*
                line* {{i.append(1)}}
                CB {{print i}}
    rule subblock: (line {{print line}})*