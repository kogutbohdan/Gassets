class Gasset:
    __articles={}
    def __init__(self,caption):
        self.__caption=caption

    @property
    def caption(self):
        return self.__caption

    def addArticles(self,name,article):
        self.__articles[name]=article

    def removeArticle(self,name):
        del self.__articles[name]

    def useArticle(self,func):
        for nameArticle in self.__articles:
            self.__articles[nameArticle].use(func)

class Printer:
    def print(self,gasset):
        print(gasset.caption)
        gasset.useArticle(print)

class Article:
    def __init__(self,caption):
        self.__caption=caption
        self.__contents=[]

    @property
    def caption(self):
        return self.__caption

    def addContent(self,content):
        self.__contents.append(content)

    def use(self,func):
        for content in self.__contents:
            func(content)


gasset=Gasset("Вода")

printer=Printer()
printer.print(gasset)
