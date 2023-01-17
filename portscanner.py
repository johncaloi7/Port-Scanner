import socket
import termcolor


def scan(target, ports):
	print('\n' + ' Scanning ports for target ' + str(target))
	for port in range(1, ports):
		scan_port(target, port)


def scan_port(ipaddress, port):
    try: 
        sock = socket.socket()
        socket.connect((ipaddress, port))
        print("[+] Port Opened " + str(port))
        sock.close()
    except:
        pass    


targets = input("[*] Enter target to be scanned/ Multiple target must be separated by a comma: ")
ports = int(input("[*] Enter how many ports will be scanned (1 - 65000): "))


if ',' in targets:
	print(termcolor.colored(("[*] Commencing scanning"), 'green'))
	for ip_addr in targets.split(','):
		scan(ip_addr.strip(' '), ports)
else:
	scan(targets,ports)


