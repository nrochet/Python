def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise. For Barbara's dignity
    
    """

    for i in meals:
       
        a=[index for index, value in enumerate(meals) if value == i]

        if len(a)>=2:
            for j in range(len(a)-1):
                if a[j+1]-a[j]==1:
                    return True
    return False