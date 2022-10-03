```python
import angr, claripy
target = angr.Project('cryogenics', auto_load_libs=False)
input_len = 15
inp = [claripy.BVS('flag_%d' %i, 8) for i in range(input_len)]
flag = claripy.Concat(*inp + [claripy.BVV(b'\n')])
st = target.factory.full_init_state(args=["./cryogenics"], stdin=flag)
for k in inp:
    st.solver.add(k > 0x20)
    st.solver.add(k < 0x7f)


sm = target.factory.simulation_manager(st)
sm.run()
y = []

for x in sm.deadended:
    if b"Flag" in x.posix.dumps(1):
        print(x.posix.dumps(0))
       
    

# sm.explore(find=0x4005BE)
# print(sm.found[0].solver.eval(flag, cast_to = bytes)) 
```
