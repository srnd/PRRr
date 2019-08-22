import unittest
import unittest
from .. import CheckRunEvent


class TestEvent(unittest.TestCase):
    def test_nested(self):
        data = {
            'nest1': {
                'nest2': {
                    'nest3': {
                        'nest4': {
                            'foo': 'bar'
                        }
                    }
                }
            }
        }
        self.event = CheckRunEvent(data)
        self.assertEqual(self.event.nest1.nest2.nest3.nest4.foo,'bar')