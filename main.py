

from utils.openspace import Openspace
from utils.file_utils import read_colleagues_data
from utils.table import Table


def main():
    # Load colleagues' data from the Excel file
    colleagues = read_colleagues_data("./utils/data/new_colleagues.csv")

    # Create an Openspace instance
    openspace = Openspace(number_of_tables=6)

    # Organize seating arrangement
    openspace.organize(colleagues)

    # Display the seating arrangement
    openspace.display()

    # Store the seating arrangement in an Excel file
    openspace.store("repartition.xlsx")


if __name__ == "__main__":
    main()
