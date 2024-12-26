import argparse
"""
TaskCli: A simple CLI application to track and manage tasks.
This script allows the user to add, update, delete, list, and mark tasks as done or in progress.
Modules:
    argparse: Provides command-line argument parsing functionality.
    task: Contains the Task class for task management.
    utils: Contains utility functions and classes, including DbManager.
    defaults: Contains default values and statuses.
Classes:
    None
Functions:
    None
Usage:
    Run the script with one of the following commands:
        - add <description>: Adds a new task with the given description.
        - update <id> <description>: Updates the task with the given ID and new description.
        - delete <id>: Deletes the task with the given ID.
        - list [done|in-progress|todo]: Lists tasks filtered by status.
        - mark-done <id>: Marks the task with the given ID as done.
        - mark-in-progress <id>: Marks the task with the given ID as in progress.
Example:
    python taskcli.py add "Finish the report"
    python taskcli.py update 1 "Review the report"
    python taskcli.py delete 1
    python taskcli.py list done
    python taskcli.py mark-done 1
    python taskcli.py mark-in-progress 1
Author:
    crixodia (https://github.com/crixodia/taskcli)
"""
import task
import utils
from defaults import Status

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="TaskCli",
        description="Track and manage your tasks with a simple CLI application",
        epilog="Made by crixodia (https://github.com/crixodia/taskcli)",
    )

    dbm = utils.DbManager("./db.json")
    tasker = task.Task(dbm)

    subparsers = parser.add_subparsers(
        dest="command",
        help="Available commands"
    )

    parser_add = subparsers.add_parser(
        "add",
        help="Adds a new task"
    )
    parser_add.add_argument(
        "description",
        type=str,
        help="Description of the task"
    )

    parser_update = subparsers.add_parser(
        "update",
        help="Update a task given its id and the new description"
    )
    parser_update.add_argument(
        "id",
        type=str,
        help="ID of the task to update"
    )
    parser_update.add_argument(
        "description",
        type=str,
        help="New description of the task"
    )

    parser_delete = subparsers.add_parser(
        "delete",
        help="Delete a task given its id"
    )
    parser_delete.add_argument(
        "id",
        type=str,
        help="ID of the task to delete"
    )

    parser_list = subparsers.add_parser("list", help="List all tasks")
    list_subparsers = parser_list.add_subparsers(
        dest="status",
        help="Filter tasks by status"
    )
    list_subparsers.add_parser(
        "done",
        help="List tasks that are done"
    )
    list_subparsers.add_parser(
        "in-progress",
        help="List tasks that are in progress"
    )
    list_subparsers.add_parser(
        "todo",
        help="List tasks that are to do"
    )

    parser_mark_done = subparsers.add_parser(
        "mark-done",
        help="Mark a task as done"
    )
    parser_mark_done.add_argument(
        "id",
        type=str,
        help="ID of the task to mark as done"
    )

    parser_mark_in_progress = subparsers.add_parser(
        "mark-in-progress",
        help="Mark a task as in progress"
    )
    parser_mark_in_progress.add_argument(
        "id",
        type=str,
        help="ID of the task to mark as in progress"
    )

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        exit(1)

    if args.command == "add":
        tasker.add(args.description)
    elif args.command == "update":
        tasker.update(args.id, args.description)
    elif args.command == "delete":
        tasker.delete(args.id)
    elif args.command == "list":
        if args.status == "done":
            tasker.list(Status.DONE)
        elif args.status == "in-progress":
            tasker.list(Status.IN_PROGRESS)
        elif args.status == "todo":
            tasker.list(Status.TODO)
        else:
            tasker.list()
    elif args.command == "mark-done":
        tasker.mark_as(args.id, Status.DONE)
    elif args.command == "mark-in-progress":
        tasker.mark_as(args.id, Status.IN_PROGRESS)
