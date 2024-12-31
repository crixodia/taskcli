import os
import typer
from rich.console import Console
from rich.table import Table
from typing import Annotated

from .defaults import Status
from .task import Task
from .utils import DbManager


app = typer.Typer(
    name="taskcli",
    help="A simple CLI task manager."
)
dbm = DbManager(
    os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "taskcli_db.json"
    )
)
tasker = Task(dbm)
console = Console()


@app.command()
def add(task: Annotated[str, typer.Argument(help="The description of the task to be added.")]):
    """
    Adds a new task to the database with the given content.
    """
    tasker.add(task)


@app.command()
def update(
    task_id: Annotated[str, typer.Argument(help="The id of the task to be updated.")],
    task: Annotated[str, typer.Argument(help="The new description of the task.")],
):
    """
    Updates the content of an existing task identified by the given id.
    """
    if task_id not in tasker.dbm.db:
        print("Task not found.")
        raise typer.Exit(code=1)

    tasker.update(task_id, task)


@app.command()
def delete(task_id: Annotated[str, typer.Argument(help="The id of the task to be deleted.")]):
    """
    Deletes a task from the database identified by the given id.
    """
    if task_id not in tasker.dbm.db.keys():
        print("Task not found.")
        raise typer.Exit(code=1)

    if not typer.confirm("Are you sure you want to delete this task?"):
        return

    tasker.delete(task_id)


@app.command()
def list(status: Annotated[Status, typer.Option(help="Filter tasks by status.")] = None):
    """
    Lists all tasks, optionally filtered by the given status.
    """
    fdb = tasker.list(status)
    table = Table(
        "ID", *fdb["0"].values(),
        title=f"Tasks marked as {status.value}" if status != None else None
    )
    for k, v in fdb.items():
        if k == "0":
            continue
        table.add_row(k, *v.values())
    console.print(table)


@app.command()
def mark(task_id: str, status: Annotated[Status, typer.Argument(help="The status to mark the task with.")] = Status.DONE.value):
    """
    Marks a task with the given id as the specified status. By default, the status is set to 'done'.
    """
    if task_id not in tasker.dbm.db:
        print("Task not found.")
        raise typer.Exit(code=1)
    tasker.mark_as(task_id, status)


if __name__ == "__main__":
    app(prog_name="taskcli")
