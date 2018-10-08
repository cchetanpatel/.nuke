import nuke

listOfNodes = []
def switch():
    g = nuke.createNode("Group" , inpanel =False)
    g.begin()
    input1 = nuke.createNode("Input" , inpanel =False)
    input2 = nuke.createNode("Input" , inpanel =False)
    switch = nuke.createNode("Switch" , inpanel =False)
    switch["name"].setValue("FileSwitch")
    out = nuke.createNode("Output" , inpanel =False)
    switch.setInput(0, input1)
    switch.setInput(1, input2)
    input1["name"].setValue("Local")
    input2["name"].setValue("Server")
    g.end()
    listOfNodes.append(g)
    renameNodes()
    setColor()

def setColor():
    for n in listOfNodes:
	s = n.node("FileSwitch")
	print s
	print s["which"]
 	if s["which"].value() is 0:
	    n["tile_color"].setValue(4278193407)
	else:
	    n["tile_color"].setValue(5308415)

def renameNodes():
    count = 0
    for n in listOfNodes:
	if count is 0:
            n["name"].setValue("LocalServerSwitch")
	else:
	    n["name"].setValue("LocalServerSwitch" + str(count))
	count += 1

def LocalServerSwitchControl():
    if(not nuke.toNode('LocalServerSwitch')):
        ctrl = nuke.createNode('NoOp', inpanel=False)
        ctrl['hide_input'].setValue(1)
        ctrl['name'].setValue('LocalServerSwitch')
        k = nuke.Enumeration_Knob('file_selector', 'File_selector', ['local', 'server'])
        ctrl.addKnob(k)

    nodes = nuke.allNodes('Switch')

    for i in nodes:
        i['which'].setExpression(ctrl['name'].getValue() + '' + '.file_selector')