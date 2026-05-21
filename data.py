from snack import Snack
import csv

data = {}

with open('healthier_snacks.csv') as file:
    reader = csv.DictReader(file)                           
    for row in reader:
        calories = int(row['calories'])
        macros = {
            'protein': int(row['protein']),
            'carbs':   int(row['carbs']),
            'fat': int(row['fat']),
            'sugar': int(row['sugar'])
            }
        ingredients = row['ingredients'].split(';')
        flavors = row['flavors'].split(';')
        brand = row['brand']
        product_type = row['product']
        why_better = row['why_better']
        snack = Snack(brand, product_type, why_better, calories, ingredients, macros, flavors)
        
        category = row['category']
        if category not in data:           
            data[category] = []             
        data[category].append(snack)
if __name__ == "__main__":
    print(data.keys())
    print(f"\nNumber of chips brands: {len(data['chips'])}")
    print(f"\nFirst chip brand:\n{data['chips'][0]}")
    print(f"\nLast pasta brand:\n{data['pasta'][-1]}")           