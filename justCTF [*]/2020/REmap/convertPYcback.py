mapping={64: 1, 9: 2, 71: 3, 60: 4, 54: 5, 56: 6, 52: 9, 26: 10, 78: 11, 27: 12, 81: 15, 70: 16, 88: 17, 12: 19, 4: 20, 68: 22, 29: 23, 11: 24, 17: 25, 67: 26, 84: 27, 86: 28, 23: 29, 76: 50, 82: 51, 19: 52, 10: 53, 59: 54, 50: 55, 65: 56, 79: 57, 6: 59, 3: 60, 28: 61, 25: 62, 16: 63, 62: 64, 85: 65, 75: 66, 73: 67, 72: 68, 83: 69, 22: 70, 2: 71, 73: 72, 5: 73, 1: 75, 53: 76, 20: 77, 63: 78, 57: 79, 66: 81, 55: 82, 89: 83, 15: 84, 24: 85, 61: 86, 77: 87, 51: 88, 69: 89, 125: 90, 136: 91, 106: 92, 98: 93, 144: 94, 126: 95, 95: 96, 156: 97, 110: 98, 97: 100, 155: 101, 91: 102, 154: 103, 153: 104, 133: 105, 132: 106, 115: 107, 108: 108, 94: 109, 102: 110, 158: 111, 103: 112, 150: 113, 130: 114, 131: 115, 113: 116, 93: 122, 141: 124, 137: 125, 114: 126, 111: 130, 122: 131, 96: 132, 124: 133, 161: 135, 147: 136, 142: 137, 112: 138, 107: 141, 138: 142, 145: 143, 116: 145, 151: 146, 152: 147, 146: 148, 109: 144, 101: 149, 157: 150, 92: 151, 148: 152, 104: 153, 160: 154, 149: 155, 105: 156, 100: 157, 143: 158, 90: 160, 135: 161, 163: 162, 162: 163}
import types
import marshal
from pwn import *
import dis

f= open('backup_decryptor.pyc','rb')
magic_bytes=f.read(4)
time_stamp=f.read(12)
code_object=marshal.load(f)

def convert_opcodes(co_code, mapping):
    new_co_code=b""
    for i in range(len(co_code)):
        if i&1:                           #odd byte is constant
            new_co_code+=p8(co_code[i])
        else:                               
            if co_code[i] in mapping:
                new_co_code+=p8(mapping[co_code[i]]) #even byte is opcode
            else:
                new_co_code+=p8(co_code[i])  #if not opcode then it constant
    return new_co_code

def recurse_convert_all(code_obj, mapping) :
    new_co_code = convert_opcodes(code_obj.co_code, mapping)
    new_co_const=[]
    for const in code_obj.co_consts:
        if type(const)== types.CodeType:
            new_const=recurse_convert_all(const, mapping)
            new_co_const.append(new_const)
        else:
            new_co_const.append(const)
    new_code_obj= code_obj.replace(co_code=new_co_code, co_consts=tuple(new_co_const))  #replace
    return new_code_obj

final=recurse_convert_all(code_object, mapping)

fw=open('backup.pyc','wb')
fw.write(b"\x55\x0d\x0d\x0a" + b"\0"*12)  #header + timestamp mapping
marshal.dump(final,fw)


