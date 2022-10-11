## root@goodboy:/usr/local/bin# stat --format="%a"  myiptablesvpnkillswitch.sh
## 755
from asyncio.proactor_events import _ProactorBaseWritePipeTransport
from dataclasses import dataclass
import os
import subprocess
import shlex
import getpass
import string
import random
import tempfile


@dataclass
class SystemdFilePaths:
    unitdir: str = "/etc/systemd/system/"
    bashdir: str = "/usr/local/bin/"
    protect_unitname: str = "rexbytes_protect.service"
    docker_unitname: str = "rexbytes_dockerkillswitch.service"
    vpn4_unitname: str = "rexbytes_vpn4killswitch.service"
    protect_service: str = f"{unitdir}{protect_unitname}"
    docker_service: str = f"{unitdir}{docker_unitname}"
    vpn4_service: str = f"{unitdir}{vpn4_unitname}"
    nuke_bash: str = f"{bashdir}rexbytes_nuke.sh"
    flush_bash: str = f"{bashdir}rexbytes_flush.sh"
    off_bash: str = f"{bashdir}rexbytes_off.sh"
    protect_bash: str = f"{bashdir}rexbytes_protect.sh"
    docker_bash: str = f"{bashdir}rexbytes_dockerkillswitch.sh"
    vpn4_bash: str = f"{bashdir}rexbytes_vpn4killswitch.sh"


class SystemIPSwitches:
    def __init__(self):
        self.systembash = SystemBash()
        self.systemctl = SystemCTL()
        self.systemd = SystemD()

    def switch_on(self, granular: bool = True):
        self.switch_flush()
        self.switch_vpn(granular)
        self.switch_docker(granular)

    def switch_off(self):
        try:
            self.systemctl.protect_ctl_disable()
        except Exception as e:
            print(e)

        try:
            self.systemctl.openvpn_ctl_disable()
        except Exception as e:
            print(e)

        try:
            self.systemctl.docker_ctl_disable()
        except Exception as e:
            print(e)
        self.systemd.off()
        self.systembash.run_off()

    def switch_protect(self):
        self.systemd.protect()
        self.systembash.run_protect()
        self.systemctl.protect_ctl_enable()

    def switch_vpn(self, granular: bool = True):
        self.systemd.openvpn(granular)
        self.systembash.run_vpn4()
        self.systemctl.openvpn_ctl_enable()

    def switch_docker(self, granular: bool = True):
        self.systemd.docker(granular)
        self.systembash.run_docker()
        self.systemctl.docker_ctl_enable()

    def switch_flush(self):
        self.switch_off()
        self.systemd.flush()
        self.systembash.run_flush()
        self.systemd.erase_all()

    def switch_nuke(self):
        self.switch_off()
        self.systemd.nuke()
        self.systembash.run_nuke()
        self.systemd.erase_all()


class SystemBash:
    def __init__(self):
        self.systemfilepaths = SystemdFilePaths()

    def run_nuke(self):
        subprocess.call(shlex.split(f"sudo {self.systemfilepaths.nuke_bash}"))

    def run_flush(self):
        subprocess.call(shlex.split(f"sudo {self.systemfilepaths.flush_bash}"))

    def run_off(self):
        subprocess.call(shlex.split(f"sudo {self.systemfilepaths.off_bash}"))

    def run_protect(self):
        subprocess.call(shlex.split(f"sudo {self.systemfilepaths.protect_bash}"))

    def run_docker(self):
        subprocess.call(shlex.split(f"sudo {self.systemfilepaths.docker_bash}"))

    def run_vpn4(self):
        subprocess.call(shlex.split(f"sudo {self.systemfilepaths.vpn4_bash}"))


class SystemCTL:
    def __init__(self):
        self.systemfilepaths = SystemdFilePaths()

    def protect_ctl_enable(self):
        subprocess.run(
            shlex.split(
                f"sudo systemctl enable {self.systemfilepaths.protect_unitname}"
            )
        )

    def protect_ctl_disable(self):
        subprocess.run(
            shlex.split(
                f"sudo systemctl disable {self.systemfilepaths.protect_unitname}"
            )
        )

    def openvpn_ctl_enable(self):
        subprocess.run(
            shlex.split(f"sudo systemctl enable {self.systemfilepaths.vpn4_unitname}")
        )

    def openvpn_ctl_disable(self):
        subprocess.run(
            shlex.split(f"sudo systemctl disable {self.systemfilepaths.vpn4_unitname}")
        )

    def docker_ctl_enable(self):
        subprocess.run(
            shlex.split(f"sudo systemctl enable {self.systemfilepaths.docker_unitname}")
        )

    def docker_ctl_disable(self):
        subprocess.run(
            shlex.split(
                f"sudo systemctl disable {self.systemfilepaths.docker_unitname}"
            )
        )


class SystemD:
    def __init__(self):
        self.systemdfiles = SystemdFiles()
        self.service_unit_text = ServiceUnitTexts()
        self.service_bash_text = ServiceBashTexts()

    def nuke(self):
        nuke_bash_filepath, nuke_bashtext = self.service_bash_text.nuke_text()
        self.systemdfiles.writebash(nuke_bash_filepath, nuke_bashtext)

    def flush(self):
        flush_bash_filepath, flush_bashtext = self.service_bash_text.flush_text()
        self.systemdfiles.writebash(flush_bash_filepath, flush_bashtext)

    def off(self):
        off_bash_filepath, off_bashtext = self.service_bash_text.off_text()
        self.systemdfiles.writebash(off_bash_filepath, off_bashtext)

    def protect(self):
        protect_service_filepath, protect_servicetext = self.service_unit_text.protect()
        protect_bash_filepath, protect_bashtext = self.service_bash_text.protect_text()
        self.systemdfiles.writebash(protect_bash_filepath, protect_bashtext)
        self.systemdfiles.writeservice(protect_service_filepath, protect_servicetext)

    def openvpn(self, granular: bool = True):
        vpn_service_filepath, vpn_servicetext = self.service_unit_text.openvpn()
        if granular:
            (
                vpn_bash_filepath,
                vpn_bashtext,
            ) = self.service_bash_text.vpnkillswitch_g_text()
        else:
            (
                vpn_bash_filepath,
                vpn_bashtext,
            ) = self.service_bash_text.vpnkillswitch_text()
        self.systemdfiles.writebash(vpn_bash_filepath, vpn_bashtext)
        self.systemdfiles.writeservice(vpn_service_filepath, vpn_servicetext)

    def docker(self, granular: bool = True):
        docker_service_filepath, docker_servicetext = self.service_unit_text.docker()
        if granular:
            (
                docker_bash_filepath,
                docker_bashtext,
            ) = self.service_bash_text.dockerkillswitch_g_text()
        else:
            (
                docker_bash_filepath,
                docker_bashtext,
            ) = self.service_bash_text.dockerkillswitch_text()
        self.systemdfiles.writebash(docker_bash_filepath, docker_bashtext)
        self.systemdfiles.writeservice(docker_service_filepath, docker_servicetext)

    def erase_all(self):
        self.systemdfiles.erase_all()


class SystemdFiles:
    def __init__(self):
        self.systemdfilepaths = SystemdFilePaths()

    def writeservice(self, servicefilepath, servicecontent):
        try:
            self.writeservice_as_root(servicefilepath, servicecontent)
        except Exception as e:
            print(f"REXBYTES:{e}")

    def writebash(self, bashfilepath, bashcontent):
        try:
            self.writebash_as_root(bashfilepath, bashcontent)
        except Exception as e:
            print(f"REXBYTES:{e}")

    def erase(self, filepath):
        try:
            self.erase_as_root(filepath)
        except Exception as e:
            print(f"REXBYTES:{e}")

    def writeservice_as_root(self, servicefilepath, servicecontent):
        with tempfile.NamedTemporaryFile(mode="w", delete=False) as servicefile_ntf:
            try:

                with open(servicefile_ntf.name, "w+") as servicefile:
                    servicefile.writelines(servicecontent)
                subprocess.run(
                    shlex.split(f"sudo cp {servicefile_ntf.name} {servicefilepath}")
                )
                subprocess.run(shlex.split(f"sudo chown root:root {servicefilepath}"))
                subprocess.run(shlex.split(f"sudo chmod 644 {servicefilepath}"))
                subprocess.run(shlex.split(f"sudo rm -f {servicefile_ntf.name}"))
            except Exception as e:
                print(f"REXBYTES:{e}")

    def writebash_as_root(self, bashfilepath, bashcontent):
        with tempfile.NamedTemporaryFile(mode="w", delete=False) as bashfile_ntf:
            try:
                with open(bashfile_ntf.name, "w+") as bashfile:
                    bashfile.writelines(bashcontent)
                subprocess.run(
                    shlex.split(f"sudo cp {bashfile_ntf.name} {bashfilepath}")
                )
                subprocess.run(shlex.split(f"sudo chown root:root {bashfilepath}"))
                subprocess.run(shlex.split(f"sudo chmod 755 {bashfilepath}"))
                subprocess.run(shlex.split(f"sudo rm -f {bashfile_ntf.name}"))
            except Exception as e:
                print(f"REXBYTES:{e}", flush=True)

    def erase_as_root(self, filepath):
        try:
            subprocess.run(shlex.split(f"sudo rm -f {filepath}"))
        except Exception as e:
            print(e)

    def erase_all(self):
        self.erase(self.systemdfilepaths.flush_bash)
        self.erase(self.systemdfilepaths.off_bash)
        self.erase(self.systemdfilepaths.protect_bash)
        self.erase(self.systemdfilepaths.protect_service)
        self.erase(self.systemdfilepaths.vpn4_bash)
        self.erase(self.systemdfilepaths.vpn4_service)
        self.erase(self.systemdfilepaths.docker_bash)
        self.erase(self.systemdfilepaths.docker_service)


class ServiceUnitTexts:
    def __init__(self):
        self.systemdfilepaths = SystemdFilePaths()

    def protect(self):
        text = f"""[Unit]
Description=Run iptable commands to create killswitch   
Before=network-pre.target
Wants=network-pre.target
[Service]
Type=oneshot
ExecStart={self.systemdfilepaths.protect_bash}
Timeoutsec=60
[Install]
WantedBy=network.target
"""
        return self.systemdfilepaths.protect_service, text

    def docker(self):
        text = f"""[Unit]
Description=Apply Docker Kill Switch Rules To DOCKER-USER chain.
After=docker.service
BindsTo=docker.service

[Service]
Type=oneshot
ExecStart={self.systemdfilepaths.docker_bash}

[Install]
WantedBy=multi-user.target"""
        return self.systemdfilepaths.docker_service, text

    def openvpn(self):
        text = f"""[Unit]
Description=Run iptable commands to create killswitch   
Before=network-pre.target
Wants=network-pre.target
[Service]
Type=oneshot
ExecStart={self.systemdfilepaths.vpn4_bash}
Timeoutsec=60
[Install]
WantedBy=network.target
"""
        return self.systemdfilepaths.vpn4_service, text


class ServiceBashTexts:
    def __init__(self):
        self.systemdfilepaths = SystemdFilePaths()
        self.bashfunctions = """
function create_filter_chain () {
    if [[ $(iptables -t filter -n --list "$1" >/dev/null 2>&1;echo $?) = 0 ]]
    then 
        echo "$1 Chain already exists"
    else 
        echo "Creating $1..."
        iptables -N "$1"
    fi
}

function create_filter_rule () {
    local ipcommand2=$(echo "$1" |tr -s ' ' |cut -d' ' -f3-)
    local ipcommand1=$(echo "$1" |tr -s ' ' |cut -d' ' -f -1)
    local checkcommand="$ipcommand1 -C $ipcommand2"
    if [[ $( $checkcommand >/dev/null 2>&1;echo $?) = 1 ]]
    then
        echo "RULE DOES NOT EXIST, CREATING..."
        ($1)
    else
        echo "RULE EXISTS"
    #iptables -A OUTPUT -o lo -j ACCEPT
    fi
}

"""

    def nuke_text(self):
        text = """#!/bin/bash
#Flush all chains, delete custom chains.
iptables -F
iptables -X
iptables -t nat -F
iptables -t nat -X
#Block all traffic as default.
iptables --policy INPUT ACCEPT
iptables --policy FORWARD ACCEPT
iptables --policy OUTPUT ACCEPT 
        """
        return self.systemdfilepaths.nuke_bash, text

    def off_text(self):
        text = """#!/bin/bash
#Block all traffic as default.
iptables --policy INPUT ACCEPT
iptables --policy FORWARD ACCEPT
iptables --policy OUTPUT ACCEPT 
echo "off-D"
iptables -D INPUT -j RB_RELATED_AND_ESTABLISHED
iptables -D OUTPUT -j RB_OUTPUT_VPN_KILL_SWITCH
iptables -D DOCKER-USER -j RB_DOCKER_VPN_KILL_SWITCH
        """
        return self.systemdfilepaths.off_bash, text

    def flush_text(self):
        text = """#!/bin/bash
#Block all traffic as default.
iptables --policy INPUT ACCEPT
iptables --policy FORWARD ACCEPT
iptables --policy OUTPUT ACCEPT 
echo "flush-D"
iptables -D INPUT -j RB_RELATED_AND_ESTABLISHED
iptables -D OUTPUT -j RB_OUTPUT_VPN_KILL_SWITCH
iptables -D DOCKER-USER -j RB_DOCKER_VPN_KILL_SWITCH
echo "flush-F"
iptables --flush RB_RELATED_AND_ESTABLISHED
iptables --flush RB_OUTPUT_VPN_KILL_SWITCH
iptables --flush RB_DOCKER_VPN_KILL_SWITCH
echo "flush-D"
iptables --delete-chain RB_RELATED_AND_ESTABLISHED
iptables --delete-chain RB_OUTPUT_VPN_KILL_SWITCH
iptables --delete-chain RB_DOCKER_VPN_KILL_SWITCH
        """
        return self.systemdfilepaths.flush_bash, text

    def protect_text(self):
        text = f"""#!/bin/bash
{self.bashfunctions}
#Block all traffic as default.
iptables --policy INPUT DROP
iptables --policy FORWARD DROP
iptables --policy OUTPUT ACCEPT
create_filter_chain 'RB_RELATED_AND_ESTABLISHED'
create_filter_rule 'iptables -A RB_RELATED_AND_ESTABLISHED -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT'
create_filter_rule 'iptables -I INPUT -j RB_RELATED_AND_ESTABLISHED'
"""
        return self.systemdfilepaths.protect_bash, text

    def vpnkillswitch_text(self):
        text = f"""#!/bin/bash
{self.bashfunctions}
#Block all traffic as default.
iptables --policy INPUT DROP
iptables --policy FORWARD DROP
iptables --policy OUTPUT DROP
create_filter_chain 'RB_RELATED_AND_ESTABLISHED'
create_filter_rule 'iptables -A RB_RELATED_AND_ESTABLISHED -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT'
create_filter_rule 'iptables -I INPUT  -j RB_RELATED_AND_ESTABLISHED'
#let's create a chain named RB_OUTPUT_VPN_KILL_SWITCH to hold our VPN rules
create_filter_chain 'RB_OUTPUT_VPN_KILL_SWITCH'
create_filter_rule 'iptables -A RB_OUTPUT_VPN_KILL_SWITCH -p udp -m udp --dport 1194 -j ACCEPT'
create_filter_rule 'iptables -A RB_OUTPUT_VPN_KILL_SWITCH -o tun+ -j ACCEPT'
create_filter_rule 'iptables -A RB_OUTPUT_VPN_KILL_SWITCH -o lo -j ACCEPT'
#If you want to, you can also allow access to your local network.
#The most common local network is class C, 192.168.0.0/16
create_filter_rule 'iptables -A RB_OUTPUT_VPN_KILL_SWITCH -d 10.0.0.0/8 -j ACCEPT'
#You must check what local network class you car connected to.
#Adjust for Class C, 192.168.0.0/16 Class B, 172.16.0.0/12 and class A 10.0.0.0/8
#The following line is to allow a single ip address for your DNS server, 
#in the case it hasn't been caught by the local network catch all rule.
#create_filter_rule 'iptables -A RB_OUTPUT_VPN_KILL_SWITCH -d 10.17.0.1 -j ACCEPT'
#let's pop a reroute to our vpn rules at the top of the OUTPUT chain using -I insert
create_filter_rule 'iptables -I OUTPUT  -j RB_OUTPUT_VPN_KILL_SWITCH'
"""
        return self.systemdfilepaths.vpn4_bash, text

    def vpnkillswitch_g_text(self):
        text = f"""#!/bin/bash
{self.bashfunctions}
#Block all traffic as default.
iptables --policy INPUT DROP
iptables --policy FORWARD DROP
iptables --policy OUTPUT DROP
#Create a custom chain to contain rules to allow related and established traffic.
create_filter_chain 'RB_RELATED_AND_ESTABLISHED'
create_filter_rule 'iptables -A RB_RELATED_AND_ESTABLISHED -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT'
#Divert input traffic to the RB_RELATED_AND_ESTABLISHED chain.
create_filter_rule 'iptables -I INPUT -j RB_RELATED_AND_ESTABLISHED'
#Let's allow the loopback device.
#let's create a chain named RB_OUTPUT_VPN_KILL_SWITCH to hold our VPN rules
create_filter_chain 'RB_OUTPUT_VPN_KILL_SWITCH'
#let's pop a reroute to our vpn rules at the top of the OUTPUT chain using -I insert 
create_filter_rule 'iptables -A RB_OUTPUT_VPN_KILL_SWITCH -p udp -m udp --dport 1194 -j ACCEPT'
#port 443 https
create_filter_rule 'iptables -A RB_OUTPUT_VPN_KILL_SWITCH -o tun+ -p tcp --dport 443 -j ACCEPT'
#port 80, used by apt-get for example.
create_filter_rule 'iptables -A RB_OUTPUT_VPN_KILL_SWITCH -o tun+ -p tcp --dport 80 -j ACCEPT'
#port 22, ssh
create_filter_rule 'iptables -A RB_OUTPUT_VPN_KILL_SWITCH -o tun+ -p tcp --dport 22 -j ACCEPT'
#port 53, git clone
create_filter_rule 'iptables -A RB_OUTPUT_VPN_KILL_SWITCH -o tun+ -p tcp --dport 53 -j ACCEPT'
#create_filter_rule 'iptables -A RB_OUTPUT_VPN_KILL_SWITCH -o tun+ -p tcp --dport 993 -j ACCEPT'
#create_filter_rule 'iptables -A RB_OUTPUT_VPN_KILL_SWITCH -o tun+ -p tcp --dport 465 -j ACCEPT'
create_filter_rule 'iptables -A RB_OUTPUT_VPN_KILL_SWITCH -o lo -j ACCEPT'
#icmp, for ping.
create_filter_rule 'iptables -A RB_OUTPUT_VPN_KILL_SWITCH -o tun+ -p icmp -j ACCEPT'
#If you want to, you can also allow access to your local network.
#The most common local network is class C, 192.168.0.0/16
create_filter_rule 'iptables -A RB_OUTPUT_VPN_KILL_SWITCH -d 10.0.0.0/8 -j ACCEPT'
#You must check what local network class you car connected to.
#Adjust for Class C, 192.168.0.0/16 Class B, 172.16.0.0/12 and class A 10.0.0.0/8
#The following line is to allow a single ip address for your DNS server, 
#in the case it hasn't been caught by the local network catch all rule.
#create_filter_rule 'iptables -A RB_OUTPUT_VPN_KILL_SWITCH -d 10.17.0.1 -j ACCEPT'
#let's pop a reroute to our vpn rules at the top of the OUTPUT chain using -I insert
create_filter_rule 'iptables -I OUTPUT -j RB_OUTPUT_VPN_KILL_SWITCH'
"""
        return self.systemdfilepaths.vpn4_bash, text

    def dockerkillswitch_text(self):
        text = f"""#!/bin/bash
{self.bashfunctions}
create_filter_chain 'RB_DOCKER_VPN_KILL_SWITCH'
create_filter_rule 'iptables -A RB_DOCKER_VPN_KILL_SWITCH -o tun+ -j ACCEPT'
create_filter_rule 'iptables -A RB_DOCKER_VPN_KILL_SWITCH -i tun+ -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT'
create_filter_rule 'iptables -A RB_DOCKER_VPN_KILL_SWITCH -j DROP'
create_filter_rule 'iptables -I DOCKER-USER  -j RB_DOCKER_VPN_KILL_SWITCH'
"""
        return self.systemdfilepaths.docker_bash, text

    def dockerkillswitch_g_text(self):
        text = f"""#!/bin/bash
{self.bashfunctions}
create_filter_chain 'RB_DOCKER_VPN_KILL_SWITCH'
#port 443 https
create_filter_rule 'iptables -A RB_DOCKER_VPN_KILL_SWITCH -o tun+ -p tcp --dport 443 -j ACCEPT'
#port 80, used by apt-get for example.
create_filter_rule 'iptables -A RB_DOCKER_VPN_KILL_SWITCH -o tun+ -p tcp --dport 80 -j ACCEPT'
#port 22, ssh
create_filter_rule 'iptables -A RB_DOCKER_VPN_KILL_SWITCH -o tun+ -p tcp --dport 22 -j ACCEPT'
#port 53, git clone
create_filter_rule 'iptables -A RB_DOCKER_VPN_KILL_SWITCH -o tun+ -p tcp --dport 53 -j ACCEPT'
#icmp, for ping.
create_filter_rule 'iptables -A RB_DOCKER_VPN_KILL_SWITCH -o tun+ -p icmp -j ACCEPT'
#create_filter_rule 'iptables -A RB_DOCKER_VPN_KILL_SWITCH -o tun+ -p tcp --dport 993 -j ACCEPT'
#create_filter_rule 'iptables -A RB_DOCKER_VPN_KILL_SWITCH -o tun+ -p tcp --dport 465 -j ACCEPT'
create_filter_rule 'iptables -A RB_DOCKER_VPN_KILL_SWITCH  -i tun+ -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT'
create_filter_rule 'iptables -A RB_DOCKER_VPN_KILL_SWITCH  -j DROP'
create_filter_rule 'iptables -I DOCKER-USER  -j RB_DOCKER_VPN_KILL_SWITCH'
"""
        return self.systemdfilepaths.docker_bash, text
