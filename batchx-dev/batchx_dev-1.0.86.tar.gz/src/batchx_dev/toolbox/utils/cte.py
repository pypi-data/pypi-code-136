import os
from pathlib import Path

# filesystem
ROOT = Path("/batchx")
TMP = Path("/tmp")
INPUT_DP = ROOT / "input"
OUTPUT_DP = ROOT / "output"
MANIFEST_DP = ROOT / "manifest"
INPUT_JSON_FP = INPUT_DP / "input.json"
OUTPUT_JSON_FP = OUTPUT_DP / "output.json"
MANIFEST_JSON_FP = MANIFEST_DP / "manifest.json"

BX_VCPUS = os.environ.get("BX_VCPUS", None)
BX_MEMORY = os.environ.get("BX_MEMORY", None)

# documentation URLS
URLS = dict(
    BED="https://genome.ucsc.edu/FAQ/FAQformat.html#format1",
    BAM="https://samtools.github.io/hts-specs/SAMv1.pdf",
    BAI="https://samtools.github.io/hts-specs/SAMv1.pdf#subsection.5.2",
    SAM="https://samtools.github.io/hts-specs/SAMv1.pdf",
    VCF="https://genome.ucsc.edu/goldenPath/help/vcf.html",
    GTF="https://genome.ucsc.edu/FAQ/FAQformat.html#format3",
    FAST5="https://medium.com/@shiansu/a-look-at-the-nanopore-fast5-format-f711999e2ff6",
    FASTA="https://en.wikipedia.org/wiki/FASTA_format",
    FASTQ="https://en.wikipedia.org/wiki/FASTQ_format",
    FAI="https://manpages.ubuntu.com/manpages/bionic/man5/faidx.5.html",
    CRAM="https://en.wikipedia.org/wiki/CRAM_(file_format)",
    PILEUP="https://en.wikipedia.org/wiki/Pileup_format",
)

FIXED_DESCRIPTIONS = {
    "schema.input.properties.sample.description": "This pipeline has the following **sample** inputs. These relate to the samples being analyzed. ",
    "schema.input.properties.global.description": "This pipeline has the following **global** inputs. These are files or values that can be reused in several workflows over different samples. ",
    "schema.input.properties.tools.description": "This pipeline has the following **tool** inputs. These are the tools this pipeline orchestrates along with their respective inputs. ",
    "schema.output.properties.dag.description": "SVG graph with the DAG of executed jobs. ",
    "schema.output.properties.tools.description": "This pipeline provides the following outputs, grouped by tool. ",
}

# readme-headers (deprecated!)
README_HEADERS = dict(
    context="# Context",
    inputs="# Inputs",
    required_inputs="## Required inputs",
    optional_inputs="## Optional inputs",
    required_outputs="## Required outputs",
    optional_outputs="## Optional outputs",
    outputs="# Outputs",
    examples="# Examples",
    links="# Links",
    tool_versions="# Tool versions",
    pipeline_overview="# Pipeline overview",
)
