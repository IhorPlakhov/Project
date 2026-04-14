
class File():

    def Check_File_Name(self, name):
        symbols = "\\/|><\"?*"
        if(len(name)<= 255):
            for i in symbols:
                if i in self.name:
                    print("Your file name cannot have symbols(\ | / > < ? \" *) ")
                    return False
            name+=".txt"
            return name
        else:
            print("Your file name cannot be more than 255 symbols")
            return False
    
class ForbiddenSymbol(Exception):

    def __init__(self, msg, ch):
        self.massage = msg
        self.char = ch
    
    def TextMassage(self):
        return f"Error: {self.massage} {self.char}"