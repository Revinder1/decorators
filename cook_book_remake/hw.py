from decorators.decor_hw import logging



def get_file(file_name):
    cook_book = dict()
    with open(file_name, mode='r', encoding='utf-8') as file:
        for line in file:
            name = line.strip()
            ingredients_quantity = int(file.readline().strip())
            for ingredient in range(ingredients_quantity):
                x = file.readline().strip()
                ingr_list = x.split("|")
                ingredients = dict()
                ingredients['Ingredient_name'] = ingr_list[0].strip()
                ingredients['quantity'] = int(ingr_list[1].strip())
                ingredients['measure'] = ingr_list[2].strip()
                if name in cook_book:
                    cook_book[name] += [ingredients]
                else:
                    cook_book[name] = [ingredients]
            file.readline()
    return cook_book


cook_book = get_file('recipes.txt')


@logging('C:/Users/Ярослав/PycharmProjects/pythonProject/cook_book_remake/')
def get_shop_list_by_dishes(dishes, person_count):
    shop_list = dict()
    already_ordered = []
    for dish in dishes:
        for ingredient in cook_book[dish]:
            if dish not in already_ordered:
                x = ingredient['Ingredient_name']
                new_dict = dict(ingredient)
                new_dict['quantity'] *= person_count
                if x not in shop_list:
                    shop_list[x] = new_dict
                else:
                    shop_list[x]['quantity'] += new_dict['quantity']
            else:
                x = ingredient['Ingredient_name']
                shop_list[x]['quantity'] *= person_count
        already_ordered.append(dish)
    for i in shop_list.values():
        del i['Ingredient_name']
    return shop_list


if __name__ == '__main__':
    print(get_shop_list_by_dishes(['Омлет', 'Омлет'], 2))
