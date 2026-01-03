from src.expenditure_manager import ExpenditureManager
from src.income_manager import IncomeManager
from src.balance_manager import BalanceManager
import src.capture_input as ci
import os
import json

expenditure_manager = ExpenditureManager()
income_manager = IncomeManager()
balance_manager = BalanceManager()

while True:

    prompt = input('请选择你的操作(add/list/modify/delete/save/exit):')

    # 添加数据
    if prompt == "add":
        while True:

            table_name = input("请输入要添加的表的名字(e,i,b)，输入 # 退出添加：")

            if table_name == "#":
                break

            elif table_name == "e":
                path = os.path.join(".", "table_header", "expenditure.json")
                with open(path, "r", encoding="utf-8") as f:
                    elements = json.load(f)
                    ways = elements["ExpenditureWay"]
                    #print(ways)
                    for item in ways:
                        while True:
                            data = ci.e(path, item)
                            if data == "#":
                                break
                            else:
                                expenditure_manager.add(data)
                    print('所有支付通道均已输入完毕')

            elif table_name == "i":
                path = os.path.join(".", "table_header", "income.json")
                while True:
                    data = ci.i(path)
                    if data == "#":
                        break
                    else:
                        income_manager.add(data)

            elif table_name == "b":
                path = os.path.join(".", "table_header", "balance.json")
                data = ci.b(path)
                balance_manager.add(data)

            else:
                print("表格名请输入(e, i, b)")

    # 查看数据
    elif prompt == "list":

        table_name = input('请选择想要查看的表格的名字(e, i, b，all):')
        if table_name == "e":
            expenditure_manager.display()

        elif table_name == "i":
            income_manager.display()

        elif table_name == "b":
            balance_manager.display()

        elif table_name == "all":
            print('=' * 30 + '以下是支出表' + '=' * 70)
            expenditure_manager.display()
            print('=' * 30 + '以下是收入表' + '=' * 70)
            income_manager.display()
            print('=' * 30 + '以下是余额表' + '=' * 70)
            balance_manager.display()

        else:
            print("表格名请输入(e, i, b)")

    #修改数据
    elif prompt == "modify":
        table_name = input('请选择想要修改的数据所在表格的名字(e, i, b):')
        input_id = int(input('请选择想要修改数据的input_id:'))
        title = input('请选择想要修改数据的字段:')
        value = input('请输入新值:')

        if table_name == "e":
            expenditure_manager.modify(input_id, title, value)
        elif table_name == "i":
            income_manager.modify(input_id, title, value)
        elif table_name == "b":
            balance_manager.modify(input_id, title, value)
        else:
            print("表格名请输入(e, i, b)")

    #删除数据
    elif prompt == "delete":
        table_name = input('请选择想要删除的数据所在表格的名字(e, i, b):')
        input_id = int(input('请选择想要删除数据的input_id:'))
        if table_name == "e":
            expenditure_manager.delete(input_id)
        elif table_name == "i":
            income_manager.delete(input_id)
        elif table_name == "b":
            balance_manager.delete(input_id)
        else:
            print("表格名请输入(e, i, b)")

    #保存数据
    elif prompt == "save":
        pass

    #退出程序
    elif prompt == "exit":
        break

    else:
        print('未知命令，请重新输入')