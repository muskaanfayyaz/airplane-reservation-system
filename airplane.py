# airplane.py

class Airplane:
    """
    A class representing an airplane seat reservation system.
    Supports First Class, Business Class, and Economy Class.
    """

    def __init__(self, rows=12, cols=7):
        self.rows = rows
        self.cols = cols
        self.seats = [[0 for _ in range(cols)] for _ in range(rows)]

    def check_available_seats(self, start_row, end_row):
        count = 0
        for i in range(start_row, end_row):
            for j in range(self.cols):
                if self.seats[i][j] == 0:
                    count += 1
        return count

    def book_seats(self, start_row, end_row, number_of_seats):
        if self.check_available_seats(start_row, end_row) < number_of_seats:
            return False

        for i in range(start_row, end_row):
            for j in range(self.cols):
                if self.seats[i][j] == 0:
                    self.seats[i][j] = 1
                    number_of_seats -= 1
                    if number_of_seats == 0:
                        return True
        return False

    def book_first_class(self, number_of_seats):
        return self.book_seats(0, 2, number_of_seats)

    def book_business_class(self, number_of_seats):
        return self.book_seats(2, 4, number_of_seats)

    def book_economy_class(self, number_of_seats):
        return self.book_seats(4, self.rows, number_of_seats)

    def reset_system(self):
        self.seats = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

    def get_seats(self):
        return self.seats

    def get_fares(self):
        return {
            "First Class": 18000,
            "Business Class": 14000,
            "Economy Class": 10000
        }
