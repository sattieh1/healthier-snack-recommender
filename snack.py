class Snack:
    def __init__(self, brand, product, why_better, calories, ingredients, macros):
         self.brand = brand
         self.product = product
         self.why_better = why_better
         self.calories = calories
         self.ingredients = ingredients
         self.macros = macros

    def __str__(self):
        return f"""This {self.product} from brand {self.brand} is better for you because it is {self.why_better} and has {self.calories} calories per 100 gram 
The list of ingredients are {self.format_ingredients()}
The macros are {self.format_macros()} """
    
    def format_macros(self):
        return ", ".join([f"{k}: {v}g" for k, v in self.macros.items()])
    def format_ingredients(self):
        return  ", ".join(self.ingredients)
    
if __name__ == "__main__":
    test_snack = Snack(
        brand="Siete",
        product="Tortilla Chips",
        why_better="grain-free and low sugar",
        calories=140,
        ingredients=["cassava flour", "avocado oil", "sea salt"],
        macros={"protein": 2, "carbs": 19, "fat": 7, "sugar": 0}
    )
    print(test_snack)