decompile file pyc thấy một chuỗi marshaled bytecode

Dùng xdis để đổi ra python bytecode

    import marshal
    bytecode=b''  #bytecode inserted here
    marshaled=marshal.loads(bytecode)

    import xdis.std as dis
    dis.dis(marshal)
   
Rồi ngồi dịch tay thôi:

out.txt[out.txt](https://github.com/Twi1ight-source/CTF-write-up/files/7491691/out.txt)

+Có một chỗ cần lưu ý: 

       int (chr(k[7]) *2) +1 ==k[9] --> Ex: chr(k[7]) = '5'*2 ='55' -->int('55')=55+1=56 -->k[9]=56

