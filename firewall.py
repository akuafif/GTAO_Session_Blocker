from subprocess import Popen, PIPE
import re
import ctypes

firewall_rule_name = "GTAO Session Blocker Rule"

# shell = True will remove console output when using .exe from pyinstaller
def running_as_admin():
    return ctypes.windll.shell32.IsUserAnAdmin()


def firewall_exist():
    netsh_firewall_exist = f'''netsh advfirewall firewall show rule name="{firewall_rule_name}"'''
    in_command = Popen(netsh_firewall_exist, stdout=PIPE, stderr=PIPE, shell=True)
    output_message, _ = in_command.communicate()

    return "No rules match the specified criteria." != output_message.decode().strip()


def firewall_scopes_list():
    if firewall_exist():
        netsh_firewall_exist = f'''netsh advfirewall firewall show rule name="{firewall_rule_name}" dir=in '''
        in_command = Popen(netsh_firewall_exist, stdout=PIPE, stderr=PIPE, shell=True)

        output_message, _ = in_command.communicate()

        output_message_decoded = output_message.decode().strip()

        remote_ip_address = output_message_decoded.split()[17]

        return remote_ip_address


def firewall_active():
    netsh_firewall_exist = f'''netsh advfirewall firewall show rule name="{firewall_rule_name}" dir=in '''
    in_command = Popen(netsh_firewall_exist, stdout=PIPE, stderr=PIPE, shell=True)

    output_message, _ = in_command.communicate()

    output_message_decoded = output_message.decode().strip()

    status = output_message_decoded.split()[8]
    return status != "No"


def valid_ip_address(ip_address):
    ip_address_pattern = "^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/?\d?\d?"
    check_ip = re.match(ip_address_pattern, ip_address)

    return check_ip is not None


def add_firewall_rule(program_path):
    netsh_add_firewall_command_in = f'''netsh advfirewall firewall add rule name="{firewall_rule_name}" dir=in action=block program="{program_path}" enable=no profile=domain,private,public protocol=UDP localport=6672'''
    netsh_add_firewall_command_out = f'''netsh advfirewall firewall add rule name="{firewall_rule_name}" dir=out action=block program="{program_path}" enable=no profile=domain,private,public protocol=UDP localport=6672'''
    in_command = Popen(netsh_add_firewall_command_in, stdout=PIPE, stderr=PIPE, shell=True)
    out_command = Popen(netsh_add_firewall_command_out, stdout=PIPE, stderr=PIPE, shell=True)

    output_message, _ = in_command.communicate()

    return "Ok." == output_message.decode().strip()


def split_ip_addresss(ip_address):
    # will be split to compare the different IP octet
    split_ip = ip_address.split(".")
    return int(split_ip[0]), int(split_ip[1]), int(split_ip[2]), int(split_ip[3])


def ip_address_above_and_below(ip_address):
    # split ip address to get different octet
    ip_address = ip_address.split('.')
    last_octet = ip_address[-1]
    other_remaining = '.'.join(ip_address[0:3])
    first_ip = f"{other_remaining}.{int(last_octet) - 1}"
    second_ip = f"{other_remaining}.{int(last_octet) + 1}"

    return first_ip, second_ip


def new_ip_address_scope(previous_scope, ip_address):
    # will be used to sort out ip address from smallest to biggest
    previous_split_scope = "-".join(previous_scope.split(","))

    multiple_ip_address = []


    # check if multiple ip_address are passed through
    if "," in ip_address:


        new_ip_address_split = ip_address.split(",")

        for ip in new_ip_address_split:
            # splitting the ip address so we can get a +1 and -1 range of the current ip address
            first_ip, second_ip = ip_address_above_and_below(ip)
            # keep track of both ip addresses
            multiple_ip_address.append(first_ip)
            multiple_ip_address.append(second_ip)

        new_unsorted_scope = previous_split_scope.split("-") + multiple_ip_address


    else:
        # splitting the ip address so we can get a +1 and -1 range of the current ip address
        first_ip, second_ip = ip_address_above_and_below(ip_address)

        # joining first and second ip to the scope list rather than having to loop twice
        new_unsorted_scope = f"{previous_split_scope}-{first_ip}-{second_ip}".split("-")


    new_sorted_scope = sorted(new_unsorted_scope, key=split_ip_addresss)
    # looping through the sorted list and combine two ip address to get the range we need
    new_scope = [f"{new_sorted_scope[index - 1]}-{ip}" for index, ip in enumerate(new_sorted_scope) if
                 (index + 1) % 2 == 0]

    return ','.join(new_scope)


def add_white_list(ip_address):
    previous_scope = firewall_scopes_list()
    # will be used to create a new scope if none exist
    zero_IP = "0.0.0.0"
    last_IP = "255.255.255.255"

    if previous_scope != "Any":

        new_scope = new_ip_address_scope(previous_scope, ip_address)

        netsh_allow_remote_address = f'''netsh advfirewall firewall set rule name="{firewall_rule_name}"  new remoteip={new_scope} '''
        Popen(netsh_allow_remote_address, shell=True)


    else:

        first_ip, second_ip = ip_address_above_and_below(ip_address)

        first_range = f"{zero_IP}-{first_ip}"
        second_range = f"{second_ip}-{last_IP}"

        new_scope = f'{first_range},{second_range}'

        netsh_allow_remote_address = f'''netsh advfirewall firewall set rule name="{firewall_rule_name}" new remoteip={new_scope} '''
        Popen(netsh_allow_remote_address, shell=True)


def ip_address_without_scope():
    ip_scope = firewall_scopes_list()

    ip_address_in_firewall = re.split('[,-]', ip_scope)

    ip_address_in_scope = []

    for index, ip_address in enumerate(ip_address_in_firewall, start=1):

        if index % 2 == 0 and index != len(ip_address_in_firewall):
            ip_address = ip_address.split('.')
            last_octet = ip_address[-1]
            original_ip = f"{'.'.join(ip_address[0:3])}.{int(last_octet) + 1}"
            ip_address_in_scope.append(original_ip)

    return ip_address_in_scope


def ip_address_exist_in_scope(ip_address):
    current_ip_scope = ip_address_without_scope()
    for ip in current_ip_scope:
        if ip == ip_address:
            return True
    return False


def remove_white_list(ip_address):
    ip_scope = re.split("[,-]", firewall_scopes_list())




    if "," in ip_address:
        ip_addresses = ip_address.split(",")

        for ip in ip_addresses:

            first_ip, second_ip = ip_address_above_and_below(ip)

            try:
                ip_scope.remove(first_ip)
                ip_scope.remove(second_ip)
                # will be used if a value was already removed form the scope
            except ValueError:
                pass
    else:
        first_ip, second_ip = ip_address_above_and_below(ip_address)

        try:
            ip_scope.remove(first_ip)
            ip_scope.remove(second_ip)
            # will be used if a value was already removed form the scope
        except ValueError:
            pass

    new_scope = ",".join([f"{ip_scope[index - 1]}-{ip}" for index, ip in enumerate(ip_scope) if
                          (index + 1) % 2 == 0])



    if len(new_scope) != 1:
        netsh_allow_remote_address = f'''netsh advfirewall firewall set rule name="{firewall_rule_name}" dir=in new remoteip={new_scope}    '''
        Popen(netsh_allow_remote_address, shell=True)

    else:
        netsh_allow_remote_address = f'''netsh advfirewall firewall set rule name="{firewall_rule_name}" dir=in new remoteip="" '''
        Popen(netsh_allow_remote_address, shell=True)


def enable_firewall_rule():
    netsh_add_firewall_command = f'''netsh advfirewall firewall set rule name="{firewall_rule_name}" new enable=yes '''
    Popen(netsh_add_firewall_command, shell=True)
    print('rule enabled')

def disable_firewall_rule():
    netsh_add_firewall_command = f'''netsh advfirewall firewall set rule name="{firewall_rule_name}" new enable=no '''
    Popen(netsh_add_firewall_command, shell=True)

def delete_firewall_rule():
    netsh_add_firewall_command = f'''netsh advfirewall firewall delete rule name="{firewall_rule_name}" '''
    in_command = Popen(netsh_add_firewall_command, stdout=PIPE, stderr=PIPE, shell=True)
    output_message, _ = in_command.communicate()
    print('Rule deleted')
    return "Ok." in output_message.decode().strip()
