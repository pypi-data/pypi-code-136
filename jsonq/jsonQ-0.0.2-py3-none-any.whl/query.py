class Query():
    def __init__(self,query):
        self.query = query

    def where(self,condition):
        data = []
        for q in self.query:
            if condition[1] == "==":
                if q[condition[0]] == condition[2]:
                    data.append(q)
            elif condition[1] == "!=":
                if q[condition[0]] != condition[2]:
                   data.append(q)
            elif  condition[1] == ">":
                if q[condition[0]] > condition[2]:
                    data.append(q)
            elif  condition[1] == ">=":
                if q[condition[0]] >= condition[2]:
                    data.append(q)
            elif  condition[1] == "<":
                if q[condition[0]] < condition[2]:
                    data.append(q)
            elif  condition[1] == "<=":
                if q[condition[0]] <= condition[2]:
                    data.append(q)
            elif condition[1] == "is":
                if q[condition[0]] is condition[2]:
                    data.append(q)
            elif condition[1] == "not":
                if q[condition[0]] != condition[2]:
                    data.append(q)
        return data
    