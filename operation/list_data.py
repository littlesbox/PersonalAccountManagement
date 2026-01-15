
def list_data(em, im, bm):

    if em.is_empty():
        print("\n支出表为空")
    else:
        print('\n' + '=' * 30 + '以下是支出表' + '=' * 70)
        em.display()
        print("\n")
    
    if im.is_empty():
        print("\n收入表为空")
    else:
        print('\n' + '=' * 30 + '以下是收入表' + '=' * 70)
        im.display()
        print("\n")

    if bm.is_empty():
        print("\n余额表为空")
    else:
        print('\n' + '=' * 30 + '以下是余额表' + '=' * 70)
        bm.display_class()
        print("\n")
