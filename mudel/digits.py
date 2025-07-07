class Digits:
    """
    this class is for return digits on the list 
    who use it ? 

    Digits.en_digits -> (whiout shift)
    Digits.en_shift_digits -> (with shift)
    Digits.en_all_digits -> (all language digits with shift and whiout shift)
    
    supported languages -> persian and english (with shift and no shift)
    """
    def __init__(self):
        #save english digit no shift typed
        self.en_digits = [
            '`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=',
            'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\\',
            'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'",
            'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/'
        ]
        #save english digit with shift typed
        self.en_shift_digits = [
            '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+',
            'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '{', '}', '|',
            'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':', '"',
            'Z', 'X', 'C', 'V', 'B', 'N', 'M', '<', '>', '?'
        ]
        #save english digit with no shift and whith typed
        self.en_all_digits = [*self.en_digits, *self.en_shift_digits]
        #save persian digit no shift typed
        self.fa_digits = [
            'ض', 'ص', 'ث', 'ق', 'ف', 'غ', 'ع', 'ه', 'خ', 'ح', 'ج', 'چ', 
            'ش', 'س', 'ی', 'ب', 'ل', 'ا', 'ت', 'ن', 'م', 'ک', 'گ',
            'ظ', 'ط', 'ز', 'ر', 'ذ', 'د', 'پ', 'و', 'ژ', 'ء',
            '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹', '۰', '-', '='
        ]
        #save persian digit with shift typed
        self.fa_shift_digits = [
            'ْ', 'ٌ', 'ٍ', 'ً', 'ُ', 'ِ', 'َ', 'ّ', ']', '[', '}', '{',
            'ؤ', 'ئ', 'إ', 'أ', 'آ', 'ة', '»', '«', '؛', ':', '"',
            'ـ', 'ٓ', 'ٰ', 'ٔ', 'ٕ', 'ٔ', 'ٓ', 'ٰ', 'ٖ', 'ٗ',
            '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+'
        ]
        #save persian digit no shift and whith typed
        self.fa_all_digits = [*self.fa_digits , *self.fa_shift_digits]