import os
from shutil import copyfile

pasta='C:\\Users\\<User>\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets\\'
imagens='C:\\Users\\<User>\\Pictures\\'
arquivos=os.listdir(pasta)

for arq in arquivos:
	if (os.stat(pasta+arq).st_size) > 100000:
		copyfile(pasta+arq, imagens+arq[0:6]+'.png')
