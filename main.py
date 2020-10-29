from src.pipeline.process_pipeline import ProcessPipelineInjectionSelection

import src.pipeline.cons_pipeline as cons
import sys
import numpy as np
import logging


def init_table() -> None:
    """
    Insert data from csv file to sql database
    :return:
    """
    for item in cons.tables:
        insert_table = item
        pipeline = ProcessPipelineInjectionSelection(insert_table=insert_table, select_table=None,
                                                     select_table_join=None,
                                                     select_table_join_2=None,
                                                     select_table_join_3=None)
        pipeline.inject_data_sql_from_file()


def run_scrapper(limit: int, offset: int) -> None:
    """
    Run searcher amnd scrapper
    :param limit: limit maximum of personas
    :param offset: number of the personas in the batch
    :return:
    """
    select_table = "persona"
    select_table_join = "geographic_zone"
    select_table_join_2 = "category"
    select_table_join_3 = "language"
    pipeline = ProcessPipelineInjectionSelection(insert_table=None, select_table=select_table,
                                                 select_table_join=select_table_join,
                                                 select_table_join_2=select_table_join_2,
                                                 select_table_join_3=select_table_join_3)
    pipeline.process_searching(limit=limit, offset=offset)


if __name__ == '__main__':
    if sys.argv[1] == "create":
        init_table()
    elif sys.argv[1] == "ss":
        list_batch = np.array_split(np.arange(int(sys.argv[3]), int(sys.argv[5])).tolist(), int(sys.argv[5]) / int(
            sys.argv[7]))
        print(list_batch)
        for batch in list_batch:
            print(list(batch))
            run_scrapper(limit=len(batch), offset=batch[0])
