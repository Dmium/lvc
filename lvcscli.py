import sys
import os
if len(sys.argv) > 1:
    if sys.argv[1] == "run":
        os.system('runlvcs')
    elif sys.argv[1] == "add":
        pass
    elif sys.argv[1] == "open":
        os.system('google-chrome-stable localhost:8080')
