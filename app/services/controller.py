from app.drivers.pickledb import PickleDB


class ControllerService:

    @classmethod
    def state(cls):
        state = PickleDB.STORAGE.setdefault("state", False)
        return state

    @classmethod
    def enable(cls):
        PickleDB()["state"] = True
        return True

    @classmethod
    def disable(cls):
        PickleDB()["state"] = False
        return True
