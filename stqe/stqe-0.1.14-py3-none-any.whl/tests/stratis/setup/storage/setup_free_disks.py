#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals
from libsan.host.cmdline import run
from stqe.host.atomic_run import atomic_run, parse_ret
from libsan.host.scsi import get_free_disks
from libsan.host.mp import mpath_name_of_wwid, remove_mpath, is_multipathd_running
from stqe.host.persistent_vars import write_var, read_var, read_env
from libsan.host.linux import is_service_running
from libsan.host.lio import TargetCLI


def setup_local_disks(number_of_disks):
    msg = "INFO: Getting local disks."
    if number_of_disks:
        msg += " Trying to get %s disks" % number_of_disks
    print(msg)
    errors = []

    disks = atomic_run(message="Getting free disks",
                       command=get_free_disks,
                       errors=errors)
    # multiple_device test needs at least 4 disks
    if disks is None:
        disks = {}

    if len(disks.keys()) < number_of_disks:
        msg = f"INFO: Found only {len(disks.keys())} disks, need {number_of_disks} disks. " \
              f"Creating "
        print(msg)
        wwn = "naa.50014054c1441891"
        stratis_device_size = "10G"
        name = "stratis-lun-"

        try:
            stratis_device_size = read_env("fmf_loopback_size")
        except KeyError:
            pass

        for file in range(number_of_disks - len(disks.keys())):
            target = TargetCLI(path="/backstores/fileio")
            atomic_run("Creating fileio backstore",
                       command=target.create,
                       name=f"{name}{file}",
                       file_or_dev=f"/home/{name}{file}.img",
                       size=stratis_device_size,
                       errors=errors,
                       )

        target.path = "/loopback"
        atomic_run("Creating loopback",
                   wwn=wwn,
                   command=target.create,
                   errors=errors
                   )

        target.path = "/loopback/" + wwn + "/" + "luns"

        for lun in range(number_of_disks - len(disks.keys())):
            atomic_run("Creating lun using fileio backstore",
                       command=target.create,
                       storage_object=f"/backstores/fileio/{name}{lun}",
                       errors=errors,
                       )

        atomic_run("Writing var STRATIS_LOOPBACK_WWN",
                   command=write_var,
                   var={'STRATIS_LOOPBACK_WWN': wwn},
                   errors=errors)

        atomic_run("Writing var STRATIS_LUN_NAME",
                   command=write_var,
                   var={'STRATIS_LUN_NAME': name},
                   errors=errors)

        atomic_run("Writing var STRATIS_NUMBER_OF_LUNS",
                   command=write_var,
                   var={'STRATIS_NUMBER_OF_LUNS': number_of_disks - len(disks.keys())},
                   errors=errors)

        if is_multipathd_running():
            lio_disks = atomic_run(message="Getting free disks",
                                   exclude_mpath_device=False,
                                   command=get_free_disks,
                                   filter={"vendor": "LIO-ORG"},
                                   errors=errors)

            # Try to remove mpath from lio disks
            for disk in lio_disks.keys():
                mpath_name = mpath_name_of_wwid(lio_disks[disk]["wwid"])
                if mpath_name:
                    print(f"INFO: Trying to remove mpath {mpath_name}")
                    remove_mpath(mpath_name)

        disks = atomic_run(message="Getting free disks",
                           command=get_free_disks,
                           errors=errors)
    else:
        atomic_run("Writing var STRATIS_NUMBER_OF_LUNS",
                   command=write_var,
                   var={'STRATIS_NUMBER_OF_LUNS': 0},
                   errors=errors)

    disks = disks.keys()
    disk_paths = ["/dev/" + j for j in disks]
    blockdevs = read_var("STRATIS_DEVICE")

    if blockdevs:
        # backup the previous devices
        atomic_run("Writing var STRATIS_DEVICE_BACKUP",
                   command=write_var,
                   var={'STRATIS_DEVICE_BACKUP': " ".join(blockdevs)},
                   errors=errors)
        if not isinstance(blockdevs, list):
            blockdevs = [blockdevs]
        disk_paths += [x for x in blockdevs if x not in blockdevs]

    print("Using these blockdevs: %s" % " ".join(disk_paths))
    for disk in disk_paths:
        atomic_run("Zeroing superblock of disk %s." % disk,
                   command=run,
                   cmd="dd if=/dev/zero of=%s bs=1M count=10" % disk,
                   errors=errors)
        if is_service_running("multipathd"):
            atomic_run("remove multipath superblock of disk %s." % disk,
                       command=run,
                       cmd="multipath -W %s" % disk,
                       errors=errors)

    atomic_run("Writing var STRATIS_AVAILABLE_DEVICES",
               command=write_var,
               var={'STRATIS_AVAILABLE_DEVICES': disk_paths},
               errors=errors)

    atomic_run("Writing var STRATIS_DEVICE",
               command=write_var,
               var={'STRATIS_DEVICE': disk_paths},
               errors=errors)

    atomic_run(message="Listing block devices.",
               command=run,
               cmd="lsblk",
               errors=errors)

    return errors


if __name__ == "__main__":
    try:
        number_of_disks = read_env("fmf_number_of_disks")
    except KeyError:
        number_of_disks = None
    errs = setup_local_disks(number_of_disks)
    exit(parse_ret(errs))
