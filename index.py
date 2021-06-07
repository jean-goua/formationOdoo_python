import xmlrpc.client


# BDD Source
url_db1 = "https://formation.vracoop.fr"
db_1 = "formation_test"
username_db1 =  ""
password_db1 = ""

# Connexion BDD 1

common_1 = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url_db1))
models_1 = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url_db1))
version_1 = common_1.version()

# mise en place uid 1
uid_1 = common_1.authenticate(db_1, username_db1, password_db1, {})

# permet de récupérer les identifiants des produits qui sont à peser avec une balance
ids = models_1.execute_kw(
    db_1, uid_1, password_db1,
    'product.product', 'search',
    [[['to_weight', '=', True]]])

# Stock dans une variable le nombre de résultats retourné
count = models_1.execute_kw(
    db_1, uid_1, password_db1,
    'product.product', 'search_count',
    [[['to_weight', '=', True]]])

# Boucle sur le nombre de résultats
for loop in range(count):
    # stock dans la variable affichage les informations d'un article selon son id
    affichage = models_1.execute_kw(
        db_1, uid_1, password_db1, 'product.product', 'read',
        [ids[loop]], {'fields': ['name', 'type', 'pos_categ_id', 'lst_price', 'standard_price', 'uom_name']})
    # Affichage des informations
    print("nom : " + affichage[0]['name'])
    print("type : " + affichage[0]['type'])
    print("catégorie : " + affichage[0]['pos_categ_id'][1])
    print("prix de vente : " + str(affichage[0]['lst_price']))
    print("prix d'achat : " + str(affichage[0]['standard_price']))
    print("unité de mesure : " + affichage[0]['uom_name'])
    print()
