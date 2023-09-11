#sheiqmnas razmis wevrebis sia vis saxel da gvarshi 2-ze meti i iqneba gaudides pirveli aso da shevides axal siashi super sia
razmis_wevrebis_sia = ["gio gagnidze" , "nikoloz gogniashvili" , "qevxishvili" , "jemiko qiqava" , "giorgi gelashvili" , "luka turadze" , "nikoloz nawyebia" , "luka zazashvili" , "davit meparishvili" , "luka tevzadze"]
super_sia = []
I_count = 0
for element in razmis_wevrebis_sia: 
    I_count = 0
    for char in element:
        if char == "i":
            I_count += 1
    if I_count > 2:
        super_sia.append(element.capitalize())
print(super_sia)