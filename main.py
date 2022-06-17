from pyteal import *
# A PyTeal program is composed of expressions
#  by combining expressions we can construct a program with complex behavior

# A Simple program, the value 1 is returned
simple_prog = Return(Int(1))
print("PyTeal Expression Tree:")
print(simple_prog)
print()

# We can compile the PyTeal expression to Teal
teal_prog = compileTeal(simple_prog, mode=Mode.Application, version=6)
print("Teal output:")
print(teal_prog)
print()

# We can then compile the TEAL program to bytecode against an API 
from algosdk.v2client.algod import AlgodClient
token = ""
host = "https://testnet-api.algonode.cloud"
client = AlgodClient(token, host)
result = client.compile(teal_prog)
print("Base64 result of compilation:")
print(result["result"])
print()
print("And same bytecode as hex: ")
import base64
print(base64.b64decode(result["result"]).hex())
print()