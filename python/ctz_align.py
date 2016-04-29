import nuke


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


def alignGrid():
    nodes = nuke.selectedNodes()
    for n in nodes:
        nuke.autoplaceSnap(n)
