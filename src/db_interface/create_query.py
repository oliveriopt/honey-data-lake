import logging

from pypika import Table, Tables
from pypika import PostgreSQLQuery

logger = logging.getLogger()


class BuildInjectQuery:

    @staticmethod
    def build_query_insert(table: str, key_duplicate: bool, list_values: list):
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
        q = str(q).replace("nan,", "NULL,", 999999999999)
        q = q.replace("nan)", "NULL)", 999999999999)
        return str(q)

    @staticmethod
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

    @staticmethod
    def build_query_select(table, table_join):
        table, table_j = Tables(table, table_join)
        if (table_join == "geographic_zone"):
            q = PostgreSQLQuery.from_(table).join(table_j).on(table.geographic_zone_id == table_j.id).select( \
                'id', 'first_name', "middle_name", "last_name", "state", "country", "continent")


