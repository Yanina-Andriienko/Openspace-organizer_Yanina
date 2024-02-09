

from random import shuffle
from .table import Table
from pandas import DataFrame


class Openspace:
    def __init__(self, number_of_tables: int) -> None:
        '''
        Initialize an Openspace object with a given number of tables.

        Args:
            number_of_tables (int): The number of tables in the openspace.
        '''
        self.number_of_tables = number_of_tables
        self.tables = [Table(4) for _ in range(number_of_tables)]

    def organize(self, names: list):
        '''
         Randomly assign people to seats in the different tables 
         (randomly reorganize the order of people in the list).

         Args:
         names (list): List of names to be assigned to seats.

         Returns:
         list: List of names that couldn't be assigned a seat.
         '''
        shuffle(names)   # Shuffle the list of names randomly
        unassigned_names = []   # Initialize a list to store unassigned names

        for name in names:    # Iterate through each name in the shuffled list
            assigned = False    # Flag to track if the name is successfully assigned
            # Iterate through each table to find a free spot
            for table in self.tables:
                if table.has_free_spot():   # Check if the table has a free spot
                    table.assign_seat(name)   # Assign the seat to the name

                    assigned = True  # Update the flag to indicate successful assignment
                    break   # Exit the loop after assignment
            if not assigned:
                # Add the unassigned name to the list
                unassigned_names.append(name)
        # Print unassigned names if there are any
        if len(unassigned_names) > 0:
            print(f'There are no free spots for: {unassigned_names}')

    def display(self) -> None:
        '''Display the different tables and their occupants'''
        for i, table in enumerate(self.tables):   # Print number of the table
            print(f"Table {i+1}:")
            for seat in table.seats:
                if not seat.free:
                    # Print the occupant of the seat
                    print(f"- {seat.occupant}")
                else:
                    print("-")  # Print "-" if the seat is free

    def store(self, filename: str) -> None:
        """
        Store the repartition in an excel file.

        Args:
            filename (str): The filename to store the Excel file.
        """

        # Initialize a dictionary to store data
        data = {"Table": [], "Occupant": []}
        # Iterate through each table and seat to populate the data dictionary
        for i, table in enumerate(self.tables):
            for seat in table.seats:
                # Append the table number to the data
                data["Table"].append(i + 1)
                data["Occupant"].append(
                    seat.occupant if not seat.free else None)  # Append the occupant to the data if seat is not free, otherwise append None
        df = DataFrame(data)    # Create a DataFrame from the data dictionary
        # Write the DataFrame to an Excel file without index
        df.to_excel(filename, index=False)

    def __str__(self) -> str:
        """
        Return a string representation of the Openspace object.

        Returns:
            str: String representation of the Openspace object.
        """
        return f"Openspace with {self.number_of_tables} tables"
