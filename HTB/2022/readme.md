## Indefinite

### Đây là một bài ptrace

Cụ thể là gồm 2 luồng riêng biệt cha và con trong đó cha điều khiển luồng của con

### Hàm tracer (cha)

1. PTRACE_PEEKTEXT

`ptrace(PTRACE_PEEKTEXT/PEEKDATA/PEEKUSER, pid, addr, 0);`

Read 8 bytes at addr


