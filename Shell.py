import click, os, shutil
import os

#ERROR HANDLING
def ExceptionHandlingCopy(ogsrc, src, dest, file):
    try:
        shutil.copy(src, dest)
    except Exception as error:
        print(error)
        
def ExceptionHandlingCopyTree(ogsrc, src, dest, file):
    try:
        shutil.copytree(src, dest)
    except Exception as error:
        print(error)


def ExceptionHandlingMove(ogsrc, src, dest, file):
    try:
        shutil.move(src, dest)
    except Exception as error:
        print(error)

#PATH FINDER
def Path(src, file):    
    path = src
    if(src == '.'):
        path = os.getcwd()
        return path
    path = os.path.join(path, file)
    return path


@click.group()

def main():
    pass

#List Directories
@click.command()
@click.argument('src')
def ls(src):
    '''Print contents of the given directory.'''
    if(src == '.'):
        src = os.getcwd()
    print('NAME' + 46*' ' + 'SIZE')
    for i in os.listdir(src):
        os.chdir(src)
        main = [i, os.stat(i).st_size]
        print(''.join(str(content).ljust(50) for content in main))
    
#Current Working Directory

@click.command()
def cwd():
    '''Current Working Directory.'''
    click.echo(os.getcwd())

#Move a file

@click.command()
@click.argument('file')
@click.argument('src')
@click.argument('dest')
def mov(file, src, dest):
    '''Move Files and Directories.'''
    ogsrc, path = src, Path(src, file)
    if(src == '.' and dest == '.'):
        src, dest = file, nnm
        ExceptionHandlingMove(ogsrc, src, dest, file)
    elif(src == '.'):
        src = file
        ExceptionHandlingMove(ogsrc, src, dest, file)
    elif(dest == '.' ):
        src, dest = path, os.path.join(os.getcwd(), file)
        ExceptionHandlingMove(ogsrc, src, dest, file)
    else:
        src = path
        ExceptionHandlingMove(ogsrc, src, dest, file)


#RENAME FILES AND DIRECTORIES
@click.command()
@click.argument('file')
@click.argument('newname')
@click.argument('src')

def rn(file, src, newname):
    '''Rename Files and Directories'''
    if(src == '.'):
        src = file
        dest, ogsrc = newname, src
        ExceptionHandlingMove(ogsrc, src, dest, file)
    else:
        src, dest = os.path.join(src, file), os.path.join(src, newname)
        ogsrc = file
        ExceptionHandlingMove(ogsrc, src, dest, file)

#COPY FILES AND DIRECTORIES

@click.command()
@click.argument('file')
@click.argument('src')
@click.argument('dest')

def cp(file, src, dest):
    '''Copy Files and Directories.'''
    ogsrc, path = src, Path(src, file)
    flag = os.path.isdir(file)
    dest = os.path.join(dest, file)
    if(not flag):
        if(src == '.'):
            src = file
            ExceptionHandlingCopy(ogsrc, src, dest, file)
        elif(dest == '.' ):
            src, dest = path, os.getcwd()
            ExceptionHandlingCopy(ogsrc, src, dest, file)
        else:
            src = path
            ExceptionHandlingCopy(ogsrc, src, dest, file)
    else:
        if(src == '.'):
            src = file
            ExceptionHandlingCopyTree(ogsrc, src, dest, file)
        elif(dest == '.' ):
            src, dest = path, os.path.join(os.getcwd(), file)
            ExceptionHandlingCopyTree(ogsrc, src, dest, file)
        else:
            src = path
            ExceptionHandlingCopyTree(ogsrc, src, dest, file)



#DELETE FILES AND DIRECTORIES
            
def DeleteDirectoryConfirm(file, src):
    try:
        if(src == '.'):
            shutil.rmtree(file,)
        else:
            shutil.rmtree(os.path.join(src, file))
    except Exception as error:
        print(error)
            
@click.command()
@click.argument('file')
@click.argument('src')

def dl(file, src):
    '''Delete Files and Directories.'''
    if(src == "."):
        path = os.path.join(os.getcwd(), file)
    else:
        path = os.path.join(src, file)
    flag = os.path.isdir(str(path))
    print(path, flag)
    if(not flag):
        try:
            if(src == '.'):
                os.remove(file)
            else:
                os.remove(os.path.join(src, file))
        except Exception as error:
            print(error)
    else:
        if(os.listdir(path) != []):
            click.echo('Directory is not empty.')
            ans = input(click.echo('Enter Y to delete, N to exit.'))
            def Response():
                ans = input(click.echo('Enter Y to delete, N to exit.'))
                if(ans == 'Y'):
                    DeleteDirectoryConfirm(file, src)
                elif(ans == 'N'):
                    pass
                else:
                    click.echo('Please enter a Valid response.')
                    Response()
            Response()
        else:
            DeleteDirectoryConfirm(file, src)

    
#CREATE Files and Directories
@click.command()
@click.argument('main')
@click.argument('src')
def cr(main, src):
    '''Create Files and Directories.'''
    try:
        if(src != '.'):
            os.chdir(src)
        if('.' in main):
            file = open(main, 'w')
            file.write('')
            file.close()
        else:
            os.makedirs(main)
    except Exception as error:
        print(error)
##
###Download from Local Server
##@click.command()
##@click.argument('file')
##@click.argument('src')
##def dwn(file, src):
##      Download(file, src)
    
#LINKING ALL THE COMMANDS TO THE MAIN FUNCTION -> main.                
main.add_command(ls)
main.add_command(cwd)
main.add_command(mov)
main.add_command(cp)
main.add_command(dl)
main.add_command(rn)
main.add_command(cr)
#main.add_command(dwn)

if __name__ == '__main__':
    main()
