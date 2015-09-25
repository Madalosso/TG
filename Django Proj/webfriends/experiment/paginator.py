def paginate(page, paginator):
    pagesIndex = {}
    pagesIndex[2] = int(page)
    if int(page) == 1:
        pagesIndex[1] = int(0)
        pagesIndex[0] = 0
    if int(page) == 2:
        pagesIndex[1] = 1
        pagesIndex[0] = 0
    if paginator.num_pages - int(page) > 1:
        pagesIndex[3] = int(page) + 1
        pagesIndex[4] = int(page) + 2
        pagesIndex[0] = int(page) - 2
        pagesIndex[1] = int(page) - 1
    if paginator.num_pages - int(page) == 1:
        pagesIndex[3] = int(page) + 1
        pagesIndex[4] = 0
        pagesIndex[0] = int(page) - 2
        pagesIndex[1] = int(page) - 1
    if paginator.num_pages - int(page) == 0:
        pagesIndex[3] = 0
        pagesIndex[4] = 0
        pagesIndex[0] = int(page) - 2
        pagesIndex[1] = int(page) - 1
    return pagesIndex
