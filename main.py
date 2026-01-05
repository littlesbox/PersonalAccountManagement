from manager.expenditure_manager import ExpenditureManager
from manager.income_manager import IncomeManager
from manager.balance_manager import BalanceManager
from operation.add_data import add_data
from operation.list_data import list_data
from operation.modify_data import modify_data
from operation.delete_data import delete_data


em = ExpenditureManager()
im = IncomeManager()
bm = BalanceManager()

while True:

    prompt = input('请选择你的操作(add/list/modify/delete/save/exit):')

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

    #退出程序
    elif prompt == "exit":
        break

    else:
        print('未知命令，请重新输入')