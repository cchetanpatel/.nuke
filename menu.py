###### This is where you put your graphic user interface (GUI) customisations ######



### import Python scripts and/or Python Modules - i.e.:    import myPythonScript
import nuke
import Victor_Toolset
import mari_bridge
import SearchReplacePanel
import createExrCamVray
import ctz_slash_switcher
import file_switcher
import open_folder
import ctz_cmd_render
import chet_utils
import VectorTracker
import animatedSnap3D



# method to add Frank Rueters Search and Replace panel
def addSRPanel():
	myPanel = SearchReplacePanel.SearchReplacePanel()
	return myPanel.addToPane()

nuke.menu('Pane').addCommand('SearchReplace', addSRPanel)
nukescripts.registerPanel('com.ohufx.SearchReplace', addSRPanel)
		
### add favourite directories
nuke.addFavoriteDir ('Current Script', 
	'[file dirname [value root.name]]', 
	nuke.IMAGE | nuke.SCRIPT, 
	icon='script_folder.png')

### add format resolutions presets - i.e.:    nuke.addFormat ('1920 797 0 0 1920 797 1.0 FullHD_Widescreen')
nuke.addFormat ('1920 797 0 0 1920 797 1.0 FullHD_Widescreen')

### add LUT to the Root - i.e.:    nuke.root().knob('luts').addCurve('nameOfTheLUT', 'formula')    # sLOG formula example: '{pow(10.0, ((t - 0.616596 - 0.03) /0.432699)) - 0.037584}'

### customise menu items from Nodes toolbar - i.e. Shuffle hotkey 'J':    nuke.menu('Nodes').addCommand('Channel/Shuffle', 'nuke.createNode("Shuffle")', 'j', icon='Shuffle.png')
### set hotkey for an existing menu item - i.e. Shuffle hotkey 'J':    nuke.menu('Nodes').findItem('Channel').findItem('Shuffle').setShortcut('j')
nuke.menu('Nodes').addCommand('Channel/Shuffle', 'nuke.createNode("Shuffle")', 'shift+j')
nuke.menu('Nodes').addCommand('Other/Backdrop', 'nukescripts.autoBackdrop()', 'shift+b')
 

### customise node default value - i.e.:    nuke.knobDefault('myNode.myKnob', 'myDefaultValue' )

m = menubar.addMenu("V-Ray")
m.addCommand("Create Camera from EXR", "createExrCamVray.createExrCamVray(nuke.selectedNode())")
 
### add menu item to existing Nuke menu - i.e.:    nodeMenu = nuke.menu('Nuke').findItem('Edit/Node').addCommand('myMenuElement', 'myPythonScript.myFunction()', 'myHotkey')    # Modifiers: Shift= shift+, Alt/Option = alt+, Control/Command = ctrl+
nuke.menu("Nuke").addCommand('Chetan/VectorTracker', "nuke.createNode('VectorTracker.gizmo')")
nuke.menu('Nuke').addCommand('Chetan/Preset Backdrop', 'Victor_Toolset.presetBackdrop()', 'alt+ctrl+b')
nuke.menu('Nuke').addCommand('Chetan/ctz Align Row', 'chet_utils.alignRow()')
nuke.menu('Nuke').addCommand('Chetan/ctz Align Col', '.chet_utils.alignCol()')
nuke.menu('Nuke').addCommand('Chetan/ctz Align Grid', 'chet_utils.alignGrid()')
nuke.menu('Nuke').addCommand('Chetan/ctz Abs to Rel', 'chet_utils.absToRel()')
nuke.menu('Nuke').addCommand('Chetan/ctz Convert to ReadGeo', 'chet_utils.convertToReadGeo()')
nuke.menu('Nuke').addCommand('Chetan/switcher', 'ctz_slash_switcher.start()')
nuke.menu('Nuke').addCommand('Chetan/File Switcher', 'file_switcher.switch()')
nuke.menu('Nuke').addCommand('Chetan/Open Folder', 'chet_utils.open_main()', 'shift+o')
nuke.menu('Nuke').addCommand('Chetan/Toggle Viewer Inputs', 'chet_utils.toggle_viewer_inputs()', 'alt+t')
nuke.menu('Nuke').addCommand('Chetan/Commandline Render', 'ctz_cmd_render.start()')


### Create a custom menu - i.e.:
# you need a gizmo to be placed in your '.nuke' folder structure
# toolbar = nuke.menu('Nodes')
# myMenu = toolbar.addMenu('myMenuElement', icon='myMenuIcon.png')
# myMenu.addCommand('myElement', 'nuke.createNode("myGizmo")', icon='myGizmoIcon.png', index=0) #the index argument (optional) indicates the position of the item within the menu
toolbar = nuke.menu('Nodes')
myMenu = toolbar.addMenu('cTz', icon='script_folder.png')
myMenu.addCommand('V_EdgeMatte', 'nuke.createNode("V_EdgeMatte")', icon='V_EdgeMatte.png')
myMenu.addCommand('SliceTool', 'nuke.createNode("SliceTool")')
myMenu.addCommand('akromatism_stRub', 'nuke.createNode("akromatism_stRub")')
myMenu.addCommand('lenskernelFFT', 'nuke.createNode("LensKernelFFT_v01")')
myMenu.addCommand('DespillMadness', 'nuke.createNode("DespillMadness")')
myMenu.addCommand('glass', 'nuke.createNode("Glass")')
myMenu.addCommand('P_Matte', 'nuke.createNode("P_Matte")')
myMenu.addCommand('SynthEyesLensDistortion', 'nuke.createNode("SynthEyesLensDistortion")')

### Run a command everytime a node of a specific type is created
# set the value of a new framehold node to the currentframe. 
nuke.addOnUserCreate(lambda:nuke.thisNode()['first_frame'].setValue(nuke.frame()), nodeClass='FrameHold')

# set the label of a new camera to show the current focal length
nuke.addOnUserCreate(lambda:nuke.thisNode()['label'].setValue('F[expr round([value focal])]'), nodeClass='Camera')
nuke.addOnUserCreate(lambda:nuke.thisNode()['label'].setValue('F[expr round([value focal])]'), nodeClass='Camera2')
