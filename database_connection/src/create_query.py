import logging

from pypika import Table
from pypika import PostgreSQLQuery

logger = logging.getLogger()


class BuildInjectQuery:

    @staticmethod
    def build_query_insert(table, key_duplicate, list_values):
        '''
        Build query Insert
        :param key_duplicate : boolean in oredr to have dupliacte key on query
        :param table : table name
        :param list_values: list of values to insert
        return query
        '''
        table = Table(table)
        values_table = []
        for i in range(len(list_values)):
            values_table.append(tuple(list_values[i]))

        q = BuildInjectQuery.function_insert(PostgreSQLQuery.into(table).insert(values_table[0]), values_table, table,
                                             0)
        if key_duplicate:
            q = q.on_conflict(table.id).do_nothing()

        return str(q)

    @staticmethod
    def function_insert(q, values, table, i):
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


table = 'language_identification'
list_values = [("0", "ES", "FR", "DE", "EN"), ("1", "EN", "DE", "FR", "ES")]
build = BuildInjectQuery
print(build.build_query_insert(table, True, list_values))
