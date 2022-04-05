import pickle


class PickleDB:
    PICKLE_DB_PATH = "./state/state_db"
    STORAGE = {}

    @classmethod
    def connect(cls):
        try:
            with open(cls.PICKLE_DB_PATH, "rb") as in_file:
                cls.STORAGE = pickle.load(in_file)
        except FileNotFoundError:
            cls.STORAGE = {}

    @classmethod
    def disconnect(cls):
        with open(cls.PICKLE_DB_PATH, "wb") as out_file:
            pickle.dump(cls.STORAGE, out_file)

    def __getitem__(self, item):
        return self.STORAGE[item]

    def __setitem__(self, key, value):
        self.STORAGE[key] = value
