from manager.expenditure_manager import ExpenditureManager
from manager.income_manager import IncomeManager
from manager.balance_manager import BalanceManager
from operation.add_data import add_data
from operation.list_data import list_data
from operation.modify_data import modify_data
from operation.delete_data import delete_data
from investment.invest_manager import InvestManager

em = ExpenditureManager()
im = IncomeManager()
bm = BalanceManager()
ivm = InvestManager()

while True:

    prompt = input('\n请选择你的操作(add/list/modify/delete/save)表示添加新的账单数据'
                   '\n(insert/remove/update/view/store)表示操作当前的投资数据'
                   '\n(exit)表示退出程序，请输入命令:')

    # 添加数据
    if prompt == "add":
        em, im, bm = add_data(em, im, bm)

    # 查看数据
    elif prompt == "list":
        list_data(em, im, bm)

    #修改数据
    elif prompt == "modify":
        em, im, bm = modify_data(em, im, bm)

    #删除数据
    elif prompt == "delete":
        em, im, bm = delete_data(em, im, bm)

    #保存数据
    elif prompt == "save":
        em.save()
        im.save()
        bm.save()
        print("\n内容已保存，三个暂存表内容已清空")
        em = ExpenditureManager()
        im = IncomeManager()
        bm = BalanceManager()

    elif prompt == "view":
        ivm.view()

    elif prompt == "store":
        ivm.store()

    elif prompt == "insert":
        ivm.insert()

    elif prompt == "remove":
        ivm.remove()

    elif prompt == "update":
        ivm.update()

    #退出程序
    elif prompt == "exit":
        break

    else:
        print('\n未知命令，请重新输入')