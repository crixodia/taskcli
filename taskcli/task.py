from .defaults import Status, DATE_FORMAT
from .utils import DbManager
from datetime import datetime
from copy import deepcopy


class Task:
    """
    A class to represent a task manager.
    Attributes
    ----------
    dbm : DbManager
        An instance of DbManager to handle database operations.
    Methods
    -------
    add(content: str):
        Adds a new task to the database with the given content.
    update(id: str, task_content: str):
        Updates the content of an existing task identified by the given id.
    delete(id: str):
        Deletes a task from the database identified by the given id.
    mark_as(id: str, status: Status):
        Marks a task with the given id as the specified status.
    list(filter: Status = None):
        Lists all tasks, optionally filtered by the given status.
    """

    def __init__(self, dbm: DbManager):
        """
        Initializes a new instance of the class.

        Args:
            dbm (DbManager): The database manager instance to be used by the class.
        """
        self.dbm = dbm

    def add(self, content: str):
        """
        Adds a new task to the database with the given content.

        Args:
            content (str): The description of the task to be added. Must not exceed 150 characters.

        Raises:
            ValueError: If the task description exceeds 150 characters.

        """
        if len(content) > 150:
            raise ValueError("Task description maximum character count is 150")
        create_date = datetime.now().strftime(DATE_FORMAT)
        self.dbm.db[self.dbm.next_id()] = {
            "description": content,
            "status": Status.TODO.value,
            "createdAt": create_date,
            "updatedAt": create_date
        }
        self.dbm.save()

    def update(self, id: str, task_content: str):
        """
        Update the task with the given id in the database.

        Args:
            id (str): The unique identifier of the task to be updated.
            task_content (str): The new content/description of the task.

        Updates:
            - The task's description with the provided task_content.
            - The task's updatedAt field with the current date and time.

        Saves:
            - The updated task information to the database.
        """
        update_date = datetime.now().strftime(DATE_FORMAT)
        self.dbm.db[id]["description"] = task_content
        self.dbm.db[id]["updatedAt"] = update_date
        self.dbm.save()

    def delete(self, id: str):
        """
        Deletes a task from the database by its ID.

        Args:
            id (str): The ID of the task to delete.

        Raises:
            ValueError: If the ID is "0", which is reserved.
        """
        if id == "0":
            raise ValueError("Id 0 is reserved")
        del self.dbm.db[id]
        self.dbm.save()

    def mark_as(self, id: str, status: Status):
        """
        Marks a task with the given ID as the specified status.

        Args:
            id (str): The unique identifier of the task to be updated.
            status (Status): The new status to be assigned to the task.

        Returns:
            None
        """
        self.dbm.db[id]["status"] = status.value
        self.dbm.save()

    def __get_lens__(self):
        """
        Calculate the maximum lengths of various fields for formatting purposes.
        This method computes the maximum lengths of the "ID", "Description", 
        "Status", and date fields based on the current entries in the database.
        It ensures that the column widths are sufficient to display the longest 
        entry in each field.
        Returns:
            tuple: A tuple containing the maximum lengths of the "ID", 
                   "Description", "Status" (with an additional padding of 2), 
                   and date fields.
        """
        len_id = len("ID")
        len_description = len("Description")
        len_status = len("Status")
        len_date = len(DATE_FORMAT) + 2

        for k, v in self.dbm.db.items():
            len_id = max(len_id, len(k))
            len_description = max(len_description, len(v["description"]))

        return len_id, len_description, len_status+2, len_date

    def list(self, filter: Status = None):
        """
        Lists tasks from the database with optional filtering by status.
        Args:
            filter (Status, optional): The status to filter tasks by. Defaults to None.
        Returns:
            str: A formatted string representing the list of tasks.
        The output is a table with columns for ID, description, status, createdAt, and updatedAt.
        The table is formatted with box-drawing characters for better readability.
        """
        db = deepcopy(self.dbm.db)
        if filter != None:
            for k in self.dbm.db:
                if not db[k]["status"] in [filter.value, "Status"]:
                    del db[k]

        return db
