class CustomStr:
    def __init__(self, text):
        self.text = text

    def custom_split(self, *splitt):
        result = [self.text]
        for delimiter in splitt:
            n = []
            for part in result:
                n.extend(part.split(delimiter))
            result = n
        return [item for item in result if item]

    def remove_duplicate(self):
        none_string = ''
        for char in self.text:
            if char not in none_string:
                none_string += char
        return none_string

    def set(self, index, word):
        if 0 <= index < len(self.text):
            result = list(self.text)
            result[index] = word
            return ''.join(result)
        return self.text

    def isfloat(self):
        try:
            float(self.text)
            return True
        except ValueError:
            return False

    def ispalindrome(self):
        return self.text == self.text[::-1]


c1 = CustomStr('sepid')
print(c1.custom_split('e', 's'))   
print(c1.remove_duplicate())        
print(c1.set(2, 'a'))               

c2 = CustomStr('1.2')
print(c2.isfloat())                 

c3 = CustomStr('biboo')
print(c3.ispalindrome())            

c4 = CustomStr('bib')
print(c4.ispalindrome())            
