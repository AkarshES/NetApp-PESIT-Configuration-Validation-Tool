parser Test:
    ignore: "[ \n]"
    token OB: "{"
    token CB: "}"
    token name: "[a-zA-Z]+"
    token data1: "[^\n\t \{\}]+"
    token data2: "[^\n\t\{\}]+"
    token eof: "\0"
    token sp: "[ ]"
    rule line:  data1 data2 {{return (data1,data2)}}
    rule blocks:(block|comment)* eof
    rule block: name  OB {{i = [(name,'')]}} 
                (name OB subblock<<[]>> CB{{i.append((name,subblock))}}  )*
                (line {{i.append(line)}})*
                CB {{print i}}
    rule subblock<<V>>: (line {{V.append(line)}})* {{return (V)}}
    
    rule comment: "##.+"