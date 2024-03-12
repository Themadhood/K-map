__Program__     = "K-Map.SolveSquare"    
__programer__   = "Themadhood Pequot"
__Date__        = "2/20/2024"
__version__     = "0.0.1"
__update__      = ""
__info__        = ""   

import math

try:
    from .GetVarStr import *
    from .SolveExpreshon import *
except:
    from GetVarStr import *
    from SolveExpreshon import *

#st = Error.time.time()
#Error.LenTime(st)
#Error.Log(f"","Log.txt")


def SolveSquare(square):
    
    expreshonDct = dict()
    expreshon = []

    #detirmin inputs
    sideVars = GetInputs(len(square))
    topVars = GetInputs(len(square[0]))
    topVars,s = GetVars(topVars,"A")
    sideVars,s = GetVars(sideVars,s)

    #get expreshons
    for side in sideVars:
        si = sideVars.index(side)
        for top in topVars:
            ti = topVars.index(top)
            #look for ok bits
            if square[si][ti] in [1,"1","?"]:
                expreshon.append(top+side)

                eca = Adjacent(si,ti,top,topVars,side,sideVars,square)
                expreshonDct.update({top+side:eca})
    Group(expreshonDct,expreshon)
    print(expreshonDct)

    PrintExpreshon(expreshon.copy())
    return expreshon


def MakeExpreshon(lst):
    expreshon = ""
    while lst > []:
        expreshon += lst.pop(0)
        if lst > []:
            expreshon += " + "
    return expreshon

def GetInputs(num):
    denominator = math.log10(2)/math.log10(num)
    IVars = int(round(1/denominator))
    return IVars


def PrintExpreshon(expreshon):
    if type(expreshon) == list:
        expreshon = MakeExpreshon(expreshon.copy())
    print(expreshon)


try:
    pass

except Exception as e:
    if self._Error:
        raise
    Error.UploadError([__Program__,__version__,"class","def",
                                f"mesage",e],"Functions")




if __name__ == "__main__":
    SolveSquare([[0,0,1,0],
                 [0,1,1,1]])
    
    ShrinkExpreshon("aBC + AbC + ABc + ABC")
    "BC + AC + AB"














