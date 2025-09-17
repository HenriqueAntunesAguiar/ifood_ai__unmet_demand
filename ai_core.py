# pip install -q -U google-genai

from pydantic import BaseModel, Field
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain.prompts import PromptTemplate
import os, dotenv

dotenv.load_dotenv()

class QueryRecipe():

    def __init__(self, recipe):
        self.recipe = recipe
        self.api_token = os.getenv('API_KEY__GEMINI')
        
    class RecipeParser(BaseModel):
        recipe_name: str = Field(..., description='Nome da Comida')
        recipe_ingredients: list[str] = Field(...,
            description="Lista de ingredientes, separados, apenas os nomes dos ingredientes"
        )

    def RunModel(self):
        llm = ChatGoogleGenerativeAI(api_key=self.api_token,
                                    model='gemini-2.0-flash-lite',
                                    temperature=0.2,
                                    max_output_tokens=8024)

        parser = JsonOutputParser(pydantic_object=self.RecipeParser)

        prompt = PromptTemplate(

            template='''Você é um chefe de cozinha renomado que já realizou todos os pratos que conseguiu.
                        Consultando suas receitas, você deve ajudar seu Chefe Junior, procurando a sua receita a partir do nome da receita que ele informar e retornar os principais ingredientes necessário para fazer aquele prato.
                        
                        ____________________________________________________________________________________________________
                        Receita informada pelo Chefe Junior:
                        {recipe}

                        ____________________________________________________________________________________________________
                        Formato de Saída:
                        {outputparser}

                        ____________________________________________________________________________________________________
                        Orientações do Formato de Saída:
                            Recipe Ingredients:
                                Lista de ingredientes, separados, apenas os nomes dos ingredientes
                        ''',

            input_variables=['recipe'],
            partial_variables={'outputparser':parser.get_format_instructions()}
        )

        chain = prompt | llm | parser

        response = chain.invoke({'recipe':self.recipe})
        return response

class CheckRestaurantAbleToAddRecipe():

    def __init__(self, data_to_able):
        self.data_to_able = data_to_able
        self.api_token = os.getenv('API_KEY__GEMINI')
        
    class CheckToAbleParser(BaseModel):
        able: list[bool] = Field(..., description='Se prato é compátivel com os outros pratos e tipos do restaurante, responder True, se não, False.')
        

    def RunModel(self):
        llm = ChatGoogleGenerativeAI(api_key=self.api_token,
                                    model='gemini-2.0-flash-lite',
                                    temperature=0.2,
                                    max_output_tokens=8024)

        parser = JsonOutputParser(pydantic_object=self.CheckToAbleParser)

        prompt = PromptTemplate(

            template='''Você é um chefe de cozinha renomado que já realizou todos os pratos que conseguiu.
                        Você receberá um json com três parâmetros:
                        
                        1) restaurant_type - tipo do restaurante;
                        2) products - pratos do restaurante;
                        3) product_to_add - prato a ser adicionado;
                        ____________________________________________________________________________________________________
                        Com base nestes dados, deve julgar e responder com True ou False, se o prato a ser adicionado condiz com o tipo do restaurante e pratos que ele já contem.
                        
                        ____________________________________________________________________________________________________
                        Dados para Análise:
                        {data_to_able}

                        ____________________________________________________________________________________________________
                        Formato de Saída:
                        {outputparser}

                        ____________________________________________________________________________________________________
                        Orientações do Formato de Saída:
                            Responder com True caso o prato a ser adicionado condiz com os outros pratos e com o estilo do restaurante, caso contrário responder com False.
                        ''',

            input_variables=['data_to_able'],
            partial_variables={'outputparser':parser.get_format_instructions()}
        )

        chain = prompt | llm | parser

        response = chain.invoke({'data_to_able':self.data_to_able})
        return response
    
class CheckIngredientsToRecipeAndRestaurant():

    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.api_token = os.getenv('API_KEY__GEMINI')

    class CheckIngredientsToRecipeAndRestaurantParser(BaseModel):
        obs: str = Field(..., description='Descreva neste campo observações sobre os ingredientes da receita, do restaurante, listando ingredientes presentes, faltantes ') # e possíveis modificações na receita para se adaptar os ingredientes da receita. --> não teve um bom resultado;
        
    def RunModel(self):
        llm = ChatGoogleGenerativeAI(api_key=self.api_token,
                                    model='gemini-2.0-flash-lite',
                                    temperature=0.2,
                                    max_output_tokens=8024)

        parser = JsonOutputParser(pydantic_object=self.CheckIngredientsToRecipeAndRestaurantParser)

        prompt = PromptTemplate(
            template='''
                        Você é um Gerente de Estoque Sr. Junto a você, tem em sua equipe um Chefe de Cozinha renomado.
                        Você receberá um json com três parâmetros:
                        
                        1) restaurant_ingredients - ingredientes do restaurante;
                        2) recipe_ingredients - ingredientes necessário para a receita;
                        3) recipe_name - nome da receita;

                        ____________________________________________________________________________________________________
                        Com base nestes dados, deve julgar e retornar:                      
                        * Observação sobre os ingredientes da receita, do restaurante, listando ingredientes presentes e faltantes.

                        ____________________________________________________________________________________________________
                        Seguem os dados para análise:
                        {input_ingredients}
                        ____________________________________________________________________________________________________
                        Formato de Saída:
                        {outputparser}
                     ''', 
                     input_variables=['input_ingredients'],
                     partial_variables={'outputparser':parser.get_format_instructions()}
                          
        )

        chain = prompt | llm | parser
        response = chain.invoke({'input_ingredients':self.ingredients})

        return response