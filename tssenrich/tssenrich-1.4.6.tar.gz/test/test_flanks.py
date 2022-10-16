import pytest

from tssenrich import (
    generate_tss, generate_tss_flanks, tss_flanks_bed_str, tss_flanks_bed_tool,
    HG19_PATH, MM10_PATH
)

@pytest.fixture()
def flanks_hg38():
    return tss_flanks_bed_tool(
        tss_flanks_bed_str(generate_tss_flanks(generate_tss()))
    )

@pytest.fixture()
def flanks_hg19():
    return tss_flanks_bed_tool(
        tss_flanks_bed_str(generate_tss_flanks(generate_tss(genome=HG19_PATH)))
    )

@pytest.fixture()
def flanks_mm10():
    return tss_flanks_bed_tool(
        tss_flanks_bed_str(generate_tss_flanks(generate_tss(genome=MM10_PATH)))
    )


def test_flanks(flanks_hg38, flanks_hg19, flanks_mm10):
    flanks_hg38.head()
    flanks_hg19.head()
    flanks_mm10.head()
