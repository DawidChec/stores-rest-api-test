from models.store import StoreModel
from tests.unit.test_unit_base import UnitBaseTest

class StoreTest(UnitBaseTest):
    def test_create_store(self):
        store = StoreModel('test')

        self.assertEqual(store.name, 'test',
                         'The name of the store creation does not equal the constructor qrgument.')
