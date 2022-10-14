import hashlib
import json
from pathlib import Path
from typing import Tuple

try:
    from solcx import compile_source, get_solc_version
except ImportError:
    compile_source = get_solc_version = None


def compile_freeze_solidity_contract(
    source_path: Path, force: bool = False, require_frozen: bool = False
) -> Tuple[list, str]:
    if force and require_frozen:
        raise Exception("The 'force' and 'require_frozen' are mutually exclusive")
    if not source_path.is_file():
        raise Exception("Solidity source is not a file")
    source_code = source_path.read_text(encoding="utf-8")
    source_checksum = hashlib.sha256(source_code.encode("utf-8")).hexdigest()

    checksum_path = source_path.with_name(source_path.name + ".sha256")
    abi_path = source_path.with_name(source_path.name + ".abi")
    bin_path = source_path.with_name(source_path.name + ".bin")
    scv_path = source_path.with_name(source_path.name + ".scv")

    # Evaluate compilation necessity if not forced initially.
    if not force:
        force = (
            not checksum_path.is_file() or not abi_path.is_file() or not bin_path.is_file() or not scv_path.is_file()
        )
        if not force:
            force = checksum_path.read_text(encoding="utf-8").strip() != source_checksum

    if force:  # force compilation by caller request or the compiled contract is out of date
        if require_frozen:
            raise Exception("Solidity source is not compiled, but it is required")
        if compile_source is None:
            raise Exception("Solcx is not available for compiling")
        compiled_sol = compile_source(source_code, output_values=["abi", "bin"], base_path=source_path.parent)
        contract_interface = compiled_sol[f"<stdin>:{source_path.stem}"]

        abi_path.write_text(json.dumps(contract_interface["abi"], indent=2), encoding="utf-8")
        bin_path.write_text(contract_interface["bin"], encoding="utf-8")
        scv_path.write_text(str(get_solc_version(with_commit_hash=True)), encoding="utf-8")
        checksum_path.write_text(source_checksum, encoding="utf-8")

    return json.loads(abi_path.read_text(encoding="utf-8")), bin_path.read_text(encoding="utf-8")
