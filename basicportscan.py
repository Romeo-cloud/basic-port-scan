import socket

def simple_port_scan(target_ip, start, end):
    print(f"Checking ports on {target_ip}...")
    for port in range(start, end + 1):
        try:
            s = socket.socket()
            s.settimeout(0.3)
            result = s.connect_ex((target_ip, port))
            if result == 0:
                print(f"Port {port} is OPEN")
            s.close()
        except:
            pass

# get input
ip = input("Target IP: ")
try:
    start_port = int(input("Start Port: "))
    end_port = int(input("End Port: "))
    simple_port_scan(ip, start_port, end_port)
except:
    print("Invalid port number")
