from mysql_connection import retreive_sql_connection

def retreive_products(connection): 
    
    cursor = connection.cursor()

    query = ("SELECT products.product_id, products.name, products.uom_id, products.price_per_unit, uom.uom_name " 
            "FROM  products inner join uom on products.uom_id=uom.uom_id;")

    cursor.execute(query)

    response = []

    for (product_id, name, uom_id, price_per_unit, uom_name) in cursor:
        response.append(
            {
                'product_id' : product_id,
                'name' : name,
                'uom_id' : uom_id,
                'price_per_unit' : price_per_unit,
                'uom_name' : uom_name,


            }
        )
    return response 

def insert_product(connection, product):
    cursor = connection.cursor()
    add_product = (
        "INSERT INTO products " 
        "(name,uom_id, price_per_unit)"
        "VALUES (%s, %s, %s)"
    )

    data = (product['product_name'], product['uom_id'], product['price_per_unit'])

    cursor.execute(add_product, data)
    connection.commit()

    return None

def delete_product(connection, product_id):
    cursor = connection.cursor()
    delete_product = ("DELETE FROM products where product_id=" + str(product_id))
    cursor.execute(delete_product)
    connection.commit()
 

if __name__ == '__main__':
    connection = retreive_sql_connection()
    print(delete_product(connection, 5))