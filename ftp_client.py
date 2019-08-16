from ftplib import FTP

#  ---------  LOGIN ---------- #

users = {'adri': '123'}


while True:
    while True:
        user = input('Digite seu Username: ')
        passwrd = input('Digite sua Senha: ')
        
        ok = False
        for i in users:
            if user == i and passwrd == users[i]:
                ok = True
                break

        if ok:
            break
        else:
            print('Tente novamente!')
    break


#  ---------  SHELL ---------- #

def comandos():
    print('Comandos: ')
    print('ls - Listar diretório.')
    print('pwd - Apresenta diretório atual do servidor.')
    print('rm "file name" - Exclui arquivo.')
    print('mv "file name" - Renomeia o arquivo.')
    print('touch "file name" - upload do arquivo.')
    print('wget "file name" - download do arquivo.')
    print('cd "directory name" - Entrar em um diretório.')
    print('mkdir "directory name - Cria uma nova pasta.')
    print('rmdir "directory name" - Exclui uma pasta.')
    print('help - Ver comandos.')
    print('exit - Sair.')

def upload(name):
    filename = './' + name
    myfile = open(filename, 'rb')
    ftp.storlines('STOR ' + filename, myfile)
    myfile.close()

def download(name):
    filename = name
    localfile = open(filename, 'wb')
    ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
    localfile.close()

ftp = FTP('')
ftp.encoding = 'utf-8'
ftp.connect('localhost', 1026)
ftp.login('user', '12345')
ftp.getwelcome()

while True:
    saber = input('ftp> {}> '.format(ftp.pwd())).split()

    if saber[0] == 'ls': 
        ftp.dir()

    elif saber[0] == 'pwd': 
        print(ftp.pwd())

    elif saber[0] == 'rm': 
        for i in range(1, len(saber)):
            ftp.delete(saber[i])

    elif saber[0] == 'mv': 
        ftp.rename(saber[1], saber[2])    

    elif saber[0] == 'touch': 
        for i in range(1, len(saber)):
            upload(saber[i])

    elif saber[0] == 'wget':
        for i in range(1, len(saber)): 
            download(saber[i])

    elif saber[0] == 'cd': 
        try:
            ftp.cwd('{}'.format(saber[1]))
        except:
            print('Diretório não existente...')

    elif saber[0] == 'mkdir': 
        for i in range(1, len(saber)):
            ftp.mkd(saber[i])

    elif saber[0] == 'rmdir': 
        for i in range(1, len(saber)):
            ftp.rmd(saber[i])

    elif saber[0] == 'help': 
        comandos()

    elif saber[0] == 'exit': 
        ftp.quit()
        break
