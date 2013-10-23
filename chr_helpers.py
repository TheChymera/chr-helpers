__author__ = 'Horea Christian'

def pre_save(filename, extension=''):
    from os import path, makedirs
    from shutil import move
    from datetime import date, datetime
    import pandas as pd
    jzt=datetime.now()
    time = str(date.today())+'_'+str(jzt.hour)+str(jzt.minute)+str(jzt.second)
    if path.isdir(path.dirname(filename)): 
		pass
    else:
		makedirs(path.dirname(filename))
    if path.isfile(filename + extension):
        if path.isdir(path.dirname(filename)+'/.backup'):
            pass
        else: makedirs(path.dirname(filename)+'/.backup')        
        newname = path.dirname(filename)+'/.backup/'+path.basename(filename)+'_'+time
        move(filename+extension, newname+extension)
        print 'moved pre-existing data file '+ filename +'.csv to backup location ('+newname+extension+')'
    else: pass
    
def save_pd_csv(dataframe, filename):
    pre_save(filename, extension='.csv')
    dataframe.to_csv(filename+'.csv')
    
def save_pd_tsv(dataframe, filename):
    pre_save(filename, extension='.tsv')
    dataframe.to_csv(filename+'.tsv', sep='\t')

def save_gen(filename, extension=''):
    pre_save(filename, extension)
    return open(filename+extension, 'a')

def get_config_file():
	from os import listdir, path
	import ConfigParser
	#GET CONFIG FILE
	cfg_file = filter(lambda x: x.endswith('.cfg'), listdir(path.dirname(path.realpath(__file__))))
	if len(cfg_file) > 1:
	    raise InputError('There are multiple *.cfg files in your experiment\'s rot directory (commonly .../faceRT/experiment) - Please delete all but one (whichever you prefer). The script will not run until then.')
	config = ConfigParser.ConfigParser()
	config.read(cfg_file)
	return config
	#END GET CONFIG FILE
