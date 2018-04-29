import nuke
import os
import platform
import subprocess
import nuke

def absToRel():
    try:
        selectedNodes = nuke.selectedNodes('Read')
        selectedNodes.append(nuke.selectedNodes('Write'))
        selectedNodes.append(nuke.selectedNodes('ReadGeo'))
        
        for n in selectedNodes:
            if n:
                relString = '[file dirname [value root.name]]'
                oldName = n['file'].value()
                if not(relString in oldName):
                    scriptName = nuke.scriptName()
                    scriptPath = os.path.dirname(scriptName)
                    newName = relString + oldName[len(scriptPath):]
                    n['file'].setValue(newName)
    except ValueError:
        print ValueError


def alignRow():
    nodes = nuke.selectedNodes()
    s = nuke.selectedNode()
    yVal = s['ypos'].value()
    for n in nodes:
        n['ypos'].setValue(yVal)


def alignCol():
    nodes = nuke.selectedNodes()
    s = nuke.selectedNode()
    xVal = s['xpos'].value()
    for n in nodes:
        n['xpos'].setValue(xVal)


def toggle_viewer_inputs():
    nodes = nuke.allNodes('Viewer')
    for n in nodes:
        n['hide_input'].setValue(not n['hide_input'].value())


def alignGrid():
    nodes = nuke.selectedNodes()
    for n in nodes:
        nuke.autoplaceSnap(n)

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
                dir = dir.replace(' ', '')
                print dir
                if ']]' in dir:
                    dir = dir.replace('[filedirname[valueroot.name]]', os.path.dirname(nuke.scriptName()))
                if os.path.exists(dir):
                    open_file(dir)
                else:
                    print "Directory does not exist"
    except ValueError:
        print "No node Selected"
