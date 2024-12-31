# `taskcli`

A simple CLI task manager.

**Usage**:

```console
$ taskcli [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `add`: Adds a new task to the database with the...
* `update`: Updates the content of an existing task...
* `delete`: Deletes a task from the database...
* `list`: Lists all tasks, optionally filtered by...
* `mark`: Marks a task with the given id as the...

## `taskcli add`

Adds a new task to the database with the given content.

**Usage**:

```console
$ taskcli add [OPTIONS] TASK
```

**Arguments**:

* `TASK`: The description of the task to be added.  [required]

**Options**:

* `--help`: Show this message and exit.

## `taskcli update`

Updates the content of an existing task identified by the given id.

**Usage**:

```console
$ taskcli update [OPTIONS] TASK_ID TASK
```

**Arguments**:

* `TASK_ID`: The id of the task to be updated.  [required]
* `TASK`: The new description of the task.  [required]

**Options**:

* `--help`: Show this message and exit.

## `taskcli delete`

Deletes a task from the database identified by the given id.

**Usage**:

```console
$ taskcli delete [OPTIONS] TASK_ID
```

**Arguments**:

* `TASK_ID`: The id of the task to be deleted.  [required]

**Options**:

* `--help`: Show this message and exit.

## `taskcli list`

Lists all tasks, optionally filtered by the given status.

**Usage**:

```console
$ taskcli list [OPTIONS]
```

**Options**:

* `--status [todo|in-progress|done]`: Filter tasks by status.
* `--help`: Show this message and exit.

## `taskcli mark`

Marks a task with the given id as the specified status. By default, the status is set to &#x27;done&#x27;.

**Usage**:

```console
$ taskcli mark [OPTIONS] TASK_ID [STATUS]:[todo|in-progress|done]
```

**Arguments**:

* `TASK_ID`: [required]
* `[STATUS]:[todo|in-progress|done]`: The status to mark the task with.  [default: done]

**Options**:

* `--help`: Show this message and exit.
