__all__ = [
    "CALLER_EXPANSIONHUNTER",
    "CALLER_HIPSTR",
    "CALLER_GANGSTR",
    "CALLER_REPEATHMM",
    "CALLER_REPEATHMM_RECALL",
    "CALLER_STRAGLR",
    "CALLER_STRAGLR_RECALL",
    "CALLER_TANDEM_GENOTYPES",
    "CALLER_TANDEM_GENOTYPES_RECALL",
    "CALL_SUPPORTED_CALLERS",

    "M_CHROMOSOME_NAMES",
    "X_CHROMOSOME_NAMES",
    "Y_CHROMOSOME_NAMES",
    "SEX_CHROMOSOMES",
    "AUTOSOMES",
    "CHROMOSOMES",

    "MI_CALLERS",
]

CALLER_EXPANSIONHUNTER = "expansionhunter"
CALLER_HIPSTR = "hipstr"
CALLER_GANGSTR = "gangstr"
CALLER_REPEATHMM = "repeathmm"
CALLER_REPEATHMM_RECALL = "repeathmm-recall"
CALLER_STRAGLR = "straglr"
CALLER_STRAGLR_RECALL = "straglr-recall"
CALLER_STRKIT = "strkit"
CALLER_STRKIT_JSON = "strkit-json"
CALLER_TANDEM_GENOTYPES = "tandem-genotypes"
CALLER_TANDEM_GENOTYPES_RECALL = "tandem-genotypes-recall"

CALL_SUPPORTED_CALLERS = (
    CALLER_REPEATHMM,
    CALLER_STRAGLR,
    CALLER_TANDEM_GENOTYPES,
)

M_CHROMOSOME_NAMES = ("chrM", "M")
X_CHROMOSOME_NAMES = ("chrX", "X")
Y_CHROMOSOME_NAMES = ("chrY", "Y")
SEX_CHROMOSOMES = (*X_CHROMOSOME_NAMES, *Y_CHROMOSOME_NAMES)

AUTOSOMES = (
    *map(str, range(1, 23)),
    *(f"chr{i}" for i in range(1, 23)),
)

CHROMOSOMES = (
    *AUTOSOMES,
    *SEX_CHROMOSOMES,
)


MI_CALLERS = (
    CALLER_EXPANSIONHUNTER,
    CALLER_GANGSTR,
    "generic-vcf",
    "hipstr",
    "lobstr",
    "pacmonstr",
    CALLER_REPEATHMM,
    CALLER_REPEATHMM_RECALL,
    CALLER_STRAGLR,
    CALLER_STRAGLR_RECALL,
    CALLER_STRKIT,
    CALLER_STRKIT_JSON,
    CALLER_TANDEM_GENOTYPES,
    CALLER_TANDEM_GENOTYPES_RECALL,
)
