import math

# Project title
project_title = "Geometric Calculator"


def calculate_circle(radius):
    area = math.pi * radius ** 2
    perimeter = 2 * math.pi * radius
    return area, perimeter


def calculate_square(side):
    area = side ** 2
    perimeter = 4 * side
    return area, perimeter


def calculate_rectangle(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter


# Main function
def main():
    print(project_title)
    print("Choose a shape to calculate:")
    print("1. Circle")
    print("2. Square")
    print("3. Rectangle")

    choice = int(input("Enter your choice (1/2/3): "))

    if choice == 1:
        radius = float(input("Enter the radius of the circle: "))
        area, perimeter = calculate_circle(radius)
        print(f"Circle - Area: {area:.2f}, Perimeter: {perimeter:.2f}")

    elif choice == 2:
        side = float(input("Enter the side length of the square: "))
        area, perimeter = calculate_square(side)
        print(f"Square - Area: {area:.2f}, Perimeter: {perimeter:.2f}")

    elif choice == 3:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area, perimeter = calculate_rectangle(length, width)
        print(f"Rectangle - Area: {area:.2f}, Perimeter: {perimeter:.2f}")

    else:
        print("Invalid choice. Please select 1, 2, or 3.")


# Run the main function
if __name__ == "__main__":
    main()
