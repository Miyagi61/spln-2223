import sys
import re
import argparse

flags_list = ['p','o']
procedure_dic = {
    'input' : 'stdin',
    'output' : 'stdout',
    'poems' : False,
    'lang' : 'pt'
}
errors = []

def get_input():
    """Gets the input text according with the register in procedure_dic"""
    text = ''
    if procedure_dic['input'] == 'stdin':
        for line in sys.stdin:
            text+=line
    else:
        input = open(procedure_dic['input'],'r')
        text = input.read()
    return text

def write_output(output):
    """Writes the ouput on the location registered in procedure_dic"""
    if procedure_dic['output'] == 'stdout':
        sys.stdout.write(output)
    else:
        file = open(procedure_dic['output'],'w')
        file.write(output)


def register_error(error):
    """Register an error on the error stack"""
    errors.append(f'Error: {error}')

def have_errors():
    """Reports if there have been errors in the program"""
    return len(errors) > 0

def print_errors():
    """Imprime todos os erros detetados"""
    for error in errors:
        print(error)

def update_files(arg,field):
    """Atualiza os ficheiros registados para leitura ou escrita pelo programa"""
    files = arg.split()
    if len(files) == 1:
        if (field == 'input' and procedure_dic[field] != 'stdin') or field == 'output' and procedure_dic[field] != 'stdout':
            register_error(f'Multiple {field} files given (4) - {files}')
        else:
            procedure_dic[field] = files[0]
    elif len(files) > 1:
        register_error(f'Multiple input files given (3)')


def get_first_word(arg):
    """Return flag from an argument (first word of the string)"""
    return re.sub(r'((\w|\.|_)+)\s*.*',r'\1',arg)

def duplicate_flags(args):
    """Checks for duplicate flags on initial arguments"""
    n_flags = {}
    for flag in flags_list:
        n_flags[flag] = 0

    for arg in args:
        word = get_first_word(arg)
        if word in flags_list:
            n_flags[word] += 1

    duplicate = False
    for flag,n in n_flags.items():
        if n > 1:
            duplicate = True
            register_error(f"Multiple {flag} used (2)")
    return duplicate

def process_flag(flag,arg):
    """Process a flag, updating procedure_dic accordingly"""
    rest = arg[len(flag):]
    if flag == 'p':
        procedure_dic['poems'] = True
        update_files(rest,'input')
    elif flag == 'o':
        update_files(rest,'output')


def process_arguments():
    """Processes and checks for errors on the initial arguments"""
    parser = argparse.ArgumentParser(
                    prog='tokenizerSPLN',
                    description='Tokenizes a text file',
                    epilog='Work done in the context of the course (SPLN) of the Master in Informatics Engineering of the University of Minho (UMinho).')
    
    parser.add_argument('-l', '--language', help='Language of the abbreviations used', default='pt')
    parser.add_argument('-i', '--input', help='Input file', default='stdin')
    parser.add_argument('-o', '--output', help='Output file', default='stdout')
    
    args = parser.parse_args()
    procedure_dic['input'] = args.input
    procedure_dic['output'] = args.output
    procedure_dic['language'] = args.language

    return procedure_dic