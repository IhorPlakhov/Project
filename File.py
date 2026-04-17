
class File():
        
    def Write_File(self, size, arr, element):
        name = "output.txt"
        with open(name,'w') as f:
            for i in range(0,len(arr),size):
                line = " ".join([str(x) for x in arr[i: i+size]])
                f.write(line+'\n')
            f.write(f"Target element: {element}")


    
class ForbiddenSymbol(Exception):
    
    def __init__(self, symbol, name):

        super().__init__(f"Error: Your file name: '{name}' has forbidden symbol {symbol}")