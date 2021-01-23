import struct

#Manage files
file = input('Enter Filename: ')
output = open(file+'.lua','w')
try:
    pnach = open(file,'r')
except:
    pnach = open(file+'.pnach','r')

#Write some syntaxes
output.write('function _OnInit()\nend\n\nfunction _OnFrame()\n')

#Parse the lines into lua syntax
cond = [] #Check the end of the conditional
skip = False #Check if the next line is part of the current code
def parse(linenum):
    global skip
    line = lines[linenum].strip().upper()
    line = line[0:37]
    code = line[11]
    if code == '0':
        address = line[12:19]
        value   = line[35:37]
        lua = 'WriteByte(0x'+address+',0x'+value+')'
    elif code == '1':
        address = line[12:19]
        value   = line[33:37]
        lua = 'WriteShort(0x'+address+',0x'+value+')'
    elif code == '2':
        address = line[12:19]
        value   = line[29:37]
        lua = 'WriteInt(0x'+address+',0x'+value+')'
    elif code == '3':
        code2   = line[13]
        address = line[30:37]
        if code2 == '0':
            value = line[17:19]
            lua   = 'WriteByte(0x'+address+',ReadByte(0x'+address+')+0x'+value+')'
        elif code2 == '1':
            value = line[17:19]
            lua   = 'WriteByte(0x'+address+',ReadByte(0x'+address+')-0x'+value+')'
        elif code2 == '2':
            value = line[15:19]
            lua   = 'WriteShort(0x'+address+',ReadShort(0x'+address+')+0x'+value+')'
        elif code2 == '3':
            value = line[15:19]
            lua   = 'WriteShort(0x'+address+',ReadShort(0x'+address+')-0x'+value+')'
        elif code2 == '4':
            value = lines[linenum+1].strip().upper()[11:19]
            lua   = 'WriteInt(0x'+address+',ReadInt(0x'+address+')+0x'+value+')'
            skip  = True
        elif code2 == '5':
            value = lines[linenum+1].strip().upper()[11:19]
            lua   = 'WriteInt(0x'+address+',ReadInt(0x'+address+')-0x'+value+')'
            skip  = True
    elif code == '4':
        address   = line[12:19]
        value     = lines[linenum+1].strip().upper()[11:19]
        repeat    = int(line[29:33],16) - 1
        increment = int(line[33:37],16) * 4
        lua = 'for i = 0,'+str(repeat)+' do WriteInt(0x'+address+'+i*'+str(increment)+',0x'+value+') end'
        skip = True
    elif code == '5':
        oldaddress = line[12:19]
        newaddress = lines[linenum+1].strip().upper()[12:19]
        numofbytes = int(line[29:37],16) - 1
        lua  = 'for i = 0,'+str(numofbytes)+' do WriteByte(0x'+newaddress+'+i,ReadByte(0x'+oldaddress+'+i)) end'
        skip = True
    elif code == '6':
        value   = line[29:37]
        pointer = line[12:19]
        offset  = lines[linenum+1].strip().upper()[29:37]
        code2   = lines[linenum+1].strip().upper()[14]
        if code2 == '0':
            lua = 'WriteByte(ReadInt(0x'+pointer+')+0x'+offset+',0x'+value+')'
        if code2 == '1':
            lua = 'WriteShort(ReadInt(0x'+pointer+')+0x'+offset+',0x'+value+')'
        if code2 == '2':
            lua = 'WriteInt(ReadInt(0x'+pointer+')+0x'+offset+',0x'+value+')'
        skip = True
    elif code == 'D':
        code2   = line[31]
        address = line[12:19]
        value   = line[33:37]
        if code2 == '0':
            op = '=='
        elif code2 == '1':
            op = '~='
        elif code2 == '2':
            op = '<'
        elif code2 == '3':
            op = '>'
        lua = 'if ReadShort(0x'+address+') '+op+' 0x'+value+' then'
        cond.append(linenum + 1 + 1)
    elif code == 'E':
        code2   = line[12]
        code3   = line[29]
        address = line[30:37]
        length  = int(line[13:15],16)
        if code3 == '0':
            op = '=='
        elif code3 == '1':
            op = '~='
        elif code3 == '2':
            op = '<'
        elif code3 == '3':
            op = '>'
        if code2 == '0':
            value = line[15:19]
            lua   = 'if ReadShort(0x'+address+') '+op+' 0x'+value+' then'
        elif code2 == '1':
            value = line[17:19]
            lua   = 'if ReadByte(0x'+address+') '+op+' 0x'+value+' then'
        cond.append(linenum + length + 1)
    else:
        print(str(code))
        lua = ''
    return lua

#Convert the pnach
lines = pnach.readlines()
for linenum in range(len(lines)):

    #Check for end of conditionals
    tab = len(cond) * '\t'
    while linenum in cond:
        cond.remove(linenum)
        tab = len(cond) * '\t' #Reduce the tab
        output.write(tab+'end\n')
    
    line    = lines[linenum].strip().upper() #Strip the line of whitespaces
    comment = line.find('//') #Check for comments

    if line[0:11] == 'PATCH=1,EE,' and line[19:29] == ',EXTENDED,':
        if skip: #This line is part of the previous line of code
            skip = False
        else:
            output.write(tab+parse(linenum))
    elif comment == -1 and line != '': #No comments and line isn't empty.
        print('Found a typo: '+line)

    if comment != -1: #Write comments
        output.write('--' + line[comment+2:])
    output.write('\n')

for remainders in range(len(cond)+1):
    output.write('end\n')
pnach.close()
output.close()
