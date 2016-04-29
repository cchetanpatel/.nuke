import nuke

class ShapePanel(nukescripts.PythonPanel ):


    def __init__( self):
        nukescripts.PythonPanel.__init__( self, 'TITLE' )
        
        #LIST OF RENDER PASSES
        primaryElements = ['Diffuse',
                            'Specular',
                            'Reflection',
                            'Refraction',
                            'Caustics',
                            'SSS']
       # secondaryElements = 
        #utilityElements = 
        # CREATE KNOBS
    

        self.renderElement = nuke.Boolean_Knob('vray_renderElement', 'name of render element', 0)
        # ADD KNOBS
        for k in ( self.typeKnob, self.elementKnob, self.renderElement ):
            self.addKnob( k )
        elements = self.getRenderElements()

    def getRenderElements(self):
        nd = nuke.createNode('VRayRenderElement',' ',False)
        k = nd['render_element']
        
        count = 0
        ele = []
        for val in k.values():
            print val
            if(count != 0):
                n = nuke.createNode('VRayRenderElement')
                n['render_element'].setValue(val)
                ele.append(n['render_element'])

            count+=1
        nuke.delete(nd)
        return ele

p = ShapePanel()
if p.showModalDialog():
    print p.elementKnob.value()

