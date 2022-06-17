import platform
print(f"running python {platform.python_version()}")

from pyteal import *

print(Seq(Int(1)))
