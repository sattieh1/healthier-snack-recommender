from data import data
from min_heap import MinHeap

def find_category_by_query(categories, query):
    results = []
    # 1. Lowercase the query once outside the loop
    query_lower = query.lower()
    query_len = len(query_lower)

    
    for category in categories:
        # 2. Lowercase the individual category
        category_lower = category.lower()
        
        # Skip categories that are shorter than the query
        if len(category_lower) < query_len:
            continue
            
        # Check character by character
        is_match = True
        for i in range(query_len):
            if category_lower[i] != query_lower[i]:
                is_match = False
                break  # Stop checking this category immediately
                
        if is_match:
            results.append(category)  # Keeps original casing in results
            
    return results

def show_categories(categories):
    return input(f"Here are the categories: {', '.join(categories)} \nplease start typing: ")
    
def select_category():
    categories = list(data.keys())
    user_input = show_categories(categories)
    confirm = False                                    
    while not confirm:                            
        results = find_category_by_query(categories, user_input)   
        if len(results) > 1:
            print(f"Several matches: {', '.join(results)}")
            user_input = input("please continue typing to select a category: ")
        elif len(results) < 1:
            print(f"Here are the categories again: {', '.join(categories)}")                     
            user_input = input("sorry no match found, please type again: ")
        else:
            confirmation = input(f"Do you want a healthier alternative to {results[0]}? y/n: ")
            if confirmation.lower() == "y":                    
                confirm = True                         
            else:
                user_input = show_categories(categories)                      
    return results[0]

def sort_snacks(snacks, key):
    heap = MinHeap(key)
    for snack in snacks:          # loop 1: fill the heap (sift-up each time)
        heap.add(snack)

    result = []
    while not heap.is_empty():              # loop 2: empty the heap (sift-down each time)
        result.append(heap.remove_min())
    return result

def display_snacks(snacks):
    print("\nHere are your healthier options, lowest calories first:\n")
    for number, snack in enumerate(snacks, start=1):
        print(f"Option {number}:")
        print(snack)
        print("-" * 40 + "\n") 

def main():
    print("Welcome to the healthier lifestyle...\n I am going to help you find healthier alternatives to your favorite snacks")                       # a welcome message
    category = select_category()      
    snacks = data[category]                    
    sorted_snacks = sort_snacks(snacks, key=lambda s: s.calories)             
    display_snacks(sorted_snacks)             

if __name__ == "__main__":
    main()       

                                      
   