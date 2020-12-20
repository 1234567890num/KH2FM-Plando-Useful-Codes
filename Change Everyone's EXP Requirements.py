import struct
base = [40,100,184,296,
        440,620,840,1128,1492,
        1940,2480,3120,3902,4838,
        5940,7260,8814,10618,12688,
        15088,17838,20949,24433,28302,
        32622,37407,42671,48485,54865,
        61886,69566,77984,87160,97177,
        108057,119887,132691,146560,161520,
        177666,195026,213699,233715,255177,
        278117,302642,328786,356660,386378,
        417978,450378,483578,517578,552378,
        587978,624378,661578,699578,738378,
        777978,818378,859578,901578,944378,
        987978,1032378,1077578,1123578,1170378,
        1217978,1266378,1315578,1365578,1416378,
        1467978,1520378,1573578,1627578,1682378,
        1737978,1794378,1851578,1909578,1968378,
        2027978,2088378,2149578,2211578,2274378,
        2337978,2402378,2467578,2533578,2600378,
        2667978,2736378,2805578,2875578] #Sora's base EXP requirements

def make(name,start):
    output.write('//'+name+'\n')
    output.write('patch=1,EE,E062FFFF,extended,0032BAE0\n')
    print(name)
    
    for a in range(98):
        value   = 13*(a+2)**2.1 #Insert New Formula Here
        value   = round(value)
        #print(a+2, round(base[a]/3) - value) #How Much EXP you saved
        value   = hex(value)[2:]
        value   = value.upper()
        value   = value.zfill(8)
        address = int(start,16) + 16*a
        address = hex(address)[2:]
        address = address.upper()
        output.write('patch=1,EE,'+address+',extended,'+value+'\n')
    output.write('\n')

output = open('New EXP Requirements.pnach','w')
make('Sora','21D0B6A8')
make('Donald','21D0BCDC')
make('Goofy','21D0C310')
make('Mickey','21D0C944')
make('Auron','21D0CF78')
make('Mulan','21D0D5AC')
make('Aladdin','21D0DBE0')
make('Jack Sparrow','21D0E214')
make('Beast','21D0E848')
make('Jack Skellington','21D0EE7C')
make('Simba','21D0F4B0')
make('Tron','21D0FAE4')
make('Riku','21D10118')
output.close()
