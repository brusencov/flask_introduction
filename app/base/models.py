import json


class BaseModel:

    def __init__(self, file_path, base_class):
        self.items = []
        self._file_path = file_path
        self.BaseClass = base_class
        self.load()

    def push(self, item, validation=lambda x: True):
        if not callable(validation):
            print('Это не функция!')
            return False
        if not validation(self.items):
            return False
        self.items.append(item)
        return True

    def get_last_id(self):
        return len(self.items)

    def save(self):
        f = open(self._file_path, 'w')
        j_items = json.dumps([x.__dict__() for x in self.items])
        f.write(j_items)
        f.close()

    def load(self):
        try:
            f = open(self._file_path, 'r')
            j_items = json.loads(f.read())
            f.close()
            self.items = [self.BaseClass(**x) for x in j_items]
        except Exception:
            self.items = []

    def __del__(self):
        self.save()


