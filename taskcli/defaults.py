from enum import Enum

DATE_FORMAT = "%d/%m/%y %H:%M"


class Status(Enum):
    """
    Enum class representing the status of a task.

    Attributes:
        TODO (str): Represents a task that has not been started.
        IN_PROGRESS (str): Represents a task that is currently in progress.
        DONE (str): Represents a task that has been completed.
    """
    TODO = "todo"
    IN_PROGRESS = "in-progress"
    DONE = "done"


DB_INIT = {
    0: {
        "description": "Description",
        "status": "Status",
        "createdAt": "Created",
        "updatedAt": "Updated",
    },
}
