dishes = [{"name":"Alu Gobi","price":"994.82"},{"name":"Alu Matar","price":"55.61"},{"name":"Barfi","price":"374.40"},{"name":"Beef Vindaloo","price":"77.62"},{"name":"Butter Chicken","price":"782.52"},{"name":"Carrot Halwa","price":"783.73"},
          {"name":"Chaat Papri","price":"663.73"},{"name":"Cham-Cham","price":"567.28"},{"name":"Chana Dal","price":"981.52"},{"name":"Chana Masala","price":"377.18"},{"name":"Chapati","price":"397.65"},{"name":"Chicken 65","price":"850.09"},
          {"name":"Chicken Biriyani","price":"617.17"}, {"name":"Chicken Tikka","price":"63.01"},{"name":"Chili Chicken","price":"575.83"},{"name":"Coriander Chutney","price":"633.36"},{"name":"Dal Makhani","price":"834.69"},{"name":"Date Tamarind Chutney","price":"709.57"},
          {"name":"Dhokla","price":"106.84"},{"name":"Gulab Jamun","price":"893.48"},{"name":"Idili","price":"154.59"},{"name":"Jalebi","price":"344.13"},{"name":"Mutton Kheema","price":"100.57"},{"name":"Kheer","price":"839.09"},{"name":"Kulfi","price":"409.05"},
          {"name":"Laddu","price":"547.87"},{"name":"Chicken Kebabs","price":"786.17"},{"name":"Chicken Vindaloo","price":"999.93"},{"name":"Lime Pickle","price":"539.86"},{"name":"Veg Balls With Sauce","price":"819.44"},{"name":"Mango Lassi","price":"318.21"},
          {"name":"Masala Chai","price":"112.89"},{"name":"Masala Dosa","price":"730.88"},{"name":"Masoor Dal","price":"848.79"},{"name":"Medu Vada","price":"952.15"},{"name":"Naan","price":"883.85"},{"name":"Missal Pav","price":"138.18"},{"name":"Onion Pakora","price":"971.00"},
          {"name":"Papadum","price":"535.06"},{"name":"Egg Pulao","price":"472.54"}]

choice = input('Are you vegetarian or non-vegetarian:')  # input the choice
print("|==============>MENU<==============|")

# vegetarian
if choice == "vegetarian":
    filt = ['Chicken Vindaloo','Chili Chicken', 'Beef Vindaloo', 'Chicken 65','Butter Chicken', 'Chicken Biriyani','Chicken Tikka', 'Beef','Egg Pulao', 'Chicken Kebabs', 'Mutton Kheema']

    filtered_dict = [d for d in dishes if d['name'] not in filt]  # vegetarian dishes only

    for index, value in enumerate(filtered_dict):  # print vegetarian list sequentially
        name = value['name']
        price = value['price']
        print("{}. {} - {}".format(index, name, price))  # print

# non-vegetarian dishes with sequentially
elif choice == "non-vegetarian":
    for index, value in enumerate(dishes):
        name = value['name']
        price = value['price']
        print("{}. {} - {}".format(index, name, price))
else:
    print('Please Enter correct choice: Vegetarian or non-vegetarian') # if input is incorrect


