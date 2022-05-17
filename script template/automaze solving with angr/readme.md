```python
import angr
import sys
from base64 import b64encode
import csv

w = csv.writer(open("output.csv", "a"))
def solve(binary):
    proj=angr.Project(f'./{binary}')
    state=proj.factory.entry_state(add_options={angr.options.LAZY_SOLVES})
    sim=proj.factory.simgr(state)

    def success(state):
        output=state.posix.dumps(sys.stdout.fileno())
        return b"Well done" in output
    
    def failed(state):
        output=state.posix.dumps(sys.stdout.fileno())
        return b"You have failed" in output

    sim.explore(find=success, avoid=failed)

    if sim.found:
        found=sim.found[0]
        res=(found.posix.dumps(0))
        
    w.writerow([binary,b64encode(res)])

for i in range(5):
    solve(f'{i}.bin')

```
