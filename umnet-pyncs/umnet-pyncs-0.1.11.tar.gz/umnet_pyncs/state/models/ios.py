from typing import List, Optional
from ipaddress import IPv4Address

from ntc_templates.parse import parse_output
from netaddr import EUI, mac_unix_expanded

from .base import BaseDevice, ARPTableEntry, MACTableEntry, Interface


# note that since we're using 'show int status',
# admin and oper status leverage the same output column, whose values can be:
#  - connected (admin up, oper up)
#  - notconnect (admin up, oper down)
#  - disabled (admin down, oper down)
#  - suspended (admin up, oper down)
#  - err-disabled (admin up, oper down)
ADMIN_STATUS = {
    "connected": "enabled",
    "notconnect": "enabled",
    "disabled": "disabled",
    "suspended": "enabled",
    "err-disabled": "enabled",
}
OPER_STATUS = {
    "connected": "up",
    "notconnect": "down",
    "disabled": "down",
    "suspended": "down",
    "err-disabled": "down",
}
DUPLEX = {
    "half": "half",
    "full": "full",
    "auto": "full",
    "a-half": "half",
    "a-full": "full",
}
SPEED = {
    "10": "10",
    "100": "100",
    "1000": "1000",
    "10G": "auto",
    "auto": "auto",
    "a-10": "10",
    "a-100": "100",
    "a-1000": "1000",
    "a-10G": "auto",
}


def _remove_prompt(results: str) -> str:
    """
    remove the trailing prompt from the results of a live_status show
    command.  This only appears to be an issue for the IOS NED. i.e:

    ...
    Gi2/0/48        notconnect   1       auto   auto 10/100/1000BaseTX
    Twe2/1/1        connected    1       full    10G SFP-10GBase-SR
    Twe2/1/2        notconnect   1       auto   auto unknown
    Ap2/0/1         connected    1     a-full a-1000 App-hosting port
    al-shallow-1#    <-- (rude)
    """
    lines = results.splitlines()
    try:
        del lines[-1]
    except IndexError:
        pass
    return "\n".join(lines)


class IOS(BaseDevice):
    def _run_cmd(self, command: str) -> str:
        """
        use NCS live-status exec to issue a raw show command towards a device.
        platform-specific models are expected to parse this output and return
        structured data.

        :param command: string CLI command, e.g. 'show interface status'
        :returns: raw string output from the device
        """
        show = self.device.live_status.__getitem__("exec").show
        inp = show.get_input()
        inp.args = [command]

        results = show.request(inp)

        return _remove_prompt(results.result)

    def get_interface_details(self, interface: Optional[str] = None) -> List[Interface]:
        """
        Gathers interface operational data from an IOS device by parsing 'show interfaces status'

        :interface: optionally get data only for a single interface

        see the ntc_templates test data for this template for details on output structure:
        https://github.com/networktocode/ntc-templates/tree/master/tests/cisco_ios/show_interfaces_status

        ---
        parsed_sample:
          - port: "Gi1/0/1"
            name: ""
            status: "notconnect"
            vlan: "1"
            duplex: "auto"
            speed: "auto"
            type: "10/100/1000BaseTX"
            fc_mode: ""
        """
        # ncs automatically adds the 'show' to the front of the cmd
        command = f"interfaces {interface} status" if interface else "interfaces status"
        self.log.debug(f"sending 'show {command}' to {self.device.name}")
        reply = self._run_cmd(command)
        # self.log.debug(f" <<<{ self.device.name }>>>: {reply.result}")

        parsed = parse_output(
            platform="cisco_ios",
            command="show interfaces status",
            data=reply,
        )

        output = []
        for entry in parsed:
            interface = Interface(
                name=entry["port"],
                description=entry["name"],
                admin_status=ADMIN_STATUS[entry["status"]],
                oper_status=OPER_STATUS[entry["status"]],
                duplex=DUPLEX[entry["duplex"]],
                speed=SPEED[entry["speed"]],
            )

            if interface.name.startswith("Vlan"):
                interface.is_logical = True

            output.append(interface)

        return output

    def get_arp_table(
        self, address: Optional[str] = None, vrf: Optional[str] = None
    ) -> List[ARPTableEntry]:
        """
        Gathers ARP data from an IOS device by parsing the output of the CLI
        command 'show ip arp [ address | vrf <VRF>]'

        :address: optionally filter device output by MAC or IP address
        :vrf: optional string name of VRF table to look in

        see the ntc_templates test data for this template for details on output structure:
        https://github.com/networktocode/ntc-templates/tree/master/tests/cisco_ios/show_ip_arp

        TODO: add support(recursion?) for vrf='all' since ios makes you run a separate
              lookup command for every vrf (so rude)

        ---
        parsed_sample:
          - protocol: "Internet"
            address: "172.16.233.229"
            age: "-"
            mac: "0000.0c59.f892"
            type: "ARPA"
            interface: "Ethernet0/0"
        """
        # ncs automatically adds the 'show' to the front of the cmd
        command = "ip arp"
        if vrf is not None:
            command = command + f" vrf {vrf}"
        if address is not None:
            command = command + f" address {address}"
            normalized_address = IPv4Address(address)

        self.log.debug(f"sending 'show {command}' to {self.device.name}")
        reply = self._run_cmd(command)
        # self.log.debug(f" <<<{ self.device.name }>>>: {reply.result}")

        parsed = parse_output(
            platform="cisco_ios",
            command="show ip arp",
            data=reply,
        )

        output = []
        for entry in parsed:
            if entry["mac"] == "Incomplete":
                continue

            normalized_entry_address = IPv4Address(entry["address"])

            if address is None or normalized_address == normalized_entry_address:
                arp = ARPTableEntry(
                    ip_address=IPv4Address(entry["address"]),
                    mac_address=EUI(entry["mac"], dialect=mac_unix_expanded),
                    interface=entry["interface"],
                    vrf=vrf,
                )
                output.append(arp)

        return output

    def get_mac_table(self, mac: Optional[str] = None) -> List[MACTableEntry]:
        """
        Gathers dynamically-learned MAC address data from an IOS device by
        parsing the output of the CLI command 'show mac address-table dynamic
        [address <address>]'

        :mac: optionally filter device output by MAC address

        see the ntc_templates test data for this template for details on output structure:
        https://github.com/networktocode/ntc-templates/tree/master/tests/cisco_ios/show_mac-address-table

        ---
        parsed_sample:
        - destination_address: "30a3.30a3.a1c3"
            type: "dynamic"
            vlan: "666"
            destination_port:
            - "Te1/30"
        """
        # ncs automatically adds the 'show' to the front of the cmd
        command = "mac address-table dynamic"
        if mac is not None:
            normalized_mac = EUI(mac, dialect=mac_unix_expanded)
            command = command + f" address {mac}"

        self.log.debug(f"sending 'show {command}' to {self.device.name}")
        reply = self._run_cmd(command)
        # self.log.debug(f" <<<{ self.device.name }>>>: {reply.result}")

        parsed = parse_output(
            platform="cisco_ios",
            command="show mac-address-table",
            data=reply,
        )

        output = []
        for entry in parsed:
            try:
                vid = int(entry["vlan"])
            except ValueError:
                vid = None

            normalized_entry_mac = EUI(
                entry["destination_address"], dialect=mac_unix_expanded
            )
            # unless there's an on-going broadcast storm we should only be
            # learning an address on a single port -- not sure why the template
            # is modelled this way?
            interface = entry["destination_port"][0]

            if mac is None or normalized_mac == normalized_entry_mac:
                mac_entry = MACTableEntry(
                    address=normalized_entry_mac,
                    vlan_id=vid,
                    interface=interface,
                )
                output.append(mac_entry)

        return output
