from digits import Digits
class Convert:
    """"""
    def __init__(self, text, language):
        self.language = language
        self.text = text
        self.en_all_digit = Digits().en_all_digits
        self.fa_all_digit = Digits().fa_all_digits
        if language in ["en","english"]:
            self.language = "en"

        elif language in ["fa" , "persian" , "farsi"]:
            self.language = "fa"

    def convert_to_persian(self):
        new_text = ""
        for char in self.text:
            if char in self.en_all_digit:
                index = self.en_all_digit.index(char)
                new_text += self.fa_all_digit[index]
            else:
                new_text += char
        return new_text
    def convert_to_english(self):
        new_text = ""
        for char in self.text:
            if char in self.en_all_digit:
                index = self.en_all_digit.index(char)
                new_text += self.fa_all_digit[index]
            else:
                new_text += char
        return new_text
my_text= Convert("\hdj,k" , "english").convert_to_persian()
print(my_text)

