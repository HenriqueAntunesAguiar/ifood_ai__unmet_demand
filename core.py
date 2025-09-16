import pandas as pd

def Top5(products_for_search_recive, clients_item_not_found):
    
    for i in range(0,5):
        products_for_search_recive.append(clients_item_not_found.searched_item.value_counts().head(5).index[i])
        print(i)

    return products_for_search_recive    
    
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

products_for_search_recive = Top5(products_for_search_recive, clients_item_not_found__location_1)
products_for_search_recive = Top5(products_for_search_recive, clients_item_not_found__location_2)
products_for_search_recive = Top5(products_for_search_recive, clients_item_not_found__location_3)
products_for_search_recive = Top5(products_for_search_recive, clients_item_not_found__location_4)

products_for_search_recive_v2 = list(set(products_for_search_recive))

import requests
import os, dotenv

dotenv.load_dotenv()
api_key = os.getenv('API_KEY__SPOONACULAR')

API_KEY = api_key
for product in products_for_search_recive_v2:
    ...

    