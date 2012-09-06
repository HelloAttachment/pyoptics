# -*- coding: utf-8 -*-
from pybench import *
from PyQt4 import QtGui, QtCore
QtCore.Signal = QtCore.pyqtSignal

import pyqtgraph as pg
import numpy as np
from pyqtgraph import Point

app = QtGui.QApplication([])

w = QtGui.QMainWindow()
view = Canvas()
view.show()
optics = []


#view.enableMouse()
#view.aspectLocked = True
#view.invertY(False)
#grid = pg.GridItem()
#view.addItem(grid)
#view.setRange(QtCore.QRectF(-150, 200, 500, 400))

optics = []
rays = []
m = Mirror(r1=-100, pos=(5,0), angle=-15)
optics.append(m)
#m.rotate(-15)
#m.translate(5,0)

allRays = []
for y in np.linspace(-10, 10, 21):
    r = Ray(start=Point(-100, y))
    view.addGraphicsItem(r)
    allRays.append(r)

for o in optics:
    view.addItem(o)
    
view.autoRange()

t = Tracer(allRays, optics)

import sys
if sys.flags.interactive == 0:
    app.exec_()