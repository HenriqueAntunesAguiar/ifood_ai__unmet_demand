import pandas as pd
from ai_core import QueryRecipe, CheckRestaurantAbleToAddRecipe, CheckIngredientsToRecipeAndRestaurant

def Top5(clients_item_not_found):
    
    top5=[]

    for i in range(0,5):

        top5.append(clients_item_not_found.searched_item.value_counts().head(5).index[i])
        print(clients_item_not_found.searched_item.value_counts())
        
    return top5    
    
def CheckAble(restaurants_of_location, top5_location, itens_to_search):

    for restaurant_line in restaurants_of_location.values:
        
        restaurant=restaurant_line[0]
        restaurant_type=restaurant_line[1]
        products=restaurant_line[2]
        product_to_add=top5_location
        
        ables = CheckRestaurantAbleToAddRecipe({
            'restaurant_type':restaurant_type,
            'products':products,
            'product_to_add':product_to_add
        }).RunModel()

        i=0

        for able in ables['able']:

            if able:

                itens_to_search.append(
                    {
                        'restaurant':restaurant,
                        'new_product':product_to_add[i]
                    }
                )

            i += 1

    return itens_to_search

clients = pd.read_csv('clients.csv')
restaurants = pd.read_csv('restaurants.csv')

datas_per_location = {}

datas_per_location['Setor 1'] = {'clients':clients[clients['location'] == 'Setor 1'],
                                 'restaurants':restaurants[restaurants['location'] == 'Setor 1']}

datas_per_location['Setor 2'] = {'clients':clients[clients['location'] == 'Setor 2'],
                                 'restaurants':restaurants[restaurants['location'] == 'Setor 2']}

datas_per_location['Setor 3'] = {'clients':clients[clients['location'] == 'Setor 3'],
                                 'restaurants':restaurants[restaurants['location'] == 'Setor 3']}

datas_per_location['Setor 4'] = {'clients':clients[clients['location'] == 'Setor 4'],
                                 'restaurants':restaurants[restaurants['location'] == 'Setor 4']}

datas_per_location['Setor 1'].update({'not_found':datas_per_location['Setor 1']['clients'][datas_per_location['Setor 1']['clients']['item_found'] == False]})
datas_per_location['Setor 2'].update({'not_found':datas_per_location['Setor 2']['clients'][datas_per_location['Setor 2']['clients']['item_found'] == False]})
datas_per_location['Setor 3'].update({'not_found':datas_per_location['Setor 3']['clients'][datas_per_location['Setor 3']['clients']['item_found'] == False]})
datas_per_location['Setor 4'].update({'not_found':datas_per_location['Setor 4']['clients'][datas_per_location['Setor 4']['clients']['item_found'] == False]})

top5_location1 = Top5(datas_per_location['Setor 1']['not_found'])
top5_location2 = Top5(datas_per_location['Setor 2']['not_found'])
top5_location3 = Top5(datas_per_location['Setor 3']['not_found'])
top5_location4 = Top5(datas_per_location['Setor 4']['not_found'])

datas_per_location['Setor 1'].update({'top_5':top5_location1})
datas_per_location['Setor 2'].update({'top_5':top5_location2})
datas_per_location['Setor 3'].update({'top_5':top5_location3})
datas_per_location['Setor 4'].update({'top_5':top5_location4})

itens_to_search = []

itens_to_search = CheckAble(datas_per_location['Setor 1']['restaurants'], datas_per_location['Setor 1']['top_5'], itens_to_search)
itens_to_search = CheckAble(datas_per_location['Setor 2']['restaurants'], datas_per_location['Setor 2']['top_5'], itens_to_search)
itens_to_search = CheckAble(datas_per_location['Setor 3']['restaurants'], datas_per_location['Setor 3']['top_5'], itens_to_search)
itens_to_search = CheckAble(datas_per_location['Setor 4']['restaurants'], datas_per_location['Setor 4']['top_5'], itens_to_search)

products_to_search_recipe = []

for item in itens_to_search:
    products_to_search_recipe.append(item['new_product'])
    print(item)

products_to_search_recipe_v2 = list(set(products_to_search_recipe))

recipes_seachered = {}

for product in products_to_search_recipe_v2:
    
    recipe = QueryRecipe(product).RunModel()
    recipes_seachered.update({recipe['recipe_name']:recipe['recipe_ingredients']})
        
    print(products_to_search_recipe_v2.index(product), len(products_to_search_recipe_v2))

final_response = []

for item in itens_to_search:
    
    restaurant = item['restaurant']
    new_product = item['new_product']
    restaurant_ingredients = list(restaurants[restaurants['name']==restaurant].ingredients.values)
    recipe_ingredients = recipes_seachered[new_product]
    
    response = CheckIngredientsToRecipeAndRestaurant(
                    {
                        'restaurant_ingredients':restaurant_ingredients,
                        'recipe_ingredients':recipe_ingredients,
                        'recipe_name':new_product,
                    }
                ).RunModel()
    
    location = list(restaurants[restaurants['name']==restaurant].location.values)[0]
    potential_customers = datas_per_location[location]['not_found'].value_counts()[new_product].values[0]

    final_response.append({'restaurant':restaurant,
                           'location':location,
                           'potential_customers':potential_customers,
                           'obs':response['obs'],                           
                           })
    
    
    print(item)   
    
final_df = pd.DataFrame(final_response)
final_df.to_csv('final_result.csv', index=False)
