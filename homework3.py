#from fileinput import filename
import os

def add_receipe(filename):
    with open(filename,'a') as file:
        title = input("Введите название блюда: ")
        file.write(title + '\n')

        num_ingredients = int(input("Введите количество ингредиентов: "))
        file.write(str(num_ingredients) + '\n')

        for i in range(num_ingredients):
            ingredient = input ("Введите название ингредиента: ")
            ingredient_qty = float(input ("Введите количество, массу или объем игредиента: "))
            ingredient_unit = input ("Введите единицу измерения: ")

            file.write(f"{ingredient} | {ingredient_qty} | {ingredient_unit}\n")

        print(f"Рецепт '{title}' добавлен успешно!")

def view_receipes(filename):
    if not os.path.exists(filename):
        print("Файл с рецептами не найден.")
        return

    with open(filename, 'r') as file:
        content = file.readlines()

    i=0
    while i < len(content):
        title = content[i].strip()
        num_ingredients = int (content[i+1].strip())
        print(f"Название блюда: {title}")
        print(f"Количество ингредиентов: {num_ingredients}")

        for j in range(num_ingredients):
            ingredient_info = content[i+2+j].strip()
            print(f"Ингредиент {j+1}: {ingredient_info}")
        i += 2 + num_ingredients

def get_cookbook(filename):
    if not os.path.exists(filename):
        print("Файл с рецептами не найден.")
        return

    cook_book = {}

    with open(filename, 'r') as file:
        content = file.readlines()

    i = 0
    while i < len(content):
        title = content[i].strip()  # Название блюда
        num_ingredients = int(content[i + 1].strip())  # Количество ингредиентов

        ingredients_list = []
        for j in range(num_ingredients):
            ingredient_info = content[i + 2 + j].strip().split(' | ')
            ingredient_name = ingredient_info[0]
            quantity = float(ingredient_info[1])
            measure = ingredient_info[2]

            ingredients_list.append({
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            })

        cook_book[title] = ingredients_list
        i += 2 + num_ingredients  # Переходим к следующему рецепту

    return cook_book


def get_shop_list_by_dishes(dishes, person_count,cook_book):
    shop_list = {}

    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                ingredient_name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count
                measure = ingredient['measure']

                if ingredient_name in shop_list:
                    shop_list[ingredient_name]['quantity'] += quantity
                else:
                    shop_list[ingredient_name] = {
                        'measure': measure,
                        'quantity': quantity
                    }
        else:
            print(f"Рецепт '{dish}' не найден в cook_book.")

    return shop_list

def main():
    filename = "recipes.txt"

    while True:
        print("\nКулинарная книга")
        print("1. Добавить рецепт")
        print("2. Просмотреть рецепты")
        print("3. Формирование словаря cook_book")
        print("4. Получить список для покупки нужных ингредиентов блюд")
        print("5. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            add_receipe(filename)
        elif choice == '2':
            view_receipes(filename)
        elif choice == '3':
            cook_book=get_cookbook(filename)
            print(cook_book)
        elif choice == '4':
            cook_book = get_cookbook(filename)
            dishes_input = input ("Введите названия блюд через запятую: ")
            dishes = [dish.strip() for dish in dishes_input.split(',')]
            person_count = int(input("Введите количество персон: "))

            shop_list = get_shop_list_by_dishes(dishes, person_count,cook_book)
            print(shop_list)
        elif choice == '5':
            print("Выход из программы.")
            break
        else:
            print("Неверный ввод, попробуйте снова")
if __name__ == "__main__":
    main()



