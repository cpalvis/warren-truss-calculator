import math


RAY = 100
RDY = 100
GRAV = -200

# Height and length of the total truss
HEIGHT = float(input('Truss Height: '))
SPAN = float(input('Truss Span: '))
BASE = SPAN * 0.25
ANGLE = math.atan((HEIGHT/BASE))
SIN = math.sin(ANGLE)
COS = math.cos(ANGLE)

# Utility function to convert radians to degrees
def toDegrees(r):
    return round(r * (180/math.pi), 1)

# Solves forces for all members connecting to point A
def A():
    global TAB

    taby = (0 - RAY)

    TAB = (taby/SIN)

    global TEA

    tabx = (TAB*COS)

    TEA = 0 + tabx

# Solves forces for all members connecting to point B
def B():
    global TEB
    
    taby = (TAB*SIN)
    teby = (0 + taby) * -1
 
    TEB = (teby/SIN)

    global TBC
   
    tabx = (TAB*COS)
    tebx = (TEB*COS)
   
    TBC = 0 - (-tabx + tebx)

# Solves forces for all members connecting to point E
def E():
    global TEC

    teby = (TEB*SIN)
    tecy = 0 - (teby + GRAV)

    TEC = (tecy/SIN)

    global TED
 
    TED = 0 + (-TEA)

# Solves forces for all members connecting to point C
def C():
    global TCD

    tecy = (TEC*SIN)
    tcdy = (0 + tecy) * -1

    TCD = (tcdy/SIN)

# NOTE: All forces are calculated at this point, so it is unnecessary to run any more calculations
print("Angle: ", toDegrees(ANGLE))

A()
B()
E()
C()

print('Results')
print("TAB ", TAB)
print("TEA ", TEA)
print("TEB ", TEB)
print("TBC ", TBC)
print("TEC ", TEC)
print("TED ", TED)
print("TCD ", TCD)
