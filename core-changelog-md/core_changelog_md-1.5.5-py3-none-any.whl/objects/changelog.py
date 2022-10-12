import datetime
import re
from typing import Optional

import packaging.version

from core_changelog_md.common.enums import ChangeTypes
from core_changelog_md.common.exceptions import UnCorrectTitleException, \
    MissedVersionsSymbolException, VersionOverTextException, NotDetectVersionException, VersionDateConvertException, \
    UnDetectLine, MissChangeBlock, UnKnownVersionAppendText
from core_changelog_md.exceptions import VersionNotFoundException
from core_changelog_md.objects.changes import ChangeCollection, ChangeBlock
from core_changelog_md.objects.version import VersionCollection, VersionBlock


class Changelog(object):
    RE_VERSION_RAW_BLOCK = re.compile(r'##[^#]?(\[.+\]?.+$)', flags=re.MULTILINE)
    RE_CHANGELOG_NAME = re.compile(r'^#[^#]\s*?(.+)[\s]*$', flags=re.MULTILINE)

    def __init__(self, name='CHANGELOG', path=None):
        self.name: str = name
        self.path: Optional[str] = path
        self.versions: VersionCollection[VersionBlock] = VersionCollection()

    @property
    def unreleased(self) -> VersionBlock:
        """
        Возвращает версию с нерелизными изменениями
        """
        return self.versions.get_by_name("unreleased") if 'unreleased' in self.versions.names() else None

    @staticmethod
    def check_version_date(version_name: str) -> Optional[datetime.datetime]:
        """
        Возвращает дату версии в формате YYYY.MM.DD
        """
        _version_name = version_name.replace(" ", "")
        if '-' not in _version_name and len([item for item in _version_name.split("]") if item.strip()]) != 1:
            raise VersionOverTextException()

        if ']-' not in _version_name and len([item for item in _version_name.split("]") if item.strip()]) != 1:
            try:
                return datetime.datetime.strptime(_version_name.split(']', maxsplit=1)[-1].strip(), "%Y-%m-%d")
            except Exception as e:
                raise VersionOverTextException()

        if "-" not in _version_name:
            return None

        try:
            return datetime.datetime.strptime(_version_name.split('-', maxsplit=1)[-1].strip(), "%Y-%m-%d")
        except Exception as e:
            raise VersionDateConvertException(
                f'Cant detect version date in {_version_name}. Date format must be XXXX-XX-XX')

    @staticmethod
    def check_version_name(version_name: str) -> (str, bool):
        """
        Возвращает имя версии
        """
        is_prerelease = False
        _version_name = version_name.replace(" ", "")
        if not _version_name.startswith("##") or \
                _version_name.startswith("##") and _version_name.startswith("###") or \
                "[" not in _version_name or "]" not in _version_name:
            raise MissedVersionsSymbolException(
                f'Version title must be "## [x.x.x]" or "## [version_name]"\nActual" {_version_name}')

        if not _version_name.replace(" ", '').startswith('##['):
            raise MissedVersionsSymbolException(
                f'Version title must be "## [x.x.x]" or "## [version_name]"\nActual" {_version_name}')

        if '[unreleased]' in _version_name.lower():
            version = 'unreleased'
        else:
            versions = VersionBlock.RE_NUM_VERSION_BLOCK.findall(_version_name)
            version = versions[0] if len(versions) == 1 else None
        if not version:
            is_prerelease = True
            versions = VersionBlock.RE_NUM_RC_VERSION_BLOCK.findall(_version_name)
            version = versions[0] if len(versions) == 1 else None
            version = version.replace('.rc', 'rc')
        if version:
            return version, is_prerelease
        raise NotDetectVersionException(f"Cant detect version name from '{_version_name}'")

    @staticmethod
    def check_name(name_block: str) -> str:
        """
        Возвращает имя ChangeLog
        """
        _name_block = name_block.replace(" ", '')
        if not _name_block.startswith("#") or _name_block.startswith("#") and _name_block.startswith("##"):
            raise UnCorrectTitleException()
        return name_block.replace("#", "").strip()

    @classmethod
    def from_file(cls, path):
        obj = Changelog.from_str(data_string=open(path, 'r', encoding='UTF8').read(), file_path=path)
        obj.path = path
        return obj

    @classmethod
    def from_str(cls, data_string: str, file_path: str = None):
        """
        Преобразование текста changelog в объект
        """

        # Первая строчка должна быть именем
        clean_data = [item.strip() for item in data_string.replace("---", '').split('\n')]
        obj = cls(name=Changelog.check_name(clean_data[0]))
        clean_data = clean_data[1:]

        # Разбиваем на версии
        for index, item in enumerate(clean_data):
            # Пропускаем пустые строчки
            if not item.strip():
                continue
            # Старт обработки новой версии
            elif item.strip().startswith("##") and not item.strip().startswith("###"):
                version_name, is_prerelease = Changelog.check_version_name(version_name=item)
                version_obj = VersionBlock(
                    version=version_name,
                    date=Changelog.check_version_date(version_name=item),
                    change_collection=ChangeCollection()
                )
                if is_prerelease:
                    if not version_obj.version.is_prerelease:
                        name = version_obj.version.base_version
                        raise UnKnownVersionAppendText(f'Find unknown text in version "{name}" Only "rc" supported!')
                obj.versions.append(version_obj)
                change_tag = None
                continue
            # Старт обработки нового change-tag
            elif item.strip().startswith("###"):
                change_tag = ChangeTypes.get_by_tag(tag=item.replace("#", '').strip())
                obj.versions.get_by_name(version_name=version_name) \
                    .change_blocks[change_tag] = ChangeBlock(change_type=change_tag)
                continue
            elif item.strip().startswith("-"):
                if change_tag is None:
                    raise MissChangeBlock(f'Changes before declared ChangeBlock in line {index + 2}')
                obj.versions.get_by_name(version_name=version_name) \
                    .change_blocks[change_tag].changes.append(item.strip()[1:].strip())
            else:
                raise UnDetectLine(
                    f'Cant detect line "{item}" in line {index + 2}\n'
                    f'Version must started by ##\n'
                    f'ChangeBlock must started by #\n'
                    f'Changes must started by "-"'
                )
        return obj

    @property
    def current_version(self) -> VersionBlock:
        """
        Возвращает текущую версию Changelog
        """
        versions = \
            list(self.versions)[1:] if self.versions[0].version.base_version == 'unreleased' else list(self.versions)
        version_list = [item for item in versions if not item.version.is_prerelease]
        return self.unreleased if len(version_list) == 0 else max(version_list)

    @property
    def next_version(self) -> str:
        """
        Возвращает строковый идентификатор возможной следующей версии
        """
        if self.unreleased is None:
            return '0.0.0'

        a = self.unreleased.get_priority()
        if a is None:
            return '0.0.0'

        v = self.current_version.version if self.current_version.version.__class__.__name__ != "LegacyVersion" else \
            packaging.version.parse('0.0.0')

        if a == 0:
            return f'{v.major}.{v.minor + 1}.0'
        else:
            return f'{v.major}.{v.minor}.{v.micro + 1}'

    @property
    def has_unreleased_changes(self):
        """
        Возвращает True если в секции unreleased есть changes
        """
        if self.unreleased:
            if len(self.unreleased.change_blocks):
                for item in self.unreleased.change_blocks:
                    if len(self.unreleased.change_blocks[item].changes) > 0:
                        return True
        return False

    def save(self, path: str = None, add_unreleased: bool = False):
        """
        Сохраняет changelog в файл. Если указан путь то по нему, если нет - то по адресу открытия
        :param path: Путь для нового сохранения
        :param add_unreleased" добавление пустой версии UNRELEASED
        """
        path = path if path else self.path
        if path:
            with open(path, 'w', encoding='UTF8') as fp:
                fp.write(self.text(add_unreleased=add_unreleased))

    def text(self, add_unreleased=True):
        """
        Возвращает текстовое представление changelog
        """
        result = f'#{self.name.upper()}\n'
        result += self.versions.text(add_unreleased=add_unreleased)
        return result.strip() + '\n'

    def sync(self, other: "Changelog"):
        difference = self.difference(other)

        for version in difference:
            if version not in self.versions:
                self.versions.append(difference.get_by_name(version_name=version))

        try:
            unreleased = difference.get_by_name(version_name="unreleased")
        except VersionNotFoundException:
            return self

        for change_type in unreleased.change_blocks:
            if change_type not in self.unreleased.change_blocks:
                self.unreleased.change_blocks[change_type] = unreleased.change_blocks[change_type]
                continue
            for change in unreleased.change_blocks[change_type].changes:
                if change not in self.unreleased.change_blocks[change_type].changes:
                    self.unreleased.change_blocks[change_type].changes.append(change)
        return self

    def difference(self, other: "Changelog", revert: bool = False) -> VersionCollection:
        res = VersionCollection()

        this_changelog = other if revert else self
        other_changelog = self if revert else other

        for version in other_changelog.versions:
            if version not in this_changelog.versions:
                res.append(version)

        unreleased = VersionBlock(version="unreleased")
        if unreleased not in res:
            released_version_diff = []
            for released_version in res:
                for change_block in released_version.change_blocks:
                    released_version_diff.extend(released_version.change_blocks[change_block].changes)

            if other_changelog.unreleased:
                for change_type in other_changelog.unreleased.change_blocks:
                    if change_type not in this_changelog.unreleased.change_blocks:
                        unreleased.change_blocks[change_type] = other_changelog.unreleased.change_blocks[change_type]
                        continue
                    for change in other_changelog.unreleased.change_blocks[change_type].changes:
                        if change not in this_changelog.unreleased.change_blocks[change_type].changes:
                            if change_type not in unreleased.change_blocks:
                                unreleased.change_blocks[change_type] = ChangeBlock(change_type=change_type)
                            unreleased.change_blocks[change_type].changes.append(change)
            res.append(unreleased)
        return res
