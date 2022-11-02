def solution(boxi, boxf):
    blk_r1 = [7, 15, 23, 31, 39, 47, 55, 63]
    blk_r2 = [6, 14, 22, 30, 38, 46, 54, 62]
    blk_d1 = [56, 57, 58, 59, 60, 61, 62, 63]
    blk_d2 = [48, 49, 50, 51, 52, 53, 54, 55]
    blk_l1 = [0, 8, 16, 24, 32, 40, 48, 56]
    blk_l2 = [1, 9, 17, 25, 33, 41, 49, 57]
    blk_u1 = [0, 1, 2, 3, 4, 5, 6, 7]
    blk_u2 = [8, 9, 10, 11, 12, 13, 14, 15]

    dr,dl,rd,ru,ul,ur,lu,ld =17,15,10,-6,-17,-15,-10,6

    def dr(position):
        if position in blk_d1:
            return 0
        elif position in blk_d2:
            return 0
        elif position in blk_r1:
            return 0
        else:
            return 17


    def dl(positon):
        if positon in blk_d1:
            return 0
        elif positon in blk_d2:
            return 0
        elif positon in blk_l1:
            return 0
        else:
            return 15


    def ur(positon):
        if positon in blk_u1:
            return 0
        elif positon in blk_u2:
            return 0
        elif positon in blk_r1:
            return 0
        else:
            return -15


    def ul(positon):
        if positon in blk_u1:
            return 0
        elif positon in blk_u2:
            return 0
        elif positon in blk_l1:
            return 0
        else:
            return -17


    def ru(positon):
        if positon in blk_r1:
            return 0
        elif positon in blk_r2:
            return 0
        elif positon in blk_u1:
            return 0
        else:
            return -6


    def rd(positon):
        if positon in blk_r1:
            return 0
        elif positon in blk_r2:
            return 0
        elif positon in blk_d1:
            return 0
        else:
            return 10


    def lu(positon):
        if positon in blk_l1:
            return 0
        elif positon in blk_l2:
            return 0
        elif positon in blk_u1:
            return 0
        else:
            return -10


    def ld(positon):
        if positon in blk_l1:
            return 0
        elif positon in blk_l2:
            return 0
        elif positon in blk_d1:
            return 0
        else:
            return 6
    n=0
    if boxi == boxf:
        return n

    list_for_boxi=[]
    available_moves= [dr(boxi),ul(boxi),dl(boxi),ur(boxi),rd(boxi),lu(boxi),ru(boxi),ld(boxi)]
    for x in available_moves:
        if x !=0:
            new_position= boxi+x
            list_for_boxi.append(new_position)
    n+=1
    if boxf in list_for_boxi:
        return n


    list_for_boxi1 = []
    for x in list_for_boxi:
        boxi=x
        available_moves = [dr(boxi), ul(boxi), dl(boxi), ur(boxi), rd(boxi), lu(boxi), ru(boxi), ld(boxi)]
        for x in available_moves:
            if x != 0:
                new_position = boxi + x
                list_for_boxi1.append(new_position)
    #print(f'list_for_boxi1={list_for_boxi1}')
    n+=1
    if boxf in list_for_boxi1:
        return n

    list_for_boxi2 = []
    for x in list_for_boxi1:
        boxi = x
        available_moves = [dr(boxi), ul(boxi), dl(boxi), ur(boxi), rd(boxi), lu(boxi), ru(boxi), ld(boxi)]
        for x in available_moves:
            if x != 0:
                new_position = boxi + x
                list_for_boxi2.append(new_position)
    n+=1
    if boxf in list_for_boxi2:
        return n


    list_for_boxi3 = []
    for x in list_for_boxi2:
        boxi = x
        available_moves = [dr(boxi), ul(boxi), dl(boxi), ur(boxi), rd(boxi), lu(boxi), ru(boxi), ld(boxi)]
        for x in available_moves:
            if x != 0:
                new_position = boxi + x
                list_for_boxi3.append(new_position)
    n+=1
    if boxf in list_for_boxi3:
        return n


    list_for_boxi4 = []
    for x in list_for_boxi3:
        boxi = x
        available_moves = [dr(boxi), ul(boxi), dl(boxi), ur(boxi), rd(boxi), lu(boxi), ru(boxi), ld(boxi)]
        for x in available_moves:
            if x != 0:
                new_position = boxi + x
                list_for_boxi4.append(new_position)
    n+=1
    if boxf in list_for_boxi4:
        return n

    list_for_boxi5 = []
    for x in list_for_boxi4:
        boxi = x
        available_moves = [dr(boxi), ul(boxi), dl(boxi), ur(boxi), rd(boxi), lu(boxi), ru(boxi), ld(boxi)]
        for x in available_moves:
            if x != 0:
                new_position = boxi + x
                list_for_boxi5.append(new_position)
    n+=1
    if boxf in list_for_boxi5:
        return n

    list_for_boxi6 = []
    for x in list_for_boxi5:
        boxi = x
        available_moves = [dr(boxi), ul(boxi), dl(boxi), ur(boxi), rd(boxi), lu(boxi), ru(boxi), ld(boxi)]
        for x in available_moves:
            if x != 0:
                new_position = boxi + x
                list_for_boxi6.append(new_position)
    n+=1
    if boxf in list_for_boxi6:
        return n











