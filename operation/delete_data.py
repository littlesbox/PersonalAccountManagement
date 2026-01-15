
def delete_data(em, im, bm):
    table_name = input('\n请选择想要删除的数据所在表格的名字(e, i, b):')
    if table_name == "e":
        if em.is_empty():
            print("\n当前表格为空")
        else:
            input_id = int(input('\n请选择想要删除数据的 id:'))
            if input_id in em.get_ids():
                em.delete(input_id)
            else:
                print("\n当前表中不存在该id，请输入正确的id")

    elif table_name == "i":
        if im.is_empty():
            print("\n当前表格为空")
        else:
            input_id = int(input('\n请选择想要删除数据的 id:'))
            if input_id in im.get_ids():
                im.delete(input_id)
            else:
                print("\n当前表中不存在该id，请输入正确的id")

    elif table_name == "b":
        if bm.is_empty():
            print("\n当前表格为空")
        else:
            input_id = int(input('\n请选择想要删除数据的 id:'))
            if input_id in bm.get_ids():
                bm.delete(input_id)
            else:
                print("\n当前表中不存在该id，请输入正确的id")
    else:
        print("\n表格名请输入(e, i, b)")
    return em, im, bm