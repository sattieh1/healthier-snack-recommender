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

def select_category():
    user_input = input("please start typing: ")
    confirm = False                                    
    while confirm == False:                            
        categories = list(data.keys())
        results = find_category_by_query(categories, user_input)   
        print(results)
        if len(results) > 1:
            user_input = input("continue typing: ")
        elif len(results) < 1:
            print(categories)                          
            user_input = input("no match found, type again: ")
        else:
            confirmation = input(f"is {results} what you want? y/n: ")
            if confirmation.lower() == "y":                    
                confirm = True                         
            else:
                confirm = False                        
    return results[0]

def sort_snacks(snacks, key):
    heap = MinHeap(key)
    for snack in snacks:          # loop 1: fill the heap (sift-up each time)
        heap.add(snack)

    result = []
    while heap.heap:              # loop 2: empty the heap (sift-down each time)
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

                                      
   