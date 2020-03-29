def decodeMorse(morse_code):
    import re
    ps1,ps2=0,0
    morse_code=morse_code.strip()
    renhua=""
    #预处理 找到里面所有的三个空格 用*代替
    while(re.search('   ',morse_code)):
        (ps1,ps2)=re.search('   ',morse_code).span()
        morse_code=morse_code[:ps1]+'*'+morse_code[ps2:]
    #再来一次 把一个空格全改为#
    morse_code=morse_code.replace(" ",'#')
    ps1,ps2=0,0
    while (ps2<len(morse_code)):
        if (morse_code[ps2]=='*') | (morse_code[ps2]=='#'):
            tword = morse_code[ps1:ps2]
            renhua+=MORSE_CODE[tword]
            if morse_code[ps2]!='#':
                renhua+=' '
            ps1=ps2+1
        ps2+=1
    tword = morse_code[ps1:]
    renhua+=MORSE_CODE[tword] #最后一个没统计！
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    return renhua
