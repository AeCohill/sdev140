'''
Author:Adam Cohill
Date Written: 07/02/23
Assignment : Module4 programming assignment pt.2
Description: Write a Python program to get the top three items price in a shop.
'''

dataFile = input('Enter a file name: ')

data = {}
with open(dataFile, 'r') as f:
    content = f.read()
    content = content.strip('}')
    
    pairs = content.split(',')

    for pair in pairs:
        pair = pair.strip()
        if ':' not in pair:
            continue

        product, price = pair.split(':', 1)
        product = product.strip()
        price = price.strip()

        if product and price:
            try:
                data[product] = float(price)
            except ValueError:
                continue

sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=True)

print("Top 3 Items:")
for item, price in sorted_data[:3]:
    print(item, price)
