# -*- coding: utf-8 -*-
"""
Created on Wed May 11 08:37:49 2022

@author: Antonio Bulgheroni (antonio.bulgheroni@ec.europa.eu)


"""
#  Copyright (c) 2022.  Antonio Bulgheroni.
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
#  documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
#  rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
#  permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
#  Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
#  WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
#  OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
#  OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
#   documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
#   rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
#   permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#
#
#
#
#
from __future__ import annotations

import configparser
import logging
import os
import random
import re
from collections import UserDict, UserList
from datetime import datetime
# TODO: remove os.path and replace it with pathlib Path
from os.path import exists
from pathlib import Path
from typing import Any

import elog
import markdown
import urllib3
import yaml
from elog.logbook_exceptions import LogbookError
from tenacity import after_log, retry, retry_if_exception_type, stop_after_attempt, wait_fixed

# TODO: remove this try/except block as soon as the new release of elog will be available.
#       When it will be available just add LogbookServerTimeout after the LogbookError here above.
try:
    from elog.logbook_exceptions import LogbookServerTimeout

    is_elog_patched = True
except ImportError:
    is_elog_patched = False

    class LogbookServerTimeout(LogbookError):
        """
        Redefine LogbookServer Timeout.

        This exception is used if and only if the elog version being used has not been patched.
        """
        pass

from PIL import Image
from PyQt5 import QtCore
from yattag import Doc, indent

from autologbook import autoconfig, autoerror, autotools
from autologbook.autotools import (
    DateType,
    ElementType,
    PictureType,
    ResolutionSource,
    ResolutionUnit,
    pretty_fmt_physical_quantity,
)

urllib3.disable_warnings()
Signal = QtCore.pyqtSignal
Slot = QtCore.pyqtSlot
log = logging.getLogger('__main__')

# TODO: remove this if statement with its messages as soon as the py_elog fork will be merged.
if not is_elog_patched:
    log.error('Attention: the py_elog package version that you are using doesn\'t support timeouts.')
    log.error('Consider using the patched version available at https://github.com/abulgher/py_elog/tree/timeout')


class SignalDispatcher(QtCore.QObject):
    """
    Signal Dispatcher class.

    A helper class to implement the Qt Signal / Slot mechanism for non Qt derived
    object.

    """

    added_element = Signal(ElementType, str, str, name='added_element')
    removed_element = Signal(ElementType, str, str, name='removed_element')
    reset_content = Signal(name='reset_content')


class ResettableList(UserList):
    """
    A subclass of UserList to contain protocol items that could be reset.
    """

    def __init__(self, initialdata=None):
        super().__init__(initialdata)

    def is_empty(self) -> bool:
        """
        Check if the list is empty.

        Returns
        -------
        bool:
            True if the list is empty.
        """
        return True if len(self.data) == 0 else False


class ResettableDict(UserDict):
    """A dictionary with a reset flag."""

    def __init__(self, initialdata=None):
        super().__init__(initialdata)

    def is_empty(self) -> bool:
        """Check if the dictionary is empty."""
        return True if len(self.data) == 0 else False


class HTMLObject:
    """
    Subclass of Object just able to generate HTML code.

    it contains only the three **variable** of the yattag package.

    """

    # the yattag for HTML code generation
    doc, tag, text, line = Doc().ttl()

    @staticmethod
    def convert_path_to_uri(path: str | Path) -> str:
        """
        Convert a path to a URI.

        This utility takes an input path and it manipulates it in order to obtain
        a valid URL.

        First it removes the IMAGE_SERVER_BASE_PATH and replaces it with the
        IMAGE_SERVER_ROOT_URL (both values are taken from the autoconfig constants)
        and then it replaces all back-slashes with normal slashes.

        Parameters
        ----------
        path : Path-like object or string
            The input path to be converted.

        Returns
        -------
        url : URL
            The URL generated by the conversion.

        """
        if isinstance(path, Path):
            path = str(path)

        return path.replace(str(autoconfig.IMAGE_SERVER_BASE_PATH), str(
            autoconfig.IMAGE_SERVER_ROOT_URL)).replace('\\', '/')

    def print_html(self, indentation: bool = True) -> str:
        """
        Print the HTML content.

        Parameters
        ----------
        indentation : BOOL, optional
            Set to True to have indentation in the output (good for humans)
            Set to False for a plain and compact out (good for file).

        Returns
        -------
        Return a string of HTML

        """
        if indentation:
            return indent(self.doc.getvalue(), indentation='\t',
                          newline='\r\n', indent_text=True)
        else:
            return self.doc.getvalue()

    def save_html_to_file(self, filename: str | Path, indentation: bool = False):
        """
        Save th HTML to a file.

        Parameters
        ----------
        filename : str | Path
            The target file name
        indentation : bool, optional
            Set to True to have indentation in the output (good for humans)
            Set to False for a plain and compact out (good for file).

        Returns
        -------
        None.

        """
        log.debug('Saving HTML to file %s' % filename)
        with open(filename, 'w', encoding='utf-8') as fp:
            fp.write(self.print_html(indentation))

    @classmethod
    def reset_html_content(cls):
        """
        Reset the HTML Content of the YATTAG doc.

        Returns
        -------
        None.

        """
        log.debug('Resetting the HTML Content')
        cls.doc, cls.tag, cls.text, cls.line = Doc().ttl()

    def get_resettable_containers(self) -> list[(ResettableDict | ResettableList)]:
        """
        Get all resettable containers.

        This method is returning a list of all resettable containers.

        Returns
        -------

        """
        res_list = []
        for resettable_element in dir(self):
            attribute = self.__getattribute__(resettable_element)
            if isinstance(attribute, (ResettableDict, ResettableList)):
                res_list.append(attribute)
        return res_list


class MicroscopePicture(HTMLObject):
    """
    The basic microscope picture class.

    This is actually a pure virtual class that need to be implemented for each microscope type.

    This basic class has an empty dictionary of parameters

    """

    # a class level list of all used ids
    _used_ids = list()

    # the next custom id to be used
    _next_to_use_id = autoconfig.CUSTOMID_START

    @staticmethod
    def _reset_ids():
        """
        Reset the used ids list (static method).

        Returns
        -------
        None.

        """
        MicroscopePicture._used_ids = []
        MicroscopePicture._next_to_use_id = autoconfig.CUSTOMID_START

    def __init__(self, path: Path | str = None, pic_type: PictureType = None, png_generation: bool = True):
        """
        Construct a microscope picture.

        Parameters
        ----------
        path : str | path-like opject, optional
            The path to the image.

        pic_type : PictureType
            It corresponds to the type of image / microscope

        Returns
        -------
        None.

        """
        # initialize all the parameters dictionary
        self.params = dict()

        if pic_type is None:
            self.params['pic_type'] = PictureType.GENERIC_MICROSCOPE_PICTURE
        else:
            self.params['pic_type'] = pic_type
        if path is not None:
            if os.path.exists(path):
                # TODO: replace all those paths with path-objects.
                self.params['path'] = path
                self.params['key'] = str(self.params.get('path'))
                self.params['fileName'] = os.path.split(path)[-1]
                self.params['fileExt'] = os.path.splitext(
                    os.path.split(path)[-1])[1]
                self.params['id'] = ''
                log.info('Created a new MicroscopePicture (%s)' %
                         self.params['fileName'])
                if png_generation:
                    self.params['thumbfile'] = self.generate_png(autoconfig.IMAGE_SAMPLE_THUMB_MAX_WIDTH, 'thumb-png',
                                                                 force_regen=False)
                    self.params['pngfile'] = self.generate_png(0, 'png', force_regen=False)
            else:
                raise FileNotFoundError(f'{path} not found')
        else:
            log.warning('Created a new MicroscopePicture without path')

    def __repr__(self) -> str:
        """
        Return the representation of a MicroscopePicture.

        Returns
        -------
        msg, str
            The representation of a MicroscopePicture.

        """
        return f'{self.__class__.__name__}(path=\"{self.params["path"]}\",pic_type={self.params["pic_type"]})'

    def __str__(self) -> str:
        """
        Print out the most relevant info of a MicroscopePicture.

        Returns
        -------
        msg : str
            The representation of a MicroscopePicture.

        """
        msg = 'Microscope Image with the following parameters\n'
        for key in self.params:
            msg += f'  - {key}: {self.params[key]}\n'
        return msg

    @staticmethod
    def _is_id_taken(pic_id: int) -> bool:
        """
        Check if an ID has been used already.

        Parameters
        ----------
        pic_id : int
            Identification number to be checked.

        Returns
        -------
        bool
            Return True if it is already used or
            False if the ID is good to be used.

        """
        if pic_id in MicroscopePicture._used_ids:
            return True
        return False

    def _get_id(self, pattern: str, tifftagcode: int | None = None):
        """
        Get a valid and unique MicroscopePicture ID.

        This method is retrieving a unique MicroscopePicture ID for the newly
        added image.

        It is getting an ID from the filename using a regular expression with
        the provided pattern and compare it with the ID stored in the TIFF file
        with the TIFF tag pointed by tifftagcode.

        Four different scenarios can happen:
            1. No valid ID is available in neither the filename nor in the TIFF
               tag. Then a valid one is internally generated and saved in the
               TIFF Tag for further use
            2. The ID from the filename is valid while the one from the TIFF tag
               is either empty or invalid. The one from the filename is accepted
               and saved to the TIFF tag for further use.
            3. The ID from the TIFF tag is good, but not the one from the
               filename. Just keep on using the one from TIFF tag.
            4. Both IDs are good. Then we take the one from the TIFF tag.

        Parameters
        ----------
        pattern : string
            Regular expression patter to identify the ID.
            See _get_id_from_filename for more details.
        tifftagcode : int, optional
            The code of the TIFF tag where the ID is located.
            If none, then the default value stored in autoconfig.CUSTOMID_TIFFCODE
            is used. The default is None.

        Returns
        -------
        None.

        """
        filename_id = self._get_id_from_filename(pattern)
        tifftag_id = self._get_id_from_tifftag(tifftagcode)
        need_file_flashing = False

        # Case 1
        if filename_id is None and tifftag_id is None:
            # it was not possible to get the ID neither from the filename
            # nor from the tifftag.
            # we need a fresh unique one

            good_id = self._get_unique_ID()
            need_file_flashing = True

        # Case 2
        elif filename_id is not None and tifftag_id is None:
            # we got an id from the filename but none from the tifftag.
            # for the sake of clarity write it to the file

            good_id = filename_id
            need_file_flashing = True

        # Case 3
        elif filename_id is None and tifftag_id is not None:
            # we got an id from the tifftag, but none from the filename
            # we can only take the one from the tifftag
            good_id = tifftag_id

        # Case 4
        else:  # if filename_id is not None and tifftag_id is not None:
            # we got id from both sources.
            # we will ignore the filename_id and consider the tifftag_id
            # valid
            good_id = tifftag_id

        self.params['id'] = good_id
        MicroscopePicture._used_ids.append(good_id)
        if need_file_flashing:
            self._write_id_in_file(ID=good_id, tifftagcode=tifftagcode)

    def _get_id_from_filename(self, pattern: str):
        r"""
        Try to get the ID from the filename using regular expression.

        This method must be always called by _get_id and will try to get a valid
        ID from the filename. To do so, it uses a regular expression pattern with
        a group named ID.

        For example this is a valid pattern: '^(?P<ID>[0-9]+)[\\w\\W]*$'.

        If a valid unique ID is found, it is returned for further use.
        None is returned if the pattern matching could not find any ID or
        if the matched ID is already in use.

        Parameters
        ----------
        pattern : str
            Regular expression pattern with a group named ID.
            An example is '^(?P<ID>[0-9]+)[\\w\\W]*$'

        Returns
        -------
        int or None
            The ID retrieved from the filename.
            If no ID is found or if it is already in use, None is returned

        """
        match = re.search(pattern, self.params['fileName'])
        if match:
            if MicroscopePicture._is_id_taken(int(match.group('ID'))):
                log.debug('ID %s taken from filename but already in use' %
                          match.group('ID'))
                return None
            else:
                return int(match.group('ID'))

    def _get_id_from_tifftag(self, tifftagcode: int = None):
        """
        Try to get the ID from the TIFF tag in the file.

        This method will try to get the picture ID from a TIFF tag stored in
        the TIFF file at position tifftagcode.

        If there is an ID at the indicated position and this is unique, then
        it is returned. Otherwise, None is returned.

        Parameters
        ----------
        tifftagcode : int, optional
            The code of the TIFF Tag where the ID is stored.
            If None, then the system level constant autoconfig.CUSTOMID_TIFFCODE
            is used.
            The default is None.

        Returns
        -------
        int or None
            The ID retrieved from the TIFF Tag.
            If no ID is found or if it is already in use, None is returned

        """
        if tifftagcode is None:
            tifftagcode = autoconfig.CUSTOMID_TIFFCODE
        with Image.open(self.get_parameter('path')) as img:
            tiffinfo = img.tag_v2
            if tifftagcode in tiffinfo:
                try:
                    if MicroscopePicture._is_id_taken(int(tiffinfo[tifftagcode])):
                        log.warning('ID %s taken from TIFF tag already in use.'
                                    % int(tiffinfo[tifftagcode]))
                        log.warning('Removing TIFF tag from MicroscopePicture %s because of conflicts'
                                    % self.params['fileName'])
                        self._write_id_in_file(reset=True)
                        log.warning(
                            'Possible wrong assignments of HTML customization in the protocol')
                        return None
                    else:
                        return int(tiffinfo[tifftagcode])
                except ValueError:
                    log.warning(
                        'The content of the TIFF tag cannot be converted in a valid ID.')
                    log.warning('Resetting the TIFF tag')
                    self._write_id_in_file(reset=True)
                    return None
            else:
                return None

    @staticmethod
    def _get_unique_ID() -> int:
        """
        Obtain an internally generated unique ID.

        This is the last chance for the ID generation. If all other attempts
        are failing, then an internally generated ID is assigned.

        Returns
        -------
        Int
            A valid ID for the MicroscopePicture

        """
        while MicroscopePicture._is_id_taken(
                MicroscopePicture._next_to_use_id
        ):
            MicroscopePicture._next_to_use_id += 1
        return MicroscopePicture._next_to_use_id

    # noinspection PyPep8Naming
    def _write_id_in_file(self, ID: int = None, tifftagcode: int = None, reset: bool = False):
        """
        Write/Update/Reset the ID in the TIFF Tag code with picture ID.

        This is the swiss army knife of the TIFF Tag picture ID.
        Using the PIL package it is opening the TIFF file, retrieving the
        tiffinfo dictionary with all the tags and writing/updating or
        resetting its value.
        The modified tiffinfo is saved to the original file.

        Parameters
        ----------
        ID : int, optional
            The id to be written to the TIFF file.
            If it is None, then the id stored in the MicroscopePicture is used.
            The default is None.
        tifftagcode : int, optional
            The code of the TIFF tag where the id has to be written.
            If None, then the system default autoconfig.CUSTOMID_TIFFCODE is used.
            The default is None.
        reset : bool, optional
            A boolean control to force the reset of the TIFF Tag.
            When True, instead of writing the id, an empty string is stored into
            the file.
            The default is False.

        Raises
        ------
        OSError
            Raised if the MicroscopePicture has no path defined. In this way
            the TIFF file cannot be opened.
        AttributeError
            Raised if id is None and the id in the MicroscopePicture parameter
            dictionary is not set.

        Returns
        -------
        None.

        """
        if self.params['path'] is None:
            raise OSError('Picture path not provided')

        if reset:
            write_id = ''
        else:
            if ID is None:
                if self.params['id'] is None:
                    raise AttributeError(
                        'Something went wrong with picture ID assignment')
                else:
                    write_id = self.params['id']
            else:
                write_id = ID

        if tifftagcode is None:
            tifftagcode = autoconfig.CUSTOMID_TIFFCODE

        if isinstance(self.params['path'], Path):
            img_path = self.params['path']
        else:
            img_path = Path(self.params['path'])

        with Image.open(img_path) as img:
            tiffinfo = img.tag_v2
            # this tag should not be existing, but check just in case
            if tifftagcode in tiffinfo:
                # this is unexpected
                # inform the user that the tag will be overwritten and lost
                log.warning('Microscope picture %s has already ID tag (%s).'
                            % (self.params['fileName'], tiffinfo[tifftagcode]))
                log.warning('It will be overwritten!')

            # add or modify with the id number
            tiffinfo[tifftagcode] = str(write_id)
            img.save(img_path, tiffinfo=tiffinfo)
        log.debug('ID stored in the TIFF tag for further use')

    # noinspection PyPep8Naming
    def getID(self) -> int:
        """
        Return the ID of the Microscope Picture.

        Returns
        -------
        ID
            The microscope picture ID.

        """
        return self.params['id']

    def get_pic_type(self) -> PictureType:
        """
        Return the picture type.

        Returns
        -------
        pic_type : PictureType
            The type of picture.

        """
        return self.params['pic_type']

    def get_parameters(self) -> dict[Any]:
        """
        Return the picture parameter dictionary.

        Returns
        -------
        The whole parameter dictionary

        """
        return self.params

    def get_parameter(self, par_name: str) -> Any:
        """
        Return a specific parameter from the dictionary if it exists, None if it is not existing.

        Parameters
        ----------
        par_name : String
            Parameter Name.

        Returns
        -------
        The value of the parameter or None if it is not existing

        """
        return self.params.get(par_name, None)

    def generate_png(self, max_width: int = 400, subfolder: str = 'png-thumb', force_regen: bool = False) -> str:
        """
        Generate a PNG version of a Microscope Picture.

        Parameters
        ----------
        max_width : int, optional
            The horizontal size of the png image.
            Set to 0 to disable the scaling.
            The default is 400.
        subfolder : str, optional
            A relative directory to the sample where the generated PNG should be stored.
            The default is 'png-thumb'.
        force_regen : bool, optional
            Force the regeneration of a PNG image even if it exists already.
            The default is False.

        Returns
        -------
        thumbfile : str
            The URI of the generated PNG file.

        """
        # save the file in a subfolder defined by subfolder
        # make the folder if it doesn't exist
        thumbpath = os.path.join(os.path.split(
            self.params['path'])[0], subfolder)
        if not os.path.exists(thumbpath):
            os.mkdir(thumbpath)
        thumbfilename = os.path.splitext(os.path.split(
            self.params['path'])[-1])[0] + '-{}.png'.format(subfolder)
        thumbfile = os.path.join(thumbpath, thumbfilename)

        # TODO: having these parameters set here is a bit confusing. Since the function is returning the path
        #       of the newly generated png file, we should assign the filename and the url outside the call.
        #       Have a look at all calls to this method and see if we can simply return a tuple (path, uri) and
        #       assign it outside.
        if max_width == 0:
            self.params['pngfilename'] = thumbfile
            self.params['pngurl'] = self.convert_path_to_uri(thumbfile)
        else:
            self.params['thumbfilename'] = thumbfile
            self.params['thumburl'] = self.convert_path_to_uri(thumbfile)

        if not force_regen and exists(thumbfile):
            log.debug('Skipping the generation of PNG for %s because already existing' %
                      self.params['fileName'])

        else:
            if max_width == 0:
                log.debug('Converting image %s in PNG format' %
                          self.params['fileName'])
            else:
                log.debug('Generating thumbnail of %s with max_width %s' % (
                    self.params['fileName'], max_width))
            with Image.open(self.params['path'], 'r') as image:
                w, h = image.size
                log.debug('Image size %s x %s' % (w, h))
                image = image.convert('RGB')
                if max_width > 0:
                    image.thumbnail(
                        (round(max_width), round(max_width * h / w)))
                image.save(thumbfile, format='PNG')

        thumbfile = self.convert_path_to_uri(thumbfile)
        thumbfile = thumbfile.replace('\\', '/')

        return thumbfile

    @property
    def key(self) -> str | None:
        return self.params.get('key', None)

    @key.setter
    def key(self, value) -> None:
        self.params['key'] = value

    def update(self):
        """
        Update Microscope Picture information.

        For the base class, this corresponds to regenerate the png files.
        """
        log.info('Updating microscope picture %s' % self.params['fileName'])
        self.params['pngfile'] = self.generate_png(0, 'png', force_regen=True)
        self.params['thumbfile'] = self.generate_png(autoconfig.IMAGE_SAMPLE_THUMB_MAX_WIDTH, 'thumb-png',
                                                     force_regen=True)


class FakePicture(MicroscopePicture):

    def __init__(self):
        # initialize all the parameters dictionary
        self.params = dict()
        self.params['pic_type'] = PictureType.GENERIC_MICROSCOPE_PICTURE
        self.params['path'] = f'{datetime.now():%Y%m%d%H%M%S%f}_{random.randint(0, 100)}'
        self.params['fileName'] = self.params['path']


class FEIPicture(MicroscopePicture):
    """
    The basic FEI pictures.

    All relevant parameters for the logbook are taken from the tiff tags and
    inserted in the parameter dictionary.

    """

    def __init__(self, path: str | Path | None = None, pic_type: PictureType = PictureType.FEI_MICROSCOPE_PICTURE,
                 png_generation: bool = True):
        super().__init__(path, pic_type, png_generation)
        if path is not None:
            try:
                self.get_tiff_file_tags()
                if autoconfig.FEI_AUTO_CALIBRATION:
                    self.calibrate()
                if autoconfig.FEI_DATABAR_REMOVAL:
                    self.crop_databar()
            except autoerror.NotFEIMicroscopePicture:
                log.error(
                    'Expected FEI Image, but could not find FEI metadata. Please double check saving format.')
                self.params['pic_type'] = PictureType.GENERIC_MICROSCOPE_PICTURE

    def calibrate(self):
        """
        Calibrate the FEI image.

        Resolution information stored in standard TIFF tags of FEI images are
        wrong. In order to have a direct calibration of the image while being
        open with ImageJ for example, the information provided in the FEI
        specific tag must be used.

        This method getting the picture resolution from the standard tags and
        comparing it with the one obtained with the FEI tags. If the two are
        different, then it means that this image was never calibrated before.
        Calibration information from FEI tags are moved to the standard tags.
        The picture file is updated and saved.

        If the two sets of resolution are the same, then there is no need to
        perform any calibration.

        Returns
        -------
        None.

        """
        if self.get_pic_type() not in [
            PictureType.FEI_MICROSCOPE_PICTURE,
            PictureType.VERSA_MICROSCOPE_PICTURE,
            PictureType.QUATTRO_MICROSCOPE_PICTURE
        ]:
            return

        log.debug('Calibrating %s' % self.params['fileName'])
        with Image.open(self.params['path']) as tif:

            tiff_tags = tif.tag_v2
            tif_res = autotools.get_picture_resolution(
                tiff_tags, ResolutionSource.TIFF_TAG, ResolutionUnit.CM)
            fei_res = autotools.get_picture_resolution(
                tiff_tags, ResolutionSource.FEI_TAG, ResolutionUnit.CM)
            if tif_res == fei_res:
                pass
            else:
                xres, yres, ures = fei_res.as_tuple()
                tif.save(self.params['path'], resolution_unit=ures, x_resolution=xres, y_resolution=yres,
                         tiffinfo=tiff_tags)

    def crop_databar(self, force_regen: bool = False):
        """
        Remove the databar from a FEI picture.

        FEI microscopes are saving a databar on the bottom part of the image
        containing user selected information.

        While this databar is generally very useful, it is not nice to see when
        the image is published on a scientific journal.

        This method allows to remove the databar saving the cropped image in
        a separated file in order to keep also the original.

        The cropped file is saved in the picture parameter:
            params['cropped_path'] with the full path including the filename
            params['cropped_url'] URL of the cropped image as it appears on the
                image server.

        Parameters
        ----------
        force_regen : bool, optional
            Force the regeneration of the cropped image even if it exists already.
            The default is False.

        Returns
        -------
        None.

        """
        if self.get_pic_type() not in [
            PictureType.FEI_MICROSCOPE_PICTURE,
            PictureType.VERSA_MICROSCOPE_PICTURE,
            PictureType.QUATTRO_MICROSCOPE_PICTURE
        ]:
            return

        # Check if the cropped file already exists.
        orig_path = Path(self.params['path'])
        crop_img_path = orig_path.parent / \
            Path('crop') / Path(str(orig_path.stem)
                                + '_crop' + str(orig_path.suffix))
        self.params['cropped_path'] = crop_img_path
        self.params['cropped_url'] = self.convert_path_to_uri(
            crop_img_path)
        if not crop_img_path.parent.exists():
            crop_img_path.parent.mkdir(parents=True, exist_ok=True)

        if not force_regen and crop_img_path.exists():
            log.debug(
                'Skipping generation of cropped image because it already exists')
            return

        log.debug('Generating a copy of %s with cropped databar' %
                  self.params['fileName'])
        self._remove_databar(orig_path, crop_img_path)

    def _remove_databar(self, input_file, output_file):

        with Image.open(input_file) as full_img:
            tiffinfo = full_img.tag_v2
            image_xsize, image_ysize = full_img.size

            fei_metadata = configparser.ConfigParser(allow_no_value=True)
            fei_metadata.read_string(tiffinfo[self.params['fei_tag_code']])

            scan_width = fei_metadata.getint('Image', 'ResolutionX')
            scan_height = fei_metadata.getint('Image', 'ResolutionY')

            if (image_xsize, image_ysize) != (scan_width, scan_height):
                crop_img = full_img.crop((0, 0, scan_width, scan_height))
                xside_code = 256
                yside_code = 257
                tiffinfo[xside_code] = scan_width
                tiffinfo[yside_code] = scan_height

                crop_img.save(output_file, tiffinfo=tiffinfo)

    def get_tiff_file_tags(self):
        """
        Get the TIFF file tags.

        Open the tiff file corresponding to the FEI picture using the PIL
        and get the fei_metadata dictionary.

        Relevant information for the logbook are transferred from the fei_metadata
        to the internal dictionary.

        The magnification is calculated starting from the display width and the
        horizontal field of view.

        Raises
        ------
        TypeError
            If the TIFF file is not a FEI image.

        Returns
        -------
        None.

        """
        path = self.params['path']

        with Image.open(path) as tif:

            tiff_tags = tif.tag_v2
            good_fei_tag_code = None
            for fei_tag_code in autotools.FEITagCodes:
                if fei_tag_code in tiff_tags:
                    good_fei_tag_code = fei_tag_code
                    break
            if good_fei_tag_code is None:
                raise autoerror.NotFEIMicroscopePicture
            else:
                self.params['fei_tag_code'] = good_fei_tag_code

            fei_metadata = configparser.ConfigParser(allow_no_value=True)
            fei_metadata.read_string(tiff_tags[good_fei_tag_code])

            # for HV add kV if > 1000
            self.params['hv'] = (
                fei_metadata.get('Beam', 'HV') + 'V',
                str(round(fei_metadata.getfloat('Beam', 'HV') / 1000)) + 'kV'
            )[fei_metadata.getfloat('Beam', 'HV') > 1000]

            self.params['beam'] = fei_metadata.get('Beam', 'Beam')
            self.params['hfw'] = fei_metadata.getfloat(
                self.params['beam'], 'HFW')
            self.params['dispwidth'] = fei_metadata.getfloat(
                'System', 'DisplayWidth')
            # for magnification there is a mystery 1.25 scale factor
            # add kx if > 1000
            self.params['magnification'] = (
                str(round(self.params['dispwidth']
                          / self.params['hfw'] / 1.25)) + 'x',
                str(round(self.params['dispwidth']
                          / self.params['hfw'] / 1.25 / 1000)) + 'kx'
            )[round(self.params['dispwidth'] / self.params['hfw'] / 1.25) > 1000]
            self.params['spotsize'] = fei_metadata.getfloat('Beam', 'Spot')
            try:
                self.params['beamcurrent'] = fei_metadata.getfloat(
                    self.params['beam'], 'beamcurrent')
            except ValueError:
                # in case of an image taken with switched off beam the current is an empty string.
                # causing the getfloat to fail.
                self.params['beamcurrent'] = 0
            self.params['detector'] = f"{fei_metadata.get('Detectors', 'Mode')}.{fei_metadata.get('Detectors', 'Name')}"
            self.params['vacuum'] = fei_metadata.get('Vacuum', 'UserMode')
            self.params['userText'] = fei_metadata.get('User', 'UserText')
            self.params['width'] = fei_metadata.getfloat(
                'Image', 'ResolutionX')
            self.params['height'] = fei_metadata.getfloat(
                'Image', 'ResolutionY')
            self.params['resolution'] = (fei_metadata.getfloat('Image', 'ResolutionX'),
                                         fei_metadata.getfloat('Image', 'ResolutionY'))
            self.params[
                'resolutionPrint'] = f"({fei_metadata['Image']['ResolutionX']} x {fei_metadata['Image']['ResolutionY']})"

        for key in self.params:
            log.debug('%s  --> %s' % (key, self.params[key]))

    def update(self):
        """
        Update the parameters of an FEI Microscope picture.

        This method is calling its super method and then update the tiff tags, calibration and databar removal.

        """
        super().update()
        try:
            self.get_tiff_file_tags()
            if autoconfig.FEI_AUTO_CALIBRATION:
                self.calibrate()
            if autoconfig.FEI_DATABAR_REMOVAL:
                self.crop_databar()
        except autoerror.NotFEIMicroscopePicture:
            log.error('Expected FEI Image, but could not find FEI metadata. Please double check saving format.')
            self.params['pic_type'] = PictureType.GENERIC_MICROSCOPE_PICTURE

    def generate_html_code(self, yaml_dict: dict):
        """
        Generate the HTML code corresponding to the FEI image.

        Parameters
        ----------
        yaml_dict : dict
            A dictionary containing the customized fields.

        Returns
        -------
        None.

        """
        log.debug('Generating HTML of picture %s ' %
                  self.get_parameter('FileName'))

        with self.tag('tr'):
            with self.tag('td', colspan=5, style='text-align:center;height:50px;background-color:cyan'):
                self.line('b', str(self.params['path']))
            with self.tag('td', style='text-align:center;height:50px;background-color:cyan'):
                self.line('a', 'PNG', href=self.params['pngurl'])
            with self.tag('td', style='text-align:center;height:50px;background-color:cyan'):
                if autoconfig.FEI_DATABAR_REMOVAL and self.params.get('cropped_url'):
                    with self.tag('a', href=self.convert_path_to_uri(self.params['path'])):
                        self.text('TIFF (full)')
                    self.text(' / ')
                    with self.tag('a', href=self.params['cropped_url']):
                        self.text('TIFF (no databar)')
                else:
                    self.line('a', 'TIFF', href=self.convert_path_to_uri(
                        self.params['path']))
        with self.tag('tr'):
            with self.tag('th', colspan=2, rowspan=2):
                with self.tag('figure', klass='image'):
                    with self.tag('a', href=self.params['pngurl']):
                        self.doc.stag('img', width=autoconfig.IMAGE_SAMPLE_THUMB_MAX_WIDTH - 10,
                                      alt=os.path.split(self.params['pngurl'])[-1], src=self.params['thumburl'])
                    caption = os.path.split(self.params['path'])[-1]
                    if 'Caption' in yaml_dict and yaml_dict['Caption']:
                        caption = yaml_dict['Caption']
                    self.line('figcaption', caption)
            with self.tag('td'):
                self.line('strong', 'ID: ')
                self.text(self.params.get('id', 'Unknown'))
            with self.tag('td'):
                self.line('strong', 'HV: ')
                self.text(self.params.get('hv', 'Unknown'))
            with self.tag('td'):
                self.line('strong', 'Beam: ')
                self.text(self.params.get('beam', 'Unknown'))
            with self.tag('td'):
                self.line('strong', 'Magnification: ')
                self.text(self.params.get('magnification', 'Unknown'))
            with self.tag('td'):
                self.line('strong', 'Resolution: ')
                self.text(self.params.get('resolutionPrint', 'Unknown'))
        with self.tag('tr'):
            with self.tag('td'):
                if self.params.get('beam', 'Unknown').lower() == 'ibeam':
                    self.line('strong', 'Beam current: ')
                    self.text(pretty_fmt_physical_quantity(
                        self.params.get('beamcurrent', 0), 'A'))
                else:
                    self.line('strong', 'Spot size: ')
                    self.text(self.params.get('spotsize', 'Unknown'))
            with self.tag('td'):
                self.line('strong', 'Detector: ')
                self.text(self.params.get('detector', 'Unknown'))
            with self.tag('td'):
                self.line('strong', 'Vacuum: ')
                self.text(self.params.get('vacuum', 'Unknown'))
            with self.tag('td'):
                self.line('strong', 'User text: ')
                self.text(self.params.get('userText', 'Unknown'))
            with self.tag('td'):
                self.line('strong', 'Filename: ')
                self.text(os.path.split(self.params['path'])[-1])

        subkey = 'Description'
        exkey = 'Extra'
        if subkey in yaml_dict:
            with self.tag('tr'):
                with self.tag('td', colspan=7):
                    self.doc.asis(markdown.markdown(yaml_dict[subkey]))
        if exkey in yaml_dict:
            if len(yaml_dict[exkey]) > 0:
                with self.tag('tr'):
                    with self.tag('td', colspan=7):
                        self.line('h3', 'Additional information')
                        self.line('p', yaml_dict[exkey])


class QuattroFEIPicture(FEIPicture):
    """
    Quattro Pictures, a subclass of FEI.

    Quattro images should be named according to this convention:

        id-samplename-someproperties.tif

    The name file is parsed against a regular expression and the picture id is stored
    in the parameters' dictionary.

    """

    filename_pattern = '^(?P<ID>[0-9]+)[\\w\\W]*$'

    def __init__(self, path: str | Path | None = None, pic_type: PictureType = PictureType.QUATTRO_MICROSCOPE_PICTURE,
                 png_generation: bool = True):
        super().__init__(path, pic_type, png_generation)
        if path is not None:
            self._get_id(self.filename_pattern)


class VersaFEIPicture(FEIPicture):
    """
    Versa Pictures, a subclass of FEI.

    Quattro images should be named according to this convention:

        samplename-someproperties_id.tif

    The name file is parsed against a regular expression and the picture id is stored
    in the parameters' dictionary.

    """

    # (?P<name>...)
    # sometext-000.tif
    # sometext_000.tif
    filename_pattern = '^[\\w\\W]*[-_](?P<ID>[0-9]+).[\\w\\W]*$'

    def __init__(self, path: str | Path | None = None, pic_type: PictureType = PictureType.VERSA_MICROSCOPE_PICTURE,
                 png_generation: bool = True):
        super().__init__(path, pic_type, png_generation)
        if path is not None:
            self._get_id(VersaFEIPicture.filename_pattern)


class Video(HTMLObject):
    """
    The basic class for a video clip.

    Video clips are rather common in microscopy analysis because they are very simple image sequence to show
    how a sample developed. For example in the case of a lamella preparation or of a pillar crashing.
    """

    def __init__(self, path: str | Path):
        """Generate a new Video with path"""
        # like for the MicrosocpePicture we use a dictionary to store all videos parameters.
        self.params = {}
        if isinstance(path, Path):
            self.params['key'] = str(path)
            self.params['path'] = path
        else:
            self.params['key'] = path
            self.params['path'] = Path(path)

        self.params['filename'] = self.get('path').name
        self.params['url'] = self.convert_path_to_uri(self.get('path'))
        self.params['ext'] = self.get('path').suffix
        self.get_video_info()

    def get(self, param: str) -> Any:
        """
        Return the value of a parameter.

        Parameters
        ----------
        param : str
            The name of the parameter to return

        Returns
        -------
        The value of the parameter or None if the parameter is not found.
        """
        return self.params.get(param, None)

    def set(self, param: str, value: Any):
        """
        Set the value of a parameter.

        Parameters
        ----------
        param : str
            The name of the parameter.
        value : Any
            The value of the parameter.
        """
        self.params[param] = value

    def get_video_info(self):
        """
        Retrieve video information from the file
        """
        if self.params['path'].exists():
            # get the information
            log.debug('Feature not completely implemented yet. For the moment it is not possible to get video '
                      'specific metadata')
            self.params['stat'] = self.get('path').stat()
            self.params['size'] = self.get('stat').st_size

    @property
    def key(self) -> str:
        """
        Get the video key to be used for the dictionary.

        Returns
        -------
        key: str
            The video key to be used for the dictionary
        """
        return self.get('key')

    @key.setter
    def key(self, value: Any):
        self.set('key', value)

    def generate_html_code(self, yaml_dict: dict):
        """
        Generate the HTML code corresponding to the video.

        Parameters
        ----------
        yaml_dict: dict
            A dictionary containing the customized fields

        Returns
        -------
        None.
        """
        with self.tag('tr'):
            with self.tag('td', colspan=3, style='text-align:center;height:50px;background-color:cyan'):
                self.line('b', f'{self.get("path")}')
            with self.tag('td', style='text-align:center;height:50px;background-color:cyan'):
                self.line('a', 'Download', href=self.get('url'))
        with self.tag('tr'):
            with self.tag('td'):
                with self.tag('iframe', allowfullscreen='True', frameborder='0', width='640', height='480',
                              scrolling='False', src=self.get('url')):
                    pass
                if 'Caption' in yaml_dict and yaml_dict.get('Caption', ''):
                    self.doc.stag('br')
                    self.line(
                        'p', yaml_dict['Caption'], style='text-align:center;font-weight:bold')
            with self.tag('td'):
                self.line('strong', 'Filename: ')
                self.text(self.get('filename'))
            with self.tag('td'):
                self.line('strong', 'Creation date: ')
                self.text(
                    f'{autotools.get_date_from_file(self.get("stat"), DateType.CTIME):%Y%m%d-%H:%M:%S}')
            with self.tag('td'):
                self.line('strong', 'File size: ')
                self.text(autotools.pretty_fmt_filesize(self.get('size')))
        subkey = 'Description'
        exkey = 'Extra'
        if subkey in yaml_dict and yaml_dict.get(subkey, ''):
            with self.tag('tr'):
                with self.tag('td', colspan=4):
                    self.doc.asis(markdown.markdown(yaml_dict.get(subkey)))
        if exkey in yaml_dict and yaml_dict.get(exkey, ''):
            with self.tag('tr'):
                with self.tag('td', colspan=4):
                    self.line('h3', 'Additional information')
                    self.line('p', yaml_dict.get(exkey))

    def update(self):
        """Update element after a file modification."""
        log.info('Updating video %s' % self.get('filename'))
        self.get_video_info()


class Sample(HTMLObject):
    """
    The basic class for sample analysis.

    It contains a list of MicroscopePictures

    """

    def __init__(self, full_name: str):
        # This is the full name, meaning that the whole hierarchy up to the top
        # level is listed.
        #
        # Something like Sample1/SubSample1.2/ThisSubSample
        self.full_name = full_name

        # For sake of simplicity
        self.last_name = self.full_name.split('/')[-1]

        # The full_name contains the whole hierarchy, so actually the parent is
        # already know.
        #
        # According to the full_name, the parent should be
        # '/'.join(self.full_name.split('/')[:-1])
        self.parent = '/'.join(self.full_name.split('/')[:-1])
        if self.parent == '':
            self.parent = None

        # signal dispatcher
        self.signal_dispatcher = SignalDispatcher()

        # a list of subsamples
        # please use full_names!
        self.subsamples = ResettableList()

        # self.images is a dictionary
        self.images = MicroscopePicDict()

        # self.videos is a VideoDict
        self.videos = VideoDict()
        log.info('Created a new sample named %s' % self.full_name)

    def __repr__(self) -> str:
        """
        Return the canonical representation of a Sample.

        Returns
        -------
        str
            Canonical representation of a Sample.

        """
        return f'{self.__class__.__name__}("{self.full_name}")'

    def __str__(self) -> str:
        """
        Represent the Sample class.

        Returns
        -------
        msg : string
            The Sample class representation.

        """
        msg = (f'Sample {self.last_name} with parent {self.parent} contains \n'
               f'  + {len(self.subsamples)} subsample(s) \n')
        return msg

    def emit_added(self, element_type: ElementType, element_name: str, parent_name: str):
        """
        Cause the signal dispatcher to emit an added_element signal.

        Parameters
        ----------
        element_type : autotools.ElementType
            This enumerator contains all possible element types
        element_name : str
            In the case of MicroPic the element_name must be the
            full path of the added element.
        parent_name : str
            In the case of MicroPic, the parent_name is the sample full name.

        Returns
        -------
        None.

        """
        self.signal_dispatcher.added_element.emit(
            element_type, element_name, parent_name)

    def emit_removed(self, element_type: ElementType, element_name: str, parent_name: str):
        """
        Cause the signal dispatcher to emit a removed_element signal.

        Parameters
        ----------
        element_type : autotools.ElementType
            This enumerator contains all possible element types
        element_name : str
            In the case of MicroPic the element_name must be the
            full path of the removed element.
        parent_name : str
            In the case of MicroPic, the parent_name is the sample name.

        Returns
        -------
        None.

        """
        self.signal_dispatcher.removed_element.emit(
            element_type, element_name, parent_name)

    def add_microscope_picture(self, micro_pic: MicroscopePicture):
        """
        Add a microscope picture to the sample.

        The sample has a dictionary to store all the microscope pictures.
        The picture path is used as a key for the dictionary.

        Parameters
        ----------
        micro_pic : autoprotocol.MicroscopePicture
            The microscope picture to be added to the sample..

        Returns
        -------
        None.

        """
        self.images.add(micro_pic)
        self.emit_added(ElementType.MICROSCOPE_PIC,
                        str(micro_pic.params['path']), self.full_name)
        log.info('Adding microscope picture (%s) to %s' % (
            micro_pic.params['fileName'], self.full_name))
        log.debug('At the moment there are %s pictures in the sample %s' % (
            len(self.images), self.full_name))

    def remove_microscope_picture_path(self, path: str | Path):
        """
        Remove a microscope picture using its path.

        Parameters
        ----------
        path : Path | string
            The full path of the microscope picture to be removed.

        Returns
        -------
        None.

        """
        if isinstance(path, Path):
            path = str(path)
        try:
            self.remove_microscope_picture(self.images[path])
        except KeyError:
            log.error(
                'Could not find an image with the following path %s' % path)

    def remove_microscope_picture(self, micro_pic: MicroscopePicture):
        """
        Remove a microscope picture from the sample.

        Parameters
        ----------
        micro_pic : autoprotocol.MicroscopePicture
            The microscope picture to be removed to the sample..

        Returns
        -------
        None.

        """
        if micro_pic.key in self.images:
            if micro_pic.getID() in MicroscopePicture._used_ids:
                MicroscopePicture._used_ids.remove(micro_pic.getID())
            else:
                log.warning('%s was not in the used_ids list.' %
                            micro_pic.getID())
            log.info('Removed %s from sample %s' %
                     (micro_pic.params['fileName'], self.full_name))
            log.debug('At the moment there are %s pictures in the sample %s' % (
                len(self.images), self.full_name))
            try:
                os.remove(micro_pic.params['pngfilename'])
                os.remove(micro_pic.params['thumbfilename'])
                if micro_pic.params.get('cropped_path', '') != '':
                    os.remove(micro_pic.params['cropped_path'])
            except IOError as e:
                log.warning('Not critical error removing auxiliary files')
                log.warning(e, exc_info=True)
            self.emit_removed(ElementType.MICROSCOPE_PIC,
                              str(micro_pic.params['path']), self.full_name)
            self.images.remove(micro_pic)
        else:
            log.warning('Attempt to remove %s from sample %s, but it was not there' % (
                micro_pic.params['fileName'], self.full_name))

    def add_video(self, video: Video | str | Path):
        """
        Add a video to the sample.

        The sample as a VideoDict to store all videos.

        Parameters
        ----------
        video: Video | str | Path
            The video to be added.

        Returns
        -------
        None
        """
        try:
            if not isinstance(video, Video):
                video = Video(video)
            self.videos.add(video)
            self.emit_added(ElementType.VIDEO_FILE, video.key, self.full_name)
            log.info('Adding video %s in the sample %s' %
                     (video.get('filename'), self.full_name))
        except KeyError as e:
            log.warning('Impossible to add  %s' % video.key)
            log.exception(e)

    def remove_video(self, video: Video | str | Path):
        """
        Remove a video from the sample

        Parameters
        ----------
        video: Video | str | Path
            The video to be removed.
        """
        if isinstance(video, Video):
            filename = video.get('filename')
            video = video.key
        elif isinstance(video, str):
            filename = Path(video).name
        elif isinstance(video, Path):
            filename = video.name
            video = str(video)

        self.videos.remove(video)
        log.info('Removed %s from sample %s' % (filename, self.full_name))
        self.emit_removed(ElementType.VIDEO_FILE, video, self.full_name)

    def add_subsample(self, child_sample_name: str | Sample):
        """
        Add a subsample reference to this sample.

        Parameters
        ----------
        child_sample_name: str | Sample
            This is the full name of the child sample.
            Instead of a string, one can provide also the sample itself.

        Raises
        ------
        autoerror.ParentSampleError:
            if the child full name is not matching the parent name.
        """
        if isinstance(child_sample_name, Sample):
            child_sample_name = child_sample_name.full_name

        # verify that the subsample full name is compatible with the
        # current sample full name.
        this_sample_full_name = '/'.join(child_sample_name.split('/')[0:-1])
        if this_sample_full_name != self.full_name:
            raise autoerror.ParentSampleError(
                'The subsample full not is not matching the parent name')

        if child_sample_name not in self.subsamples:
            self.subsamples.append(child_sample_name)

    def remove_subsample(self, child_sample: str | Sample):
        """Remove a subsample from the subsample list."""
        if isinstance(child_sample, Sample):
            child_sample = child_sample.full_name

        if child_sample in self.subsamples:
            self.subsamples.remove(child_sample)

    def is_empty(self) -> bool:
        """
        Check if a Sample is empty.

        A sample is considered empty when all its resettable containers are empty

        Returns
        -------
        bool
            True is the sample is empty.

        """
        return all([r.is_empty() for r in self.get_resettable_containers()])


class Attachment(HTMLObject):
    """The class to hold the attachment information."""

    def __init__(self, path: str | Path = None):
        """
        Generate instance of an attachment.

        Parameters
        ----------
        path : str | path-like, optional
            The full path to the attachment.
            The default is None.

        Returns
        -------
        None.

        """
        # prepare the empty dictionary
        self.params = {}

        if path is None:
            log.warning('Generating an attachment without path')
            return

        if not isinstance(path, (str, Path)):
            msg = f'Wrong type for {path} in attachment creation'
            log.error(msg)
            raise TypeError(msg)
        elif isinstance(path, str):
            path = Path(path)

        # before continuing we need to check if the file exists.
        if path.exists() and path.is_file():
            self.params['stat'] = path.stat()
            self.params['size'] = path.stat().st_size
            self.params['path'] = path
            self.params['key'] = str(path)
            self.params['filename'] = path.name
            self.params['extension'] = path.suffix
        else:
            if not path.exists():
                msg = f'{path} not found'
                raise FileNotFoundError(msg)
            if not path.is_file():
                msg = f'{path} not a valid file'
                raise IsADirectoryError(msg)

    def __repr__(self) -> str:
        """Represent an Attachment."""
        return f'{__class__.__name__}(path=\'{self.params.get("path", None)}\')'

    def __str__(self) -> str:
        """Represent an attachment as a string."""
        s = f"Attachment {self.params['filename']} has the following parameters:\n"
        for key, value in self.params.items():
            s += f'  {key:<12}: {value}\n'
        return s

    def __eq__(self, other: Attachment) -> bool:
        """
        Equality operator.

        Parameters
        ----------
        other : Attachment
            Another attachment

        Returns
        -------
        bool
            True if both attachments have the same key set and their values
            are all the same.
            False otherwise.

        """
        my_keys = set(self.params.keys())
        other_keys = set(other.params.keys())

        if my_keys.intersection(other_keys) != my_keys:
            return False

        overall_eq = True
        for mkey, mvalue in self.params.items():
            overall_eq = overall_eq and (mvalue == other.params[mkey])

        return overall_eq

    def update(self):
        """
        Update the file stat and size.

        It is possible that during the analysis these parameters were changed.

        Returns
        -------
        None
        """
        self.params['stat'] = self.params['path'].stat()
        self.params['size'] = self.params['path'].stat().st_size

    def is_empty(self) -> bool:
        """
        Check if an attachment is empty.

        Empty means that the file has 0 size.

        Returns
        -------
        bool
            True if the attachment file is empty.
            False otherwise

        """
        self.update()
        return int(self.params.get('size', 0)) == 0

    @property
    def key(self) -> str | None:
        """Attachment key."""
        return self.params.get('key', None)

    @key.setter
    def key(self, value: Any):
        """Attachment key setter."""
        self.params['key'] = value

    def generate_html_code(self, yaml_dict: dict):
        """
        Generate the HTML code for an attachment.

        Parameters
        ----------
        yaml_dict : dict
            The dictionary with the customized information for this attachment.

        Returns
        -------
        None.

        """
        log.debug('Generating HTML of attachment %s' % self.key)

        with self.tag('tr'):
            with self.tag('td'):
                with self.tag('b'):
                    self.text('Filename: ')
                self.line('a', f'{self.params["filename"]}',
                          href=self.convert_path_to_uri(self.params["path"]))
            with self.tag('td'):
                with self.tag('b'):
                    self.text('Type: ')
                self.text(self.params['extension'][1:])
            with self.tag('td'):
                with self.tag('b'):
                    self.text('Size: ')
                self.text(
                    f'{autotools.pretty_fmt_filesize(self.params["size"])}')
            with self.tag('td'):
                with self.tag('b'):
                    self.text('Creation date: ')
                self.text(
                    f'{autotools.get_date_from_file(self.params["stat"], DateType.CTIME):%Y-%m-%d %H:%M:%S}')

        subkey = 'Description'
        exkey = 'Extra'

        if subkey in yaml_dict and yaml_dict[subkey] != '':
            # let's add a line
            with self.tag('tr'):
                with self.tag('td', colspan=1):
                    self.text('')
                with self.tag('td', colspan=1):
                    self.line('b', 'Description:')
                with self.tag('td', colspan=2):
                    self.doc.asis(markdown.markdown(yaml_dict[subkey]))
        if exkey in yaml_dict and yaml_dict[exkey] != '':
            # let's add a line
            with self.tag('tr'):
                with self.tag('td', colspan=1):
                    self.text('')
                with self.tag('td', colspan=1):
                    self.line('b', 'Extra information:')
                with self.tag('td', colspan=2):
                    self.doc.asis(markdown.markdown(yaml_dict[exkey]))


class Protocol(HTMLObject):
    """
    The basic protocol class.

    it contains:
        - an empty list of samples
        - an empty list of attachments
        - a protocol number
        - a project name
        - a project responsible

    """

    def __init__(self, path: str | Path, protocol: int | str = None, project: str = None, responsible: str = None):
        r"""
        Generate an instance of Protocol.

        It creates and initialize all instance variables of a Protocol,
        in particular the path that is where the all files will be living,
        and the three *ownership* variables, i.e. the protocol number,
        the project name and the responsible person.

        The *ownership variables* are normally retrieved from the path if it
        follows the standard naming convention (see path for the regular
        expression pattern), but they can also be overwritten if explicitly
        specified here.

        Parameters
        ----------
        path : str or path object
            The full path where the protocol is living.
            In order to retrieve the *ownership* variable automatically the path
            should look like these two examples:
                12458-Project-Responsible
                12458_Project_Responsible
            The regular expression pattern being used is the following:
                '^#*([\\d]+)\\s*[-_]\\s*([\\w\\W]+)\\s*[-_]\\s*([\\w\\W]+)$'
        protocol : int or string, optional
            The protocol number. This field is used to identy the analysis inside
            the logbook and of course it must unique. There is no unicity test
            performed here, but it should be done somewhere else.
            When the user wants to have the protocol number guessed from the path
            then, set this variable to None.
            The default is None.
            TODO: Implement a unicity check on the protocol number.
        project : string, optional
            The project name. As for the protocol number (see above), this is
            generally provided with the path.
            The default is None.
        responsible : string, optional
            The name of the responsible person. As for the protocol number (see above),
            this is generally provided with the path.
            The default is None.


        Raises
        ------
        autoerror.MissingProtocolInformation
            This exception is raised if the user did not provided customized
            ownership variables and the automatic guessing from the path
            was failing.

        Returns
        -------
        None.

        """
        super().__init__()

        if not isinstance(path, Path):
            path = Path(path)
        self.path = path

        skip_guessing = False
        if protocol is not None and project is not None and responsible is not None:
            # the user wants to use its own variables
            skip_guessing = True
            self.protocol = protocol
            self.project = project
            self.responsible = responsible

        if not skip_guessing:
            # the user didn't provide his custom ownership variables.
            # we need to guess them from the path.
            folder = self.path.parts[-1]
            pattern = '^#*([\\d]+)\\s*[-_]\\s*([\\w\\W]+)\\s*[-_]\\s*([\\w\\W]+)$'
            match = re.search(pattern, folder)

            if match:
                self.protocol = match.group(1)
                self.project = match.group(2)
                self.responsible = match.group(3)
            else:
                err_msg = '''
                Ownership variables not provided and not available in the path
                '''
                raise autoerror.MissingProtocolInformation(err_msg)

        log.info('Created a new Protocol (#=%s, Project=%s, Responsible=%s)' %
                 (self.protocol, self.project, self.responsible))

        # all containers for images, samples and everything must be of resettable types
        # initialize empty container for attachments
        self.attachments = AttachmentDict()
        # initialize empty container for samples
        self.samples = SampleDict()
        # ordered sample list
        self.ordered_sample_list = ResettableList()

        # a signal dispatcher
        self.signal_dispatcher = SignalDispatcher()

        # initialize yaml_dict and its filename
        self.yamlDict = None
        self.yamlFilename = None

        # reset the picture ID list
        MicroscopePicture._reset_ids()

    def __str__(self) -> str:
        """Return basic string representation of a Protocol."""
        msg = (
            f'Protocol #{self.protocol} - {self.project} - {self.responsible}\n')
        if len(self.samples) == 0:
            msg += 'with no samples\n'
        elif len(self.samples) == 1:
            msg += 'with 1 sample\n'
        else:
            f'with {len(self.samples)}.\n'
        if len(self.samples):
            msg += ('\n'
                    'Sample list:\n\n')
        for sample in self.samples:
            msg += self.samples[sample].__str__()
            msg += '\n'

        return msg

    def emit_added(self, element_type: ElementType, element_name: str, parent_name: str):
        """
        Emit a signal for the addition of a given element to the protocol.

        This method implements an interface to the Qt Signal / Slot mechanism.
        Every time a new element is added to the protocol, this method should be
        called in order to make the GUI aware of the changes, in particular
        the TreeViewModel where the whole protocol is described.

        Parameters
        ----------
        element_type : autotools.ElementType
            This enumerator contains all possible element types
        element_name : String
            In the case of ElementType.MICROSCOPE_PIC, ElementType.NAVIGATION_PIC
            and ElementType.ATTACHMENT the element_name must be the full path of
            the newly added element.
            In the case of ElementType.SAMPLE, the element_name is exactly the
            sample full name
        parent_name : String
            In the case of ElementType.NAVIGATION_PIC, the parent_name is totally
            optional because all navigation images will be added to the
            'Navigation Images' section.
            Same situation for ElementType.ATTACHMENT because the parent is the
            'Attachments' section.
            In the case of ElementType.MICROSCOPE_PIC, the parent_name is the
            sample full name.
            In the case of ElementType.SAMPLE, the parent_name the name of the
            parent full sample or 'Samples' if it is a top level sample.

        Returns
        -------
        None.

        """
        self.signal_dispatcher.added_element.emit(
            element_type, element_name, parent_name)

    def emit_removed(self, element_type: ElementType, element_name: str, parent_name: str):
        """
        Emit a signal for the removal of a given element from the protocol.

        This method implments an interface to the Qt Signal / Slot mechanism.
        Every time an element is removed from the protocol, this method should be
        called in order to make the GUI aware of the changes, in particular
        the TreeViewModel where the whole protocol is described.

        Parameters
        ----------
        element_type : autotools.ElementType
            This enumerator contains all possible element types
        element_name : String
            In the case of ElementType.MICROSCOPE_PIC, ELementType.Attachment and
            ElementType.NAVIGATION_PIC, the element_name must be the full path
            of the removed element.
            In the case of Sample, the element_name is exactly the sample name
        parent_name : String
            In the case of NavPic, the parent_name is totally optional because
            all navigation images are located in the 'Navigation Images' section.
            In the case of Attachment, the parent_name is also totally optional.
            In the case of MicroPic, the parent_name is the sample name.
            In the case of ElementType.SAMPLE, the parent_name the name of the
            parent full sample or 'Samples' if it is a top level sample.

        Returns
        -------
        None.

        """
        self.signal_dispatcher.removed_element.emit(
            element_type, element_name, parent_name)

    def add_attachment(self, attachment_path: Path | str):
        """
        Add an attachment at the Protocol.

        Parameters
        ----------
        attachment_path : PATH | string
            The path of the attachment file.

        Returns
        -------
        None.

        """
        if not isinstance(attachment_path, Path):
            attachment_path = Path(attachment_path)
        self.attachments.add(attachment_path)
        self.emit_added(ElementType.ATTACHMENT_FILE,
                        str(attachment_path), 'Attachments')
        log.info('Added %s to the attachment list' %
                 attachment_path.name)

    def remove_attachment(self, attachment_path: str | Path):
        """
        Remove one attachment.

        Parameters
        ----------
        attachment_path : Path | String
            The path of the attachment file

        Returns
        -------
        None.

        """
        self.attachments.remove(attachment_path)
        self.emit_removed(ElementType.ATTACHMENT_FILE,
                          attachment_path, 'Attachments')
        log.info('Removed %s to the attachment list' %
                 os.path.split(attachment_path)[-1])

    def add_sample(self, sample: Sample | str):
        """
        Add a new sample to the protocol.

        The sample name is guessed from the folder


        Parameters
        ----------
        sample : autologbook.Sample | str
            This is an instance of the autologbook.Sample or the full name of a new sample.

        Returns
        -------
        None.

        """
        # this is adding the sample to the sample dictionary.
        # the used key is the full name and should avoid problems with subsamples.
        # the add method of the sample dictionary will transform the string in a sample
        # object if need it.
        self.samples.add(sample)

        if isinstance(sample, str):
            # get the sample object back if we had a string as input
            sample = self.samples[sample]

        # the parent name is again a full_name or None if the current sample
        # is a top level sample.
        #
        # for the protocol editor we need to pass Samples in case of a top level
        # sample or the whole hierarchy.
        parent = sample.parent
        if parent is None:
            parent_name = 'Samples'
        else:
            parent_name = parent
            # make the parent sample aware that he got a child!
            if parent_name in self.samples:
                self.samples[parent_name].add_subsample(sample.full_name)
            else:
                self.samples.remove(sample)
                raise autoerror.ParentSampleError(f'Sample {sample.full_name} has a parent ({parent_name})'
                                                  ' not existing in protocol sample list.')

        self.emit_added(ElementType.SAMPLE, sample.full_name, parent_name)
        sample.signal_dispatcher.added_element.connect(
            self.signal_dispatcher.added_element)
        sample.signal_dispatcher.removed_element.connect(
            self.signal_dispatcher.removed_element)
        if parent is None:
            log.info('Added %s to the sample list' % sample.full_name)
        else:
            log.info('Added %s to the sample list under %s' %
                     (sample.last_name, parent_name))
        log.debug('At the moment there are %s samples in the list' % (
            len(self.samples)))

    def remove_sample(self, sample_full_name: str):
        """
        Remove one sample.

        Parameters
        ----------
        sample_full_name : str
            This is the sample full name

        Returns
        -------
        None.

        """
        if sample_full_name in self.samples:
            if self.samples[sample_full_name].parent:
                parent_name = self.samples[sample_full_name].parent
                log.debug('Removing subsample %s from its parent %s'
                          % (sample_full_name, parent_name))
                if parent_name in self.samples:
                    self.samples[parent_name].remove_subsample(
                        sample_full_name)
                    log.debug('Those are the remaining subsamples of %s'
                              % parent_name)
                    for ssample in self.samples[parent_name].subsamples:
                        log.debug('-> %s' % ssample)
                else:
                    log.warning('Could not find parent sample (%s) for %s' %
                                (parent_name, self.samples[sample_full_name].last_name))
            else:
                parent_name = 'Samples'
            self.emit_removed(ElementType.SAMPLE,
                              sample_full_name, parent_name)
            del self.samples[sample_full_name]
            log.info('Removed %s from the sample list' % sample_full_name)
            log.debug('At the moment there are %s samples in the list' %
                      len(self.samples))
        else:
            log.warning(
                'Attempt to remove %s from the sample list, but it was not there' % sample_full_name)

    def generate_custom_html(self, main_key: Any):
        """
        Generate custom HTML.

        Helper function to generate customized HTML code for a given section.
        The section is identified by the mainkey parameter.

        The user can provide via the YAML customization file or the GUI, additional
        test (markdown formatted) to be added to each section of the protocol.

        Parameters
        ----------
        main_key : Any
            The section of the HTML for which the customized HTML is being
            generated.

        Returns
        -------
        None.

        """
        subkey = 'Description'
        exkey = 'Extra'
        if main_key in self.yamlDict.keys() and self.yamlDict[main_key]:
            if subkey in self.yamlDict[main_key].keys() and self.yamlDict[main_key][subkey]:
                self.doc.asis(markdown.markdown(
                    self.yamlDict[main_key][subkey]))
            if exkey in self.yamlDict[main_key].keys():
                if self.yamlDict[main_key][exkey]:
                    if len(self.yamlDict[main_key][exkey]) > 0:
                        self.line('h3', 'Additional information')
                        self.doc.asis(markdown.markdown(
                            self.yamlDict[main_key][exkey]))

    def generate_html(self):
        """
        Generate the HTML code for the protocol.

        This function is calling a similar function for each of the main sections
        of the protocol.
            1. Introduction
            2. Samples
            3. Closure

        Returns
        -------
        None.

        """
        log.info('Generating HTML code for protocol %s' % self.protocol)
        self.sanity_check()
        self.generate_html_intro()
        self.generate_html_samples()
        self.generate_html_closure()
        self.generate_html_attachments()

    def generate_html_intro(self):
        """
        Generate the introduction for the HTML output.

        It generates the following:
            1. The protocol title
            2. The customized introduction part
            3. The sample list

        Returns
        -------
        None.

        """
        log.debug('Generating HTML intro of protocol %s' % self.protocol)
        self.line(
            'h1', f'Analysis protocol {self.protocol}', style='text-align: center;', id='intro')
        self.generate_custom_html('Introduction')

        # generate sample list
        self.generate_html_sample_list()

    def generate_html_sample_list(self):
        """
        Generate HTML Sample list.

        Generate a list with all the samples found in the protocol

        Returns
        -------
        None.

        """
        self.ordered_sample_list = ResettableList()
        self.generate_custom_html('Samples')
        log.debug('Generating HTML sample list')
        if len(self.samples):
            if len(self.samples) == 1:
                sample = 'sample'
            else:
                sample = 'samples'
            self.line(
                'h2', f'This analysis contains the following {sample}:', id='samplelist')
            with self.tag('ul'):
                # the key is the full_name
                for full_name, sample in self.samples.items():
                    if sample.parent is None:
                        # add this sample to the ordered sample list
                        self.ordered_sample_list.append(full_name)
                        with self.tag('li'):
                            with self.tag('a', href=f'#{full_name}'):
                                self.text(full_name)
                            if len(sample.images) and len(sample.videos):
                                image = 'image' if len(
                                    sample.images) == 1 else 'images'
                                video = 'video' if len(
                                    sample.videos) == 1 else 'videos'
                                self.text(
                                    f' with {len(sample.images)} {image} and {len(sample.videos)} {video}')
                            else:
                                if len(sample.images):
                                    image = 'image' if len(
                                        sample.images) == 1 else 'images'
                                    self.text(
                                        f' with {len(sample.images)} {image}')
                                if len(sample.videos):
                                    video = 'video' if len(
                                        sample.videos) == 1 else 'videos'
                                    self.text(
                                        f' with {len(sample.videos)} {video}')
                            if len(sample.subsamples):
                                self.generate_html_subsamplelist_recursively(
                                    sample.subsamples)

    def generate_html_subsamplelist_recursively(self, sample_list: list):
        """
        Generate the HTML for the sub sample list.

        In order to generate a nested bullet list of subsample this function
        is called for all top level samples.

        Parameters
        ----------
        sample_list : list
            A list of samples for which the HTML code has to be generated.

        Returns
        -------
        None.

        """
        with self.tag('ul'):
            # sample_name is a full_name
            for sample_name in sample_list:
                self.ordered_sample_list.append(sample_name)
                sample = self.samples[sample_name]
                with self.tag('li'):
                    with self.tag('a', href=f'#{sample_name}'):
                        self.text(self.samples[sample_name].last_name)
                    if len(sample.images) and len(sample.videos):
                        image = 'image' if len(
                            sample.images) == 1 else 'images'
                        video = 'video' if len(
                            sample.videos) == 1 else 'videos'
                        self.text(
                            f' with {len(sample.images)} {image} and {len(sample.videos)} {video}')
                    else:
                        if len(sample.images):
                            image = 'image' if len(
                                sample.images) == 1 else 'images'
                            self.text(f' with {len(sample.images)} {image}')
                        if len(sample.videos):
                            video = 'video' if len(
                                sample.videos) == 1 else 'videos'
                            self.text(f' with {len(sample.videos)} {video}')
                    if len(sample.subsamples):
                        self.generate_html_subsamplelist_recursively(
                            sample.subsamples)

    def sanity_check(self):
        """
        Perform a sanity check on the protocol.

        When several images are added and removed quickly it is possible that
        the sample, subsample structure gets corrupted.

        This method along with the private _check_subsamples goes through all
        registered samples and sub-samples.

        TODO: this method can be improved.

        Returns
        -------
        None.

        """
        for full_name, sample in self.samples.items():
            if sample.parent is None:
                self._check_subsamples(sample.subsamples, sample)

    def _check_subsamples(self, sample_list: list, parent: Sample):
        for full_name in sample_list:
            if full_name not in self.samples:
                parent.subsamples.remove(full_name)
            else:
                if len(self.samples[full_name].subsamples) != 0:
                    self._check_subsamples(
                        self.samples[full_name].subsamples, self.samples[full_name])

    def generate_html_samples(self):
        """
        Generate the HTML code of the Samples section.

        If there are no samples, then it prints a no samples found message and quit.
        Otherwise, it prints a table with all the images for each of the samples.

        The HTML code generation for each image is done by the
        MicroscopePicture.generate_html_code method.

        Returns
        -------
        None.

        """
        if len(self.samples) == 0:
            self.doc.stag('hr')
            message = 'No samples found for this protocol'
            self.line('h2', message)
            log.debug(message)

        # the ordered_sample_list contains sample full names
        for full_name in self.ordered_sample_list:
            if full_name not in self.samples:
                continue
            sample = self.samples[full_name]

            self.doc.stag('hr')
            self.line('h2', f'Sample {full_name}', id=full_name)
            # generate the custom html for this specific sample.
            self.generate_custom_html(full_name)

            if len(sample.images) == 0 and len(sample.videos) == 0:
                message = f'No microscope pictures nor videos found for {full_name}'
                self.line('h3', message, id=f'{full_name}pics')
                log.debug(message)
            else:
                if len(sample.images):
                    self.line(
                        'h3', f'Picture list for sample: {full_name}', id=f'{full_name}pics')
                    self.line('a', 'Hide / show the picture list',
                              onclick=f'hideDiv(\'{full_name}picstable\')', href='javascript:void(0);')
                    with self.tag('table', border=1, cellpaggind=1, cellspacing=1,
                                  style='display:table; width:1200px; border-collapse:collapse',
                                  id=f'{full_name}picstable'):
                        with self.tag('tbody'):
                            for key, image in sample.images.items():
                                image.generate_html_code(
                                    self.yamlDict.get(image.getID(), {}))

                if len(sample.videos):
                    self.line(
                        'h3', f'Video list for sample: {full_name}', id=f'{full_name}vids')
                    self.line('a', 'Hide / show the video list', onclick=f'hideDiv(\'{full_name}vidstable\')',
                              href='javascript:void(0);')
                    with self.tag('table', border=1, cellpadding=1, cellspacing=1,
                                  style='display:table; width:1200px; border-collapse:collapse',
                                  id=f'{full_name}vidstable'):
                        with self.tag('tbody'):
                            for key, video in sample.videos.items():
                                video.generate_html_code(
                                    self.yamlDict.get(key, {}))

                self.doc.stag('br')
                self.line('a', 'Go back to the sample list',
                          href='#samplelist')
                self.doc.stag('br')
                self.line('a', 'Go back home', href='#intro')

    def generate_html_closure(self):
        """
        Generate the HTML code for the closure of the protocol.

        It is useful to add here all javascript that needs to be referred from
        page elements.

        Returns
        -------
        None.

        """
        # it makes sense to generate a conclusion title only if there is some
        # custom conclusion text.
        # this means that the main key should exists and at least one between Description
        mainkey = 'Conclusion'
        if mainkey in self.yamlDict.keys() and any([self.yamlDict[mainkey].get('Description', False),
                                                    self.yamlDict[mainkey].get('Extra', False)]):
            self.line('h1', 'Conclusion',
                      style='text-align: center;', id='conclusion')
            self.generate_custom_html(mainkey)

        # add all scripts for sure
        with self.tag('script'):
            self.doc.asis('''
                          function hideDiv(div_name) {
                              var x = document.getElementById(div_name);
                              if (x.style.display == "none") {
                                      x.style.display = "table";
                              } else {
                                  x.style.display = "none" ;
                             }
                         }
                        ''')

    def generate_html_attachments(self):
        """
        Generate the HTML for the attachment section.

        Returns
        -------
        None.

        """
        mainkey = 'Attachments'
        if mainkey in self.yamlDict.keys() and self.yamlDict[mainkey] or len(self.attachments) != 0:
            self.line('h2', 'Attachments',
                      style='text-align: left;', id='attachments')
            self.generate_custom_html(mainkey)
        if len(self.attachments) != 0:
            with self.tag('table', border=1, cellpaggind=1, cellspacing=1,
                          style='display:table; width:1200px; border-collapse:collapse', id='attachment-table'):
                with self.tag('tbody'):
                    for key, attach in self.attachments.items():
                        ydict = self.yamlDict.get(key, {})
                        attach.generate_html_code(ydict)

    def clear_resettable_content(self):
        """
        Reset the content of a protocol so that it can be reused.

        This method just empties the containers (samples and attachments), it does not remove other properties.

        Returns
        -------

        """
        for f in self.get_resettable_containers():
            f.clear()

    def is_empty(self) -> bool:
        """
        Check if the protocol containers are empty.

        Returns
        -------
        bool:
            True if all protocol containers are empty.
            False, otherwise.
        """
        empty = True
        for resettable_element in dir(self):
            attribute = self.__getattribute__(resettable_element)
            if isinstance(attribute, (ResettableDict, ResettableList)):
                empty = empty and attribute.is_empty()
        return empty


class ELOGProtocol(Protocol):
    """Subclass of Protocol having information about ELOG."""

    def __init__(self, path: str | Path, elog_hostname: str, elog_port: int, elog_user: str, elog_password: str,
                 elog_use_ssl: bool = True, elog_logbook: str = None, protocol: int | str = None,
                 project: str = None, responsible: str = None, yaml_filename: str | Path | None = None):
        super().__init__(path, protocol, project, responsible)
        self.elog_hostname = elog_hostname
        self.elog_port = elog_port
        self.elog_user = elog_user
        self.elog_password = elog_password
        self.elog_use_ssl = elog_use_ssl
        self.elog_logbook = elog_logbook

        # initialize the yaml engine for HTML customization
        self.initialize_yaml(yaml_filename)

        # initialize an empty dictionary for the ELOG attributes
        self.attributes = {}

        # set the elog instance to none
        self.elog_instance = None

    def initialize_yaml(self, yaml_filename):
        """
        Initialize the YAML customization tool.

        It looks for a yaml file in the protocol folder named according to the
        rule protocol-xxxxx.yaml where xxxxx is the protocol-id.

        If none is found than a new empty one is created, otherwise it is safely
        loaded and its content transferred to the yaml_dict

        Returns
        -------
        None.

        """
        # initialize the yaml_dict
        self.yamlDict = {}

        if yaml_filename is not None:
            if isinstance(yaml_filename, str):
                yaml_filename = Path(yaml_filename)

        if self.yamlFilename is None and yaml_filename is None:
            # the user didn't specify a custom yaml_filename and we didn't have any one before
            # so we need to assign the default one.
            self.yamlFilename = Path(self.path) / \
                Path(f'protocol-{self.protocol}.yaml')

        if yaml_filename is not None:
            # if we are here it means that the user specified a yaml_filename to be used
            # then we have to use it.
            self.yamlFilename = yaml_filename

        if not self.yamlFilename.exists():
            log.info('No yaml file found, copying an empty one')
            with open(self.yamlFilename, 'w', encoding='utf-8') as file:
                file.write('#empty yaml file')

        with open(self.yamlFilename, 'rt', encoding='utf-8') as file:
            self.yamlDict = yaml.safe_load(file)
            if not self.yamlDict:
                # the file might be empty, then we need to set is as a dictionary
                self.yamlDict = {}
        log.info('Loaded yaml file %s' % self.yamlFilename.name)

    def remove_from_yaml(self, key: str, force_dump: bool = False) -> None:
        """
        Remove an element from the YAML customization dictionary.

        This method looks if element is present in the YAML dictionary.
        If so, it deletes it, otherwise simply return

        Parameters
        ----------
        key : string
            The key of the element to be removed from the yaml dictionary

        force_dump : bool, optional
            If True, the yaml dictionary will be dumped to the file.
            The default is false.

        Returns
        -------
        None.

        """
        if key in self.yamlDict:
            del (self.yamlDict[key])
            log.debug('Removed %s from the yaml dictionary' % key)
            if force_dump:
                autotools.dump_yaml_file(self.yamlDict, self.yamlFilename)

    def remove_sample(self, sample: str):
        """
        Remove Sample overload.

        This overload method just implement the removal from the yaml
        customization dictionary.

        Parameters
        ----------
        sample : string
            Sample name to be removed.

        Returns
        -------
        None.

        """
        super().remove_sample(sample)
        self.remove_from_yaml(sample)

    @retry(retry=retry_if_exception_type(LogbookServerTimeout),
           reraise=True, stop=stop_after_attempt(autoconfig.ELOG_TIMEOUT_MAX_RETRY),
           wait=wait_fixed(autoconfig.ELOG_TIMEOUT_WAIT),
           after=after_log(log, logging.WARNING))
    def connect_to_elog(self):
        """
        Connect to the ELOG.

        This method is calling the elog.open function to generate an instance
        to the elog protocol.

        The elog.open itself is not checking whether the connection is valid or not,
        so to be sure we are actually getting a valid elog_instance, a real query to
        the elog (get_message_ids) is also performed.

        Returns
        -------
        elog_instance
            The elog_instance to be used to query the elog. The same value is
            also stored as an instance parameter

        """
        if self.elog_instance:
            return self.elog_instance
        log.info('Establishing connection with the ELOG server')
        try:
            self.elog_instance = elog.open(
                hostname=self.elog_hostname,
                port=self.elog_port,
                user=self.elog_user,
                password=self.elog_password,
                use_ssl=self.elog_use_ssl,
                logbook=self.elog_logbook,
                encrypt_pwd=False
            )
            # the elog open doesn't check if the connection is ok
            # while the get message_ids perform a real connection
            # TODO: find a better way to test if the connection is valid.
            #       this is probably to be done in the elog package.

            self.elog_instance.get_message_ids(timeout=autoconfig.ELOG_TIMEOUT)
            log.info('Connection to the eLOG server successfully established')
            return self.elog_instance
        except LogbookServerTimeout as e:
            log.warning('Attempt to connect to the ELOG server failed due to timeout (%d s).'
                        ' New attempt in a few seconds' % autoconfig.ELOG_TIMEOUT)
            log.exception(e)
            raise LogbookServerTimeout
        except elog.LogbookAuthenticationError:
            log.critical('Logbook Authentication Error')
        except Exception as err:
            log.critical(
                'Unable to establish a connection with the eLOG server. Here is the returned error message.')
            log.exception(err)

    @retry(retry=retry_if_exception_type(LogbookServerTimeout),
           reraise=True, stop=stop_after_attempt(autoconfig.ELOG_TIMEOUT_MAX_RETRY),
           wait=wait_fixed(autoconfig.ELOG_TIMEOUT_WAIT),
           after=after_log(log, logging.WARNING))
    def post_elog_message(self, skip_attachments: bool = False):
        """
        Post the protocol to the ELOG server.

        This method will do the following:
            1. Attempt a connection to the elog server
            2. Check if other entries with the same protocol number exist.
                2.1 If yes and if it is one, just delete it.
                2.2 If no, just go ahead.
                2.3 If yes and they are many, then raise an exception.
            3. Post a new entry with all the required attributes and the HTML
               content.


        Parameters
        ----------
        skip_attachments : Bool, optional
            Decide whether to post also attachment or not.
            Posting attachments maybe bandwidth heavy and it makes no sense
            while updating the protocol during the analysis. It is only meaningful
            at the end of the analysis.
            The default is False.

        Raises
        ------
        NameError
            Exception raised when more than one entry with the same protocol
            number is found already existing in the elog.

        Returns
        -------
        None.

        """
        if not self.elog_instance:
            self.connect_to_elog()
        # check if an entry with the same protocol id already exists
        protocol_ids = self.elog_instance.search(
            {'Protocol ID': self.protocol}, timeout=autoconfig.ELOG_TIMEOUT)

        real_ids = []
        for ID in protocol_ids:
            log.debug('Entry %s with protocol %s' % (ID, self.protocol))
            message, attributes, attachments = self.elog_instance.read(
                ID, timeout=autoconfig.ELOG_TIMEOUT)
            if attributes['Protocol ID'] == self.protocol:
                real_ids.append(ID)

        log.debug('Searching for IDs with %s' % self.protocol)
        if (len(real_ids)) > 1:
            # there are more than 1 entry with this protocol ID.
            # It is a problem. Ask the user what to do.
            # TODO: implement this situation
            log.warning(
                'Several protocols with the same IDs have been found %s' % len(real_ids))
            raise NameError

        # if an entry already exists, try to see if we are allowed to edit it

        if real_ids:
            try:
                self.elog_instance.delete(
                    real_ids[0], timeout=autoconfig.ELOG_TIMEOUT)
                log.debug('Found already an eLog entry with protocol %s. Deleting it' %
                          self.protocol)
            except LogbookError as e:
                log.exception('Logbook error', e)

        attachments = []
        if skip_attachments:
            attachments = []
        else:
            # please load only not empty attachments.
            for att in self.attachments:
                if os.stat(att).st_size:
                    attachments.append(att)
        try:
            self.elog_instance.post(self.print_html(
                False), reply=False, attributes=self.attributes, attachments=attachments, encoding='HTML',
                timeout=autoconfig.ELOG_TIMEOUT)
            log.info('Successfully posted eLog entry for protocol %s' %
                     self.protocol)
        except elog.LogbookAuthenticationError as e:
            log.exception('Logbook error', e)
        except elog.LogbookMessageRejected:
            log.critical(
                'ELOG Message too large, please split the project in subpart!')
            log.critical(
                'This operation must be done manually. Just rename this project as')
            log.critical('   %s-p1-%s-%s' %
                         (self.protocol, self.project, self.responsible))
            log.critical('and create another one as')
            log.critical('   %s-p2-%s-%s' %
                         (self.protocol, self.project, self.responsible))


class QuattroELOGProtocol(ELOGProtocol):
    """
    Subclass of the ELOGProtocol dedicated to the Quattro Microscope.

    This subclass implements all the specificities of the Quattro in particular
    the presence of navigation camera images.

    """

    def __init__(self, path: Path | str, elog_hostname: str, elog_port: int, elog_user: str, elog_password: str,
                 elog_use_ssl: bool = True, elog_logbook: str = autoconfig.QUATTRO_LOGBOOK,
                 protocol: int | str = None, project: str = None, responsible: str = None,
                 yaml_filename: str | Path | None = None):

        super().__init__(path, elog_hostname, elog_port, elog_user, elog_password, elog_use_ssl, elog_logbook, protocol,
                         project, responsible, yaml_filename)

        # initialize the navigation camera image list
        self.navcamimages = NavigationImagesList()
        self.attributes = {
            'Protocol ID': self.protocol,
            'Project': self.project,
            'Customer': self.responsible,
            'Operator': elog_user,
            'Creation date': datetime.today().timestamp(),
            'Edit Lock': 'Unprotected'
        }

    def generate_html_intro(self):
        """
        Overload the standard HTML introduction.

        This overloaded method allows to implement the specific HTML introduction
        for the Quattro microscope.

        It prints the following:
            1. Protocol Title
            2. Customized introduction taken from the YAML file
            3. Sample list
            4. Navigation camera section

        """
        log.debug('Generating HTML intro for protocol %s' % self.protocol)
        self.line(
            'h1', f'Quattro SEM Analysis protocol {self.protocol}', style="text-align:center;", id='intro')
        self.generate_custom_html('Introduction')
        self.generate_html_sample_list()
        self.generate_html_navigation_camera_images()

    def generate_html_navigation_camera_images(self):
        """
        Generate the HTML code for the Navigation camera section.

        It prints the following:
            1. Section title if at least one navigation image is provided.
            2. Custom text provided via the YAML file
            3. A single column table with a navigation image per line


        Returns
        -------
        None.

        """
        log.debug('Generating HTML code for the navigation camera images of protocol %s' % self.protocol)
        if len(self.navcamimages) == 0:
            log.debug('No navigation picture provided!')
            self.line('h2', 'No navigation picture provided!')
        else:
            self.line('h2', 'Navigation Camera image(s)')
            self.generate_custom_html('Navigation images')

            with self.tag('table', align='left', border='1', cellpadding='1', cellspacing='1',
                          style=f'float:none;width:{autoconfig.IMAGE_NAVIGATION_MAX_WIDTH}px;'
                                + ' border-collapse:collapse'):
                with self.tag('tbody'):
                    for navcamimage in self.navcamimages:
                        with self.tag('tr'):
                            with self.tag('td'):
                                with self.tag('p', style='text-align-center'):
                                    with self.tag('figure', klass='image'):
                                        with self.tag('figure'):
                                            with self.tag('a', href=self.convert_path_to_uri(navcamimage)):
                                                self.doc.stag('img', width=autoconfig.IMAGE_NAVIGATION_MAX_WIDTH - 10,
                                                              alt=os.path.split(navcamimage)[-1],
                                                              src=self.convert_path_to_uri(navcamimage))

                                            caption = os.path.split(navcamimage)[-1]
                                            if os.path.split(navcamimage)[-1] in self.yamlDict and \
                                                    self.yamlDict[os.path.split(navcamimage)[-1]]:
                                                if 'Caption' in self.yamlDict[os.path.split(navcamimage)[-1]]:
                                                    caption = self.yamlDict[os.path.split(navcamimage)[-1]]['Caption']
                                            self.line('figcaption', caption)
                                self.generate_custom_html(os.path.split(navcamimage)[-1])

    def add_navigation_camera_image(self, path: Path | str):
        """
        Add a navigation camera image at the Protocol.

        Parameters
        ----------
        path : path-like | string
            The path of the navigation image file.

        Returns
        -------
        None.

        """
        self.navcamimages.append(path)
        log.info('Added %s to the navcam list' % path)
        log.debug('At the moment there are %s pictures in the navcam list' % len(self.navcamimages))
        self.emit_added(ElementType.NAVIGATION_PIC, str(path), 'Navigation Images')

    def remove_navigation_camera_image(self, path: Path | str):
        """
        Remove one navigation camera image file.

        The navigation camera is also removed from the YAML customization
        dictionary if it was present.

        Parameters
        ----------
        path : Path | String
            The path of the navigation image file.

        Returns
        -------
        None.

        """
        if path in self.navcamimages:
            self.navcamimages.remove(path)
            log.info('Removed %s to the navcam list' % path)
            log.debug('At the moment there are %s pictures in the navcam list' % len(
                self.navcamimages))
            self.emit_removed(ElementType.NAVIGATION_PIC,
                              path, 'Navigation Images')
            self.remove_from_yaml(path)
        else:
            log.warning(
                'Attempt to remove %s from the navcam list, but it was not there' % path)

    def is_empty(self) -> bool:
        """
        Check if the protocol is empty.

        Returns
        -------
        bool
            True if the protocol does not contain any item in the resettable containers.
        """
        protocol_empty = super().is_empty()
        navigation_empty = True if len(self.navcamimages) == 0 else False

        return protocol_empty and navigation_empty

    def clear_resettable_content(self):
        """
        Reset the protocol content.

        It overloads the Protocol reset method and it also clears the navigation camera images.

        Returns
        -------

        """
        super().clear_resettable_content()
        self.navcamimages = NavigationImagesList()


class VersaELOGProtocol(ELOGProtocol):
    """
    Subclass of the ELOGProtocol dedicated to the Versa Microscope.

    This subclass implements all the specificities of the Versa in particular
    the presence of navigation camera images.

    """

    def __init__(self, path: Path | str, elog_hostname: str, elog_port: int, elog_user: str, elog_password: str,
                 elog_use_ssl: bool = True, elog_logbook: str = autoconfig.VERSA_LOGBOOK,
                 protocol: int | str = None, project: str = None, responsible: str = None,
                 yaml_filename: str | Path | None = None):
        super().__init__(path, elog_hostname, elog_port, elog_user, elog_password, elog_use_ssl,
                         elog_logbook, protocol, project, responsible, yaml_filename)
        self.attributes = {
            'Protocol ID': self.protocol,
            'Project': self.project,
            'Customer': self.responsible,
            'Operator': elog_user,
            'Creation date': datetime.today().timestamp(),
            'Edit Lock': 'Unprotected'

        }

    def generate_html_intro(self):
        """
        Overload the standard HTML introduction.

        This overloaded method allows to implement the specific HTML introduction
        for the Versa microscope.

        It prints the following:
            1. Protocol Title
            2. Customized introduction taken from the YAML file
            3. Sample list

        """
        log.debug('Generating HTML intro for protocol %s' % self.protocol)
        self.line(
            'h1', f'VERSA 3D FIB Analysis protocol {self.protocol}', style="text-align:center;", id='intro')
        self.generate_custom_html('Introduction')
        self.generate_html_sample_list()


class MicroscopePicDict(ResettableDict):
    """A subclass of resettable dictionary specialized for microscope images."""

    def __init__(self, initialdata=None):
        super().__init__(initialdata)

    def add(self, image: MicroscopePicture):
        """
        Add a MicroscopePicture to the dictionary.

        Parameters
        ----------
        image: MicroscopePicture
            Element to be added.

        """
        if not isinstance(image, MicroscopePicture):
            raise TypeError(
                'Only microscope pictures can be added to the image dictionary.')
        if image.key is None:
            # it is a picture without a path.
            # it cannot be added to the dictionary
            raise KeyError('Impossible to add a picture without path')
        if image.key in self.data.keys():
            log.warning(
                'Attempt to add another image with the same key (%s) to the dictionary.' % image.key)
        else:
            self.data[image.key] = image

    def remove(self, image: MicroscopePicture | str) -> None:
        """
        Remove a MicroscopePicture from the dictionary.

        Parameters
        ----------
        image: MicroscopePicture | str
            The element to be removed, it can either be the element itself, or its key.
        """
        if isinstance(image, MicroscopePicture):
            key = image.key
        elif isinstance(image, str):
            key = image
        else:
            raise TypeError(
                'image can only be a MicroscopePicture or a string')
        if key not in self.data.keys():
            log.warning(
                'Attempt to remove an image (%s) not found in the dictionary' % key)
        else:
            del self.data[key]


class AttachmentDict(ResettableDict):
    """A dictionary of attachments."""

    def __init__(self, initialdata=None):
        super().__init__(initialdata)

    def add(self, attachment: Attachment | str | Path):
        """
        Add an attachment to the dictionary.

        Parameters
        ----------
        attachment : Attachment or str or path-like
            The attachment that must be added.

        Raises
        ------
        TypeError: if attachment is not one of the accepted types.
        KeyError: if adding another attachment with an existing key.

        Returns
        -------
        None.

        """
        if not isinstance(attachment, (Attachment, str, Path)):
            raise TypeError(
                'Attachment type must be Attachment, string or path-like')

        if isinstance(attachment, (str, Path)):
            attachment = Attachment(attachment)

        if attachment.key in self.data:
            raise KeyError(
                'Attempt to add another attachment with the same key %s' % attachment.key)

        self.data[attachment.params['key']] = attachment

    def remove(self, attachment: Attachment | str | Path) -> None:
        """Remove an attachment from the list.

        Parameters
        ----------
        attachment : Attachment or str or path-like
            The attachment that must be removed.

        Raises
        ------
        TypeError: if attachment is not one of the acceptable types.

        Returns
        -------
        None.

        """
        if not isinstance(attachment, (Attachment, str, Path)):
            raise TypeError(
                'Attachment type must be Attachment, string or path-like')

        if isinstance(attachment, Attachment):
            key = attachment.key
        else:
            key = str(attachment)

        if key in self.data:
            del self.data[key]
        else:
            log.warning('Attempt to remove %s from the attachments dictionary, but it was not there'
                        % key)


class SampleDict(ResettableDict):
    """A dictionary of samples"""

    def __init__(self, initialdata=None):
        super().__init__(initialdata)

    def add(self, sample: Sample | str):
        """
        Add a sample to the Sample dictionary.

        Parameters
        ----------
        sample : Sample | str
            The sample to be added.

        Returns
        -------

        """
        if not isinstance(sample, (Sample, str)):
            raise TypeError('Sample type must be Sample or string')

        if isinstance(sample, str):
            # if it is a str, just make a sample out of it.
            sample = Sample(sample)

        if sample.full_name in self.data:
            raise autoerror.SampleNameAlreadyExisting(
                f'Attempt to add another sample with the same key ({sample.full_name})')

        self.data[sample.full_name] = sample

    def remove(self, sample: Sample | str) -> None:
        """
        Remove a sample from the dictionary.

        Parameters
        ----------
        sample : Sample | str
            The sample that must be removed.

        Returns
        -------

        """
        if not isinstance(sample, (Sample, str)):
            raise TypeError('Sample type must be Sample or string')

        if isinstance(sample, Sample):
            key = sample.full_name
        else:
            key = sample

        if key in self.data:
            del self.data[key]
        else:
            log.warning(
                'Attempt to remove %s from the sample dictionary, but it was not there' % key)


class VideoDict(ResettableDict):
    """A dictionary of videos."""

    def __init__(self, initialdata=None):
        super().__init__(initialdata)

    def add(self, video: str | Path | Video):
        """
        Add a video to the dictionary

        Parameters
        ----------
        video : str | Path | Video

        Raises
        ------
        TypeError: if video is not one of the accepted types.
        KeyError: if adding another video with already used key

        Returns
        -------
        None
        """
        if not isinstance(video, (str | Path | Video)):
            raise TypeError('Video type must be Video, string or path-like')

        if not isinstance(video, Video):
            video = Video(video)

        if video.key in self.data:
            raise KeyError(
                'Attempt to add another video with the same key %s' % video.key)

        self.data[video.key] = video

    def remove(self, video: Video | str | Path) -> None:
        """
        Remove a video from the dictionary

        Parameters
        ----------
        video : Video | str | Path
            The video to be removed.

        Raises
        ------
        TypeError: if video is not one of the acceptable types.

        Returns
        -------
        None.
        """
        if not isinstance(video, (Video, str, Path)):
            raise TypeError('Video type must be Video, string or path-like')

        if isinstance(video, Video):
            key = video.key
        else:
            key = str(video)

        if key in self.data:
            del self.data[key]
        else:
            log.warning('Attempt to remove %s from the video dictionary, but it was not there'
                        % key)


class NavigationImagesList(ResettableList):
    """
    A subclass of resettable list to hold navigation images.

    The only difference between this subclass and a normal ResettableList
    is that we do a type check on append.

    Object added to the list must be either Path or string pointing to the navigation image path.
    When adding a Path, this is internally converted to a string.
    """

    def __init__(self, initialdata=None):
        super().__init__(initialdata)

    def append(self, image: Path | str) -> None:
        """
        Append an item.

        Parameters
        ----------
        image: Path | str
        """
        if not isinstance(image, (Path, str)):
            raise TypeError('image must be Path or string')

        if isinstance(image, Path):
            image = str(image)
        else:
            image = image

        if image in self.data:
            log.warning(
                'A navigation image with path %s already exists in the list' % image)
        else:
            super().append(image)

    def remove(self, image: Path | str) -> None:
        """
        Remove an image.

        Parameters
        ----------
        image: Path | str

        Returns
        -------

        """
        if not isinstance(image, (Path, str)):
            raise TypeError('image must be Path or string')

        if isinstance(image, Path):
            image = str(image)

        super().remove(image)
