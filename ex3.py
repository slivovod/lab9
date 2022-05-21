def rectangle(width, height):
    for i in range(height):
        print(width * "*")

rec_width = int(input("enter the width of the rectangle: "))
rec_height = int(input("enter the height of the rectangle: "))
rectangle(rec_width, rec_height)