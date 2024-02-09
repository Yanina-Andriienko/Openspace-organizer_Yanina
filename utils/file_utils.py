from pandas import read_csv


def read_colleagues_data(file_path: str) -> list:
    """
    Read colleagues' data from an Excel file.

    Args:
        file_path (str): Path to the Excel file containing colleagues' data.

    Returns:
        list: List of colleagues' names.
    """
    # Read data from the Excel file
    colleagues_df = read_csv(file_path, header=None, names=["Name"])

    # Extract names from the DataFrame
    colleagues = colleagues_df["Name"].tolist()

    return colleagues
