import os, sys, shutil
import os.path
import diz

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

variabile = []
path = sys.argv[1]
dirs=os.listdir(path)
dirname = []
count = 0
count_spy = 0
count_obf = 0
count_deal = 0
apk = 0
library = []

for file in dirs:
        if file.endswith('.apk'):
                print(file)
                apk = apk + 1
                os.system('jadx-1/bin/jadx %s' % (file))

for dirpath, dirnames, filenames in os.walk(path):
    for filename in [f for f in filenames if f.endswith(".so")]:
        if not os.path.basename(dirpath)in dirname:
            dirname.append(os.path.basename(dirpath))
        if not filename in variabile:
            variabile.append(filename)

if len(variabile) == 0:
    print('\n')
    print(color.BOLD + "No library found in the dictionary" + color.END)

print('\n')
print(color.BOLD + "Libraries found:" + color.END)
print('\n')
print(*variabile, sep = '\n')
print('\n')
print(color.BOLD + 'Different supported architectures: \n' + color.END)
print(*dirname, sep = '\n')

print('\n')
print(color.BOLD + 'Libraries found in the dictionary: \n' + color.END)

for i in variabile: 
    if i in diz.type1: 
        print('{} type: Obfuscator {} \n'.format(i, diz.type1[i])) 
        count = 1        
        count_obf = count_obf + 1
        library.append(i)
    if i in diz.type2: 
        print('{} type: Spyware {} \n'.format(i, diz.type2[i])) 
        count = 1       
        count_spy = count_spy + 1
        library.append(i)      
    if i in diz.type3: 
        print('{} type: SpyDealer {} \n'.format(i, diz.type3[i])) 
        count = 1
        count_deal = count_deal + 1
        library.append(i)
                        
print('\n')
print(color.BOLD +'ANALYSIS SUMMARY'+ color.END)
print('Number of APK analyzed: '+ str(apk))
if count == 0:
    print(color.BOLD + "No library found in the dictionary" + color.END)
else:
    print('Libraries: ',*library, sep='\n')
    print('Number of Obfuscator: '+ str(count_obf))
    print('Number of Spyware: '+ str(count_spy))
    print('Number of SpyDealer: '+ str(count_deal))


