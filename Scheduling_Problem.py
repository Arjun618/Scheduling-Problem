import pyfiglet
import subprocess

def STYLES(x):
    res = pyfiglet.figlet_format(x, font="digital")
    print("*" * 80)
    print(res)
    print("*" * 80)

def colour_vertices(graph):
    vertices = sorted(list(graph.keys()))
    colour_graph = {}

    for vertex in vertices:
        unused_colours = [True] * len(vertices)
        for neighbor in graph[vertex]:
            if neighbor in colour_graph:
                colour = colour_graph[neighbor]
                unused_colours[colour] = False
        for colour, unused in enumerate(unused_colours):
            if unused:
                colour_graph[vertex] = colour
                break
    return colour_graph

def SeeGraph():
    ans = input("DO YOU WANT TO SEE THE GRAPH (Y/N) ? \t:\t")
    print("*" * 80)
    if ans == 'Y':
        path = 'Graph.pdf'
        subprocess.Popen([path], shell=True)
        print("0 => STANDS FOR BLUE COLOUR\n")
        print("1 => STANDS FOR ORANGE COLOUR\n")
        STYLES(" THANK YOU")
    else:
        STYLES(" THANK YOU")

def NoDegree():
    n = 0
    L = ["MNG", "GEO", "CW", "LNG", "PHIL", "SAS", "COM", "ECO", "EVS"]
    for i in L:
        print({i: n}, end=" ")
    print()
    print("*" * 80)

def inputVertex():
    ListV = []
    EdgeV1 = []
    EdgeV2 = []
    EdgeV3 = []
    EdgeV4 = []
    EdgeV5 = []
    EdgeV6 = []
    EdgeV7 = []
    EdgeV8 = []
    EdgeV9 = []
    EdgeV10 = []
    EdgeV11 = []
    EdgeV12 = []
    EdgeV13 = []
    EdgeV14 = []
    EdgeV15 = []
    EdgeV16 = []
    EdgeV17 = []
    EdgeV18 = []
    EdgeV19 = []
    EdgeV20 = []
    EdgeV21 = []
    EdgeV22 = []
    EdgeV23 = []
    EdgeV24 = []
    EdgeV25 = []

    totalV = int(input("ENTER THE TOTAL VERTICES OF GRAPH \t:\t"))
    print("*" * 80)
    
    for i in range(totalV):
        NameV = input("ENTER THE NAME OF VERTEX \t\t:\t")
        ListV.append(NameV)
        print("*" * 80)
    
    for i in range(totalV):
        print("*" * 80)
        print(" 1. Maths connect (MATH) 2. Physics connect (PHY)")
        print(" 3. Chemistry connect (CHEM) 4. Programming connect (PR)")
        print(" 5. Creative Writing connect (CW) 6. Entrepreneurship connect (EP)")
        print(" 7. EVS connect (EVS) 8. Social Emotional Learning connect (SEL)")
        print(" 9. History connect (HIS) 10. Political Science connect (POLS)")
        print("11. Economics connect (ECO) 12. Maths2 connect (MATH2)")
        print("13. Management connect (MNG) 14. Programming2 connect (PR2)")
        print("15. Biotechnology connect (BT) 16. Mechanics connect (MECH)")
        print("17. Entrepreneurship2 connect (EP2) 18. Geography connect (GEO)")
        print("19. Communication connect (COM) 20. Philosophy connect (PHIL)")
        print("21. Political Science2 connect (POLS2) 22. Linguistics connect (LNG)")
        print("23. Science and Society connect (SAS) 24. History2 connect (HIS2)")
        print("25. Sociology connect (SOC)")
        print("*" * 80)
        print("*" * 80)
        ch = int(input("ENTER YOUR CHOICE\t\t:\t"))
        print("*" * 80)
        
        if ch == 1:
            print("*" * 80)
            a1 = int(input("MATHS HAS HOW MUCH DEGREE \t\t:\t"))
            for i in range(a1):
                NameV = input("ENTER THE NAME OF CONNECTED VERTEX \t:\t")
                print("*" * 80)
                EdgeV1.append(NameV)
                
        if ch == 2:
            print("*" * 80)
            a2 = int(input("PHYSICS HAS HOW MUCH DEGREE \t\t:\t"))
            for i in range(a2):
                NameV = input("ENTER THE NAME OF CONNECTED VERTEX \t:\t")
                print("*" * 80)
                EdgeV2.append(NameV)
                
        if ch == 3:
            print("*" * 80)
            a3 = int(input("CHEMISTRY HAS HOW MUCH DEGREE \t\t:\t"))
            for i in range(a3):
                NameV = input("ENTER THE NAME OF CONNECTED VERTEX \t:\t")
                print("*" * 80)
                EdgeV3.append(NameV)
                
        if ch == 4:
            print("*" * 80)
            a4 = int(input("PROGRAMMING HAS HOW MUCH DEGREE \t:\t"))
            for i in range(a4):
                NameV = input("ENTER THE NAME OF CONNECTED VERTEX \t:\t")
                print("*" * 80)
                EdgeV4.append(NameV)
                
        if ch == 5:
            print("*" * 80)
            a5 = int(input("CREATIVE WRITING HAS HOW MUCH DEGREE \t\t:\t"))
            for i in range(a5):
                NameV = input("ENTER THE NAME OF CONNECTED VERTEX \t:\t")
                print("*" * 80)
                EdgeV5.append(NameV)
                
        if ch == 6:
            print("*" * 80)
            a6 = int(input("ENTREPRENEURSHIP HAS HOW MUCH DEGREE \t\t:\t"))
            for i in range(a6):
                NameV = input("ENTER THE NAME OF CONNECTED VERTEX \t\t:\t")
                print("*" * 80)
                EdgeV6.append(NameV)
                
        if ch == 7:
            print("*" * 80)
            a7 = int(input("EVS HAS HOW MUCH DEGREE \t\t:\t"))
            for i in range(a7):
                NameV = input("ENTER THE NAME OF CONNECTED VERTEX \t:\t")
                print("*" * 80)
                EdgeV7.append(NameV)
                
        if ch == 8:
            print("*" * 80)
            a8 = int(input("SOCIAL EMOTIONAL LEARNING HAS HOW MUCH DEGREE \t:\t"))
            for i in range(a8):
                NameV = input("ENTER THE NAME OF CONNECTED VERTEX \t\t:\t")
                print("*" * 80)
                EdgeV8.append(NameV)
                
        if ch == 9:
            print("*" * 80)
            a9 = int(input("HISTORY HAS HOW MUCH DEGREE \t\t:\t"))
            for i in range(a9):
                NameV = input("ENTER THE NAME OF CONNECTED VERTEX \t:\t")
                print("*" * 80)
                EdgeV9.append(NameV)
                
        if ch == 10:
            print("*" * 80)
            a10 = int(input("POLITICAL SCIENCE HAS HOW MUCH DEGREE \t:\t"))
            for i in range(a10):
                NameV = input("ENTER THE NAME OF CONNECTED VERTEX \t:\t")
                print("*" * 80)
                EdgeV10.append(NameV)
                
        if ch == 11:
            print("*" * 80)
            a11 = int(input("ECONOMICS HAS HOW MUCH DEGREE \t:\t"))
            for i in range(a11):
                NameV = input("ENTER THE NAME OF CONNECTED VERTEX \t:\t")
                print("*" * 80)
                EdgeV11.append(NameV)
                
        if ch == 12:
            print("*" * 80)
            a12 = int(input("MATHS2 HAS HOW MUCH DEGREE \t\t:\t"))
            for i in range(a12):
                NameV = input("ENTER THE NAME OF CONNECTED VERTEX \t:\t")
                print("*" * 80)
                EdgeV12.append(NameV)
                
        if ch == 13:
            print("*" * 80)
            a13 = int(input("MANAGEMENT HAS HOW MUCH DEGREE \t\t:\t"))
            for i in range(a13):
                NameV = input("ENTER THE NAME OF CONNECTED VERTEX \t:\t")
                print("*" * 80)
                EdgeV13.append(NameV)
                
        if ch == 14:
            print("*" * 80)
            a14 = int(input("PROGRAMMING2 HAS HOW MUCH DEGREE \t:\t"))
            for i in range(a14):
                NameV = input("ENTER THE NAME OF CONNECTED VERTEX \t:\t")
                print("*" * 80)
                EdgeV14.append(NameV)
                
        if ch == 15:
            print("*" * 80)
            a15 = int(input("BIOTECHNOLOGY HAS HOW MUCH DEGREE \t:\t"))
            for i in range(a15):
                NameV = input("ENTER THE NAME OF CONNECTED VERTEX \t:\t")
                print("*" * 80)
                EdgeV15.append(NameV)
                
        if ch == 16:
            print("*" * 80)
            a16 = int(input("MECHANICS HAS HOW MUCH DEGREE \t\t:\t"))
            for i in range(a16):
                NameV = input("ENTER THE NAME OF CONNECTED VERTEX \t:\t")
                print("*" * 80)
                EdgeV16.append(NameV)
                
        if ch == 17:
            print("*" * 80)
            a17 = int(input("ENTREPRENEURSHIP2 HAS HOW MUCH DEGREE \t:\t"))
            for i in range(a17):
                NameV = input("ENTER THE NAME OF CONNECTED VERTEX \t:\t")
                print("*" * 80)
                EdgeV17.append(NameV)
                
        if ch == 18:
            print("*" * 80)
            a18 = int(input("GEOGRAPHY HAS HOW MUCH DEGREE \t:\t"))
            for i in range(a18):
                NameV = input("ENTER THE NAME OF CONNECTED VERTEX \t:\t")
                print("*" * 80)
                EdgeV18.append(NameV)
                
        if ch == 19:
            print("*" * 80)
            a19 = int(input("COMMUNICATION HAS HOW MUCH DEGREE \t\t:\t"))
            for i in range(a19):
                NameV = input("ENTER THE NAME OF CONNECTED VERTEX \t:\t")
                print("*" * 80)
                EdgeV19.append(NameV)
                
        if ch == 20:
            print("*" * 80)
            a20 = int(input("PHILOSOPHY HAS HOW MUCH DEGREE \t:\t"))
            for i in range(a20):
                NameV = input("ENTER THE NAME OF CONNECTED VERTEX \t:\t")
                print("*" * 80)
                EdgeV20.append(NameV)
                
        if ch == 21:
            print("*" * 80)
            a21 = int(input("POLITICAL SCIENCE2 HAS HOW MUCH DEGREE \t:\t"))
            for i in range(a21):
                NameV = input("ENTER THE NAME OF CONNECTED VERTEX \t:\t")
                print("*" * 80)
                EdgeV21.append(NameV)
                
        if ch == 22:
            print("*" * 80)
            a22 = int(input("LINGUISICS HAS HOW MUCH DEGREE \t:\t"))
            for i in range(a22):
                NameV = input("ENTER THE NAME OF CONNECTED VERTEX \t:\t")
                print("*" * 80)
                EdgeV22.append(NameV)
                
        if ch == 23:
            print("*" * 80)
            a23 = int(input("SCIENCE AND SOCIETY HAS HOW MUCH DEGREE \t:\t"))
            for i in range(a23):
                NameV = input("ENTER THE NAME OF CONNECTED VERTEX \t:\t")
                print("*" * 80)
                EdgeV23.append(NameV)
                
        if ch == 24:
            print("*" * 80)
            a24 = int(input("HISTORY2 HAS HOW MUCH DEGREE \t\t:\t"))
            for i in range(a24):
                NameV = input("ENTER THE NAME OF CONNECTED VERTEX \t:\t")
                print("*" * 80)
                EdgeV24.append(NameV)
                
        if ch == 25:
            print("*" * 80)
            a25 = int(input("SOCIOLOGY HAS HOW MUCH DEGREE \t\t:\t"))
            for i in range(a25):
                NameV = input("ENTER THE NAME OF CONNECTED VERTEX \t:\t")
                print("*" * 80)
                EdgeV25.append(NameV)

    graph = {
        ListV[0]: [EdgeV1[0]],  # MATH
        ListV[1]: [EdgeV2[0]],  # PHY
        ListV[2]: [EdgeV3[0]],  # CHEM
        ListV[3]: [EdgeV4[0]],  # PR
        # CW
        ListV[5]: [EdgeV6[0]],  # EP
        # EVS
        ListV[7]: [EdgeV8[0]],  # SEL
        ListV[8]: [EdgeV9[0]],  # HIS
        ListV[9]: [EdgeV10[0]],  # POLS
        # ECO
        ListV[11]: [EdgeV12[0]],  # MATH2
        # MNG
        ListV[13]: [EdgeV14[0]],  # PR2
        ListV[14]: [EdgeV15[0]],  # BT
        ListV[15]: [EdgeV16[0]],  # MECH
        ListV[16]: [EdgeV17[0]],  # EP2
        # GEO
        # COM
        # PHIL
        ListV[20]: [EdgeV21[0]],  # POLS2
        # LNG
        # SAS
        ListV[23]: [EdgeV24[0]],  # HIS2
        ListV[24]: [EdgeV25[0]],  # SOC
    }

    result = colour_vertices(graph)
    print(result)
    NoDegree()
    SeeGraph()
    STYLES(" GRAPH COLOURING ")

inputVertex()
