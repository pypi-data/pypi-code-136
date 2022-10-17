import gzip
import shutil
import subprocess as sp
import sys
from functools import partial
from pathlib import Path
from typing import Callable

from ..parsers import Input, Manifest


class Actions:
    @property
    def callables(self):
        return dict(
            mv_to_dp=self.mv_to_dp,
            ln_to_tmp=self.ln_to_tmp,
            given_pattern_find_matches_in_dp=self.given_pattern_find_matches_in_dp,
            given_dp_find_matches_with_pattern=self.given_dp_find_matches_with_pattern,
            conditional_unzip_gzip=self.conditional_unzip_gzip,
            paths_to_strings=self.paths_to_strings,
        )

    def mv_to_dp(
        self,
        input: Input,
        manifest: Manifest,
        value: str | Path | list[str] | list[Path],
        dp: str = "idp",
        as_string: bool = True,
    ) -> str | Path | list[str] | list[Path]:
        """
        Rename provided filepath(s) to be inside of a specified directory.

        Args:
            input (Input): Input object.
            manifest (Manifest): Manifest object.
            value (str | Path | list[str] | list[Path]): Filename or list of filenames (as string or Paths) which should be altered to be inside of the specified directory.
            dp (str, optional): Directory path known in "self.fs". Provided filenames will be altered such that the modified filenames will be inside this directory. Defaults to "idp".
            as_string (bool, optional): Whether or not the results should be Paths or converted back to regular strings. Defaults to True.

        Returns:
            str | Path | list[str] | list[Path]: Altered Filename(s)/filepaths.
        """
        if dp in self.fs.keys():
            directory_path = getattr(self.fs, dp)
        elif Path(dp).exists():
            directory_path = Path(dp)
            if self.verbose:
                msg = """
                DIRECTORY PATH NOT FOUND IN SELF.FS
                -----------------------------------
                directory path {dp} 
                    - not found in self.fs (Keys: {k}),
                    - but refers directly to an existing directory. Using this.
                """.format(
                    dp=dp, k=set(self.fs.keys())
                )
                print(msg, flush=True)
        else:
            directory_path = Path()
            if self.verbose:
                msg = """
                DIRECTORY PATH NOT FOUND
                ------------------------
                directory path {dp} 
                    - not found in self.fs (Keys: {k})
                    - does not refer to an existing directory (Path(dp).exists() == False)
                As a fallback: replaced by current directory {r}
                """.format(
                    dp=dp, k=set(self.fs.keys()), r=directory_path.absolute()
                )
                print(msg, flush=True)

        def _rename(v):
            r = directory_path / v
            if self.verbose:
                msg = """

                RENAME FILE TO BE INSIDE DIRECTORY
                ----------------------------------
                Renamed file {f}
                to           {r}      
                """.format(
                    f=v, r=r
                )
                print(msg)
            if as_string:
                r = str(r)
            return r

        if isinstance(value, list):
            return [_rename(e) for e in value]
        else:
            return _rename(value)

    def ln_to_tmp(
        self,
        input: Input,
        manifest: Manifest,
        value: str | Path | list[str] | list[Path],
        as_string: bool = True,
    ) -> str | Path | list[str] | list[Path]:
        """
        Symlink provided filepath(s) inside /tmp directory.

        Args:
            input (Input): Input object.
            manifest (Manifest): Manifest object.
            value (str | Path | list[str] | list[Path]): Filename or list of filenames (as string or Paths) which should be symlinked into the /tmp directory.
            as_string (bool, optional): Whether or not the results should be Paths or converted back to regular strings. Defaults to True.

        Returns:
            str | Path | list[str] | list[Path]: Filename(s)/filepaths in tmp.
        """

        def _command(fn):
            return "ln -s {fn} {tmp}/.".format(fn=fn, tmp=self.fs.tmp)

        def _symlink(v):
            # do symlink
            command = _command(v)
            sp.check_call(command, shell=True)

            # construct filename
            r = self.fs.tmp / Path(v).name

            if self.verbose:
                msg = """

                SYMLINK TO TMP
                --------------
                Symlinked file {f}
                to             {r}
                via command    {c}

                """.format(
                    c=command, f=v, r=r
                )
                print(msg)
            if as_string:
                r = str(r)
            return r

        if isinstance(value, list):
            return [_symlink(e) for e in value]
        else:
            return _symlink(value)

    def given_pattern_find_matches_in_dp(
        self,
        input: Input,
        manifest: Manifest,
        value: str,
        dp: str = "idp",
        as_string: bool = True,
        kind: str = "prefix",
    ) -> list[str] | list[Path]:
        dp = getattr(self.fs, dp, None)
        """
        Find filepaths in a specified directory that adhere to the pattern specified by `value`.

        Args:
            input (Input): Input object.
            manifest (Manifest): Manifest object.
            value (str): (part of) pattern to match
            dp (str, optional): Directory path known in "self.fs", in which to look for files matching the pattern. Defaults to "idp".
            as_string (bool, optional): Whether or not the results should be Paths or converted back to regular strings. Defaults to True.
            kind (str, optional):   Kind of pattern you are providing as value. E.g. a prefix pattern yields "{value}*" as the `glob` pattern to matched. Defaults to "prefix".

        Returns:
            list[str] | list[Path]: List of matching filepaths.
        """
        return self.given_dp_find_matches_with_pattern(
            input,
            manifest,
            value=dp,
            pattern=value,
            as_string=as_string,
            kind=kind,
        )

    def given_dp_find_matches_with_pattern(
        self,
        input: Input,
        manifest: Manifest,
        value: str | Path,
        pattern: str = "*",
        as_string: bool = True,
        kind: str = "prefix",
    ) -> list[str] | list[Path]:
        """
        Find filepaths in a specified directory that adhere to the pattern specified by `pattern`.

        Args:
            input (Input): Input object.
            manifest (Manifest): Manifest object.
            value (str | Path): Directory path where to look for the specified pattern.
            pattern (str, optional): Pattern to match. Defaults to "*".
            as_string (bool, optional): Whether or not the results should be Paths or converted back to regular strings. Defaults to True.
            kind (str, optional): Kind of pattern you are providing as value. E.g., a "prefix" pattern yields "{value}*" as the `glob` pattern to matched. Recognized options {"prefix", "suffix"}. If the option is not recognized, the assumption is a valid glob pattern was provided.  Defaults to "prefix".

        Returns:
            list[str] | list[Path]: List of matching filepaths.
        """

        dp = Path(value)
        assert (
            dp.exists()
        ), "This function expects its argument to be a valid directory. {dp} not found.".format(
            dp=dp
        )

        if kind in {"prefix"}:
            pattern = "{p}*".format(p=pattern)
        elif kind in {"suffix"}:
            pattern = "*{p}".format(p=pattern)
        else:
            pattern = pattern

        matches = list(Path(dp).glob(pattern))

        if self.verbose:
            msg = """
            Scanning directory {d}
            for files matching pattern {v}

            Found {n} matches:
                {m}
            """.format(
                d=dp, v=dp, n=len(matches), m=matches
            )
            print(msg)

        if as_string:
            return [str(fp) for fp in matches]
        else:
            return matches

    def conditional_unzip_gzip(
        self,
        input: Input,
        manifest: Manifest,
        value: str | Path,
        as_string: bool = True,
        use_pigz: bool = False,
        only_unzip_these_extensions: tuple[str] = (),
    ) -> str | Path:
        """
        Unzip a file if it is in fact gzipped.

        If so, unzip the file and return the filepath of the unzipped file.
        Otherwise, do nothing an return the original filepath.

        Args:
            input (Input): Input object.
            manifest (Manifest): Manifest object.
            value (str | Path): Filename of filepath of the file that should be unzipped if applicable.
            as_string (bool, optional): Whether or not the results should be Paths or converted back to regular strings. Defaults to True.
            use_pigz (bool, optional): Whether or not `pigz` should be used to unzip a gzipped file. If set to True, the `pigz`tool needs to be available on the system. Defaults to False.

        Returns:
            str | Path: Filename or filepath of the unzipped file. Could be the original if it never was zipped in the first place.
        """

        def _should_be_unzipped(
            fp: str | Path, only_unzip_these_extensions: tuple[str] = ()
        ) -> bool:
            """Check whether provided file is gzipped yes/no."""

            with open(fp, "rb") as f:
                is_gzipped = f.read(2) == b"\x1f\x8b"

            extensions_provided = len(only_unzip_these_extensions) > 0

            if extensions_provided:
                extension_should_be_unzipped = any(
                    [str(fp).endswith(ext) for ext in only_unzip_these_extensions]
                )
            else:
                extension_should_be_unzipped = True  # Trivial pass

            return is_gzipped and extension_should_be_unzipped

        def _unzip_gzip_using_pigz(gzip_fp: Path, unzip_fp: Path):
            """Unzips a gzipped file properly using pigz."""
            if self.verbose:
                msg = """Unzipping file {fp} using pigz.
                """.format(
                    fp=gzip_fp
                )
                print(msg, flush=True)
            with open(unzip_fp, "w") as f:
                cmd = ["pigz", "-dc", str(gzip_fp)]
                exit_code = sp.check_call(cmd, stdout=f)
                if exit_code != 0:
                    sys.exit(exit_code)
            return unzip_fp

        def _unzip_gzip_using_gzip(gzip_fp: Path, unzip_fp: Path):
            """Unzips a gzipped file properly using gzip python package."""
            if self.verbose:
                msg = """Unzipping file {fp} using gzip python package.
                """.format(
                    fp=gzip_fp
                )
                print(msg, flush=True)
            with gzip.open(gzip_fp, "rb") as f_in:
                with open(unzip_fp, "wb") as f_out:
                    shutil.copyfileobj(f_in, f_out)
            return unzip_fp

        fp = Path(value)
        if _should_be_unzipped(
            fp, only_unzip_these_extensions=only_unzip_these_extensions
        ):
            unzip_fp = fp.parent / fp.stem  # removes .gz suffix
            if use_pigz:
                result = _unzip_gzip_using_pigz(fp, unzip_fp)
            else:
                result = _unzip_gzip_using_gzip(fp, unzip_fp)
        else:
            result = fp

        if as_string:
            return str(result)
        else:
            return result

    def paths_to_strings(
        input: Input, manifest: Manifest, value: list[Path | str]
    ) -> list[str]:
        """
        Convert a list of objects to a list of strings.

        Useful if the list contains (or could contain) Path objects, as those cannot be serialized to json, or
        inject into a shell command.

        Args:
            input (Input): Input object.
            manifest (Manifest): Manifest object.
            list_of_paths (list): List of filenames or filepaths.

        Returns:
            list[str]: List of filenames. As in: all of the entries will be strings.
        """
        return [str(p) for p in value]


class ActionMixin(Actions):
    def do_actions(self, input, manifest):
        """Do all actions. This may or may not involve transforming the input."""

        for key in self.actions.keys():
            self.do_actions_for_one_key(input, manifest, key)
        return input

    def do_actions_for_one_key(self, input, manifest, key):
        relevant_actions = self.actions.get(key, [])
        for action in relevant_actions:
            if self.verbose:
                print(
                    "Executing action for key: {k}".format(k=key),
                    flush=True,
                )

            old_val = getattr(input, key, None)  # really needs to be *inside* the loop

            if old_val is not None:
                new_val = action(input, manifest, old_val)

                if new_val is None and self.verbose:
                    print(
                        "NB: Action removed the value for key {k}.".format(k=key),
                        flush=True,
                    )

                setattr(input, key, new_val)
            else:
                """
                Here, there is no distinction between
                - an absent key (i.e. getattr(input, key, None) is None)
                - a key with value None

                Both are interpreted as "this attribute does not exist". Therefore,
                since an action represents a transformation of an attribute, no action
                is executed.
                """
                pass
        return

    def add_action(
        self, action: Callable | str = None, key: str | None = None, **kwargs
    ):
        if key is None:
            key = self.active_key

        if isinstance(action, str):
            if action in self.callables:
                action = self.callables.get(action)
            else:
                raise ValueError("Did not recognize action {a}".format(a=action))
        elif isinstance(action, Callable):
            action = action
        else:
            raise ValueError("Action needs to be string or callable.")

        # partially initialize function if desired
        if len(kwargs) > 0:
            action = partial(action, **kwargs)

        if self.actions.get(key, None) is not None:
            self.actions[key].append(action)
        else:
            self.actions[key] = [action]

        self.active_key = key
        return self
