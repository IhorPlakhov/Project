class SearchType:
    SEQUENTIAL = "Sequential Search"
    FIBONACCI = "Fibonacci Search"
    INTERPOLATION = "Interpolation Search"
    HASH = "Hash Function Search"
    SORTED_REQUIRED = (FIBONACCI, INTERPOLATION)

class UIConfig:
    WINDOW_SIZE = "450x300"
    TABLE_SIZE = "1500x850"
    TABLE_COLUMNS = 40
    TABLE_ROWS = 25
    MIN_ARRAY_SIZE =  100
    MAX_ARRAY_SIZE =  1000
    MAX_INPUT_LENGTH = 5
    COMBO_PLACEHOLDER = "Choose algorithm"
    MAIN = ("Comfortaa", 20)
    LABEL_SMALL = ("Comfortaa", 18)
    TABLE_CELL = ("Comfortaa", 10)
    TABLE_INFO = ("Comfortaa", 25)
    TABLE_COUNTER = ("Comfortaa", 30)
    BUTTONS_BACKGROUND = "#303938"
    BUTTONS_TEXT = "#edc68d"
    TEXT_COLOR = "#04c7ee"
    CELL_DEFAULT = "#edc68d"
    CELL_VISITED = "#deda03"
    CELL_FOUND = "#15970c"
    TABLE_BACKGROUND = "#000000"
    CELL_TEXT = "#000000"
    STATUS_FOUND = "#51ea3d"
    STATUS_NOT_FOUND = "#f1392b"