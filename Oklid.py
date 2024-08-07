def euclideanDistance(point1, point2):
    dx = point2[0] - point1[0]
    dy = point2[1] - point1[1]
    return (dx * dx + dy * dy) ** 0.5

# Noktaların Tanımlanması
points = []
num_points = int(input("Kaç tane nokta gireceksiniz? "))

for i in range(num_points):
    x = float(input(f"{i+1}. noktanın x koordinatını girin: "))
    y = float(input(f"{i+1}. noktanın y koordinatını girin: "))
    points.append((x, y))

# Mesafelerin Hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum Mesafenin Bulunması
min_distance = distances[0]
for distance in distances:
    if distance < min_distance:
        min_distance = distance
print("min_distance")
