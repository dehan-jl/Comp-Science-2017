population = float(input("Enter population: "))
land_area = float(input("Enter land area: "))

density = population/land_area

k10m = 10000000
k35m = 35000000

if population < k10m:
    print("Population:", population)
elif k10m < population < k35m:
    print("Population:", population)

if density > 100:
    print("Densely populated")
else:
    print("Sparsely populated")