#save h:\.nuke\python\my_code.py

# function declaration
# create a function to change scanline render settings
import nuke
import platform
import subprocess
import os


def lower_settings():
  
    # get antialiasing value from user
    # make panel
    p = nuke.Panel('my custom panel')
    # add knobs to panel
    p.addEnumerationPulldown('antialiasing', 'none low medium high')
    p.addSingleLineInput('samples', '1')
    p.addBooleanCheckBox('disable motion blur', '0')    
    p.addBooleanCheckBox('disable regrain', '0')    
    p.addBooleanCheckBox('disable defocus', '0')    
    # show panel
    p.show()

    # get the results of the user input
    antialising_result = p.value('antialiasing') 
    samples_result = p.value('samples')
    motion_blur_result = p.value('disable motion blur')
    regrain_result = p.value('disable regrain')
    defocus_result = p.value('disable defocus')


    # get all the scanline render nodes
    node_list = nuke.allNodes('ScanlineRender')
    # for each node scanline node
    for node in node_list:
        # change the antialiasing settings
        node['antialiasing'].setValue(antialising_result)
        node['samples'].setValue( int(samples_result) )

    # disable motion blur nodes
    node_list = nuke.allNodes('VectorBlur')
    for node in node_list:
        node['disable'].setValue(motion_blur_result)

    node_list = nuke.allNodes('VectorBlur2')
    for node in node_list:
        node['disable'].setValue(motion_blur_result)

    node_list = nuke.allNodes('MotionBlur2D')
    for node in node_list:
        node['disable'].setValue(motion_blur_result)

    node_list = nuke.allNodes('MotionBlur3D')
    for node in node_list:
        node['disable'].setValue(motion_blur_result)

    # disable grains nodes
    node_list = nuke.allNodes('OFXuk.co.thefoundry.furnace.f_regrain_v403')
    for node in node_list:
        node['disable'].setValue(regrain_result)

    node_list = nuke.allNodes('Grain')
    for node in node_list:
        node['disable'].setValue(regrain_result)

    node_list = nuke.allNodes('Grain2')
    for node in node_list:
        node['disable'].setValue(regrain_result)

    # disable defocus nodes
    node_list = nuke.allNodes('Defocus')
    for node in node_list:
        node['disable'].setValue(defocus_result)

    node_list = nuke.allNodes('ZDefocus')
    for node in node_list:
        node['disable'].setValue(defocus_result)

    node_list = nuke.allNodes('ZDefocus2')
    for node in node_list:
        node['disable'].setValue(defocus_result)


# helper function to open files on different platforms
def open_file(path):
    if platform.system() == "Windows":
        os.startfile(path)
    elif platform.system() == "Darwin":
        subprocess.Popen(["open", path])
    else:
        subprocess.Popen(["xdg-open", path])

# function to open a folder for the given node if it has a file knob
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

def quick_3d():

# create a checkerboard, card, scene, scanlinerender, camera node
    checkerboard_node = nuke.createNode('CheckerBoard2', inpanel=False)
    card_node = nuke.createNode('Card', inpanel=False)
    scene_node = nuke.createNode('Scene', inpanel=False)
    scanline_node = nuke.createNode('ScanlineRender', inpanel=False)
    cam_node = nuke.createNode('Camera', inpanel=False)

# Connect the camera to the scanline render
    scanline_node.setInput(2, cam_node) # input_number, node_to_connect

# Connect the camera to the scene
    scene_node.setInput(1, cam_node)

    x_pos = checkerboard_node['xpos'].value()
    y_pos = checkerboard_node['ypos'].value()

    card_node['xpos'].setValue(x_pos)
    card_node['ypos'].setValue(y_pos + 100)
    
    scene_node['xpos'].setValue(x_pos)
    scene_node['ypos'].setValue(y_pos + 200)

    scanline_node['xpos'].setValue(x_pos)
    scanline_node['ypos'].setValue(y_pos + 300)

    cam_node['xpos'].setValue(x_pos - 100)
    cam_node['ypos'].setValue(y_pos + 300)

