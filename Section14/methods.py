import db

def addProduct(productName, price):

    db.products.append({
        "id": len(db.products) + 1 ,
        "productName": productName,
        "price": price
        })
    print("Add succesfully")
    

def updateProduct(id,newProductName,newPrice):
    for product in db.products:
        if product["id"] == id:
            product["productName"] = newProductName
            product["price"] = newPrice
            print(f"Succesful {product}")
            break
    print("Product not found")

def getProducts():
    return db.products   
