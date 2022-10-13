# -*- coding: utf-8 -*-
# vim: set ts=4
#
# Copyright 2021-present Linaro Limited
#
# SPDX-License-Identifier: MIT

from typing import Dict, List, Optional

from tuxrun import templates
from tuxrun.devices import Device
from tuxrun.exceptions import InvalidArgument
from tuxrun.utils import compression, notnone


class FVPDevice(Device):
    flag_use_pre_run_cmd = True

    def device_dict(self, context):
        return templates.devices().get_template("fvp.yaml.jinja2").render(**context)


class AEMvAFVPDevice(FVPDevice):
    name = "fvp-aemva"

    flag_cache_rootfs = True

    bl1 = "https://storage.tuxboot.com/fvp-aemva/bl1.bin"
    dtb = "https://storage.tuxboot.com/fvp-aemva/fvp-base-revc.dtb"
    fip = "https://storage.tuxboot.com/fvp-aemva/fip.bin"
    kernel = "https://storage.tuxboot.com/fvp-aemva/Image"
    rootfs = "https://storage.tuxboot.com/fvp-aemva/rootfs.ext4.zst"
    uefi = "https://storage.tuxboot.com/fvp-aemva/edk2-flash.img"

    def validate(
        self,
        bl1,
        command,
        dtb,
        fip,
        kernel,
        rootfs,
        uefi,
        parameters,
        modules,
        tests,
        **kwargs,
    ):
        invalid_args = ["--" + k.replace("_", "-") for k in kwargs if kwargs[k]]
        if len(invalid_args) > 0:
            raise InvalidArgument(
                f"Invalid option(s) for fvp devices: {', '.join(sorted(invalid_args))}"
            )

        if modules and compression(modules) not in [("tar", "gz"), ("tar", "xz")]:
            raise InvalidArgument(
                "argument --modules should be a .tar.gz, tar.xz or .tgz"
            )

        for test in tests:
            test.validate(device=self, parameters=parameters, **kwargs)

    def definition(self, **kwargs):
        kwargs = kwargs.copy()

        # Options that can be updated
        kwargs["bl1"] = notnone(kwargs.get("bl1"), self.bl1)
        kwargs["dtb"] = notnone(kwargs.get("dtb"), self.dtb)
        kwargs["fip"] = notnone(kwargs.get("fip"), self.fip)
        kwargs["kernel"] = notnone(kwargs.get("kernel"), self.kernel)
        kwargs["rootfs"] = notnone(kwargs.get("rootfs"), self.rootfs)
        kwargs["uefi"] = notnone(kwargs.get("uefi"), self.uefi)

        # render the template
        tests = [
            t.render(
                arch="arm64",
                command=kwargs["command"],
                tmpdir=kwargs["tmpdir"],
                overlays=kwargs["overlays"],
                parameters=kwargs["parameters"],
                test_definitions=kwargs["test_definitions"],
            )
            for t in kwargs["tests"]
        ]
        return (
            templates.jobs().get_template("fvp-aemva.yaml.jinja2").render(**kwargs)
            + "\n"
            + "".join(tests)
        )

    def extra_assets(self, tmpdir, dtb, kernel, **kwargs):
        dtb = notnone(dtb, self.dtb).split("/")[-1]
        kernel = notnone(kernel, self.kernel).split("/")[-1]
        # Drop the extension if the kernel is compressed. LAVA will decompress it for us.
        if compression(kernel)[1]:
            kernel = kernel[: -1 - len(compression(kernel)[1])]
        (tmpdir / "startup.nsh").write_text(
            f"{kernel} dtb={dtb} console=ttyAMA0 earlycon=pl011,0x1c090000 root=/dev/vda ip=dhcp",
            encoding="utf-8",
        )
        return [f"file://{tmpdir / 'startup.nsh'}"]


class MorelloFVPDevice(FVPDevice):
    mandatory = [
        "ap_romfw",
        "mcp_fw",
        "mcp_romfw",
        "rootfs",
        "scp_fw",
        "scp_romfw",
        "fip",
    ]

    prompts: List[str] = []
    auto_login: Dict[str, str] = {}
    boot_timeout = 20
    kernel_start_message: Optional[str] = None
    support_tests = False
    rootfs: Optional[str] = None

    def validate(
        self,
        ap_romfw,
        mcp_fw,
        mcp_romfw,
        rootfs,
        scp_fw,
        scp_romfw,
        parameters,
        tests,
        fip,
        **kwargs,
    ):
        invalid_args = ["--" + k.replace("_", "-") for k in kwargs if kwargs[k]]
        if len(invalid_args) > 0:
            raise InvalidArgument(
                f"Invalid option(s) for fvp-morello devices: {', '.join(sorted(invalid_args))}"
            )

        args = locals()
        missing_args = [
            "--" + k.replace("_", "-") for k in self.mandatory if not args[k]
        ]
        if len(missing_args) > 0:
            raise InvalidArgument(
                f"Missing option(s) for fvp devices: {', '.join(sorted(missing_args))}"
            )

        if tests and not self.support_tests:
            raise InvalidArgument("Tests are not supported on this device")

        if self.rootfs and rootfs:
            raise InvalidArgument("Invalid option for this fvp device: --rootfs")

        for test in tests:
            test.validate(device=self, parameters=parameters, **kwargs)

    def definition(self, **kwargs):
        kwargs = kwargs.copy()

        # Options that can *not* be updated
        kwargs["prompts"] = self.prompts.copy()
        kwargs["auto_login"] = self.auto_login.copy()
        kwargs["kernel_start_message"] = self.kernel_start_message
        kwargs["support_tests"] = self.support_tests

        kwargs["rootfs"] = self.rootfs if self.rootfs else kwargs.get("rootfs")
        kwargs["boot_timeout"] = self.boot_timeout

        # render the template
        tests = [
            t.render(
                tmpdir=kwargs["tmpdir"],
                parameters=kwargs["parameters"],
                prompts=kwargs["prompts"],
            )
            for t in kwargs["tests"]
        ]
        return (
            templates.jobs().get_template("fvp-morello.yaml.jinja2").render(**kwargs)
            + "\n"
            + "".join(tests)
        )


class FVPMorelloAndroid(MorelloFVPDevice):
    name = "fvp-morello-android"

    prompts = ["console:/ "]
    support_tests = True


class FVPMorelloBusybox(MorelloFVPDevice):
    name = "fvp-morello-busybox"

    prompts = ["/ # "]
    support_tests = True
    virtiop9_path = "/etc"


class FVPMorelloBaremetal(MorelloFVPDevice):
    name = "fvp-morello-baremetal"

    mandatory = ["ap_romfw", "mcp_fw", "mcp_romfw", "scp_fw", "scp_romfw", "fip"]
    prompts = ["hello"]
    kernel_start_message = "Booting Trusted Firmware"


class FVPMorelloOE(MorelloFVPDevice):
    name = "fvp-morello-oe"

    prompts = ["root@morello-fvp:~# "]
    support_tests = True


class FVPMorelloUbuntu(MorelloFVPDevice):
    name = "fvp-morello-ubuntu"

    mandatory = ["ap_romfw", "mcp_fw", "mcp_romfw", "scp_fw", "scp_romfw", "fip"]

    prompts = ["morello@morello-server:"]
    auto_login = {
        "login_prompt": "morello-server login:",
        "username": "morello",
        "password_prompt": "Password:",
        "password": "morello",
    }
    boot_timeout = 60
    rootfs = "https://storage.tuxboot.com/fvp-morello-ubuntu/ubuntu.satadisk.xz"
