
from PySteppables import *
import CompuCell
import sys
class vasc_demoSteppable(SteppableBasePy):

    def __init__(self,_simulator,_frequency=1):
        SteppableBasePy.__init__(self,_simulator,_frequency)
        
    def start(self):
                
        self.cellField[120:125, 120:125, 0] = self.newCell(self.TUMOR)
        
        for cell in self.cellList:
            if cell.type == self.VASC:
                
                cell.targetVolume=12.0
                cell.lambdaVolume=20.0
                
            elif cell.type == self.TUMOR:                
                
                cell.targetVolume=30.0
                cell.lambdaVolume=10.0
        
        
    def step(self,mcs): 
        glucose = self.getConcentrationField('Glucose')
                
        for cell in self.cellListByType(self.VASC): 
            x = int(round(cell.xCOM))
            y = int(round(cell.yCOM))
            if x>80 and y > 80:
            
                glucose[x, y, 0] += 1.0
        
        k = 0.1
        for cell in self.cellListByType(self.TUMOR): 
                
            glucose_level = glucose[ int(round(cell.xCOM)), int(round(cell.yCOM)),0]
            
            cell.targetVolume += min( k * glucose_level , 0.2)
        
        
from PySteppables import *
from PySteppablesExamples import MitosisSteppableBase
import CompuCell
import sys

from PlayerPython import *
from math import *


class Mitosis(MitosisSteppableBase):
    def __init__(self,_simulator,_frequency=1):
        MitosisSteppableBase.__init__(self,_simulator, _frequency)
    
    def step(self,mcs):
        cells_to_divide=[]
        for cell in self.cellList:
            if cell.type==self.TUMOR and cell.volume > 60:
                
                cells_to_divide.append(cell)
                
        for cell in cells_to_divide:

            self.divideCellRandomOrientation(cell)

    def updateAttributes(self):
        self.parentCell.targetVolume /= 2.0 # reducing parent target volume                 
        self.cloneParent2Child()            
        
        
