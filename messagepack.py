class messagepack:
    def __init__(self,*args):
        self.code = -1
        self.type = -1
        self.message = ""

        self.setAttr(args)

    def setAttr(self, *args):
        # set attribute for a pack with passed argument
        length = len(args)
        
        if length < 1 or length > 3 or length == 2:
            pass
        elif length == 3:
            # code, type and message passed
            if args[0] < 0 or args[0] > 4:
                pass
            elif args[1] != 0 or args[1] != 1:
                pass
            else: 
                self.code = args[0]
                self.type = args[1]
                for i in range(2,len(args)):
                    self.message += args[i]
        elif length == 1:
            if type(args[0]) is list or type(args[0] is tuple):
                # if arguments represented as list or tuple
                self.setAttr(args[0][0],args[0][1],args[0][2])
            else:
                if "." in args[0]:
                # a list represented as string
                    buffer = args[0].split(".")
                    if buffer[0].isdigit() and buffer[1].isdigit():
                        self.setAttr(int(buffer[0]),int(buffer[1]),buffer[2])
                elif self.code != -1 and self.type != -1:
                    # message passed with specified code and type
                    self.message = args[0]
        # return default pack attribute if args is invalid
        return self

    def ToString(self):
        return f"{self.code}.{self.type}.{self.message}"

    @staticmethod
    def Parse(string):
        pack = messagepack().setAttr(string)
        return pack

    

