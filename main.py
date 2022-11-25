import os


class Background:
    BG_RED      = "\033[41m"
    BG_GREEN    = "\033[42m"
    BG_YELLOW   = "\033[43m"
    BG_BLUE     = "\033[44m"
    BG_MAGENTA  = "\033[45m"
    BG_CYAN     = "\033[46m"
    ENDC        = "\033[0m"
    def __init__(self) -> None:
        self.color={}
        self.colors=['red', 'green', 'yellow', 'blue', 'magenta', 'cyan']
        self.bg_color_functions = [self.bg_red, self.bg_green, self.bg_yellow, self.bg_blue, self.bg_magenta, self.bg_cyan]
    def magenta(self,text):  return f"{self.BG_MAGENTA}{text}{self.ENDC}"
    def green(self,text):    return f"{self.BG_GREEN}{text}{self.ENDC}"
    def blue(self,text):     return f"{self.BG_BLUE}{text}{self.ENDC}"
    def red(self,text):      return f"{self.BG_RED}{text}{self.ENDC}"
    def yellow(self,text):   return f"{self.BG_YELLOW}{text}{self.ENDC}"
    def cyan(self,text):     return f"{self.BG_CYAN}{text}{self.ENDC}"    

class Text:
    RED         = "\033[31m"
    GREEN       = "\033[32m"
    MAGENTA     = "\033[35m"
    BLUE        = "\033[34m"
    YELLOW      = "\033[33m"
    CYAN        = "\033[36m"
    BG_RED      = "\033[41m"
    BG_GREEN    = "\033[42m"
    BG_YELLOW   = "\033[43m"
    BG_BLUE     = "\033[44m"
    BG_MAGENTA  = "\033[45m"
    BG_CYAN     = "\033[46m"
    ENDC        = "\033[0m"
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    ALPHABET = alphabet.upper()
    beggining_of_all_colors_lower = 'rgybmc'
    beggining_of_all_colors_upper = beggining_of_all_colors_lower.upper()
    ending_of_all_colors_lower = 'dnwean'
    ending_of_all_colors_upper = ending_of_all_colors_lower.upper()
    non_alphbetical = '!@#$%^&*()_+=-1234567890][}{";:?/\\<>,.`~|'
    punctuation = '?!.,;:()"'

    def __init__(self):
        self.colors={'red':self.red, 'green':self.green, 'yellow':self.yellow, 'blue':self.blue, 'magenta':self.magenta, 'cyan':self.cyan}
        self.color_functions = [self.red, self.green, self.yellow, self.blue, self.magenta, self.cyan]
        self.fs_color_functions = frozenset(self.color_functions)
    def magenta(self,text:str):     return f"{self.GREEN}{text}{self.ENDC}"
    def green(self,text:str):       return f"{self.GREEN}{text}{self.ENDC}"
    def blue(self,text:str):        return f"{self.BLUE}{text}{self.ENDC}"
    def red(self,text:str):         return f"{self.RED}{text}{self.ENDC}"
    def yellow(self,text:str):      return f"{self.YELLOW}{text}{self.ENDC}"
    def cyan(self,text:str):        return f"{self.CYAN}{text}{self.ENDC}"

    def colorUpperText(self, color:str, text:str):
        func = self.colors[color]
        retv = []
        for x in text:
            if x in self.ALPHABET:addition = func(x)
            else:addition = x
            retv.append(addition)
        rstring = "".join(retv)
        return rstring

    def colorLowerText(self, color:str, text:str):
        func = self.colors[color]
        retv = []
        for x in text:
            if x in self.alphabet:addition = func(x)
            else:addition = x
            retv.append(addition)
        rstring = "".join(retv)
        return rstring

    def __remove_non_alphabetical(self, string):
        return "".join([x for x in string if string not in self.non_alphbetical])

    def colorAlphabeticalText(self, color:str, text:str):
        """ color <text> using <color> if it is in uppercase or lowercase alphabet """
        func = self.colors[color]
        retv = []
        for x in text:
            if x in self.alphabet or x in self.ALPHABET:addition = func(x)
            else:addition = x
            retv.append(addition)
        rstring = "".join(retv)
        return rstring

    def colorChar(self, string_char:str, color:str):
        func = self.__get_color_function(color)
        retv=[]
        for x in text:
            if x == string_char:addition = func(x)
            else:addition = x
            retv.append(addition)
        rstring = "".join(retv)
        return rstring

    def highlightWord(self, word:str, paragraph:str, color:str):
        func = self.colors[color]
        words = paragraph.split(" ")
        retv = []
        has_period = False
        for x in words:
            if x[-1] in self.punctuation:
                punc = x[-1]
                xword = x[:-1]
            else:
                punc = ""
                xword = x
            if x == word:
                wordstring = f" {func(xword)}{punc}"
            else:
                wordstring = f" {xword}{punc}"
            retv+=wordstring
            retval = "".join(retv)
        print(retval)
            
def example():
    text = Text()
    text.highlightWord(word="hello", paragraph="why hello there how are you. it is a hello day", color='yellow')
    text.colorUpperText(color="green", text="ABC asdf |||[]")
    text.colorLowerText(color="green", text="ABC asdf |||[]")

example()
exit()