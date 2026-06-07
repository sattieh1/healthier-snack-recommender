class Snack:
    def __init__(self, brand, product_type, why_better, calories, ingredients, macros, flavors):
         self.brand = brand
         self.product_type = product_type
         self.why_better = why_better
         self.calories = calories
         self.ingredients = ingredients
         self.macros = macros
         self.flavors = flavors

    def __str__(self):
        return f"""Brand {self.brand}'s {self.product_type} are better for you because it is {self.why_better} and has {self.calories} calories per 100 grams 
The representative list of ingredient(s) {self.format_method(self.ingredients)}.
The representative macros are {self.format_macros()} 
The available flavor(s) {self.format_method(self.flavors)}"""
    
    def format_macros(self):
        return ", ".join([f"{k}: {v}g" for k, v in self.macros.items()])
    def format_method(self, items):
        if len(items) < 2:
            return f"is {', '.join(items)}"
        return f"are {', '.join(items[:-1])} and {items[-1]}"
    
    def __repr__(self):
        return f"Snack({self.brand}, {self.product_type})"
    
if __name__ == "__main__":
    test_snack = Snack(
        brand="Siete",
        product_type="Tortilla Chips",
        why_better="grain-free and low sugar",
        calories=140,
        ingredients=["cassava flour", "avocado oil", "sea salt"],
        macros={"protein": 2, "carbs": 19, "fat": 7, "sugar": 0},
        flavors=["Sea Salt", "Lime", "Nacho", "Chipotle BBQ"]
    )
    print(test_snack)