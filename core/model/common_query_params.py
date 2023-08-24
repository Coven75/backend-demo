class CommonQueryParams:
    def __init__(self, pageIndex: int = 0, pageSize: int = 10, sortName: str = None, sortDirection: str = None):
        self.pageIndex = pageIndex
        self.pageSize = pageSize
        self.sortName = sortName
        self.sortDirection = sortDirection
