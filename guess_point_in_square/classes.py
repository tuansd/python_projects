"""
Tuan(Tony) Tran
"""
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw_point(self):
        print(f"Point ({self.x}, {self.y})")

    def get_input_point(self):
        self.x = input("Guess X: ")
        self.y = input("Guess Y: ")


class Square():
    def __init__(self, x, y, length):
        self.point_low_left = Point(x, y)
        self.point_high_right = Point(x + length, y + length)
        self.length = length

    def draw_square(self):
        # self.point_low_left.draw_point()
        # self.point_high_right.draw_point()
        print(f"X1 - X2: {self.point_low_left.x} - {self.point_high_right.x}")
        print(f"Y1 - Y2: {self.point_low_left.y} - {self.point_high_right.y}")

    def is_in_square(self, the_point):
        if self.point_low_left.x <= the_point.x \
            <= self.point_high_right.x and \
            self.point_low_left.y <= the_point.y \
                <= self.point_high_right.y:

            print(f"\nPoint ({the_point.x}, {the_point.y}) is IN square")
            return True
        else:
            print("\n🤦‍♀️ Sorry Try Again!")
            print(f"\nPoint ({the_point.x}, {the_point.y}) is NOT IN square")

            return False

    # case up, down, left, right

    def compare_message(self, p):
        the_message = "\nYour point is too far: "
        # down
        if p.x < self.point_low_left.x:
            the_message += " left"
        if p.x > self.point_high_right.x:
            the_message += " right"
        if p.y < self.point_low_left.y:
            the_message += " down"
        if p.y > self.point_high_right.y:
            the_message += " up"

        print(the_message, "\n")
