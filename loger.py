import sys
import paramiko
import getpass


def ssh_command(ssh):
    counter = True
    while counter:
        command = input("Command:")
        ssh.invoke_shell('gnome-terminal')
        stdin, stdout, stderr = ssh.exec_command(command)
        print(stdout.read())
        if command == 'exit':
            print('Im out!')
            counter = False

def ssh_connect(host, user, password):
    try:
        ssh = paramiko.SSHClient()
        print('Calling paramiko')
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=host, username=user, password=key)

        ssh_command(ssh)
    except Exception as e:
        print('Connection Failed')
        print(e)

if __name__=='__main__':
    user = ''
    key = ''
    host = ''
    ssh_connect(host, user, key)
