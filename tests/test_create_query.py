from unittest import TestCase
from src.db_interface import BuildInjectQuery
from pypika import PostgreSQLQuery

class TestBuildInjectQuery(TestCase):

    def setUp(self):
        self.table_str = 'language_identification'
        self.l_values = [("0", "ES", "FR", "DE", "EN"), ("1", "EN", "DE", "FR", "ES")]

    def tearDown(self):
        del self.table_str, self.l_values

    def test_build_query_insert(self):
        pass

    def test_function_insert(self):
        pass

    def function_insert(q: PostgreSQLQuery, values: list, table: str, i: int):
        '''
        Isnert values of list on query
        :param q : list of entities
        :param table : table name
        :param values : values of the list
        :param i : index
        return query
        '''

        if i == 0:
            return BuildInjectQuery.function_insert(q, values, table, i + 1)
        if i != 0 and i < len(values):
            q = q.insert(values[i])
            return BuildInjectQuery.function_insert(q, values, table, i + 1)
        else:
            return q

