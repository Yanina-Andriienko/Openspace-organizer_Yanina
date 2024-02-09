# Openspace-organizer_Yanina

This project is designed to create a program that facilitates seating arrangement in an open-space office environment. The program randomly assigns colleagues to seats at different tables to foster interaction and collaboration among team members.

## Purpose

The project consists of several Python files organized in a specific structure to achieve the functionality. Below is an overview of each file:

- `main.py`: Main entry point of the program.
- `repartition.xlsx`: The file in which the result of the repartition is saved in an Excel file.
- `utils/`: Directory containing utility files required for the project.
  - `file_utils.py`: Utility functions for file handling, such as reading data from an Excel file.
  - `table.py`: Definition of classes representing seats and tables in the open space.
  - `openspace.py`: Definition of the main `Openspace` class responsible for organizing seating arrangements.
  - `data/`: Directory containing file with list of colleagues.
    - `new_colleagues.csv`: List of colleagues.

## Installation

To run the program, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/challenge-openspace-classifier.git
   ```

2. Navigate to the project directory:

   ```bash
   cd challenge-openspace-classifier
   ```

3. Ensure you have Python installed. The project is developed using Python 3.

4. Install the required dependencies:

   ```bash
   pip install pandas
   ```

## Usage

To use the program, execute the `main.py` file. This will launch the seating organizer, load colleagues' data from an Excel file, and display the seating arrangement.

```bash
python main.py
```
