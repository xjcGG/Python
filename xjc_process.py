from multiprocessing import Process


class Myprocess(Process):

    def __init__(self, name):
        super(Myprocess,self).__init__(Process)
        self.name = name
