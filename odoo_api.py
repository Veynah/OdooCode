import base64
from email.mime import image
from itertools import product
import logging
from urllib import response
import requests
import erppeek

logging.basicConfig(level=logging.INFO)

# def _get_image(url):
#     #Download imah-ge and return as a base64 decode in string 
#     if url == "N/A":
#         return False
#     try:
#         requests = requests.get(url)
#         img = base64.b64decode(response.content)
#         return img.decode("utf-8")
#     except requests.RequestException as err:
#         logging.error(f"Error on loading the picture : {err}")
#         return False

def connection_odoo_local():
    #Connect to Odoo local
    odoo_url = "http://localhost:8069"
    # odoo_db = "name of db"
    odoo_username = "admin"
    odoo_password = "admin"
    return erppeek.Client(odoo_url, odoo_username, odoo_password)

def get_products(client):
    #Get products from Odoo
    products = client.model("product.template").search([])
    product_list = []
    
    for product in products:
        product = client.model("product_template").browse(product)
        product_list.append(product)
    return product_list

def search_product_image(product_name):
    #Search the image from the product
    image = edenai.search_images(product_name)
    #Mettre le code de l'API !!
    

def main():
    odoo = connection_odoo_local()

    product_list = get_products(odoo)

    for product in product_list:
        product_name = product.name
        search_product_image(product_name)

    import pdb, pdb.set_trace()

if __name__ == "__main__":
    main()