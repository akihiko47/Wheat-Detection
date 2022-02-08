from scripts_and_functions.model import *
from scripts_and_functions.field import *

corners = get_coords('координаты контура.txt')
photos = get_coords('координаты фотографий.txt')

dir_from = "images"
dir_to = "detected_images"

field_lst = make_predictions('png', dir_from, dir_to)
area = calculate_field_area(corners)

total_wheat, total_density = make_calculations(field_lst, area)

print(f'area = {area}')
print(f'total wheat = {total_wheat}')
print(f'density = {total_density}')

create_points_plot(corners, photos, field_lst)
