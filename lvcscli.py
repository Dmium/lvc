import sys
import os
import webbrowser
if len(sys.argv) > 1:
    if sys.argv[1] == "run":
        os.system('runlvcs')
    elif sys.argv[1] == "add":
        pass
    elif sys.argv[1] == "open":
        webbrowser.open('localhost:8080', new=2)
