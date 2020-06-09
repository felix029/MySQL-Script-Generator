import sys

def readTypes(bloodTypes):

    typeConversion = {
        "O-":   0,
        "O+":   1,
        "A-":   2,
        "A+":   3,
        "B-":   4,
        "B+":   5,
        "AB+":  6,
        "AB-":  7
    }

    types = []

    for bloodType in bloodTypes:
        types.append(typeConversion.get(bloodType.upper(), "Invalid blood type"))

    return types

def compatibilityCheck(types):

    table = (
                (1, 0, 0, 0, 0, 0, 0, 0),
                (1, 1, 0, 0, 0, 0, 0, 0),
                (1, 0, 1, 0, 0, 0, 0, 0),
                (1, 1, 1, 1, 0, 0, 0, 0),
                (1, 0, 0, 0, 1, 0, 0, 0),
                (1, 1, 0, 0, 1, 1, 0, 0),
                (1, 0, 1, 0, 1, 0, 1, 0),
                (1, 1, 1, 1, 1, 1, 1, 1)
            )

    if table[types[1]][types[0]]:
        print("Compatible")
    else:
        print("Incompatible")

def main():

    # Put your blood types here!
    # First one is donor, second one is recipient
    bloodTypes = ("a-", "ab+")

    compatibilityCheck(readTypes(bloodTypes))



if __name__ == '__main__':
    sys.exit(main())