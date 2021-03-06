if __name__ == "__main__":
    inputfile = open("UA-Nodeset/Schema/NodeIds.csv")
    outputfile = open("../asyncua/ua/object_ids.py", "w")
    outputfile.write("#AUTOGENERATED!!!\n")
    outputfile.write("\n")
    outputfile.write("from enum import IntEnum\n")
    outputfile.write("\n")
    # Making ObjectIds inherit IntEnum has a huge performance impact!!!!!
    # so we use a normal class and a reverse one for the few places we need it
    outputfile.write("class ObjectIds:\n")
    outputfile.write("    Null = 0\n")
    for line in inputfile:
        name, nb, datatype = line.split(",")
        outputfile.write("    {0} = {1}\n".format(name, nb))
    inputfile.close()
    inputfile = open("UA-Nodeset/Schema/NodeIds.csv")
    outputfile.write("\n\nObjectIdNames = {}\n")
    outputfile.write("ObjectIdNames[0] = 'Null'\n".format(nb, name))
    for line in inputfile:
        name, nb, datatype = line.split(",")
        outputfile.write("ObjectIdNames[{0}] = '{1}'\n".format(nb, name))

    inputfile = open("UA-Nodeset/Schema/AttributeIds.csv")
    outputfile = open("../asyncua/ua/attribute_ids.py", "w")
    outputfile.write("#AUTOGENERATED!!!\n")
    outputfile.write("\n")
    outputfile.write("from enum import IntEnum\n")
    outputfile.write("\n")
    outputfile.write("class AttributeIds(IntEnum):\n")
    for line in inputfile:
        name, nb = line.split(",")
        outputfile.write("    {0} = {1}\n".format(name.strip(), nb.strip()))

