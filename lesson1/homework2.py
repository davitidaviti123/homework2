#თქვენი რაზმის წევრებიდან ვისი სახელი და გვარის სიგრძე ნაკლებია 16 სიმბოლოზე, გაუდიდდეს სახელი და გვარი და დაიპრინტოს გადიდებულად.
razmis_wevrebis_sia = ["gio gagnidze" , "nikoloz gogniashvili" , "qevxishvili" , "jemiko qiqava" , "giorgi gelashvili" , "luka turadze" , "nikoloz nawyebia" , "luka zazashvili" , "davit meparishvili" , "luka tevzadze"]
for element in razmis_wevrebis_sia:
    if len(element) < 16:
        print(element.upper())