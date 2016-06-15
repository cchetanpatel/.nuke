###### This is where you put your graphic user interface (GUI) customisations ######



### import Python scripts and/or Python Modules - i.e.:    import myPythonScript
import nuke
import Victor_Toolset
import ctz_align
import ctz_absToRel
import mari_bridge
import SearchReplacePanel
import createExrCamVray
import ctz_convertToReadGeo
import ctz_slash_switcher
import file_switcher

# method to add Frank Rueters Search and Replace panel
def addSRPanel():
        '''Run the panel script and add it as a tab into the pane it is called from'''
        myPanel = SearchReplacePanel.SearchReplacePanel()
        return myPanel.addToPane()
		
### add favourite directories
###nuke.addFavoriteDir ('Test', '/job/Test', nuke.IMAGE | nuke.SCRIPT, tooltip='Test images and Scripts')
###nuke.addFavoriteDir ('Current Script', '[file dirname [value root.name]]', nuke.IMAGE | nuke.SCRIPT, icon='script_folder.png')

### add format resolutions presets - i.e.:    nuke.addFormat ('1920 797 0 0 1920 797 1.0 FullHD_Widescreen')



### add LUT to the Root - i.e.:    nuke.root().knob('luts').addCurve('nameOfTheLUT', 'formula')    # sLOG formula example: '{pow(10.0, ((t - 0.616596 - 0.03) /0.432699)) - 0.037584}'



### customise menu items from Nodes toolbar - i.e. Shuffle hotkey 'J':    nuke.menu('Nodes').addCommand('Channel/Shuffle', 'nuke.createNode("Shuffle")', 'j', icon='Shuffle.png')
### set hotkey for an existing menu item - i.e. Shuffle hotkey 'J':    nuke.menu('Nodes').findItem('Channel').findItem('Shuffle').setShortcut('j')
nuke.menu('Nodes').addCommand('Channel/Shuffle', 'nuke.createNode("Shuffle")', 'shift+j')
nuke.menu('Nodes').addCommand('Other/Backdrop', 'nukescripts.autoBackdrop()', 'shift+b')
 


### customise node default value - i.e.:    nuke.knobDefault('myNode.myKnob', 'myDefaultValue' )

### add pane

m = menubar.addMenu("V-Ray")
m.addCommand("Create Camera from EXR", "createExrCamVray.createExrCamVray(nuke.selectedNode())")
 
#THIS LINE WILL ADD THE NEW ENTRY TO THE PANE MENU
nuke.menu('Pane').addCommand('SearchReplace', addSRPanel)
 
#THIS LINE WILL REGISTER THE PANEL SO IT CAN BE RESTORED WITH LAYOUTS
nukescripts.registerPanel('com.ohufx.SearchReplace', addSRPanel)

### add menu item to existing Nuke menu - i.e.:    nodeMenu = nuke.menu('Nuke').findItem('Edit/Node').addCommand('myMenuElement', 'myPythonScript.myFunction()', 'myHotkey')    # Modifiers: Shift= shift+, Alt/Option = alt+, Control/Command = ctrl+
nodeMenu = nuke.menu('Nuke').addCommand('Chetan/Preset Backdrop', 'Victor_Toolset.presetBackdrop()', 'alt+ctrl+b')
nodeMenu = nuke.menu('Nuke').addCommand('Chetan/ctz Align Row', 'ctz_align.alignRow()')
nodeMenu = nuke.menu('Nuke').addCommand('Chetan/ctz Align Col', 'ctz_align.alignCol()')
nodeMenu = nuke.menu('Nuke').addCommand('Chetan/ctz Align Grid', 'ctz_align.alignGrid()')
nodeMenu = nuke.menu('Nuke').addCommand('Chetan/ctz Abs to Rel', 'ctz_absToRel.absToRel()')
nodeMenu = nuke.menu('Nuke').addCommand('Chetan/ctz Convert to ReadGeo', 'ctz_convertToReadGeo.convertToReadGeo()')
nodeMenu = nuke.menu('Nuke').addCommand('Chetan/switcher', 'ctz_slash_switcher.start()')
nodeMenu = nuke.menu('Nuke').addCommand('Chetan/File Switcher', 'file_switcher.switch()')


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


