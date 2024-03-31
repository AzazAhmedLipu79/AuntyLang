import re

# Define token types
TOKEN_TYPES = [
    ('KNOCK_KNOCK', r'knock knock aunty'),
    ('COMMENT', r'!!.*'), 
    ('DISPLAY', r'shunen\s*\(\s*"([^"]*)"\s*\)'),
    ('FOR_LOOP', r'tahole\s*\(\s*tho\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*(\d+)\s*;\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*<\s*(\d+)\s*;\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*[\+\-]\s*[\+\-]\s*\)\s*{'),
    ('WHILE_LOOP', r'jokhon\s*\(\s*(hae)\s*\)\s*{'),
    ('BREAK', r'baad_den'),
    ('CONTINUE', r'abar'),
    ('ARRAY_DECLARATION', r'(tho|ar)\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*\[\s*(\".*?\"|\d+|na|hae)(\s*,\s*(\".*?\"|\d+|na|hae))*\s*\]'),
    ('ARRAY_ITERATION', r'tahole\s*\(\s*tho\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*0\s*;\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*<\s*([a-zA-Z_][a-zA-Z0-9_]*)\.qty\s*;\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*[\+\-]\s*[\+\-]\s*\)\s*{'),
    ('FUNCTION_DECLARATION', r'ekta_kaj_koren\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*=>\s*\(\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*\)\s*{'),
    ('FUNCTION_CALL', r'shunen\s*\(\s*"([^"]*)"\s*\)'),
    ('IF_ELSE', r'jodi_aunty\s*\(\s*(.*?)\s*\)\s*{'),
    ('PROGRAM_END', r'accha_aunty_ashi;'),
    ('NUMBER', r'\d+'), 
    ('BOOLEAN', r'(na|hae)'),
    ('OPERATOR', r'[\+\-\*\/]'),
    ('COMPARATOR', r'==|!=|<|>|<=|>='),
    ('NEWLINE', r'\n'),
    ('LEFT_PAREN', r'\('),
    ('RIGHT_PAREN', r'\)'),
    ('LEFT_BRACE', r'\{'),
    ('RIGHT_BRACE', r'\}'),
    ('SEMICOLON', r';'),
    ('VAR_DECLARATION', r'(tho|ar)\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*((?:".*?")|\d+|na|hae|[\w\s+\-*/]+)'),
    ('STRING', r'\"(.*?)\"'),
   ('VARIABLE', r'(?:[a-zA-Z_][a-zA-Z0-9_]*|(?<=")[a-zA-Z_][a-zA-Z0-9_]*(?="))'),
]

 
def shunen(message):
    print(message)

    
# Compile regex patterns for tokenization
TOKEN_REGEXES = [(name, re.compile(pattern)) for name, pattern in TOKEN_TYPES]

def lexer(code):
    tokens = []
    lines = code.split('\n')
    for line in lines:
        print("Current line:", line)
        while line:
            match = None
            for token_name, token_regex in TOKEN_REGEXES:
                pattern = token_regex.pattern
                match = re.match(pattern, line)
                if match:
                    if token_name == 'NEWLINE':
                        break
                    value = match.group(0)
                    if token_name != 'COMMENT':
                        print("Token:", token_name, "| Value:", value)
                        tokens.append((token_name, value))
                    line = line[len(value):].lstrip()
                    break
            if not match:
                raise SyntaxError('Invalid syntax near: ' + line)
    return tokens


SAMPLE_CODE ='''

knock knock aunty

!! data types and variables String, Number, Boolean, Array
tho amar_nam = "Kamal"
ar amar_bari = "Dhaka"
ar amar_ghor = "Mirpur"
ar amar_phone = "01711111111"
ar amar_jonmo_sal = 1990
ar ekhon = 2021
ar amar_umur = ekhon - amar_jonmo_sal
ar amiPorayValo = na 
ar amiKhelayValo = hae
tho bazarer_list = ["alu", "potol", "begun", "kumra", "mula"]


shunen("Amar nam " + amar_nam);
shunen("Amar bari " + amar_bari);
shunen("Amar ghor " + amar_ghor);
shunen("Amar phone " + amar_phone);
shunen("Amar umur " + amar_umur);
shunen("Ami poray valo " + amiPorayValo);
shunen("Ami khelay valo " + amiKhelayValo);
shunen("Bazarer list " + bazarer_list);




!! loop for and while
!!tahole(tho i = 0; i < 5; i++) {
!!  shunen("i hocche " + i);
!!}

jokhon(hae) {
    shunen("Ami khelay valo");
    amiKhelayValo = na;
    jodi_aunty (amiKhelayValo == na) {
        shunen("Ami khelay na");
        baad_den;
    } naile {
        abar;
    }

}



!! iterate array
tho bazarer_list = ["alu", "potol", "begun", "kumra", "mula"]
tahole(tho i = 0; i < bazarer_list.qty; i++) {
    shunen("Bazarer item " + bazarer_list[i]);
}



!! amar bio 
shunen("Amar nam hocche @amar_nam \n
\ar amar phone hocche @amar_phone \n 
\ar amar umur hocche @amar_umur");


ekta_kaj_koren nam_bolen=> (nam) => {
    shunen("Amar nam hocche " + nam);
    hyeche hae;
}

nam_bolen("Kamal");
nam_bolen("@amar_nam");



!! if else
jodi_aunty (amiPorayValo == na) {
    shunen("Ami poray valo na");
} othoba jodi_aunty (amiPorayValo == hae) {
    shunen("Ami poray valo hae");
} naile {
    shunenti("Ami beche nei");
}




accha_aunty_ashi;

'''
tokens = lexer(SAMPLE_CODE)
for token in tokens:
    print(token)
