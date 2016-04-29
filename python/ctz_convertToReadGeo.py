import os
import nuke

def convertToReadGeo():
    nodes = nuke.selectedNodes()
    extensions = ['.abc', ',obj', '.fbx']

    for node in nodes:
        if node['file']:
            path =  node['file'].value()
            filename = os.path.basename(path)
            ext = os.path.splitext(filename)[-1]
            print ext
            if ext in ext:
                n = nuke.nodes.ReadGeo()
                n['file'].setValue(path)
                nuke.createScenefileBrowser(path, n['name'].value())