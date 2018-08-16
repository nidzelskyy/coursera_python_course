from mypackage.utils import multiply
import dis
import opcode

print(dir(multiply))

print(multiply.__code__)

print(multiply.__code__.co_code)

print(dis.dis(multiply))

print(opcode.opmap)