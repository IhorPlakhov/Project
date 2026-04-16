
class File():

    def __init__(self, name):
        self.name = name

    def Check_File_Name(self):
        symbols = "\\/|><\"?*"
        if(len(self.name)<= 255):
            for i in symbols:
                if i in self.name:
                    raise ForbiddenSymbol(self.name, i)
            self.name+=".txt"
            return True
        else:
            print("Your file name cannot be more than 255 symbols")
            return False
        
    def Write_File(self, size, arr, element):
        with open(self.name,'w') as f:
            for i in range(0,len(arr),size):
                line = " ".join([str(x) for x in arr[i: i+size]])
                f.write(line+'\n')
            f.write(f"Target element: {element}")


    
class ForbiddenSymbol(Exception):
    
    def __init__(self, symbol, name):

        super().__init__(f"Error: Your file name: '{name}' has forbidden symbol {symbol}")