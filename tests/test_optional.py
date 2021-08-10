import unittest
from python_optional import optional


class test_optiona(unittest.TestCase):
    def test_returns_value_if_key_exists(self):
        data = {'a': 'b'}

        self.assertEqual(
            optional(data).get('a'),
            'b'
        )

    def test_returns_none_if_key_is_missing(self):
        data = {'a': 'b'}

        self.assertEqual(
            optional(data).get('z'),
            None
        )

    def test_returns_none_if_data_is_not_dict(self):
        self.assertEqual(
            optional(None).get('z'),
            None
        )

        self.assertEqual(
            optional(['a']).get('z'),
            None
        )

        self.assertEqual(
            optional(123).get('z'),
            None
        )

    def test_multilevel_dicts(self):
        data = {'a': 'b', 'c': {'d': 'e', 'f': 'g'}}

        self.assertEqual(
            optional(optional(data).get('c')).get('d'),
            'e'
        )

        self.assertEqual(
            optional(optional(data).get('c')).get('z'),
            None
        )

    def test_returns_object_properties_if_set(self):
        class Something():
            foo = 'bar'

        data = {'a': Something(), 'b': 123}

        self.assertEqual(
            optional(data).get('a').foo,
            'bar'
        )

        self.assertEqual(
            optional(data).get('b'),
            123
        )

        self.assertIsNone(optional(data).get('z'))

        self.assertEqual(
            optional(data).a.foo,
            'bar'
        )

        self.assertEqual(
            optional(data).b,
            123
        )

        self.assertIsNone(optional(data).z)


if __name__ == '__main__':
    unittest.main()
