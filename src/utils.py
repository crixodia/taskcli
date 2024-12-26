import json
"""
This module provides utility functions and classes for managing JSON-based databases.
Functions:
    check_and_create_json(json_path: str, default_content: str = "") -> dict:
        Checks if a JSON file exists at the given path, creates it with default content if it doesn't,
        and returns the content of the JSON file.
Classes:
    DbManager:
        A class to manage a JSON-based database.
        Methods:
            __init__(self, db_json_path: str):
                Initializes the DbManager with the path to the JSON database file and loads the database content.
            save(self):
                Saves the current state of the database to the JSON file.
            next_id(self) -> str:
                Returns the next available ID for a new entry in the database.
"""
import os
import sys

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../src')))

from defaults import DB_INIT


def check_and_create_json(json_path: str, default_content: str = ""):
    """
    Checks if a JSON file exists at the given path, and if not, creates it with the provided default content.
    Args:
        json_path (str): The relative path to the JSON file.
        default_content (str, optional): The default content to write to the JSON file if it does not exist. Defaults to an empty string.
    Returns:
        dict: The content of the JSON file.
    """
    content = None
    complete_path = os.path.join(os.getcwd(), json_path)

    if not os.path.exists(complete_path):
        with open(complete_path, "w", encoding="utf8") as f:
            f.write(json.dumps(default_content, indent=4))

    content = json.load(open(complete_path, "r", encoding="utf8"))
    return content


class DbManager:
    """
    A class to manage a JSON-based database.
    Attributes:
        db_path (str): The file path to the JSON database.
        db (dict): The dictionary representing the JSON database.
    Methods:
        __init__(db_json_path: str):
            Initializes the DbManager with the given JSON database path.
        save():
            Saves the current state of the database to the JSON file.
        next_id() -> str:
            Returns the next available ID as a string.
    """
    def __init__(self, db_json_path: str):
        """
        Initializes the utility class with the given database JSON path.

        Args:
            db_json_path (str): The path to the database JSON file.

        Attributes:
            db_path (str): The absolute path to the database JSON file.
            db (dict): The database initialized from the JSON file.
        """
        self.db_path = os.path.join(os.getcwd(), db_json_path)
        self.db = check_and_create_json(db_json_path, DB_INIT)

    def save(self):
        """
        Saves the current state of the database to a file.

        This method writes the contents of the database (self.db) to a file specified
        by self.db_path in JSON format with an indentation of 4 spaces.

        Raises:
            IOError: If the file cannot be opened or written to.
        """
        with open(self.db_path, "w") as f:
            f.write(json.dumps(self.db, indent=4))

    def next_id(self):
        """
        Generate the next unique identifier for a new entry in the database.

        This method finds the maximum integer key in the database, increments it by one,
        and returns it as a string.

        Returns:
            str: The next unique identifier as a string.
        """
        return str(max([int(x) for x in self.db.keys()]) + 1)


if __name__ == "__main__":
    dbm = DbManager("db.json")
    print(dbm.db)
