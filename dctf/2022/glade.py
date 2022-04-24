

# 'U' -> v14=-1
# 'D' -> v14=1
# 'L' -> v10=-1
# 'R' -> v10=1

# next_func=this+v10*0xdc+v14*0x1c*0xde
fun_trap={
'0x112a':'',
'0x850':'D',
'0x8ef':'L',
'0x98e':'DL',
'0xa26':'U',
'0xac5':'DU',
'0xb5d':'LU',
'0xbf5':'DLU',
'0xc86':'R',
'0xd25':'DR',
'0xdbd':'LR',
'0xe55':'DLR',
'0xee6':'UR',
'0xf7e':'DUR',
'0x100f':'LUR',
'0x10a0':'DULR',
}

# import angr
# proj = angr.Project("./glade", load_options={'auto_load_libs': False})
# cfg = proj.analyses.CFG()
# addrs = list(cfg.kb.functions.keys())
# for i in addrs:
#     print(hex(i),end=", ")

mapping={}
func=[0x40113f, 0x40121b, 0x4012f7, 0x4013d3, 0x4014af, 0x40158b, 0x401667, 0x401743, 0x40181f, 0x4018fb, 0x4019d7, 0x401ab3, 0x401b8f, 0x401c6b, 0x401d47, 0x401e23, 0x401eff, 0x401fdb, 0x4020b7, 0x402193, 0x40226f, 0x40234b, 0x402427, 0x402503, 0x4025df, 0x4026bb, 0x402797, 0x402873, 0x40294f, 0x402a2b, 0x402b07, 0x402be3, 0x402cbf, 0x402d9b, 0x402e77, 0x402f53, 0x40302f, 0x40310b, 0x4031e7, 0x4032c3, 0x40339f, 0x40347b, 0x403557, 0x403633, 0x40370f, 0x4037eb, 0x4038c7, 0x4039a3, 0x403a7f, 0x403b5b, 0x403c37, 0x403d13, 0x403def, 0x403ecb, 0x403fa7, 0x404083, 0x40415f, 0x40423b, 0x404317, 0x4043f3, 0x4044cf, 0x4045ab, 0x404687, 0x404763, 0x40483f, 0x40491b, 0x4049f7, 0x404ad3, 0x404baf, 0x404c8b, 0x404d67, 0x404e43, 0x404f1f, 0x404ffb, 0x4050d7, 0x4051b3, 0x40528f, 0x40536b, 0x405447, 0x405523, 0x4055ff, 0x4056db, 0x4057b7, 0x405893, 0x40596f, 0x405a4b, 0x405b27, 0x405c03, 0x405cdf, 0x405dbb, 0x405e97, 0x405f73, 0x40604f, 0x40612b, 0x406207, 0x4062e3, 0x4063bf, 0x40649b, 0x406577, 0x406653, 0x40672f, 0x40680b, 0x4068e7, 0x4069c3, 0x406a9f, 0x406b7b, 0x406c57, 0x406d33, 0x406e0f, 0x406eeb, 0x406fc7, 0x4070a3, 0x40717f, 0x40725b, 0x407337, 0x407413, 0x4074ef, 0x4075cb, 0x4076a7, 0x407783, 0x40785f, 0x40793b, 0x407a17, 0x407af3, 0x407bcf, 0x407cab, 0x407d87, 0x407e63, 0x407f3f, 0x40801b, 0x4080f7, 0x4081d3, 0x4082af, 0x40838b, 0x408467, 0x408543, 0x40861f, 0x4086fb, 0x4087d7, 0x4088b3, 0x40898f, 0x408a6b, 0x408b47, 0x408c23, 0x408cff, 0x408ddb, 0x408eb7, 0x408f93, 0x40906f, 0x40914b, 0x409227, 0x409303, 0x4093df, 0x4094bb, 0x409597, 0x409673, 0x40974f, 0x40982b, 0x409907, 0x4099e3, 0x409abf, 0x409b9b, 0x409c77, 0x409d53, 0x409e2f, 0x409f0b, 0x409fe7, 0x40a0c3, 0x40a19f, 0x40a27b, 0x40a357, 0x40a433, 0x40a50f, 0x40a5eb, 0x40a6c7, 0x40a7a3, 0x40a87f, 0x40a95b, 0x40aa37, 0x40ab13, 0x40abef, 0x40accb, 0x40ada7, 0x40ae83, 0x40af5f, 0x40b03b, 0x40b117, 0x40b1f3, 0x40b2cf, 0x40b3ab, 0x40b487, 0x40b563, 0x40b63f, 0x40b71b, 0x40b7f7, 0x40b8d3, 0x40b9af, 0x40ba8b, 0x40bb67, 0x40bc43, 0x40bd1f, 0x40bdfb, 0x40bed7, 0x40bfb3, 0x40c08f, 0x40c16b, 0x40c247, 0x40c323, 0x40c3ff, 0x40c4db, 0x40c5b7, 0x40c693, 0x40c76f, 0x40c84b, 0x40c927, 0x40ca03, 0x40cadf, 0x40cbbb, 0x40cc97, 0x40cd73, 0x40ce4f, 0x40cf2b, 0x40d007, 0x40d0e3, 0x40d1bf, 0x40d29b, 0x40d377, 0x40d453, 0x40d52f, 0x40d60b, 0x40d6e7, 0x40d7c3, 0x40d89f, 0x40d97b, 0x40da57, 0x40db33, 0x40dc0f, 0x40dceb, 0x40ddc7, 0x40dea3, 0x40df7f, 0x40e05b, 0x40e137, 0x40e213, 0x40e2ef, 0x40e3cb, 0x40e4a7, 0x40e583, 0x40e65f, 0x40e73b, 0x40e817, 0x40e8f3, 0x40e9cf, 0x40eaab, 0x40eb87, 0x40ec63, 0x40ed3f, 0x40ee1b, 0x40eef7, 0x40efd3, 0x40f0af, 0x40f18b, 0x40f267, 0x40f343, 0x40f41f, 0x40f4fb, 0x40f5d7, 0x40f6b3, 0x40f78f, 0x40f86b, 0x40f947, 0x40fa23, 0x40faff, 0x40fbdb, 0x40fcb7, 0x40fd93, 0x40fe6f, 0x40ff4b, 0x410027, 0x410103, 0x4101df, 0x4102bb, 0x410397, 0x410473, 0x41054f, 0x41062b, 0x410707, 0x4107e3, 0x4108bf, 0x41099b, 0x410a77, 0x410b53, 0x410c2f, 0x410d0b, 0x410de7, 0x410ec3, 0x410f9f, 0x41107b, 0x411157, 0x411233, 0x41130f, 0x4113eb, 0x4114c7, 0x4115a3, 0x41167f, 0x41175b, 0x411837, 0x411913, 0x4119ef, 0x411acb, 0x411ba7, 0x411c83, 0x411d5f, 0x411e3b, 0x411f17, 0x411ff3, 0x4120cf, 0x4121ab, 0x412287, 0x412363, 0x41243f, 0x41251b, 0x4125f7, 0x4126d3, 0x4127af, 0x41288b, 0x412967, 0x412a43, 0x412b1f, 0x412bfb, 0x412cd7, 0x412db3, 0x412e8f, 0x412f6b, 0x413047, 0x413123, 0x4131ff, 0x4132db, 0x4133b7, 0x413493, 0x41356f, 0x41364b, 0x413727, 0x413803, 0x4138df, 0x4139bb, 0x413a97, 0x413b73, 0x413c4f, 0x413d2b, 0x413e07, 0x413ee3, 0x413fbf, 0x41409b, 0x414177, 0x414253, 0x41432f, 0x41440b, 0x4144e7, 0x4145c3, 0x41469f, 0x41477b, 0x414857, 0x414933, 0x414a0f, 0x414aeb, 0x414bc7, 0x414ca3, 0x414d7f, 0x414e5b, 0x414f37, 0x415013, 0x4150ef, 0x4151cb, 0x4152a7, 0x415383, 0x41545f, 0x41553b, 0x415617, 0x4156f3, 0x4157cf, 0x4158ab, 0x415987, 0x415a63, 0x415b3f, 0x415c1b, 0x415cf7, 0x415dd3, 0x415eaf, 0x415f8b, 0x416067, 0x416143, 0x41621f, 0x4162fb, 0x4163d7, 0x4164b3, 0x41658f, 0x41666b, 0x416747, 0x416823, 0x4168ff, 0x4169db, 0x416ab7, 0x416b93, 0x416c6f, 0x416d4b, 0x416e27, 0x416f03, 0x416fdf, 0x4170bb, 0x417197, 0x417273, 0x41734f, 0x41742b, 0x417507, 0x4175e3, 0x4176bf, 0x41779b, 0x417877, 0x417953, 0x417a2f, 0x417b0b, 0x417be7, 0x417cc3, 0x417d9f, 0x417e7b, 0x417f57, 0x418033, 0x41810f, 0x4181eb, 0x4182c7, 0x4183a3, 0x41847f, 0x41855b, 0x418637, 0x418713, 0x4187ef, 0x4188cb, 0x4189a7, 0x418a83, 0x418b5f, 0x418c3b, 0x418d17, 0x418df3, 0x418ecf, 0x418fab, 0x419087, 0x419163, 0x41923f, 0x41931b, 0x4193f7, 0x4194d3, 0x4195af, 0x41968b, 0x419767, 0x419843, 0x41991f, 0x4199fb, 0x419ad7, 0x419bb3, 0x419c8f, 0x419d6b, 0x419e47, 0x419f23, 0x419fff, 0x41a0db, 0x41a1b7, 0x41a293, 0x41a36f, 0x41a44b, 0x41a527, 0x41a603, 0x41a6df, 0x41a7bb, 0x41a897, 0x41a973, 0x41aa4f, 0x41ab2b, 0x41ac07, 0x41ace3, 0x41adbf, 0x41ae9b, 0x41af77, 0x41b053, 0x41b12f, 0x41b20b, 0x41b2e7, 0x41b3c3, 0x41b49f, 0x41b57b, 0x41b657, 0x41b733, 0x41b80f, 0x41b8eb, 0x41b9c7, 0x41baa3, 0x41bb7f, 0x41bc5b, 0x41bd37, 0x41be13, 0x41beef, 0x41bfcb, 0x41c0a7, 0x41c183, 0x41c25f, 0x41c33b, 0x41c417, 0x41c4f3, 0x41c5cf, 0x41c6ab, 0x41c787, 0x41c863, 0x41c93f, 0x41ca1b, 0x41caf7, 0x41cbd3, 0x41ccaf, 0x41cd8b, 0x41ce67, 0x41cf43, 0x41d01f, 0x41d0fb, 0x41d1d7, 0x41d2b3, 0x41d38f, 0x41d46b, 0x41d547, 0x41d623, 0x41d6ff, 0x41d7db, 0x41d8b7, 0x41d993, 0x41da6f, 0x41db4b, 0x41dc27, 0x41dd03, 0x41dddf, 0x41debb, 0x41df97, 0x41e073, 0x41e14f, 0x41e22b, 0x41e307, 0x41e3e3, 0x41e4bf, 0x41e59b, 0x41e677, 0x41e753, 0x41e82f, 0x41e90b, 0x41e9e7, 0x41eac3, 0x41eb9f, 0x41ec7b, 0x41ed57, 0x41ee33, 0x41ef0f, 0x41efeb, 0x41f0c7, 0x41f1a3, 0x41f27f, 0x41f35b, 0x41f437, 0x41f513, 0x41f5ef, 0x41f6cb, 0x41f7a7, 0x41f883, 0x41f95f, 0x41fa3b, 0x41fb17, 0x41fbf3, 0x41fccf, 0x41fdab, 0x41fe87, 0x41ff63, 0x42003f, 0x42011b, 0x4201f7, 0x4202d3, 0x4203af, 0x42048b, 0x420567, 0x420643, 0x42071f, 0x4207fb, 0x4208d7, 0x4209b3, 0x420a8f, 0x420b6b, 0x420c47, 0x420d23, 0x420dff, 0x420edb, 0x420fb7, 0x421093, 0x42116f, 0x42124b, 0x421327, 0x421403, 0x4214df, 0x4215bb, 0x421697, 0x421773, 0x42184f, 0x42192b, 0x421a07, 0x421ae3, 0x421bbf, 0x421c9b, 0x421d77, 0x421e53, 0x421f2f, 0x42200b, 0x4220e7, 0x4221c3, 0x42229f, 0x42237b, 0x422457, 0x422533, 0x42260f, 0x4226eb, 0x4227c7, 0x4228a3, 0x42297f, 0x422a5b, 0x422b37, 0x422c13, 0x422cef, 0x422dcb, 0x422ea7, 0x422f83, 0x42305f, 0x42313b, 0x423217, 0x4232f3, 0x4233cf, 0x4234ab, 0x423587, 0x423663, 0x42373f, 0x42381b, 0x4238f7, 0x4239d3, 0x423aaf, 0x423b8b, 0x423c67, 0x423d43, 0x423e1f, 0x423efb, 0x423fd7, 0x4240b3, 0x42418f, 0x42426b, 0x424347, 0x424423, 0x4244ff, 0x4245db, 0x4246b7, 0x424793, 0x42486f, 0x42494b, 0x424a27, 0x424b03, 0x424bdf, 0x424cbb, 0x424d97, 0x424e73, 0x424f4f, 0x42502b, 0x425107, 0x4251e3, 0x4252bf, 0x42539b, 0x425477, 0x425553, 0x42562f, 0x42570b, 0x4257e7, 0x4258c3, 0x42599f, 0x425a7b, 0x425b57, 0x425c33, 0x425d0f, 0x425deb, 0x425ec7, 0x425fa3, 0x42607f, 0x42615b, 0x426237, 0x426313, 0x4263ef, 0x4264cb, 0x4265a7, 0x426683, 0x42675f, 0x42683b, 0x426917, 0x4269f3, 0x426acf, 0x426bab, 0x426c87, 0x426d63, 0x426e3f, 0x426f1b, 0x426ff7, 0x4270d3, 0x4271af, 0x42728b, 0x427367, 0x427443, 0x42751f, 0x4275fb, 0x4276d7, 0x4277b3, 0x42788f, 0x42796b, 0x427a47, 0x427b23, 0x427bff, 0x427cdb, 0x427db7, 0x427e93, 0x427f6f, 0x42804b, 0x428127, 0x428203, 0x4282df, 0x4283bb, 0x428497, 0x428573, 0x42864f, 0x42872b, 0x428807, 0x4288e3, 0x4289bf, 0x428a9b, 0x428b77, 0x428c53, 0x428d2f, 0x428e0b, 0x428ee7, 0x428fc3, 0x42909f, 0x42917b, 0x429257, 0x429333, 0x42940f, 0x4294eb, 0x4295c7, 0x4296a3, 0x42977f, 0x42985b, 0x429937, 0x429a13, 0x429aef, 0x429bcb, 0x429ca7, 0x429d83, 0x429e5f, 0x429f3b, 0x42a017, 0x42a0f3, 0x42a1cf, 0x42a2ab, 0x42a387, 0x42a463, 0x42a53f, 0x42a61b, 0x42a6f7, 0x42a7d3, 0x42a8af, 0x42a98b, 0x42aa67, 0x42ab43, 0x42ac1f, 0x42acfb, 0x42add7, 0x42aeb3, 0x42af8f, 0x42b06b, 0x42b147, 0x42b223, 0x42b2ff, 0x42b3db, 0x42b4b7, 0x42b593, 0x42b66f, 0x42b74b, 0x42b827, 0x42b903, 0x42b9df, 0x42babb, 0x42bb97, 0x42bc73, 0x42bd4f, 0x42be2b, 0x42bf07, 0x42bfe3, 0x42c0bf, 0x42c19b, 0x42c277, 0x42c353, 0x42c42f, 0x42c50b, 0x42c5e7, 0x42c6c3, 0x42c79f, 0x42c87b, 0x42c957, 0x42ca33, 0x42cb0f, 0x42cbeb, 0x42ccc7, 0x42cda3, 0x42ce7f, 0x42cf5b, 0x42d037, 0x42d113, 0x42d1ef, 0x42d2cb, 0x42d3a7, 0x42d483, 0x42d55f, 0x42d63b, 0x42d717, 0x42d7f3, 0x42d8cf, 0x42d9ab, 0x42da87, 0x42db63, 0x42dc3f, 0x42dd1b, 0x42ddf7, 0x42ded3, 0x42dfaf, 0x42e08b, 0x42e167, 0x42e243, 0x42e31f, 0x42e3fb, 0x42e4d7, 0x42e5b3, 0x42e68f, 0x42e76b, 0x42e847, 0x42e923, 0x42e9ff, 0x42eadb, 0x42ebb7, 0x42ec93, 0x42ed6f, 0x42ee4b, 0x42ef27, 0x42f003, 0x42f0df, 0x42f1bb, 0x42f297, 0x42f373, 0x42f44f, 0x42f52b, 0x42f607, 0x42f6e3, 0x42f7bf, 0x42f89b, 0x42f977, 0x42fa53, 0x42fb2f, 0x42fc0b, 0x42fce7, 0x42fdc3, 0x42fe9f, 0x42ff7b, 0x430057, 0x430133, 0x43020f, 0x4302eb, 0x4303c7, 0x4304a3, 0x43057f, 0x43065b, 0x430737, 0x430813, 0x4308ef, 0x4309cb, 0x430aa7, 0x430b83, 0x430c5f, 0x430d3b, 0x430e17, 0x430ef3, 0x430fcf, 0x4310ab, 0x431187, 0x431263, 0x43133f, 0x43141b, 0x4314f7, 0x4315d3]
fun=[]
for i in func:
    fun.append(i-0x400000)

from capstone import *
from capstone.x86 import *

md=Cs(CS_ARCH_X86,CS_MODE_64)

for i in fun:
    for inss in md.disasm(open('glade','rb').read()[i:0x31677],i):
        if inss.mnemonic=='call':
            mapping[hex(i)]=fun_trap[inss.op_str]
            break


maze=[]
for i in mapping:
    maze.append(mapping[i])
           
    
def walk(maze, x0,y0):
    visited = [0 for i in range(len(maze))]
    q= []
    q.append([x0])
    while (len(q) != 0):
        path = q.pop()
        x = path[-1]
        visited[x] = True
        if (x ==y0):
            return path
        status = maze[x]
        neighbor = []
        if  'L' in status:
            neighbor.append(x+1)
        if  'D' in status:
            neighbor.append(x-30)
        if  'U' in status:
            neighbor.append(x+30)
        if  'R' in status:
            neighbor.append(x-1)
        
        new_path = [path + [x] for x in neighbor if not visited[x]]
        q += new_path

  

b=walk(maze,899,0)
moves=''
for i in range(len(b)):
    if i==len(b)-1:
        break
    if b[i]-b[i+1]==1:
        moves+='R'
    if b[i]-b[i+1]==-1:
        moves+='L'
    
    if b[i]-b[i+1]==30:
        moves+='D'
    
    if b[i]-b[i+1]==-30:
        moves+='U'
 
print(moves[::-1])