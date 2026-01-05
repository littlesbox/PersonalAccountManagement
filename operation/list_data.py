
def list_data(em, im, bm):
    table_name = input('请选择想要查看的表格的名字(e, i, b，all):')
    if table_name == "e":
        em.display()
    
    elif table_name == "i":
        im.display()
    
    elif table_name == "b":
        bm.display_class()
    
    elif table_name == "all":
        print('=' * 30 + '以下是支出表' + '=' * 70)
        em.display()
        print('=' * 30 + '以下是收入表' + '=' * 70)
        im.display()
        print('=' * 30 + '以下是余额表' + '=' * 70)
        bm.display_class()
    
    else:
        print("表格名请输入(e, i, b)")