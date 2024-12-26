import unittest
from unittest.mock import MagicMock
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from task import Task
from defaults import Status


class TestTask(unittest.TestCase):

    def setUp(self):
        self.dbm = MagicMock()
        self.tasker = Task(self.dbm)

    def test_add_task(self):
        self.tasker.add("Test task")
        self.dbm.save.assert_called_once()

    def test_update_task(self):
        self.dbm.db = {
            "1": {"description": "Old task", "status": Status.TODO.value}}
        self.tasker.update("1", "Updated task")
        self.assertEqual(self.dbm.db["1"]["description"], "Updated task")
        self.dbm.save.assert_called_once()

    def test_delete_task(self):
        self.dbm.db = {
            "1": {"description": "Test task", "status": Status.TODO.value}}
        self.tasker.delete("1")
        self.assertNotIn("1", self.dbm.db)
        self.dbm.save.assert_called_once()

    def test_list_tasks(self):
        self.dbm.db = {
            "1": {"description": "Task 1", "status": Status.TODO.value},
            "2": {"description": "Task 2", "status": Status.DONE.value}
        }
        tasks = self.tasker.list()
        self.assertIn("Task 1", tasks)
        self.assertIn("Task 2", tasks)

    def test_list_done_tasks(self):
        self.dbm.db = {
            "1": {"description": "Task 1", "status": Status.TODO.value},
            "2": {"description": "Task 2", "status": Status.DONE.value}
        }
        tasks = self.tasker.list(Status.DONE)
        self.assertNotIn("Task 1", tasks)
        self.assertIn("Task 2", tasks)

    def test_list_in_progress_tasks(self):
        self.dbm.db = {
            "1": {"description": "Task 1", "status": Status.IN_PROGRESS.value},
            "2": {"description": "Task 2", "status": Status.DONE.value}
        }
        tasks = self.tasker.list(Status.IN_PROGRESS)
        self.assertIn("Task 1", tasks)
        self.assertNotIn("Task 2", tasks)

    def test_list_todo_tasks(self):
        self.dbm.db = {
            "1": {"description": "Task 1", "status": Status.TODO.value},
            "2": {"description": "Task 2", "status": Status.DONE.value}
        }
        tasks = self.tasker.list(Status.TODO)
        self.assertIn("Task 1", tasks)
        self.assertNotIn("Task 2", tasks)


if __name__ == "__main__":
    unittest.main()
