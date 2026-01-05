
def modify_data(em, im, bm):
    table_name = input('请选择想要修改的数据所在表格的名字(e, i, b):')
    input_id = int(input('请选择想要修改数据的input_id:'))
    title = input('请选择想要修改数据的字段:')
    value = input('请输入新值:')

    if table_name == "e":
        if title == "金额":
            em.modify(input_id, title, float(value))
        else:
            em.modify(input_id, title, value)
    elif table_name == "i":
        if title == "金额":
            im.modify(input_id, title, float(value))
        else:
            im.modify(input_id, title, value)
    elif table_name == "b":
        if title == '日期':
            bm.modify(input_id, title, value)
        else:
            bm.modify(input_id, title, float(value))
    else:
        print("表格名请输入(e, i, b)")

    return em, im, bm