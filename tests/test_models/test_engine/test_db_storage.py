import unittest
from models.db_storage import DBStorage

class TestDBStorage(unittest.TestCase):
    def setUp(self):
        self.storage = DBStorage()

    def tearDown(self):
        self.storage.close()

    def test_all(self):
        pass

    def test_new(self):
        pass

    def test_save(self):
        pass

    def test_delete(self):
        pass

    def test_reload(self):
        pass

    def test_close(self):
        pass

if __name__ == '__main__':
    unittest.main()

