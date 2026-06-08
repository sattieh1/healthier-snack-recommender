from data import data

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
if __name__ == "__main__":
    categories = list(data.keys())
    print(find_category_by_query(categories, "c"))      # expect chips, chocolate, candy, cereal
    print(find_category_by_query(categories, "ch"))     # expect chips, chocolate
    print(find_category_by_query(categories, "chi"))    # expect chips
    print(find_category_by_query(categories, "xyz"))    # expect []