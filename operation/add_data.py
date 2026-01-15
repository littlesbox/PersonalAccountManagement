from pathlib import Path
import json
import operation.capture_input as ci

def add_data(em, im, bm):
    base_dir = Path(__file__).resolve().parent.parent

    while True:

        table_name = input("\n请输入要添加的表的名字(e,i,b)，输入 # 退出添加：")

        if table_name == "#":
            break

        elif table_name == "e":
            path = base_dir.joinpath("table_header", "expenditure.json")
            with open(path, "r", encoding="utf-8") as f:
                elements = json.load(f)
                ways = elements["ExpenditureWay"]
                # print(ways)
            for item in ways:
                while True:
                    data = ci.e(path, item)
                    if data == "#":
                        break
                    elif len(data) == 0:
                        print('\n输入内容有误，请重新输入')
                    else:
                        em.add(data)
            print('\n所有预设支付通道均已输入完毕')

            while True:
                other_ways = input('\n是否还有其他支付通道的支出，如果有请输入支付通道，如果没有请输入 # :')
                if other_ways == '#':
                    break
                else:
                    while True:
                        data = ci.e(path, other_ways)
                        if data == "#":
                            break
                        elif len(data) == 0:
                            print('\n输入内容有误，注意日期格式和金额为负以及用空格分隔，请重新输入')
                        else:
                            em.add(data)


        elif table_name == "i":
            path = base_dir.joinpath("table_header", "income.json")
            while True:
                data = ci.i(path)
                if data == "#":
                    break
                elif len(data) == 0:
                    print('\n输入内容有误，注意日期格式和金额为正以及用空格分隔，请重新输入')
                else:
                    im.add(data)

        elif table_name == "b":
            path = base_dir.joinpath("table_header", "balance.json")
            data = ci.b(path)
            bm.add(data)

        else:
            print("\n表格名请输入(e, i, b)")

    return em, im, bm