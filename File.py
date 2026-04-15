
class File():

    def Check_File_Name(self, name):
        symbols = "\\/|><\"?*"
        if(len(name)<= 255):
            for i in symbols:
                if i in name:
                    raise ForbiddenSymbol(i)
            name+=".txt"
            return name
        else:
            print("Your file name cannot be more than 255 symbols")
            return False
        
    def WriteFile(self,name):
        with open(name,'w') as f:
            pass


    
class ForbiddenSymbol(Exception):
    
    def __init__(self, symbol, name):

        super().__init__(f"Error: Your file name: '{name}' has forbidden symbol {symbol}")