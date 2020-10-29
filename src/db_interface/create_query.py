import logging

from pypika import Table, Tables
from pypika import PostgreSQLQuery

logger = logging.getLogger()


class BuildInjectQuery:

    @staticmethod
    def build_query_insert(table: str, key_duplicate: bool, list_values: list) -> str:
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
    def function_insert(q: PostgreSQLQuery, values: list, table: str, i: int) -> str:
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
    def build_query_select(table: str, table_join: str, table_join_2: str, table_join_3: str, limit: int,
                           offset:int)-> str:
        """
        Build the query select with three joins
        :param table:
        :param table_join:
        :param table_join_2:
        :param table_join_3:
        :return:
        """
        table, table_j1, table_j2, table_j3 = Tables(table, table_join, table_join_2, table_join_3)
        q = PostgreSQLQuery.from_(table).join(table_j1).on(table.geographic_zone_id == table_j1.id).join(
            table_j2).on(table.category_id == table_j2.id).join(table_j3).on(table.language_id ==
                                                                               table_j3.id).select( \
            table.id, table.first_name, table.middle_name, table.last_name, table_j1.id, table_j1.state,
            table_j1.country,
            table_j1.continent, table_j2.id, table_j2.category, table_j3.id , table_j3.primar).limit(limit).offset(
            offset)
        q = str(q).replace("JOIN", "FULL JOIN")
        return str(q)
