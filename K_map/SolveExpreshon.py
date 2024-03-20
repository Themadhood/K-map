__Program__     = "K-Map.SolveExpreshon"    
__programer__   = "Themadhood Pequot"
__Date__        = "2/20/2024"
__version__     = "0.0.1"
__update__      = ""
__info__        = ""   

try:
    from .SameLst import *
except:
    from SameLst import *

#st = Error.time.time()
#Error.LenTime(st)
#Error.Log(f"","Log.txt")


def ShrinkExpreshon(expreshon):
    retar = []
    if type(expreshon) == str:
        expreshon = expreshon.split(" + ")

    #aBC + AbC + ABc + ABC
    #aBC + AbC + ABc + ABC + ABC + ABC
    #(aBC + ABC) + (AbC + ABC) + (ABc + ABC)
    #BC + AC + AB

def Adjacent(y,x,top,topVars,side,sideVars,square):
    ex = {"N":None,"E":None,"S":None,"W":None}
    
    if square[y-1][x] in [1,"1","?"]: #N
        ex["N"] = top+sideVars[y-1]
        
    if square[y][x-1] in [1,"1","?"]: #W
        ex["W"] = topVars[x-1]+side

    if x+1 == len(topVars):
        x = -1
    if y+1 == len(sideVars):
        y = -1
    
    if square[y][x+1] in [1,"1","?"]: #E
        ex["E"] = topVars[x+1]+side
    
    if square[y+1][x] in [1,"1","?"]: #S
        ex["S"] = top+sideVars[y+1]

    return ex

def Group(dct,lst):
    groups = []

    print(lst)
    for ex in lst:
        group = []
        _SearchVertical(dct[ex],group,dct)
        groups.append(group)
        group = []
        _SearchHorizontal(dct[ex],group,dct)
        groups.append(group)

    groups = RemoveEqivlentLsts(groups)
    print(groups)

    
def _SearchVertical(ex,group,dct):
    if ex["N"] != None:
        if ex["N"] not in group:
            group.append(ex["N"])
            _SearchVertical(dct[ex["N"]],group,dct)
    if ex["S"] != None:
        if ex["S"] not in group:
            group.append(ex["S"])
            _SearchVertical(dct[ex["S"]],group,dct)

def _SearchHorizontal(ex,group,dct):
    if ex["E"] != None:
        if ex["E"] not in group:
            group.append(ex["E"])
            _SearchHorizontal(dct[ex["E"]],group,dct)
    if ex["W"] != None:
        if ex["W"] not in group:
            group.append(ex["W"])
            _SearchHorizontal(dct[ex["W"]],group,dct)



try:
    pass
except Exception as e:
    if self._Error:
        raise
    Error.UploadError([__Program__,__version__,"class","defs",
                           f"msg",e],"Functions")






if __name__ == "__main__":
    ShrinkExpreshon("aBC + AbC + ABc + ABC")
    "BC + AC + AB"














