from src.pipeline.process_pipeline import ProcessPipelineInjectionSelection
from src.pipeline.argum_parser import parse_arguments
from pathlib import Path

import src.pipeline.cons_pipeline as cons
import os
import numpy as np


pth = os.path.abspath(os.getcwd())
PATH = str(Path(pth))

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

    args = parse_arguments()
    print(args)
    if args.action == "init":
        init_table()
        pass
    elif args.action == "scrap":
        list_batch = np.array_split(np.arange(int(args.start_row), int(args.end_row)).tolist(),
                                    int(args.end_row - args.start_row) / int(args.length_batch))
        print(list_batch)
        for batch in list_batch:
            print(batch)
            run_scrapper(limit=len(batch), offset=batch[0])
