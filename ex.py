from sasimport import Dataset, SASFile 

rawdata = '/path/to/rawdata.txt'
libpath = '/path/to/sas/libname'
sasprog = '/path/to/generated/sasscript.sas'

ds = Dataset(infile=rawdata, delimiter='tab', dsd=True, libname='test', libpath=libpath, dsname='test')

# Variable order maps to column order (from left to right) of the raw data source.
# "name" is the only required argument
ds.variable(name='uid', type='num', length='5', informat='19.', format='19.', label='Unique Identifier')
ds.variable(name='desc', type='char', length='18', informat='18.', format='18.', label='Description')
ds.variable(name='datestamp', type='num', informat='yymmdd10.', format='yymmddn8.', label='Date Entered')
ds.variable(name='timestamp', type='num', informat='time8.', format='time8.', label='Time Entered')

sas = SASFile(sasprog, ds.generate())
sas.output() # Create SAS File
sas.run()    # Run SAS program -> defaults logfile to same dir as sasprog
