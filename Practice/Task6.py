import csv
data=[
    ['Product', 'Price'],
    ['Apple', 1.5],
    ['Banana', 0.8]
]
with open("product.csv", "w", encoding="utf-8") as f:
    writer=csv.writer(f)
    writer.writerows(data)
with open("product.csv", "r", encoding="utf-8") as f:
    content=f.read()
    print(content)