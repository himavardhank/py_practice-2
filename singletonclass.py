class Singleton:
    __instance=None
    @staticmethod
    def getInstance():
        if Singleton.__instance==None:
            Singleton()
        return Singleton.__instance
    def __init__(self):
        if Singleton.__instance!=None:
            raise Exception("this class is a singleton")
        else:
            Singleton.__instance=self
s=Singleton()
print(s)
s1=Singleton.getInstance()
print(s1)
s2=Singleton.getInstance()
print(s2)
