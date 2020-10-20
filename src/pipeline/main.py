from src.pipeline.process_pipeline import ProcessPipelineInjectionSelection

import src.pipeline.cons_pipeline as cons

def init_table() -> None:
    for item in cons.tables:
        insert_table = item
        pipeline = ProcessPipelineInjectionSelection(insert_table=insert_table, select_table=None,
                                                     select_table_join=None,
                                                     select_table_join_2=None,
                                                     select_table_join_3=None)
        pipeline.inject_data_sql_from_file()


def run_scrapper():
    select_table = "persona"
    select_table_join = "geographic_zone"
    select_table_join_2 = "category"
    select_table_join_3 = "language"
    pipeline = ProcessPipelineInjectionSelection(insert_table=None, select_table=select_table,
                                                 select_table_join=select_table_join,
                                                 select_table_join_2=select_table_join_2,
                                                 select_table_join_3=select_table_join_3)
    pipeline.process_searching()


if __name__ == '__main__':
    var_do = "CREATE!"
    if var_do == "CREATE":
        init_table()
    else:
        run_scrapper()
