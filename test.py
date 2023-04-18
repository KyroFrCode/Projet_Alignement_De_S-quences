import distance

#Test et calcule des distances des Instances de genome Inst_0000010_44.adn,Inst_0000010_7.adn,Inst_0000010_8.adn

Inst_0000010_44 = open("./Instances_genome/Inst_0000010_44.adn","r")
Inst_0000010_7 = open("./Instances_genome/Inst_0000010_7.adn","r")
Inst_0000010_8 = open("./Instances_genome/Inst_0000010_8.adn","r")

lignes = Inst_0000010_44.readlines()
lignes2 = Inst_0000010_7.readlines()
lignes3 = Inst_0000010_8.readlines()

Sequences_Inst1044 = distance.Struct_Instance(lignes)
Sequences_Inst107 = distance.Struct_Instance(lignes2)
Sequences_Inst108 = distance.Struct_Instance(lignes3)

#Inst_0000010_44
print("Sequences_Inst_0000010_44:\nX: "+str(Sequences_Inst1044["X"])+"\nY: "+str(Sequences_Inst1044["Y"])+"\ntaille_X: "+str(len(Sequences_Inst1044["X"]))+"\ntaille_Y: "+str(len(Sequences_Inst1044["Y"])))
print("distance:"+str(distance.DIST_NAIF(Sequences_Inst1044["X"],Sequences_Inst1044["Y"]))+"\n")

#Inst_0000010_7
print("Sequences_Inst_0000010_7:\nX: "+str(Sequences_Inst107["X"])+"\nY: "+str(Sequences_Inst107["Y"])+"\ntaille_X: "+str(len(Sequences_Inst107["X"]))+"\ntaille_Y: "+str(len(Sequences_Inst107["Y"])))
print("distance:"+str(distance.DIST_NAIF(Sequences_Inst107["X"],Sequences_Inst107["Y"]))+"\n")

#Inst_0000010_8
print("Sequences_Inst_0000010_8:\nX: "+str(Sequences_Inst108["X"])+"\nY: "+str(Sequences_Inst108["Y"])+"\ntaille_X: "+str(len(Sequences_Inst108["X"]))+"\ntaille_Y: "+str(len(Sequences_Inst108["Y"])))
print("distance:"+str(distance.DIST_NAIF(Sequences_Inst108["X"],Sequences_Inst108["Y"]))+"\n")