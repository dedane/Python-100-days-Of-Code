

#Write your code above this line 👆
def paint_calc(height,width,cover):
    print(f'number of paint cans needed is {int((height * width)/cover)}')


# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

