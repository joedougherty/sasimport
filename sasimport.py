class Dataset(object):
    variable_list = []
    lengths = []
    inputs = []
    informats = []
    formats = []
    labels = []

    def __init__(self, infile, delimiter, dsd, libname, libpath, dsname):
        self.infile = infile
        self.delimiter = delimiter
        self.dsd = dsd
        self.libname = libname
        self.libpath = libpath
        self.dsname = dsname

    def get_libname(self):
        return 'libname ' + self.libname + ' ' + '"' + self.libpath + '";\n' 

    def get_filename(self):
        return 'filename datafile ' + '"' + self.infile + '";\n'

    def get_infile(self):
        dlm = self.get_delimiter()
        if dlm == '09': 
            dlm = '"09"x'
        else:
            dlm = '"' + dlm + '"'

        return 'infile datafile dlm=' + dlm + ' ' + self.get_dsd() + ';\n'

    def get_dsd(self):
        if self.dsd == True:
            return 'dsd'
        return '' 

    def get_delimiter(self):
        readable_delims = {'tab': '09'}

        if self.delimiter in readable_delims:
            return readable_delims.get(self.delimiter)
        else:
            return self.delimiter

    def get_dsname(self):
        return 'data ' + self.libname + '.' + self.dsname + ';\n'
    
    def variable(self, name, type, length='', informat='', format='', label=''):
        self.variable_list.append(name)
        
        self.lengths.append(self.var_length(name, type, length))
        self.inputs.append(self.var_type(name, type))
        self.informats.append(self.var_informat(name, informat, type))
        self.formats.append(self.var_format(name, format, type))
        self.labels.append(self.var_label(name, label))

    def var_length(self, name, type, length):
        if length == '': return ''
        
        if type == 'char':
            return name + ' $' + length
        elif type == 'num':
            return name + ' ' + length 
        else:
            raise TypeError

    def gen_stmt(self, list, prefix, separator, suffix):
        stmt = prefix + ' '
        for i in list:
            stmt = stmt + i + separator
        return stmt + suffix

    def var_type(self, name, type):
        if type == 'num':
           return name
        elif type == 'char':
            return name + ' $'
        elif type == '':
            pass
        else:
            raise TypeError 

    def var_informat(self, name, informat, type):
        if informat == '': return ''

        if type == 'char':
            return name + ' $' + informat
        elif type == 'num':
            return name + ' ' + informat
        elif type == '':
            pass
        else:
            raise TypeError

    def var_format(self, name, format, type):
        if format == '': return ''

        if type == 'char':
            return name + ' $' + format
        elif type == 'num':
            return name + ' ' + format
        elif type == '':
            pass
        else:
            raise TypeError

    def var_label(self, name, label):
        return name + ' = ' + label  

    def generate(self):
        str = self.get_libname()
        str += self.get_filename()
        str += self.get_dsname()
        str += self.get_infile()
        str += self.gen_stmt(self.lengths, prefix='length', separator=' ', suffix=';\n')
        str += self.gen_stmt(self.informats, prefix='informat', separator=' ', suffix=';\n')
        str += self.gen_stmt(self.formats, prefix='format', separator=' ', suffix=';\n')
        str += self.gen_stmt(self.labels, prefix='label', separator='\n', suffix=';\n')
        str += self.gen_stmt(self.inputs, prefix='input', separator=' ', suffix=';\n')
        str += '\nrun;'
        return str

class SASFile(object):
    def __init__(self, file_location, code_string):
        self.file_location = file_location
        self.code_string = code_string
    
    def output(self):
        f = open(self.file_location, 'w')
        f.write(self.code_string)
        f.close()
