import configparser
config = configparser.ConfigParser()
config.read('examples.ini')
print('Sections in the INI File : ',config.sections())
print('It is','bitbucket.org' in config ,'that [bitbucket.org] is a section of examples.ini')
print('It is','bytebong.com' in config ,'that [bytebong.org] is a section of examples.ini')

print('config[\'bitbucket.org\'][\'User\']=',config['bitbucket.org']['User'])
print('config[\'DEFAULT\'][\'Compression\']=',config['DEFAULT']['Compression'])
topsecret = config['topsecret.server.com']
print('config[\'topsecret.server.com\']=',topsecret['ForwardX11'])
print('config[\'topsecret.server.com\']=',topsecret['Port'])


print("The for Loop:")
bigbuck=config['bitbucket.org']
for key in bigbuck: print(bigbuck,'[',key,']=',bigbuck[key])
default=config['DEFAULT']
print(default.get('CompressionLevel', '3'))
