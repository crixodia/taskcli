from enum import Enum
import datetime

# TODO: datetime.datetime.fromtimestamp


class Status(Enum):
    TODO = "todo"
    IN_PROGRESS = "in-progress"
    DONE = "done"


DEFAULTS = {
    "sym": {
        "done": "[x]",
        "in-progress": "[~]",
        "todo": "[ ]"
    },
    "commands": {
        "add": "add",
        "update": "update",
        "delete": "delete",
        "list": "list",
        "mark": "mark"
    },
    "status": {
        "done": {"complete": "done", "short": "d"},
        "in-progress": {"complete": "in-progress", "short": "p"},
        "todo": {"complete": "todo", "short": "t"}
    },
}

DB_INIT = [
    {
        "id": -1,
        "description": "initdb",
        "status": Status.TODO.value,
        "createdAt": f"{datetime.datetime.now().timestamp()}",
        "updatedAt": f"{datetime.datetime.now().timestamp()}",
    },
]
