from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class DataBun:
    bun_name = 'Чиабатта'
    bun_price = 429

class DataIngredient:
    sause_name = 'Пикадор'
    topping_name = 'Крем-фрэш'
    sause_type = 'Итальянский'
    topping_type = 'Сливочный'
    sause_price = 228
    topping_price = 322

class DataPriceAllBurger:
    price_burger = DataIngredient.sause_price + DataIngredient.topping_price + DataBun.bun_price * 2

class DataBaseIngredientAndBun:
    database_buns = [
        [0,'black bun',100],
        [1,'white bun',200],
        [2,'red bun',300]
    ]

    database_ingredients = [
        [0, INGREDIENT_TYPE_SAUCE, "hot sauce", 100],
        [1, INGREDIENT_TYPE_SAUCE, "sour cream", 200],
        [2, INGREDIENT_TYPE_SAUCE, "chili sauce", 300],

        [3, INGREDIENT_TYPE_FILLING, "cutlet", 100],
        [4, INGREDIENT_TYPE_FILLING, "dinosaur", 200],
        [5, INGREDIENT_TYPE_FILLING, "sausage", 300]
    ]





