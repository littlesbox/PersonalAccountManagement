
def delete_data(em, im, bm):
    table_name = input('请选择想要删除的数据所在表格的名字(e, i, b):')
    input_id = int(input('请选择想要删除数据的input_id:'))
    if table_name == "e":
        em.delete(input_id)
    elif table_name == "i":
        im.delete(input_id)
    elif table_name == "b":
        bm.delete(input_id)
    else:
        print("表格名请输入(e, i, b)")
    return em, im, bm