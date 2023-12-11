with open('recipes.txt', 'r', encoding='utf-8') as file:
    cook_book = {}
    for dish in file:
        ingredients_count = int(file.readline())
        ingredients = []
        for ingredient in range(ingredients_count):
            name, quantity, measure = file.readline().strip().split('|')
            ingredients.append({
                'ingredient_name' : name,
                'quantity' : quantity,
                'measure': measure
            })
        file.readline()
        cook_book[dish.strip()] = ingredients


def get_shop_list_by_dishes(dishes, person_count):
    ingredients_to_cooking = {}
    dish = []
    for i in dishes:
        dish.append(cook_book[i])       
    for j in dish:
            for i in j:
                 if i['ingredient_name'] not in ingredients_to_cooking:
                      ingredients_to_cooking[i['ingredient_name']] = {'mesuare': (i['measure']), 'quantity': (int(i['quantity']) * person_count)}
                 else:
                      q = int(i['quantity']) * person_count
                      ingredients_to_cooking[i['ingredient_name']] = {'measure': (i['measure']),
                                                               'quantity': (q + int(i['quantity']) * person_count)}                     
                 
    return ingredients_to_cooking
    
print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))