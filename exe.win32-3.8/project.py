from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np
from appJar import gui
plt.style.use('seaborn-v0_8')
def line3d(x1,y1,z1,x2,y2,z2):
    fig=plt.figure()
    ax=plt.axes(projection="3d")
    plt.plot([x1,x2],[y1,y2],[z1,z2])
    plt.title("line3d")
    plt.show();
def line2d(x1,y1,x2,y2):
    plt.plot([x1,x2],[y1,y2],'-k')
    plt.title("line2d")
    plt.show();
def sin3d(x1=0,y1=10):
    x=np.linspace(x1,y1,5000)
    fig=plt.figure()
    ax=plt.axes(projection="3d")
    plt.plot(x,np.sin(x))
    plt.title("sin3d")
    plt.show();
def cos3d(x1=0,y1=10):
    x=np.linspace(x1,y1,5000)
    fig=plt.figure()
    ax=plt.axes(projection="3d")
    plt.plot(x,np.cos(x))
    plt.title("cos3d")
    plt.show();
def sin2d(x1=0,y1=10):
    x=np.linspace(x1,y1,5000)
    plt.plot(x,np.sin(x))
    plt.title("sin2d")
    plt.show();
def cos2d(x1=0,y1=10):
    x=np.linspace(x1,y1,5000)
    plt.plot(x,np.cos(x))
    plt.title("cos2d")
    plt.grid(alpha=.4,linestyle='--')
    plt.show();
def graph(formula, x1=0,y1=10):
    x=np.linspace(x1,y1,5000)
    y=eval(formula)
    plt.plot(x,y)
    plt.show();
def graph3d(formula,x1=0,y1=10):
    fig = plt.figure()
    ax = plt.axes(projection="3d")
    x=np.linspace(x1,y1,5000)
    y=eval(formula)
    plt.plot(x,y)
    plt.show();
def pressli3d(button):
    if button == "Cancel":
        app.hideSubWindow("Line-3D")
    else:
        li3dx1=app.getEntry("x1")
        li3dx2=app.getEntry("x2")
        li3dy1=app.getEntry("y1")
        li3dy2=app.getEntry("y2")
        li3dz1=app.getEntry("z1")
        li3dz2=app.getEntry("z2")
        line3d(li3dx1,li3dy1,li3dz1,li3dx2,li3dy2,li3dz2)
def pressli2d(button):
    if button == "L2DCancel":
        app.hideSubWindow("Line-2D")
    else:
        li2dx1=app.getEntry("li2dx1")
        li2dx2=app.getEntry("li2dx2")
        li2dy1=app.getEntry("li2dy1")
        li2dy2=app.getEntry("li2dy2")
        line2d(li2dx1,li2dy1,li2dx2,li2dy2)
def presssin3d(button):
    if button == "S3DCancel":
        app.hideSubWindow("Sin-3D")
    else:
        sin3dx1= app.getEntry("s3dx1")
        sin3dy1=app.getEntry("s3dy1")
        sin3d(sin3dx1,sin3dy1)
def presssin2d(button):
    if button == "S2DCancel":
        app.hideSubWindow("Sin-2D")
    else:
        sin2dx1=app.getEntry("s2dx1")
        sin2dy1=app.getEntry("s2dy1")
        sin2d(sin2dx1,sin2dy1)
def presscos3d(button):
    if button == "C3DCancel":
        app.hideSubWindow("Cos-3D")
    else:
        cos3dx1=app.getEntry("c3dx1")
        cos3dy1=app.getEntry("c3dy1")
        cos3d(cos3dx1,cos3dy1)
def presscos2d(button):
    if button == "C2DCancel":
        app.hideSubWindow("Cos-2D")
    else:
        cos2dx1=app.getEntry("c2dx1")
        cos2dy1=app.getEntry("c2dy1")
        cos2d(cos2dx1,cos2dy1)
def pressgraph2d(button):
    if button =="G2DCancel":
        app.hideSubWindow("Graph-2D")
    else:
        g2dformula=app.getEntry("g2dformula")
        g2dx1=app.getEntry("g2dx1")
        g2dy1=app.getEntry("g2dy1")
        graph(g2dformula,g2dx1,g2dy1)
def pressgraph3d(button):
    if button == "G3DCancel":
        app.hideSubWindow("Graph-3D")
    else:
        g3dformula=app.getEntry("g3dformula")
        g3dx1=app.getEntry("g3dx1")
        g3dy1=app.getEntry("g3dy1")
        graph3d(g3dformula,g3dx1,g3dy1)
app=gui()
app.setTitle("CS Project:Jaira and Chaudhary")
def startbutton(button):
    if button == "Line-3D":
        app.showSubWindow("Line-3D")
    elif button == "Line-2D":
        app.showSubWindow("Line-2D")
    elif button == "Cos-3D":
        app.showSubWindow("Cos-3D")
    elif button == "Sin-3D":
        app.showSubWindow("Sin-3D")
    elif button == "Cos-2D":
        app.showSubWindow("Cos-2D")
    elif button == "Sin-2D":
        app.showSubWindow("Cos-2D")
    elif button == "Graph-2D":
        app.showSubWindow("Graph-2D")
    elif button == "Graph-3D":
        app.showSubWindow("Graph-3D")
app.setBg("Blue")
app.setFont(size=16, family="Times", underline=True, slant="italic")
app.setButtonFont(size=14, family="Verdana", underline=False,
slant="roman")
app.setSize(400,400)
app.setTransparency(100)
app.startSubWindow("Line-3D")
app.addNumericEntry("x1")
app.setEntryDefault("x1","x1")
app.addNumericEntry("x2")
app.setEntryDefault("x2","x2")
app.addNumericEntry("y1")
app.setEntryDefault("y1","y1")
app.addNumericEntry("y2")
app.setEntryDefault("y2","y2")
app.addNumericEntry("z1")
app.setEntryDefault("z1","z1")
app.addNumericEntry("z2")
app.setEntryDefault("z2","z2")
app.addButtons(["Submit", "Cancel"],pressli3d)
app.stopSubWindow()
app.startSubWindow("Line-2D")
app.addNumericEntry("li2dx1")
app.setEntryDefault("li2dx1","x1")
app.addNumericEntry("li2dx2")
app.setEntryDefault("li2dx2","x2")
app.addNumericEntry("li2dy1")
app.setEntryDefault("li2dy1","y1")
app.addNumericEntry("li2dy2")
app.setEntryDefault("li2dy2","y2")
app.addNamedButton("Submit","L2DSubmit",pressli2d)
app.addNamedButton("Cancel","L2DCancel",pressli2d)
app.stopSubWindow()
app.startSubWindow("Sin-3D")
app.addNumericEntry("s3dx1")
app.setEntryDefault("s3dx1","Start Co-Ordinate")
app.addNumericEntry("s3dy1")
app.setEntryDefault("s3dy1","End Co-Ordinate")
app.addNamedButton("Submit","S3DSubmit",presssin3d)
app.addNamedButton("Cancel","S3DCancel",presssin3d)
app.stopSubWindow()
app.startSubWindow("Sin-2D")
app.addNumericEntry("s2dx1")
app.setEntryDefault("s2dx1","Start Co-Ordinate")
app.addNumericEntry("s2dy1")
app.setEntryDefault("s2dy1","End Co-Ordinate")
app.addNamedButton("Submit","S2DSubmit",presssin2d)
app.addNamedButton("Cancel","S2DCancel",presssin2d)
app.stopSubWindow()
app.startSubWindow("Cos-3D")
app.addNumericEntry("c3dx1")
app.setEntryDefault("c3dx1","Start Co-Ordinate")
app.addNumericEntry("c3dy1")
app.setEntryDefault("c3dy1","End Co-Ordinate")
app.addNamedButton("Submit","C3DSubmit",presscos3d)
app.addNamedButton("Cancel","C3DCancel",presscos3d)
app.stopSubWindow()
app.startSubWindow("Cos-2D")
app.addNumericEntry("c2dx1")
app.setEntryDefault("c2dx1","Start Co-Ordinate")
app.addNumericEntry("c2dy1")
app.setEntryDefault("c2dy1","End Co-Ordinate")
app.addNamedButton("Submit","C2DSubmit",presscos2d)
app.addNamedButton("Cancel","C2DCancel",presscos2d)
app.stopSubWindow()
app.startSubWindow("Graph-2D")
app.addEntry("g2dformula")
app.setEntryDefault("g2dformula","Formula")
app.addNumericEntry("g2dx1")
app.setEntryDefault("g2dx1","Start Co-Ordinate")
app.addNumericEntry("g2dy1")
app.setEntryDefault("g2dy1","Ending Co-Ordinate")
app.addNamedButton("Submit","G2DSubmit",pressgraph2d)
app.addNamedButton("Cancel","G2DCancel",pressgraph2d)
app.stopSubWindow()
app.startSubWindow("Graph-3D")
app.addEntry("g3dformula")
app.setEntryDefault("g3dformula","Formula")
app.addNumericEntry("g3dx1")
app.setEntryDefault("g3dx1","Start Co-Ordinate")
app.addNumericEntry("g3dy1")
app.setEntryDefault("g3dy1","Ending Co-Ordinate")
app.addNamedButton("Submit","G3DSubmit",pressgraph3d)
app.addNamedButton("Cancel","G3DCancel",pressgraph3d)
app.stopSubWindow()
app.addButtons(["Line-3D","Line-2D"],startbutton)
app.addButtons(["Sin-3D","Sin-2D"],startbutton)
app.addButtons(["Cos-3D","Cos-2D"],startbutton)
app.addButtons(["Graph-3D","Graph-2D"],startbutton)
app.show()
app.go()

