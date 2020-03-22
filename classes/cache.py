import os
import json
import time


class Cache:

    def __init__(self, file):
        self.file = file

    def time_diff(self):
        if os.path.isfile(self.file):
            last_time = int(os.path.getmtime(self.file))
            current_time = int(time.time())
            return current_time - last_time
        return None

    def set(self, data) -> None:
        if len(data) == 0:
            return None
        os.makedirs(os.path.dirname(self.file), exist_ok=True)
        with open(self.file, 'w+', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        pass

    def get(self):
        try:
            with open(self.file, encoding="utf8") as json_file:
                return json.load(json_file)
        except EnvironmentError:
            return None
