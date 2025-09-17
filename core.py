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

        # print({
        #     'restaurant_type':restaurant_type,
        #     'products':products,
        #     'product_to_add':product_to_add
        # })
        
        ables = CheckRestaurantAbleToAddRecipe({
            'restaurant_type':restaurant_type,
            'products':products,
            'product_to_add':product_to_add
        }).RunModel()

        # print(ables, restaurant_type, product_to_add)

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

clients_of_location_1 = clients[clients['location'] == 'Setor 1']
restaurants_of_location_1 = restaurants[restaurants['location'] == 'Setor 1']

clients_of_location_2 = clients[clients['location'] == 'Setor 2']
restaurants_of_location_2 = restaurants[restaurants['location'] == 'Setor 2']

clients_of_location_3 = clients[clients['location'] == 'Setor 3']
restaurants_of_location_3 = restaurants[restaurants['location'] == 'Setor 3']

clients_of_location_4 = clients[clients['location'] == 'Setor 4']
restaurants_of_location_4 = restaurants[restaurants['location'] == 'Setor 4']

products_for_search_recive = []

clients_item_not_found__location_1 = clients_of_location_1[clients_of_location_1['item_found'] == False]
clients_item_not_found__location_2 = clients_of_location_2[clients_of_location_2['item_found'] == False]
clients_item_not_found__location_3 = clients_of_location_3[clients_of_location_3['item_found'] == False]
clients_item_not_found__location_4 = clients_of_location_4[clients_of_location_4['item_found'] == False]

top5_location1 = Top5(clients_item_not_found__location_1)
top5_location2 = Top5(clients_item_not_found__location_2)
top5_location3 = Top5(clients_item_not_found__location_3)
top5_location4 = Top5(clients_item_not_found__location_4)

itens_to_search = []

itens_to_search = CheckAble(restaurants_of_location_1, top5_location1, itens_to_search)
itens_to_search = CheckAble(restaurants_of_location_2, top5_location2, itens_to_search)
itens_to_search = CheckAble(restaurants_of_location_3, top5_location3, itens_to_search)
itens_to_search = CheckAble(restaurants_of_location_4, top5_location4, itens_to_search)

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
    final_response.append({'restaurant':restaurant,
                           'obs':response['obs'],})
    print(item)

final_df = pd.DataFrame(final_response)
final_df.to_csv('final_result.csv', index=False)
# Se sim, verificar se produtos condizem com receita e se precisa de adaptação;
