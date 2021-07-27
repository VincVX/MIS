import math


def entropy(p1,p2):
    frac = p1 + p2
    frac_p1 = p1/frac
    frac_p2 = p2/frac
    return - frac_p1 * math.log2(frac_p1) - frac_p2 * math.log2(frac_p2)
#print(entropy())
def IG(entp,pc1, entc1, pc2, entc2):
    return entp - (pc1 *entc1 + pc2*entc2)

#print(IG())


# Hauspreisregression mit kNN - Normalisierung

def normalize(array):
    min_x = min(array)
    max_x = max(array)
    storage_list = list()
    for i in array:
        storage_list.append(round((i - min_x)/(max_x - min_x),2))
    print("Die normalisierung ist : ", storage_list)
    return storage_list





#Hauspreisregression - Standardisierung der Daten

def finalscore(array):
    storagearray = list()
    def sigmafinal():
        mu = round(1/len(array)*sum(array),2)
        storage = list()
        length = len(array) - 1
        for i in array:
            storage.append((i - mu)**2)
        sum_storage = sum(storage)
        return round(math.sqrt(sum_storage/ length),2)
    sigma = sigmafinal()
    mu = round(1/len(array)*sum(array),2)
    for x in array:
        storagearray.append(round((x - mu) / sigma,2))
    print("mu ist ", mu)
    print("sigma ist", sigma)
    return storagearray


