import json
import os

from defaults import DEFAULTS, DB_INIT


def check_and_create_json(json_path: str, default_content: str = ""):
    content = None
    complete_path = os.path.join(os.getcwd(), json_path)

    if not os.path.exists(complete_path):
        with open(complete_path, "w", encoding="utf8") as f:
            f.write(json.dumps(default_content, indent=4))

        content = json.load(open(complete_path, "r", encoding="utf8"))

    return content


class ConfigManager:
    def __init__(self, config_file_path: str):
        self.config_path = os.path.join(os.getcwd(), config_file_path)
        self.config = check_and_create_json(config_file_path, DEFAULTS)


class DbManager:
    def __init__(self, db_json_path: str):
        self.db_path = os.path.join(os.getcwd(), db_json_path)
        self.db = check_and_create_json(db_json_path, DB_INIT)


if __name__ == "__main__":
    cfm = ConfigManager("config.json")
    dbm = DbManager("db.json")
    print(cfm.config)
    print(dbm.db)
