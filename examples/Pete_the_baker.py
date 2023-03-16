def cakes(recipe, available):
    for i in recipe:
        if i not in available:
            return 0
    return min([available.get(i) // recipe.get(i) for i in [i for i in recipe if i in available]])


if __name__ == '__main__':
    print(cakes({'flour': 500, 'sugar': 200, 'eggs': 1}, {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200}))
    print(cakes({"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100},
                {"sugar": 500, "flour": 2000, "milk": 2000}))
