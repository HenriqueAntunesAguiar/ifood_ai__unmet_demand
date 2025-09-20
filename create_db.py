import random
import pandas as pd

class CreateDb():

    def __init__(self):

        self.clients = []
        self.products_list = []

        self.restaurants_db()
        self.restaurants_per_ticket = [self.restaurant_high_ticket, self.restaurant_medium_high_ticket, self.restaurant_medium_ticket, self.restaurant_low_ticket]
        self.client_db()
        
    def restaurants_db(self):

        self.restaurant_high_ticket = [
            {
                'name':'Restaurante 1',
                'type':'Steakhouse Premium',
                'products':['Wagyu','Prime Rib Dry Aged','Tomahawk','Filé Mignon com Foie Gras','Ribeye Black Angus','Chateaubriand'],
                'ingredients':["carne wagyu A5","sal Maldon","azeite de oliva","pimenta-do-reino moída na hora","costela bovina maturada","manteiga","alho","alecrim fresco","tomilho","corte de costela com osso longo","chimichurri (salsa, orégano, alho, azeite, vinagre)","sal grosso","filé mignon alto","foie gras","vinho do Porto","pimenta preta","ribeye angus","legumes grelhados (abobrinha, pimentão, cebola roxa)","sal marinho","filé central bovino","batatas rústicas","manteiga trufada"],
                'location':'Setor 1'
            },
            {
                'name':'Restaurante 2',
                'type':'Restaurante Japonês de Luxo',
                'products':['Sashimi de Toro','Nigiri de Uni','Tataki de Wagyu','Sushi de Enguia','Temaki de Caviar','Ramen Trufado'],
                'ingredients':["atum bluefin (parte gordurosa)","shoyu","wasabi fresco","gengibre em conserva","arroz japonês temperado (vinagre de arroz, açúcar, sal)","ouriço-do-mar","alga nori","carne wagyu selada","molho ponzu (shoyu, limão, saquê)","cebolinha","gergelim torrado","enguia grelhada","molho tare (shoyu doce)","sementes de gergelim","caviar","pepino em tiras","creme de wasabi","caldo de ossobuco","noodles de trigo","ovo cozido","cogumelos shiitake","óleo de trufa negra"],
                'location':'Setor 2'
            },
            {
                'name':'Restaurante 3',
                'type':'Francesa',
                'products':['Foie Gras','Coq au Vin','Bouillabaisse','Filé Rossini','Ratatouille','Soufflé de Chocolate'],
                'ingredients':["fígado de pato","brioche tostado","figo","redução de vinho branco","frango caipira","vinho tinto borgonha","cogumelos Paris","bacon","cebola pérola","ervas de Provence","peixes variados (rouget, robalo, dourada)","camarão","mexilhão","tomate","alho","açafrão","azeite de oliva","trufas negras","molho demi-glace","berinjela","abobrinha","pimentão","cebola","manjericão","chocolate amargo","ovos","açúcar","licor Grand Marnier"],
                'location':'Setor 1'
            },
            {
                'name':'Restaurante 4',
                'type':'Frutos do Mar Premium',
                'products':['Lagosta Grelhada','King Crab','Ostras Frescas','Linguado com Trufas','Risoto de Camarão','Caviar com Blinis'],
                'ingredients':["lagosta","manteiga","alho","ervas finas (salsa, tomilho, estragão)","limão siciliano","caranguejo-real","vinho branco","creme de leite fresco","cebolinha","ostras","molho mignonette (vinagre de vinho tinto, chalota, pimenta)","linguado fresco","trufa branca","creme de leite","arroz arbóreo","cebola","parmesão","blinis (farinha, leite, ovos, fermento)","crème fraîche"],
                'location':'Setor 1'
            }
            ]  
        
        self.restaurant_medium_high_ticket = [
            {
                'name':'Restaurante 5',
                'type':'Italiana Premium',
                'products':['Risoto de Funghi','Pappardelle ao Ragu de Cordeiro','Ravioli de Ricota e Espinafre','Gnocchi ao Sugo','Polvo Grelhado','Tiramisu'],
                'ingredients':["arroz arbóreo","funghi seco","parmesão","azeite de oliva","massa fresca","cordeiro","tomate","alho","cebola","ervas de Provence","ricota","espinafre","farinha de trigo","batata","polvo","limão siciliano","cacau","café","ovos","açúcar","mascarpone"],
                'location':'Setor 1'
            },
            {
                'name':'Restaurante 6',
                'type':'Brasileira Contemporânea',
                'products':['Moqueca de Peixe','Bobó de Camarão','Arroz de Pato','Costela com Mandioca','Farofa de Banana','Pudim de Leite'],
                'ingredients':["peixe branco","camarão","pato","arroz","mandioca","banana","farinha de mandioca","óleo de dendê","leite de coco","pimentão","cebola","tomate","coentro","costela bovina","alho","ovos","açúcar","leite condensado"],
                'location':'Setor 2'
            },
            {
                'name':'Restaurante 7',
                'type':'Mediterrânea',
                'products':['Salada Grega','Moussaka','Polvo à Lagareiro','Paella Valenciana','Cordeiro Assado','Creme Catalão'],
                'ingredients':["azeite de oliva","pepino","tomate","azeitona preta","queijo feta","berinjela","batata","carne moída","polvo","arroz","açafrão","frango","camarão","mariscos","cordeiro","ervas finas","leite","ovos","canela","açúcar"],
                'location':'Setor 3'
            },
            {
                'name':'Restaurante 8',
                'type':'Churrascaria Premium',
                'products':['Picanha','Alcatra na Brasa','Fraldinha','Linguiça Artesanal','Costelão','Abacaxi Grelhado'],
                'ingredients':["picanha","alcatra","fraldinha","linguiça artesanal","costela bovina","sal grosso","carvão","abacaxi","açúcar mascavo"],
                'location':'Setor 3'
            },
                {
                'name':'Restaurante 9',
                'type':'Churrascaria Premium',
                'products':['Picanha','Alcatra na Brasa','Fraldinha','Linguiça Artesanal','Costelão','Abacaxi Grelhado'],
                'ingredients':["picanha","alcatra","fraldinha","linguiça artesanal","costela bovina","sal grosso","carvão","abacaxi","açúcar mascavo"],
                'location':'Setor 4'
            }
        ]
        
        self.restaurant_medium_ticket = [
            {
                'name':'Restaurante 10',
                'type':'Italiana Tradicional',
                'products':['Spaghetti à Bolonhesa','Lasagna','Pizza Margherita','Fettuccine Alfredo','Polenta Cremosa','Panna Cotta'],
                'ingredients':["massa seca","molho de tomate","carne moída","queijo parmesão","presunto","muçarela","manjericão","creme de leite","manteiga","milho de fubá","gelatina","baunilha"],
                'location':'Setor 2'
            },
            {
                'name':'Restaurante 11',
                'type':'Comida Árabe',
                'products':['Kibe Assado','Esfiha de Carne','Homus','Tabule','Kafta','Baklava'],
                'ingredients':["trigo para kibe","carne moída","hortelã","alho","cebola","azeite de oliva","grão-de-bico","tahine","salsinha","tomate","arroz","nozes","mel","massa folhada"],
                'location':'Setor 3'
            },
            {
                'name':'Restaurante 12',
                'type':'Mexicana',
                'products':['Tacos de Carne','Burrito de Frango','Quesadilla','Nachos com Guacamole','Chili com Carne','Churros'],
                'ingredients':["tortilla de milho","carne bovina","frango desfiado","queijo cheddar","tomate","abacate","feijão vermelho","pimenta chili","cebola","alho","açúcar","canela"],
                'location':'Setor 4'
            }
        ]

        self.restaurant_low_ticket = [
            {
                'name':'Restaurante 14',
                'type':'Lanchonete',
                'products':['X-Salada','X-Bacon','Cachorro-Quente','Batata Frita','Misto Quente','Milkshake'],
                'ingredients':["pão de hambúrguer","carne bovina","queijo prato","alface","tomate","bacon","salsicha","batata","presunto","pão de forma","sorvete","leite"],
                'location':'Setor 2'
            },
            {
                'name':'Restaurante 15',
                'type':'Self-service Popular',
                'products':['Arroz Branco','Feijão Preto','Frango Grelhado','Carne de Panela','Farofa Simples','Gelatina'],
                'ingredients':["arroz","feijão preto","frango","óleo de soja","alho","carne bovina","farinha de mandioca","ovo cozido","cenoura","gelatina em pó","açúcar"],
                'location':'Setor 3'
            },
            {
                'name':'Restaurante 16',
                'type':'Pizzaria Popular',
                'products':['Pizza de Calabresa','Pizza de Muçarela','Pizza Portuguesa','Pizza de Frango com Catupiry','Pizza de Chocolate','Esfiha Doce'],
                'ingredients':["massa de pizza","molho de tomate","calabresa","muçarela","presunto","ovo","pimentão","frango desfiado","catupiry","chocolate","banana","canela"],
                'location':'Setor 4'
            },
            {
                'name':'Restaurante 17',
                'type':'Prato Feito',
                'products':['Arroz com Feijão','Bife Acebolado','Frango à Milanesa','Omelete','Macarrão ao Sugo','Salada Simples'],
                'ingredients':["arroz","feijão carioca","bife bovino","cebola","frango","farinha de rosca","ovo","macarrão","molho de tomate","alface","tomate","cenoura","óleo"],
                'location':'Setor 4'
            }
        ]
        
        self.restaurants = self.restaurant_high_ticket + self.restaurant_medium_high_ticket + self.restaurant_medium_ticket + self.restaurant_low_ticket

    def products(self):
        
        self.product_per_location = {}

        

        for restaurant in self.restaurants:
            self.products_list += restaurant['products']

            for product in restaurant['products']:
                
                try:
                    if restaurant['location'] not in self.product_per_location[product]:
                        self.product_per_location[product] += [restaurant['location']]

                except:
                    self.product_per_location[product] = [restaurant['location']]

    
    def client_db(self):

        locations = ['Setor 1', 'Setor 2', 'Setor 3', 'Setor 4']
        tickets = ['High Ticket', 'Mediu-high Ticket', 'Mediu Ticket', 'Low Ticket']

        self.products()
        
        for i in range(0, 1000):
            self.clients.append(
                {
                    'searched_item':random.choice(self.products_list),
                    'ticket':random.choice(tickets)
                }
            )

            client = self.clients[-1]
            if client['ticket'] == 'High Ticket':
                client['location'] = 'Setor 1'

            elif client['ticket'] == 'Medium-high Ticket':
                client['location'] = random.choice(['Setor 2', 'Setor 3'])

            elif client['ticket'] == 'Medium Ticket':
                client['location'] = random.choice(['Setor 3', 'Setor 4'])
            
            else:
                client['location'] = 'Setor 4'
                
            client['item_found'] = client['location'] in self.product_per_location[client['searched_item']]

db = CreateDb()

df_clients = pd.DataFrame(CreateDb().clients)
df_restaurants = pd.DataFrame(CreateDb().restaurants)

df_clients.item_found.value_counts().values

df_clients.to_csv('clients.csv', index=False)
df_restaurants.to_csv('restaurants.csv', index=False)
