import re
import json
from pathlib import Path

def modify_data(em, im, bm):
    table_name = input('\n请选择想要修改的数据所在表格的名字(e, i, b):')

    if table_name == "e":
        if em.is_empty():
            print("\n当前表为空")
        else:
            input_id = int(input('\n请选择想要修改数据的input_id:'))
            if input_id in em.get_ids():
                title = input('\n请选择想要修改数据的字段:')
                headers = em.get_header(input_id)
                if title in headers:
                    if title == "金额":
                        while True:
                            value = input('\n请输入新值:')
                            m = re.match(r"^-\d+\.?\d*$", value)
                            if m is not None:
                                em.modify(input_id, title, float(value))
                                break
                            else:
                                print('\n请输入负数')
                    elif title == "日期":
                        while True:
                            value = input('\n请输入新值:')
                            m = re.match(r"^\d{8}$", value)
                            if m is not None:
                                em.modify(input_id, title, value)
                                break
                            else:
                                print('\n请输入正确的日期格式，例如，20260101')
                    else:
                        value = input('\n请输入新值:')
                        em.modify(input_id, title, value)
                else:
                    print(f"\n当前表中不存在该字段，当前表中的字段为{headers}，请输入正确的字段值")
            else:
                print("\n当前表中不存在该id，请输入正确的id")

    elif table_name == "i":
        if im.is_empty():
            print("\n当前表为空")
        else:
            input_id = int(input('\n请选择想要修改数据的input_id:'))
            if input_id in im.get_ids():
                title = input('\n请选择想要修改数据的字段:')
                headers = im.get_header(input_id)
                if title in headers:
                    if title == "金额":
                        while True:
                            value = input('\n请输入新值:')
                            m = re.match(r"^\d+\.?\d*$", value)
                            if m is not None:
                                im.modify(input_id, title, float(value))
                                break
                            else:
                                print('\n请输入正数')
                    elif title == "日期":
                        while True:
                            value = input('\n请输入新值:')
                            m = re.match(r"^\d{8}$", value)
                            if m is not None:
                                im.modify(input_id, title, value)
                                break
                            else:
                                print('\n请输入正确的日期格式，例如，20260101')
                    else:
                        value = input('\n请输入新值:')
                        im.modify(input_id, title, value)
                else:
                    print(f"\n当前表中不存在该字段，当前表中的字段为{headers}，请输入正确的字段值")
            else:
                print("\n当前表中不存在该id，请输入正确的id")

    elif table_name == "b":
        if bm.is_empty():
            print("\n当前表为空")
        else:
            input_id = int(input('\n请选择想要修改数据的input_id:'))
            if input_id in bm.get_ids():
                title = input('\n请选择想要修改数据的字段:')
                headers = bm.get_header(input_id)
                if title in headers:
                    base_dir = Path(__file__).resolve().parent.parent
                    path = base_dir.joinpath("table_header", "income.json")
                    with open(path, "r", encoding="utf-8") as f:
                        elements = json.load(f)
                    Liabilities = elements["Liabilities"]
                    if title == '日期':
                        while True:
                            value = input('\n请输入新值:')
                            m = re.match(r"^\d{8}$", value)
                            if m is not None:
                                bm.modify(input_id, title, value)
                                break
                            else:
                                print('\n请输入正确的日期格式，例如，20260101')
                    elif title in Liabilities:
                        while True:
                            value = input('\n请输入新值:')
                            m = re.match(r"^-\d+\.?\d*$", value)
                            if m is not None:
                                bm.modify(input_id, title, float(value))
                                break
                            else:
                                print('\n请输入负数')
                    else:
                        while True:
                            value = input('\n请输入新值:')
                            m = re.match(r"^\d+\.?\d*$", value)
                            if m is not None:
                                bm.modify(input_id, title, float(value))
                                break
                            else:
                                print('\n请输入正数')
                else:
                    print(f"\n当前表中不存在该字段，当前表中的字段为{headers}，请输入正确的字段值")
            else:
                print("\n当前表中不存在该id，请输入正确的id")

    else:
        print("\n表格名请输入(e, i, b)")

    return em, im, bm