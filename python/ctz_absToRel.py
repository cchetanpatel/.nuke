import nuke
import os


def absToRel():
    try:
        selectedNodes = nuke.selectedNodes('Read')
        selectedNodes.append(nuke.selectedNodes('Write'))
        selectedNodes.append(nuke.selectedNodes('ReadGeo'))
        
        for n in selectedNodes:
            relString = '[file dirname [value root.name]]'
            oldName = n['file'].value()
            if not(relString in oldName):
                scriptName = nuke.scriptName()
                scriptPath = os.path.dirname(scriptName)
                newName = relString + oldName[len(scriptPath):]
                n['file'].setValue(newName)
    except ValueError:
        print ValueError
