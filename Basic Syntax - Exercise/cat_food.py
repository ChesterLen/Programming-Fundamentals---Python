from math import floor, ceil
paint_boxes_count = int(input())
rolls_wallpapers_count = int(input())
a_pair_of_gloves_price = float(input())
paint_brush_price = float(input())
paint_price = 21.50
roll_wallpaper_price = 5.20
total_price_paint = paint_boxes_count * paint_price
total_rolls_wallpaper_price = rolls_wallpapers_count * roll_wallpaper_price
pairs_gloves_needed = ceil(rolls_wallpapers_count * 35 / 100)
paint_brushes_needed = floor(paint_boxes_count * 48 / 100)
total_pairs_gloves_price = a_pair_of_gloves_price * pairs_gloves_needed
total_paint_brushes_price = paint_brushes_needed * paint_brush_price
total_price = total_price_paint + total_rolls_wallpaper_price + total_pairs_gloves_price + total_paint_brushes_price
total_price /= 15
print(f"This delivery will cost {total_price:.2f} lv.")
