
recipe ={
    "name": "Musakka",
    "decription": "Açıklama",
    "img":"1.jpeg"
}

#acces items
result = recipe["name"]
result = recipe.get("name")
result = recipe.keys()
result = recipe.values()
result = recipe.items()

#update items

# recipe["name"] = "Mantı"
recipe.update({"name":"Mantı"})
result = recipe

#delete items
# recipe.pop("name")
# recipe.popitem()
recipe.clear()
result = recipe
print(result)