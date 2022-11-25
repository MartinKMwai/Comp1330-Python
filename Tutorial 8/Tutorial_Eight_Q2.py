a=input()

b=a.split(',')

for c in b:
    
    d=c.strip()
    
    if d.isnumeric():
        print(int(d), end=' ')
        
    else:
        if d[0]!='0':
            
            d='0' +d
        print(int(d,16),end=' ')
