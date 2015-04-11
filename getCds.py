import sys

with open("cooldown_vals.csv", 'r') as f:
    raw = f.readlines()[1:]
    cdData = tuple(l.replace('\n',"").split(',') for l in raw)
    
def getChampCds(champ):
    """Returns a 3 value tuple of cooldown values at
    levels 1, 2, and 3 of ult for champion given by 
    champ string
    """
    def getHelper(lst):
        if not lst:
            raise Exception("Champion not found")
        mid = len(lst)//2
        if champ == lst[mid][0]:
            return lst[mid][1:]
        if champ < lst[mid][0]:
            return getHelper(lst[:mid])
        else:
            return getHelper(lst[mid+1:])
    return getHelper(cdData)
    
def getMultipleChampCds(champs):
    for champ in champs:
        print("{}: {}".format(champ, getChampCds(champ)))

if __name__ == "__main__":
    getMultipleChampCds(sys.argv[1:])
