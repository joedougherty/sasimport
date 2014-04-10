from sasimport import Dataset, SASFile 

rawdata = '/path/to/rawdata.txt'
libpath = '/path/to/sas/libname'
sasprog = '/path/to/generated/sasscript.sas'

ds = Dataset(infile=rawdata, delimiter='tab', dsd=True, libname='comscore', libpath=libpath, dsname='test')

ds.variable(name='uid', type='num', length='5', informat='19.', format='19.', label='Unique Identifier')
ds.variable(name='desc', type='char', length='18', informat='18.', format='18.', label='Description')
ds.variable(name='datestamp', type='num', informat='yymmdd10.', format='yymmddn8.', label='Date Entered')
ds.variable(name='timestamp', type='num', informat='time8.', format='time8.', label='Time Entered')

sas = SASFile(sasprog, ds.generate())
sas.output()
