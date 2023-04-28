import cv2
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET
import random

def random_color():
    return (random.random(), random.random(), random.random())

# Парсинг XML файла
tree = ET.parse('annotations.xml')
root = tree.getroot()

# Цикл по всем объектам в XML файле
for member in root.findall('image'):
    image_name = member.get('name')

    image = cv2.imread(image_name)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Создание фигуры и осей
    fig, ax = plt.subplots(1)

    # Отображение изображения
    ax.imshow(image)

    for polyline in member.findall('polyline'):
        points = polyline.get('points').split(';')
        for point in points:
            x, y = map(float, point.split(','))
            # Рисование точки
            ax.plot(x, y, 'o', color=random_color())

    # Отображение изображения с наложенными точками
    plt.savefig(image_name + 'Polygon.png')