class Text:
    def __init__(self,text):
        self.__text=text

    def add(self,article):
        article._addContent(self.__text)

class Image:
    def __init__(self,img):
        self.__img=img

    def add(self,article):
        article._addContent(f"print {self.__img}")

class ObjectInform:
    def __init__(self,caption):
        self.__caption=caption
        self.__contents=[]

    @property
    def caption(self):
        return self.__caption

    def _addContent(self,content):
        self.__contents.append(content)

    def _useContent(self,func):
        for content in self.__contents:
            func(content)


class Gasset(ObjectInform):
    def addArticle(self,caption,*contents):
        article=Article(caption)
        for content in contents:
            article.add(content)
        self._addContent(article)

    def useArticle(self,func):
        self._useContent(func)


class Printer:
    def __printArticle(self,article):
        print(article.caption)
        article.use(print)

    def print(self,gasset):
        print(gasset.caption)
        gasset.useArticle(self.__printArticle)

class Article(ObjectInform):
    def add(self,type):
        type.add(self)

    def use(self,func):
        self._useContent(func)



gasset=Gasset("Вода")
gasset.addArticle("hdjfhkjdd", Image("img.png"),Text("j<shkdfjghshdfgakjdgfahldsgf"))
printer=Printer()
printer.print(gasset)
