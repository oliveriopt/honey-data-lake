import csv
import re


def read_file(path_file: str) -> list:
    """
    Read File
    :return:
    """
    list_items = []
    with open(path_file, 'r') as fd:
        reader = csv.reader(fd)
        for row in reader:
            if len(row) > 0:
                list_items.append(row)
    return list_items


def convert_states(list_states: list) -> list:
    """
    Retunr list of states converted
    :param list_states:
    :return:
    """
    list_states_conv = []
    for item in list_states:
        list_states_conv.append(item[0].lower())
    return list_states_conv

def clean_list_string(list_items=list):
    for item in list_items:
        .lower().replace("'", "").replace(",", "")
    pass


def extract_information(list_polit: list, list_states: list) -> list:
    """

    :param list_polit:
    :param list_states:
    :return:
    """

    items = []
    for i in range(len(list_polit)):

        name = (list_polit[i])
        if i % 2 == 0:
            polit_item = []
            polit_item.append(str(name[0]).lower().replace(" ", ""))
            if len(name) > 2:
                polit_item.append(str(name[1].lower().replace(" ", "")) + " " + str(name[2]).lower().replace(" ", ""))
            else:
                polit_item.append(name[1].lower().replace(" ", ""))
        else:
            for state in list_states:
                if " " + state in name[0].lower():
                    polit_item.append(state)
                    items.append(polit_item)
    return items


def export_csv(list_politians: list) -> None:
    with open("politicians/politicians_usa.csv", "w+") as f:
        writer = csv.writer(f)
        writer.writerows(list_politians)


list_polit = read_file('politicians/politicians.txt')
list_states = read_file('politicians/list_states.csv')
list_states = convert_states(list_states)
list_congressmann = extract_information(list_polit, list_states)
export_csv(list_congressmann)
# print
