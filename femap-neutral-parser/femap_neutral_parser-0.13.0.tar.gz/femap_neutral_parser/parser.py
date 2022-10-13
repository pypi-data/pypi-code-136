import logging
import os
from collections import defaultdict as dd
from functools import reduce
from io import StringIO
from typing import Dict, List, Tuple

import numpy as np
import numpy.lib.recfunctions as rfn

from femap_neutral_parser import blocks
from femap_neutral_parser.neutral_flavors import Flavor

try:
    import pandas as pd

    ISPANDAS = True
except ImportError:
    ISPANDAS = False


def _todf(array):
    if not ISPANDAS:
        raise ValueError("Pandas library is not available")
    df = pd.DataFrame(array)
    ix = [c for c in ["SubcaseID", "NodeID", "ElementID"] if c in df]
    return df.set_index(ix)


def get_flavor(from_prog):
    if from_prog == "Unknown":
        return "MYSTRAN"
    return from_prog


class Parser(Flavor):
    def __init__(self, fpath: str) -> None:
        self.fpath = os.path.expanduser(fpath)
        if not os.path.isfile(self.fpath):
            raise ValueError(f'file path "{fpath}" not found')
        self._build_toc()  # -> self._toc
        self._parse_header()
        # self.blocks = {}
        # ---------------------------------------------------------------------
        # collect available defined blocks (code-wise, **not** neutral file wise)
        # this will create once self.__getattr__ will be called:
        #  * `self.header` from B100
        #  * `self.output_sets` from B450
        #  * `self._output_vectors` from B451
        self._defined_block_names = {
            getattr(blocks, b).NAME: getattr(blocks, b)
            for b in dir(blocks)
            if b.startswith("B")
        }
        # get flavor
        self.flavor = get_flavor(
            self.output_sets[list(self.output_sets.keys())[0]]["from_prog"]
        )
        logging.info(f"flavor={self.flavor}")

    def info(self, doprint=True, show_unknown=True):
        msg = []
        if 450 in self._toc:
            msg.append("\nAnalysis")
            msg.append("========")
            for lcid, lc_data in self.output_sets.items():
                flavor = get_flavor(lc_data["from_prog"])
                msg.append(
                    f" * subcase {lcid}: {lc_data['title']} ({flavor}::{lc_data['anal_type']})"
                )
        if 451 in self._toc:
            msg.append("\nOutputs")
            msg.append("=======")
            msg.append(
                "access to one of them using `._output_vectors[<title>][<SubcaseID>]['record']\n"
            )
            for output_title, output_data in self._output_vectors.items():
                # lcids = ", ".join(map(str, output_data.keys()))
                try:
                    initial_title = self.headers_to_title(output_title)
                    _field = f" * {output_title}"
                    isknown = True
                except ValueError:
                    # logging.warning(f"{output_title} is not known")
                    initial_title = f"{output_title}"
                    _field = f" * ## {output_title}"
                    isknown = False
                if not isknown and not show_unknown:
                    # skip Unknown vectors
                    continue
                _field += f" -> {initial_title}"
                msg.append(_field)
        if doprint:
            print("\n".join(msg))
            return
        return msg

    def vectors(
        self,
        titles,
        SubcaseIDs=None,
        raw=False,
        asdf=False,
        prefixed=True,
        incl_totals=True,
    ):
        if not SubcaseIDs:
            SubcaseIDs = tuple(self.output_sets.keys())
        if isinstance(SubcaseIDs, int):
            SubcaseIDs = (SubcaseIDs,)
        if isinstance(titles, str):
            titles = (titles,)
        recs = []
        key = None
        for SubcaseID in SubcaseIDs:
            arrays = []
            for title in titles:
                try:
                    ov = self._output_vectors[title.lower()]
                except KeyError:
                    raise KeyError(f"vector {title} is unknown")
                try:
                    data = ov[SubcaseID]
                except KeyError:
                    # no results for this loadcase
                    logging.warning(f"no results for {SubcaseID} / {title}")
                    continue
                arrays.append(data["record"])
            if not key:
                key = "NodeID" if "NodeID" in arrays[0].dtype.names else "ElementID"
            arr = reduce(lambda a1, a2: rfn.rec_join(key, a1, a2), arrays)
            arr = rfn.append_fields(
                arr, "SubcaseID", [SubcaseID] * len(arr), asrecarray=True, usemask=False
            )
            recs.append(arr)
        arr = rfn.stack_arrays(recs, asrecarray=True, usemask=False)
        return self._clean_df_goodies(
            arr,
            neutral_headers=titles,
            raw=raw,
            asdf=asdf,
            prefixed=prefixed,
            incl_totals=incl_totals,
        )

    def available_blocks(self) -> Dict[int, str]:
        return {
            getattr(blocks, b).NAME: getattr(blocks, b).id()
            for b in dir(blocks)
            if b.startswith("B")
        }

    def __getattr__(self, key: str):
        # look for blocks having key as NAME
        try:
            block_id = self._defined_block_names[key].id()
        except KeyError as exc:
            selfattrs = [attr for attr in dir(self) if attr.startswith("get_")]
            msg = f"'{key}' not found in _defined_block_names."
            msg += f"\n  available attributes are {selfattrs}"
            raise KeyError(msg)
        block = self._parse_blocks(block_id)
        if block_id == 451:
            data = block.digest(translate=self.title_to_headers)
        else:
            data = block.digest()
        setattr(self, key, data)
        return data

    def _parse_header(self):
        """parse block 100. This needs to be done at low-level since we will
        pick FEMAP's version number from there."""
        txt = tuple(self._get_block_raw_data(100))[0]
        b100 = blocks.B100(version=0)  # we do not have correct version at this point
        b100.parse(txt)
        self.header = b100.data[0]
        # also assign directly for convenieance
        self.femap_version = b100.data[0]["femap_version"]
        self.db_title = b100.data[0]["db_title"]

    def _build_toc(self, verbose=True):
        """parse the document to retrieve blocks locations"""
        _toc = dd(list)
        nb_lines = 0
        current_block = None
        for line_nb, line in enumerate(open(self.fpath, "r")):
            # if line_nb == 1598:
            #     breakpoint()
            line = line.strip()
            if line == "-1":
                if not current_block:
                    logging.debug(f"{line_nb=}:: {line}, new block is coming")
                    # ---------------------------------------------------------
                    # new block is coming, block ID known the line after
                    # ---------------------------------------------------------
                    current_block = -1  # set waiting status
                    continue
                else:
                    logging.debug(
                        f"{line_nb=}:: {line}, block {current_block} is finishing"
                    )
                    # ---------------------------------------------------------
                    # block is finishing
                    # ---------------------------------------------------------
                    _toc[current_block][-1].append(line_nb)
                    current_block = None
                    continue
            if current_block == -1:
                # -------------------------------------------------------------
                # waiting status
                current_block = int(line)
                logging.debug(
                    f"{line_nb=}:: {line}, block {current_block} is beginning"
                )
                _toc[current_block].append([line_nb + 1])
            nb_lines += 1
        # ---------------------------------------------------------------------
        # EOF
        # we sometimes miss trailing "-1". fix it:
        if current_block is not None and current_block > 0:
            _toc[current_block][-1].append(line_nb)
            logging.debug(
                f"{line_nb=}:: {line}, arbitrarilly closing {current_block} is finishing"
            )
        self._toc = dict(_toc)
        logging.info("parsed %d lines", nb_lines)

    def _get_block_raw_data(self, block_id, as_file_like=False):
        """yield file-like objects containing block data"""
        fh = open(self.fpath)
        line_offset = 0
        for line_start, line_end in self._toc[block_id]:
            lines = range(line_start, line_end)
            lines_content = []
            for line_nb, line in enumerate(fh, start=line_offset):
                if line_nb > line_end:
                    line_offset = line_nb + 1
                    break
                if line_nb in lines:
                    lines_content.append(line)
            if as_file_like:
                txt = StringIO()
                txt.writelines(lines_content)
                txt.seek(0)
            else:
                txt = lines_content
            yield txt
        fh.close()

    def _parse_blocks(self, block_id: int) -> None:
        """instantiate a block and feed it with relevant raw block text.
        Next step is supposed to be block.digest()
        """
        block = getattr(blocks, f"B{block_id}")(version=self.femap_version)
        for txt in self._get_block_raw_data(block_id=block_id):
            block.parse(txt)
        return block

    # =========================================================================
    # engineering shortcuts goodies
    # =========================================================================
    def get(self, what, asdf=False, prefixed=False, incl_totals=False, raw=False):
        try:
            neutral_headers = self.get_vectors(what, merge_aliases=True)
        except KeyError:
            raise KeyError(
                f"{what=} is not implemented. Select one of {set(self.get_vectors())}"
            )
        data = self.vectors(
            neutral_headers,
            raw=raw,
            asdf=asdf,
            prefixed=prefixed,
            incl_totals=incl_totals,
        )
        return data

    def _clean_df_goodies(
        self,
        data,
        neutral_headers,
        raw=False,
        asdf=False,
        prefixed=False,
        incl_totals=False,
    ):
        if not incl_totals:
            data = rfn.drop_fields(
                data, [f for f in rfn.get_names(data.dtype) if "total" in f]
            )
        if not prefixed and not raw:
            # drop vector from "<vector>::<axis>"
            renaming = {
                t: t.split("::")[1] for t in rfn.get_names(data.dtype) if "::" in t
            }
            data = rfn.rename_fields(data, renaming)
        if raw:
            renaming = {t: self.headers_to_title(t) for t in neutral_headers}
            data = rfn.rename_fields(data, renaming)
        if asdf:
            data = _todf(data)
        return data

    # -------------------------------------------------------------------------
    # Bar engineering forces
    def get_bar_local_forces(
        self,
        raw=False,
        asdf=False,
        prefixed=False,
        incl_totals=False,
    ):
        vectorsA = [
            "cbar_force::axial",
            "cbar_force::shear1",
            "cbar_force::shear2",
            "cbar_force::torque",
            "cbar_force::bending_moment_a1",
            "cbar_force::bending_moment_a2",
        ]
        pntA = self.vectors(vectorsA, prefixed=True)
        vectorsB = [
            "cbar_force::axial",
            "cbar_force::shear1",
            "cbar_force::shear2",
            "cbar_force::torque",
            "cbar_force::bending_moment_b1",
            "cbar_force::bending_moment_b2",
        ]
        pntB = self.vectors(vectorsB, prefixed=True)
        # reverse sign for point B
        for col in vectorsB:
            pntB[col] = -1 * pntB[col]
        # ---------------------------------------------------------------------
        # keep track of extremity
        pntA = rfn.append_fields(
            pntA, "ga/gb", ["A"] * len(pntA), asrecarray=True, usemask=False
        )
        pntB = rfn.append_fields(
            pntB, "ga/gb", ["B"] * len(pntA), asrecarray=True, usemask=False
        )
        neutral_headers = self.get_vectors("cbar_force")
        renaming = {
            t: t.split("::")[1].replace("_a", "")
            for t in rfn.get_names(pntA.dtype)
            if "::" in t
        }
        pntA = rfn.rename_fields(pntA, renaming)
        renaming = {
            t: t.split("::")[1].replace("_b", "")
            for t in rfn.get_names(pntB.dtype)
            if "::" in t
        }
        pntB = rfn.rename_fields(pntB, renaming)
        # ---------------------------------------------------------------------
        # stack
        data = rfn.stack_arrays((pntA, pntB), asrecarray=True, usemask=False)
        # ---------------------------------------------------------------------
        # change signs for loads (and not moments)
        for col in ("axial", "shear1", "shear2", "torque", "bending_moment1"):
            data[col] = -1 * data[col]
        data = self._clean_df_goodies(
            data, neutral_headers, raw, asdf, prefixed, incl_totals
        )
        return data


if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE)
