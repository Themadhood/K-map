__Program__     = "Duplicate.SameLst"    
__programer__   = "Themadhood Pequot"
__Date__        = "2/21/2024"
__version__     = "0.0.1"
__update__      = ""
__info__        = ""   

import Error

#st = Error.time.time()
#Error.LenTime(st)
#Error.Log(f"","Log.txt")


def SamelstDifrentOrder(lst1,lst2,error=False):
    try:
        if lst1 is lst2:
            return True
        #if != len then !~ lst
        if len(lst1) != len(lst2):
            return False
        #if same len check items
        for i in lst2:
            if i not in lst1: # item not in lst then not same
                return False
        return True
    except Exception as e:
        if error:
            raise
        Error.UploadError([__Program__,__version__,"","SamelstDifrentOrder",
                           f"error cheking if list are the same",e],"Functions")

def RemoveEqivlentLsts(lstOfLsts,error=False):
    retar = []
    try:
        while lstOfLsts > []:
            poped = lstOfLsts.pop()
            if poped != [] and poped not in retar:
                if retar == []:
                    retar.append(poped)
                else:
                    for group in retar:
                        if SamelstDifrentOrder(poped,group,error):
                            break

                        if group == retar[-1]:
                            retar.append(poped)
    except Exception as e:
        if error:
            raise
        Error.UploadError([__Program__,__version__,"","_RemoveDuplicatLst",
                                    f"failed to remove duplicats",e],"Functions")
    return retar
    


if __name__ == "__main__":
    ShrinkExpreshon("aBC + AbC + ABc + ABC")
    "BC + AC + AB"














