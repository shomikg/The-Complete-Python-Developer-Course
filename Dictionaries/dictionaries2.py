fruit = {"orange": "a sweet, organge, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit",
         "lime": "a sour, green citrus fruit"}

print(fruit)


for i in range(10):
    for snack in fruit:
        print(snack + " is " + fruit[snack])
    print('-' * 40) 