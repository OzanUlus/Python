import methods as m

m.addProduct("Huawei Pro9", 32000)
m.updateProduct(6,"Huawei Pro11",38000)

for product in m.getProducts():
    print(product)
