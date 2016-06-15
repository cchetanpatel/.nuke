import os
import platform
import subprocess
import nuke

print


def open_file(path):
    if platform.system() == "Windows":
        os.startfile(path)
    elif platform.system() == "Darwin":
        subprocess.Popen(["open", path])
    else:
        subprocess.Popen(["xdg-open", path])


def open_main():
    try:
        node = nuke.selectedNode()
        if node:
            if node["file"]:
                dir = os.path.dirname(node["file"].value())
                if os.path.exists(dir):
                    open_file(dir)
                else:
                    print "Directory does not exist"
    except ValueError:
        print "No node Selected"




