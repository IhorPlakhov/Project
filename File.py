class File():

    def __init__ (self, name = "output.txt"):
        self.name = name
        
    def write_file(self, size, arr, element):
        with open(self.name,'w') as f:
            for i in range(0,len(arr),size):
                line = " ".join([str(x) for x in arr[i: i+size]])
                f.write(line+'\n')
            f.write(f"Target element: {element}")
            