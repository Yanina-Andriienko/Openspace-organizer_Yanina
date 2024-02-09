
class Seat:
    def __init__(self, free: bool, occupant: str):
        '''
        Initialize a Seat object.

        :param free: A boolean indicating whether the seat is free or occupied.
        :param occupant: A string representing the name of the occupant.
        '''
        self.free = free  # Set the initial availability of the seat
        self.occupant = occupant  # Set the initial occupant of the seat

    def __str__(self) -> str:
        '''
        Return a string representation of the seat.

        :return: A string describing the seat's availability and occupant.
        '''
        if self.free:
            return ("Seat is available.")  # Return if the seat is available
        else:
            # Return if the seat is occupied
            return (f"Seat of {self.occupant}")

    def set_occupant(self, name: str) -> None:
        '''Function that will check if seat is free and 
        assign someone a seat if it's free

        :param name: A string representing the name of the occupant.
        '''
        if self.free:
            self.occupant = name  # Assign the occupant to the seat
            self.free = False  # Update the seat availability
        else:
            # Print message if seat is already occupied
            print("Seat is not available.")

    def remove_occupant(self) -> str:
        """
        Remove the occupant from the seat.

        :return: A string representing the name of the removed occupant.
        """
        if not self.free:
            removed_occupant = self.occupant   # Store the name of the removed occupant
            self.occupant = None    # Remove the occupant from the seat
            self.free = True   # Update the seat availability
            return removed_occupant   # Return the removed occupant's name
        else:
            print("Seat is available.")  # Print message if seat is available


class Table:
    def __init__(self, capacity: int) -> None:
        '''
        Initialize a Table object with a given capacity.

        :param capacity: An integer representing the number of seats at the table.
        '''
        self.capacity = capacity   # Set the capacity of the table
        self.seats = [Seat(True, None) for _ in range(capacity)]
        # Create a list of Seat objects, representing the seats at the table

    def __str__(self):
        """
        Return a string representation of the table.

        :return: A string describing the table's capacity.
        """
        return (f"A table with {self.capacity} seats")

    def has_free_spot(self) -> bool:
        '''Check if there is a free spot at the table

        :return: A boolean indicating whether there is a free spot at the table.
        '''
        for seat in self.seats:
            if seat.free:
                return True    # Return True if a free spot is found
        return False   # Return False if no free spot is found

    def assign_seat(self, name: str) -> None:
        '''
        Assign a seat to an occupant.

        :param name: A string representing the name of the occupant.
        '''
        for seat in self.seats:
            if seat.free:
                # Assign the seat to the occupant if it's free
                seat.set_occupant(name)
                return
            else:
                # Print message if no free spot is available
                print("No free spot")

    def left_capacity(self, left_capacity: int) -> int:
        '''
        Calculate the left capacity (number of free seats) at the table.

        :return: An integer representing the left capacity at the table.
        '''
        left_capacity = 0    # Initialize the left capacity counter
        for seat in self.seats:
            if seat.free:
                left_capacity += 1  # Increment the left capacity counter if the seat is free
        return left_capacity    # Return the left capacity
