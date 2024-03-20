__Program__     = "K-Map.GetVarStr"    
__programer__   = "Themadhood Pequot"
__Date__        = "2/20/2024"
__version__     = "0.0.1"
__update__      = ""
__info__        = ""   

import Error

#st = Error.time.time()
#Error.LenTime(st)
#Error.Log(f"","Log.txt")

Cap = ["A","B","C","D","E","F","G","H","I","J","K","L",
        "M","N","O","P","Q","R","S","T","U","V","W","X",
        "Y","Z"]
Low = ["a","b","c","d","e","f","g","h","i","j","k","l",
       "m","n","o","p","q","r","s","t","u","v","w","x",
       "y","z"]

def GetVars(number, start="A"):
    try:
        start = Cap.index(start.upper())
        if number > 1:
            retar = _IIVar(Cap[start],Cap[start+1])
            number -=2
            start += 2
            for n in range(0,number):
                retar = _JoinVarSets(retar,_IVar(Cap[start]))
                start += 1
        else:
            retar = _IVar(Cap[start])
            start += 1
        return retar,Cap[start]
    except Exception as e:
        if self._Error:
            raise
        Error.UploadError([__Program__,__version__,"","GetVars",
                           f"failed to get lst of vars as str",e],"Functions")
        return [],"A"
        
def _JoinVarSets(varSet,addset):
    retar = []
    try:
        append = varSet.copy()
        for i in range(0,2):
            for vs in varSet:
                nvs = addset[i]+vs
                retar.append(nvs)
    except Exception as e:
        if self._Error:
            raise
        Error.UploadError([__Program__,__version__,"","_JoinVarSets",
                           f"failed to join two lst of str to one",e],
                          "Functions")
    return retar

def _IVar(let):
    try:
        return [let.lower(),let.upper()]
    except Exception as e:
        if self._Error:
            raise
        Error.UploadError([__Program__,__version__,"","_IVar",
                           f"failed to get lst of str",e],"Functions")

def _IIVar(let1,let2):
    try:
        return [let1.lower() + let2.lower(),
                let1.lower() + let2.upper(),
                let1.upper() + let2.upper(),
                let1.upper() + let2.lower()]
    except Exception as e:
        if self._Error:
            raise
        Error.UploadError([__Program__,__version__,"","_IIVar",
                           f"failed to get lst of str",e],"Functions")




if __name__ == "__main__":
    print(GetVars(4,"A"))














