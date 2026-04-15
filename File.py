
class File():

    def Check_File_Name(self, name):
        symbols = "\\/|><\"?*"
        if(len(name)<= 255):
            for i in symbols:
                if i in name:
                    raise ForbiddenSymbol(name, i)
            name+=".txt"
            return name
        else:
            print("Your file name cannot be more than 255 symbols")
            return False
        
    def WriteFile(self,name, arr, element):
        with open(name,'w') as f:
            print(arr[i],file=f,end=" ")
            for i in range (1,len(arr),50):
                for i in range (1,50):
                    print(arr[i],file=f,end=" ")
                    print(" ")


    
class ForbiddenSymbol(Exception):
    
    def __init__(self, symbol, name):

        super().__init__(f"Error: Your file name: '{name}' has forbidden symbol {symbol}")