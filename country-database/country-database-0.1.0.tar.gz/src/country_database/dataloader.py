from dataclasses import dataclass
from pathlib import Path
from typing import ClassVar
from typing import Optional


@dataclass(frozen=True)
class CountryCode:
    alpha2_code: str
    alpha3_code: str
    numeric_code: str


class DataLoader:
    DEFAULT_DATA_DIR: ClassVar[Path] = Path(__file__).parent / "database"

    class OverrideLevel:
        """
        Override level for merging databases.

        {
            field_name: {
                locale: { // <-- LOCALE level
                    country_code: value // ITEM level
                }
            }
        }
        """

        ITEM = 0
        LOCALE = 1

    def __init__(self, data_dir: Path = DEFAULT_DATA_DIR) -> None:
        self.databases = []  # [ (Path, OverrideLevel) ]
        self.countries = {}  # { code: CountryCode }
        self.dat = {}  # { field_name: { locale: { alpha3_code: value } } }
        self.reload_callbacks = []
        self.merge_database(data_dir, reload=False)

    def merge_database(
        self,
        data_dir: Path,
        override_level: OverrideLevel = OverrideLevel.ITEM,
        reload=True,
    ) -> None:
        """
        Merge a new database into the data loader.

        Raises:
            ValueError: if the database is already loaded or the database is invalid.
        """
        if any(x[0] == data_dir for x in self.databases):
            raise ValueError(f"Database {data_dir} already loaded")
        self.__load_database(data_dir, override_level)
        if reload is True:
            self.__reload()

    def register_reload_callback(self, callback: callable) -> None:
        """Register a callback to be called when the database is reloaded."""
        self.reload_callbacks.append(callback)

    def lookup(self, country_code: str, name: str, locale: str = "en") -> Optional[str]:
        """Lookup a country property value from the database.

        Args:
            country_code: alpha-3 code of the country.
            name: name of the property.
            locale: locale code, e.g. "en", "de", "fr", etc.

        Returns:
            The value of the property, or None if not found.
        """
        return self.dat.get(name, {}).get(locale, {}).get(country_code)

    def lookup_country_code(self, fuzzy_code: str) -> Optional["CountryCode"]:
        """Lookup country code by fuzzy_code.

        Args:
            fuzzy_code: can be alpha-3 code, alpha-2 code, or numeric code.

        Returns:
            The country code, or None if not found.
        """
        return self.countries.get(fuzzy_code)

    def __reload(self) -> None:
        for callback in self.reload_callbacks:
            callback()

    def __load_database(self, data_dir: Path, override_level: OverrideLevel) -> None:
        if not self.countries:
            self.__load_country_codes()  # only load countries once
        files = self.__build_data_file_index(data_dir)
        for field_name, locale_files in files.items():
            for locale, file in locale_files.items():
                self.__load_data_file(field_name, locale, file, override_level)
        self.databases.append((data_dir, override_level))

    def __load_country_codes(self) -> None:
        """Load codes.tsv from the default database."""
        with open(self.DEFAULT_DATA_DIR / "codes.tsv") as f:
            for line in f:
                alpha2_code, alpha3_code, numeric_code = line.strip().split("\t")
                code = CountryCode(
                    alpha2_code=alpha2_code,
                    alpha3_code=alpha3_code,
                    numeric_code=numeric_code,
                )
                self.countries[alpha2_code] = code
                self.countries[alpha3_code] = code
                self.countries[numeric_code] = code

    def __build_data_file_index(self, data_dir: Path) -> dict:
        files = {}  # { field_name: { locale: file } }
        for file in data_dir.glob("*/*.tsv"):
            if not file.is_file():
                raise ValueError(f"File {file} is not a file")
            relative = file.relative_to(
                data_dir
            )  # e.g. "name/en.tsv", "capital/zh.tsv", etc.
            field_name = relative.parent.name  # e.g. "name", "capital", etc.
            locale = relative.stem  # e.g. "en", "zh", etc.
            if field_name not in files:
                files[field_name] = {}
            files[field_name][locale] = file
        return files

    def __load_data_file(
        self, field_name: str, locale: str, file: Path, override_level: OverrideLevel
    ) -> None:
        if field_name not in self.dat:
            self.dat[field_name] = {}

        if (
            locale not in self.dat[field_name]
            or override_level == self.OverrideLevel.LOCALE
        ):
            self.dat[field_name][locale] = {}

        with open(file) as f:
            for line in f:
                alpha3_code, value = line.strip().split("\t")
                self.dat[field_name][locale][alpha3_code] = value


# the builtin dataloader with the default database loaded
default_dataloader = DataLoader()
