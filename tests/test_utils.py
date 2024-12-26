import unittest
import os
from unittest.mock import patch, mock_open
from utils import DbManager, check_and_create_json
from defaults import DB_INIT


class TestUtils(unittest.TestCase):

    @patch("utils.os.path.exists")
    @patch("utils.open", new_callable=mock_open, read_data='{}')
    @patch("utils.json.load")
    @patch("utils.json.dumps")
    def test_check_and_create_json_file_exists(self, mock_json_dumps, mock_json_load, mock_open, mock_exists):
        mock_exists.return_value = True
        mock_json_load.return_value = {}

        result = check_and_create_json("test.json", {"default": "content"})
        self.assertEqual(result, {})
        mock_open.assert_called_once_with(os.path.join(
            os.getcwd(), "test.json"), "r", encoding="utf8")

    @patch("utils.os.path.exists")
    @patch("utils.open", new_callable=mock_open)
    @patch("utils.json.load")
    @patch("utils.json.dumps")
    def test_check_and_create_json_file_not_exists(self, mock_json_dumps, mock_json_load, mock_open, mock_exists):
        mock_exists.return_value = False
        mock_json_load.return_value = {"default": "content"}

        result = check_and_create_json("test.json", {"default": "content"})
        self.assertEqual(result, {"default": "content"})
        mock_open.assert_any_call(os.path.join(
            os.getcwd(), "test.json"), "w", encoding="utf8")
        mock_open.assert_any_call(os.path.join(
            os.getcwd(), "test.json"), "r", encoding="utf8")

    @patch("utils.check_and_create_json")
    def test_dbmanager_init(self, mock_check_and_create_json):
        mock_check_and_create_json.return_value = {
            "1": {"description": "Test task"}}
        dbm = DbManager("test.json")
        print(dbm.db)
        self.assertEqual(dbm.db, {"1": {"description": "Test task"}})
        mock_check_and_create_json.assert_called_once_with(
            "test.json", DB_INIT)

    def test_dbmanager_next_id(self):
        dbm = DbManager("test.json")
        dbm.db = {"1": {"description": "Test task"},
                  "2": {"description": "Another task"}}
        next_id = dbm.next_id()
        self.assertEqual(next_id, "3")


if __name__ == "__main__":
    unittest.main()
