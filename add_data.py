
def add_data():
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
            print("未知命令请重新输入")