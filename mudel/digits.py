
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
            'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\\',
            'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'",
            'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/','`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=',
        ]
        #save english digit with shift typed
        self.en_shift_digits = [
            'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '{', '}', '|',
            'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':', '"',
            'Z', 'X', 'C', 'V', 'B', 'N', 'M', '<', '>', '?','~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+',
        ]
        #save english digit with no shift and whith typed
        self.en_all_digits = [*self.en_digits, *self.en_shift_digits]
        #save persian digit no shift typed
        self.fa_digits = [
            'ض', 'ص', 'ث', 'ق', 'ف', 'غ', 'ع', 'ه', 'خ', 'ح', 'ج', 'چ', "\\",
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
    @classmethod
    def detect_language(cls , text):
        """
        check language (persian , english)
        input:
            text: input text
        output:
            'persian' if text persian
            'english' if text english
            'mixed' if text mixed
            'unknown' if not in persian or english
        """
        persian_chars = 0
        english_chars = 0
        other_chars = 0
        
        # unicode persian char range
        persian_range = (
            (0x0600, 0x06FF),  
            (0xFB50, 0xFDFF),    
            (0xFE70, 0xFEFF),
            )
        
        for char in text:
            if char.isalpha():
                code_point = ord(char)
                is_persian = False
                for start, end in persian_range:
                    if start <= code_point <= end:
                        persian_chars += 1
                        is_persian = True
                        break
                
                if not is_persian and char.isascii():
                    english_chars += 1
                elif not is_persian:
                    other_chars += 1
        
        total_alpha = persian_chars + english_chars
        
        if total_alpha == 0:
            return 'unknown'
        
        persain_ratio = persian_chars / total_alpha
        english_ratio = english_chars / total_alpha
        
        if persain_ratio > 0.7:
            return 'persian'
        elif english_ratio > 0.7:
            return 'english'
        else:
            return 'mixed'
