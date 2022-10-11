import base64
from typing import Dict, List, Tuple
from .types import EnclaveSpecification
from .compute import GcgDriverDecoder
from .sql.compute import SqlWorkerDecoder
from .container.compute import ContainerWorkerDecoder
from .s3_sink.compute import S3SinkWorkerDecoder
from .proto import (
    AttestationSpecification,
    AttestationSpecificationIntelDcap,
    AttestationSpecificationAwsNitro,
    AttestationSpecificationAmdSnp,
)
import asn1crypto.pem
from .certs import (
    aws_nitro_root_ca_pem,
    amd_snp_ark_pem,
    intel_sgx_dcap_root_ca,
    intel_sgx_ias_root_ca,
)


intel_sgx_dcap_root_ca_der = asn1crypto.pem.unarmor(intel_sgx_dcap_root_ca)[2]
intel_sgx_ias_root_ca_der = asn1crypto.pem.unarmor(intel_sgx_ias_root_ca)[2]
aws_nitro_root_ca_der = asn1crypto.pem.unarmor(aws_nitro_root_ca_pem)[2]
amd_snp_ark_der = asn1crypto.pem.unarmor(amd_snp_ark_pem)[2]

# From https://developers.cloudflare.com/time-services/roughtime/recipes/
roughtime_public_key = base64.b64decode("gD63hSj3ScS+wuOeGrubXlq35N1c5Lby/S+T7MNTjxo=")

# Allowed Decentriq AMD CPU Chip IDs
amd_snp_authorized_chip_ids = [
  bytes.fromhex("ce8a61aea3f76bbdd05706bcbfb4ade4c65b33ad41f49d0e89dec177951117d247781a3195de2e85399b7117d9eee2f6f2c2e5d21064a4d7e2815380212f0937"),
  bytes.fromhex("86185338a275af6b5e26e06a21b4e0c65db0fc9033e4a24e27cb528321726dc152f28b08c05493c48e8fba3047aba6f0a0dd01d3eebb055b3318c1029c0a74ee"),
]

SPECIFICATIONS = {
    "decentriq.driver:v6": EnclaveSpecification(
        name="decentriq.driver",
        proto=AttestationSpecification(
            intelDcap=AttestationSpecificationIntelDcap(
                mrenclave=bytes.fromhex(
                    "fcceb6327c283923e1ae608abf2906a3c94f24cad7f98016054cdda39e18dee0"
                ),
                dcapRootCaDer=intel_sgx_dcap_root_ca_der,
                accept_debug=False,
                accept_out_of_date=False,
                accept_configuration_needed=False,
                accept_sw_hardening_needed=False,
                accept_revoked=False,
            )
        ),
        workerProtocols=[0],
        decoder=GcgDriverDecoder(),
        clientProtocols=[1, 2],
    ),
    "decentriq.driver:v5": EnclaveSpecification(
        name="decentriq.driver",
        proto=AttestationSpecification(
            intelDcap=AttestationSpecificationIntelDcap(
                mrenclave=bytes.fromhex(
                    "5433c37d119b884d93cb2a42c491b2d98dda03a0dc4ec04b3734d2fb47962d1e"
                ),
                dcapRootCaDer=intel_sgx_dcap_root_ca_der,
                accept_debug=False,
                accept_out_of_date=False,
                accept_configuration_needed=False,
                accept_sw_hardening_needed=False,
                accept_revoked=False,
            )
        ),
        workerProtocols=[0],
        decoder=GcgDriverDecoder(),
        clientProtocols=[1],
    ),
    "decentriq.driver:v4": EnclaveSpecification(
        name="decentriq.driver",
        proto=AttestationSpecification(
            intelDcap=AttestationSpecificationIntelDcap(
                mrenclave=bytes.fromhex(
                    "f3746dc7b06d7f1aa6fc1fc9dbf61920663466bc75476a9b1460f6a112be71cf"
                ),
                dcapRootCaDer=intel_sgx_dcap_root_ca_der,
                accept_debug=False,
                accept_out_of_date=False,
                accept_configuration_needed=False,
                accept_sw_hardening_needed=False,
                accept_revoked=False,
            )
        ),
        workerProtocols=[0],
        decoder=GcgDriverDecoder(),
        clientProtocols=[1],
    ),
    "decentriq.driver:v3": EnclaveSpecification(
        name="decentriq.driver",
        proto=AttestationSpecification(
            intelDcap=AttestationSpecificationIntelDcap(
                mrenclave=bytes.fromhex(
                    "564d4744604e252e046be2b2ba4d86fb7eb5a2ec85046735bd5abe62654b9d61"
                ),
                dcapRootCaDer=intel_sgx_dcap_root_ca_der,
                accept_debug=False,
                accept_out_of_date=False,
                accept_configuration_needed=False,
                accept_sw_hardening_needed=False,
                accept_revoked=False,
            )
        ),
        workerProtocols=[0],
        decoder=GcgDriverDecoder(),
        clientProtocols=[1],
    ),
    "decentriq.driver:v2": EnclaveSpecification(
        name="decentriq.driver",
        proto=AttestationSpecification(
            intelDcap=AttestationSpecificationIntelDcap(
                mrenclave=bytes.fromhex(
                    "a88ec2195974edf693e45b2ccdf39cf53c9382bb5309ba3863b5d0f2591542f1"
                ),
                dcapRootCaDer=intel_sgx_dcap_root_ca_der,
                accept_debug=False,
                accept_out_of_date=False,
                accept_configuration_needed=False,
                accept_sw_hardening_needed=False,
                accept_revoked=False,
            )
        ),
        workerProtocols=[0],
        decoder=GcgDriverDecoder(),
        clientProtocols=[0],
    ),
    "decentriq.sql-worker:v5": EnclaveSpecification(
        name="decentriq.sql-worker",
        proto=AttestationSpecification(
            intelDcap=AttestationSpecificationIntelDcap(
                mrenclave=bytes.fromhex(
                    "4b6178678bd60bcb988234c6ec47b7d0ef1cf982dffc996bb7211ef8b3b72ad7"
                ),
                dcapRootCaDer=intel_sgx_dcap_root_ca_der,
                accept_debug=False,
                accept_out_of_date=False,
                accept_configuration_needed=False,
                accept_sw_hardening_needed=False,
                accept_revoked=False,
            )
        ),
        workerProtocols=[0],
        decoder=SqlWorkerDecoder(),
        clientProtocols=None,
    ),
    "decentriq.sql-worker:v4": EnclaveSpecification(
        name="decentriq.sql-worker",
        proto=AttestationSpecification(
            intelDcap=AttestationSpecificationIntelDcap(
                mrenclave=bytes.fromhex(
                    "5f07de831d93b1ff5446ef0e17d8dcf0418ce8416cd0d5039c4266503fd4c7c9"
                ),
                dcapRootCaDer=intel_sgx_dcap_root_ca_der,
                accept_debug=False,
                accept_out_of_date=False,
                accept_configuration_needed=False,
                accept_sw_hardening_needed=False,
                accept_revoked=False,
            )
        ),
        workerProtocols=[0],
        decoder=SqlWorkerDecoder(),
        clientProtocols=None,
    ),
    "decentriq.sql-worker:v3": EnclaveSpecification(
        name="decentriq.sql-worker",
        proto=AttestationSpecification(
            intelDcap=AttestationSpecificationIntelDcap(
                mrenclave=bytes.fromhex(
                    "5b1838ec6d3509fe1c1ac1b13d394bc9df76057ddd18c1b8fff882b379d110e2"
                ),
                dcapRootCaDer=intel_sgx_dcap_root_ca_der,
                accept_debug=False,
                accept_out_of_date=False,
                accept_configuration_needed=False,
                accept_sw_hardening_needed=False,
                accept_revoked=False,
            )
        ),
        workerProtocols=[0],
        decoder=SqlWorkerDecoder(),
        clientProtocols=None,
    ),
    "decentriq.sql-worker:v2": EnclaveSpecification(
        name="decentriq.sql-worker",
        proto=AttestationSpecification(
            intelDcap=AttestationSpecificationIntelDcap(
                mrenclave=bytes.fromhex(
                    "c04e429edd5fc767e00ec4839b1f8c57375fda178905866ac6d4debee4fbe7d1"
                ),
                dcapRootCaDer=intel_sgx_dcap_root_ca_der,
                accept_debug=False,
                accept_out_of_date=False,
                accept_configuration_needed=False,
                accept_sw_hardening_needed=False,
                accept_revoked=False,
            )
        ),
        workerProtocols=[0],
        decoder=SqlWorkerDecoder(),
        clientProtocols=None,
    ),
    "decentriq.s3-sink-worker:v1": EnclaveSpecification(
        name="decentriq.s3-sink-worker",
        proto=AttestationSpecification(
            intelDcap=AttestationSpecificationIntelDcap(
                mrenclave=bytes.fromhex(
                    "799bb8ca2a4da8b74d4bbfabde3a2b2d3853f0c0b2c583a003e0163f6051c85c"
                ),
                dcapRootCaDer=intel_sgx_dcap_root_ca_der,
                accept_debug=False,
                accept_out_of_date=False,
                accept_configuration_needed=False,
                accept_sw_hardening_needed=False,
                accept_revoked=False,
            )
        ),
        workerProtocols=[0],
        decoder=S3SinkWorkerDecoder(),
        clientProtocols=None,
    ),
    "decentriq.python-ml-worker-32-64:v1": EnclaveSpecification(
        name="decentriq.python-ml-worker",
        proto=AttestationSpecification(
            amdSnp=AttestationSpecificationAmdSnp(
                amdArkDer=amd_snp_ark_der,
                measurement=bytes.fromhex("141ebf6108bd025b075bc833fb54b0d6e0bcb609b348991e0e15b1b6ba8e52fad6d727ae10fb2e6c3f9a89064cb18420"),
                roughtimePubKey=roughtime_public_key,
                authorizedChipIds=amd_snp_authorized_chip_ids,
            )
        ),
        workerProtocols=[0],
        decoder=ContainerWorkerDecoder(),
        clientProtocols=None,
    ),
    "decentriq.python-ml-worker:v2": EnclaveSpecification(
        name="decentriq.python-ml-worker",
        proto=AttestationSpecification(
            awsNitro=AttestationSpecificationAwsNitro(
                nitroRootCaDer=aws_nitro_root_ca_der,
                pcr0=bytes.fromhex("ea004dce7a444fdf4603b903f9bc730494fc6c876ffd86fdf8f7c3910803b38ca60d0e38af0bbd44f159918d90fa46c4"),
                pcr1=bytes.fromhex("ea004dce7a444fdf4603b903f9bc730494fc6c876ffd86fdf8f7c3910803b38ca60d0e38af0bbd44f159918d90fa46c4"),
                pcr2=bytes.fromhex("21b9efbc184807662e966d34f390821309eeac6802309798826296bf3e8bec7c10edb30948c90ba67310f7b964fc500a"),
                pcr8=bytes.fromhex("000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000")
            )
        ),
        workerProtocols=[0],
        decoder=ContainerWorkerDecoder(),
        clientProtocols=None,
    ),
    "decentriq.python-ml-worker:v1": EnclaveSpecification(
        name="decentriq.python-ml-worker",
        proto=AttestationSpecification(
            awsNitro=AttestationSpecificationAwsNitro(
                nitroRootCaDer=aws_nitro_root_ca_der,
                pcr0=bytes.fromhex("9103b7019cd97a2837b1631648bc683b3470b402b3c0638d8ff16178c7fd031407c06aeff8f96517a320fb573d7d281f"),
                pcr1=bytes.fromhex("9103b7019cd97a2837b1631648bc683b3470b402b3c0638d8ff16178c7fd031407c06aeff8f96517a320fb573d7d281f"),
                pcr2=bytes.fromhex("21b9efbc184807662e966d34f390821309eeac6802309798826296bf3e8bec7c10edb30948c90ba67310f7b964fc500a"),
                pcr8=bytes.fromhex("000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000")
            )
        ),
        workerProtocols=[0],
        decoder=ContainerWorkerDecoder(),
        clientProtocols=None,
    ),
    "decentriq.python-synth-data-worker-32-32:v1": EnclaveSpecification(
        name="decentriq.python-synth-data-worker",
        proto=AttestationSpecification(
            amdSnp=AttestationSpecificationAmdSnp(
                amdArkDer=amd_snp_ark_der,
                measurement=bytes.fromhex("eb4da359c5a46bfea871dd06b987e61a9d062bf7e8dbdbbf8708a46ef0f9aa626748580d404e9f27a189471e49837ae5"),
                roughtimePubKey=roughtime_public_key,
                authorizedChipIds=amd_snp_authorized_chip_ids,
            )
        ),
        workerProtocols=[0],
        decoder=ContainerWorkerDecoder(),
        clientProtocols=None,
    ),
    "decentriq.python-synth-data-worker:v2": EnclaveSpecification(
        name="decentriq.python-synth-data-worker",
        proto=AttestationSpecification(
            awsNitro=AttestationSpecificationAwsNitro(
                nitroRootCaDer=aws_nitro_root_ca_der,
                pcr0=bytes.fromhex("3759aad200a137252997a459a38c1953c8868844c7271487ae536a441133c407fb2dd3e1d4b167d997a8aa48b54341c1"),
                pcr1=bytes.fromhex("3759aad200a137252997a459a38c1953c8868844c7271487ae536a441133c407fb2dd3e1d4b167d997a8aa48b54341c1"),
                pcr2=bytes.fromhex("21b9efbc184807662e966d34f390821309eeac6802309798826296bf3e8bec7c10edb30948c90ba67310f7b964fc500a"),
                pcr8=bytes.fromhex("000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000")
            )
        ),
        workerProtocols=[0],
        decoder=ContainerWorkerDecoder(),
        clientProtocols=None,
    ),
    "decentriq.python-synth-data-worker:v1": EnclaveSpecification(
        name="decentriq.python-synth-data-worker",
        proto=AttestationSpecification(
            awsNitro=AttestationSpecificationAwsNitro(
                nitroRootCaDer=aws_nitro_root_ca_der,
                pcr0=bytes.fromhex("b1eeccf3396b7d2163b7ff90017dfea71911b282e7ac683574237b0f6011d1617cb42322342e43d8721ccb9aefb918f4"),
                pcr1=bytes.fromhex("b1eeccf3396b7d2163b7ff90017dfea71911b282e7ac683574237b0f6011d1617cb42322342e43d8721ccb9aefb918f4"),
                pcr2=bytes.fromhex("21b9efbc184807662e966d34f390821309eeac6802309798826296bf3e8bec7c10edb30948c90ba67310f7b964fc500a"),
                pcr8=bytes.fromhex("000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000")
            )
        ),
        workerProtocols=[0],
        decoder=ContainerWorkerDecoder(),
        clientProtocols=None,
    ),
    "decentriq.r-latex-worker:v2": EnclaveSpecification(
        name="decentriq.r-latex-worker",
        proto=AttestationSpecification(
            awsNitro=AttestationSpecificationAwsNitro(
                nitroRootCaDer=aws_nitro_root_ca_der,
                pcr0=bytes.fromhex("43223aecfeae895fcb966b41618611f16d675991c472ad58d358a846bd9fa472d2eeabd130ad1aee97bf74067ccf5ac8"),
                pcr1=bytes.fromhex("43223aecfeae895fcb966b41618611f16d675991c472ad58d358a846bd9fa472d2eeabd130ad1aee97bf74067ccf5ac8"),
                pcr2=bytes.fromhex("21b9efbc184807662e966d34f390821309eeac6802309798826296bf3e8bec7c10edb30948c90ba67310f7b964fc500a"),
                pcr8=bytes.fromhex("000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000")
            )
        ),
        workerProtocols=[0],
        decoder=ContainerWorkerDecoder(),
        clientProtocols=None,
    ),
    "decentriq.r-latex-worker:v1": EnclaveSpecification(
        name="decentriq.r-latex-worker",
        proto=AttestationSpecification(
            awsNitro=AttestationSpecificationAwsNitro(
                nitroRootCaDer=aws_nitro_root_ca_der,
                pcr0=bytes.fromhex("7e78d613db8801fe051abc1325eb1dfd12a42b3c8cd9ba6925c35d2bc91549c79b62577c1fd799bedc8ed8a3f85422e6"),
                pcr1=bytes.fromhex("7e78d613db8801fe051abc1325eb1dfd12a42b3c8cd9ba6925c35d2bc91549c79b62577c1fd799bedc8ed8a3f85422e6"),
                pcr2=bytes.fromhex("21b9efbc184807662e966d34f390821309eeac6802309798826296bf3e8bec7c10edb30948c90ba67310f7b964fc500a"),
                pcr8=bytes.fromhex("000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000")
            )
        ),
        workerProtocols=[0],
        decoder=ContainerWorkerDecoder(),
        clientProtocols=None,
    )
}


class EnclaveSpecifications:
    """
    Provider of the available enclave specifications provided by the Decentriq platform.

    Enclave specifications enable you to express which particular enclaves you trust.
    The field containing the measurement (e.g. `mrenclave` in the case of Intel SGX) identifies
    the exact binary that will process your data.
    Users of the Decentriq platform are encouraged to reproduce this value by building the enclave
    binary from audited source code and re-producing the measurement (in the case of Intel SGX,
    this would involve simply hashing the produced executable).

    When connecting to the driver enclave, the configured attestation algorithm will guarantee that the
    enclave you connect to is the one corresponding to the enclave specification you chose.
    The associated root certificate will be used to verify that the attestation was signed
    by the expected party (e.g. Intel/AMD/Amazon, depending on the CC technology used).

    Any communication between the driver enclave and worker enclaves handling your data will also
    first be secured by additional attestation procedures. Which enclaves are trusted by the
    driver enclave is controlled by choosing the additional enclave specs from the respective
    compute packages.

    A list of enclave specifications, each encoding your trust in a particular enclave type, can
    be obtained by selecting a subset of the enclave specifications provided by the object
    `decentriq_platform.enclave_specifications`. Selecting the subset of versions should be done
    by calling its `versions` method.
    """

    def __init__(self, specifications: Dict[str, EnclaveSpecification]):
        self.specifications = specifications

    def list(self) -> List[str]:
        """Get a list of all available enclave identifiers."""
        return sorted(self.specifications.keys())

    def versions(self, enclave_versions: List[str]) -> Dict[str, EnclaveSpecification]:
        """
        Get the enclave specifications for the given versioned enclave types.

        Make sure to always include the specification of a *driver enclave*, e.g.
        `"decentriq.driver:v1"` as this is the node with which you communicate directly.
        Add additional versioned enclaves depending on the compute module you use.
        Refer to the main documentation page of each compute module to learn which
        enclaves are available.
        """
        selected_specifcations = {}
        for version in enclave_versions:
            enclave_type = version.split(":")[0]
            selected_specifcations[enclave_type] = self.specifications[version]
        return selected_specifcations

    def all(self) -> List[EnclaveSpecification]:
        """Get a list of all available enclave specifications."""
        return list(self.specifications.values())

    def merge(self, other):
        """
        Merge two sets of enclave specifications into a single set.
        """
        return EnclaveSpecifications({**self.specifications, **other.specifications})


enclave_specifications: EnclaveSpecifications = EnclaveSpecifications(SPECIFICATIONS)
"""The main catalogue of enclave specifications available within the Decentriq platform."""
