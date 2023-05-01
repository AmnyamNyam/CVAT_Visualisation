import cv2
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import xml.etree.ElementTree as ET
import random

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
    for box in member.findall('box'):
        label = box.get('label')
        xmin = float(box.get('xtl'))
        ymin = float(box.get('ytl'))
        xmax = float(box.get('xbr'))
        ymax = float(box.get('ybr'))

        # Создание прямоугольника
        rect = patches.Rectangle((xmin, ymin), xmax - xmin, ymax - ymin,
        linewidth=1, edgecolor='r', facecolor='none')

        # Добавление созданного прямоугольника на изображение
        ax.add_patch(rect)

        # Отображение изображения с наложенными полигонами
        plt.savefig(image_name + 'Rectangle.png')