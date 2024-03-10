import configparser

config = configparser.ConfigParser()
config.read('Test.cfg')
 
 
print(config.sections())
 

print(config['Regular Expression']['Pattern1']) 
 
print(config['Regular Expression']['Pattern2'])

print(config['Regular Expression1']['Pattern3']) 
 
print(config['Regular Expression1']['Pattern4'])

pattern1=config['Regular Expression']['Pattern1']
pattern2=config['Regular Expression']['Pattern2']

pattern3=config['Regular Expression1']['Pattern3']
pattern4=config['Regular Expression1']['Pattern4']
