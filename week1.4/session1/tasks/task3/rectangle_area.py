
# function implementation
height = int(input("Enter the height:"))
width = int(input("Enter the width:"))
def rectangle_area(h,w):  # define suitable input data
    # returns height and width of rectangle                # implement the function
    area = height * width
    return area              # return an appropriate value

# testing the function

print(f"Area is {rectangle_area(height,width)}")   # provide suitable data matching your inputs
