# -*- coding: utf-8 -*-
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

def get_config_file(localpath=False):
	from os import listdir, path
	import ConfigParser
	if not localpath:
		localpath = path.dirname(path.realpath(__file__)) + '/'
	#GET CONFIG FILE
	cfg_file_names = filter(lambda x: x.endswith('.cfg'), listdir(localpath))
	if len(cfg_file_names) > 1:
	    raise IndexError('There are multiple *.cfg files in your experiment\'s rot directory (commonly .../faceRT/experiment) - Please delete all but one (whichever you prefer). The script will not run until then.')
	if len(cfg_file_names) == 0:
	    localpath += '/config_examples/'
	    cfg_file_names = ["gen.cfg"]
	
	config = ConfigParser.ConfigParser()
	config.read(localpath+cfg_file_names[0])
	return config
	#END GET CONFIG FILE
	
def flatten_list(lis):
    from collections import Iterable
    for item in lis:
	if isinstance(item, Iterable) and not isinstance(item, basestring):
	    for x in flatten_list(item):
		yield x
	    else:
		yield item
