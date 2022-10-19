# Copyright 2019 Splunk Inc. All rights reserved.

"""
### Splunk app packaging standards

These checks validate that a Splunk app has been correctly packaged, and can be provided safely for package validation.
"""
import logging
import os
import stat
import json
from packaging import version
from functools import wraps

import splunk_appinspect
from splunk_appinspect.app_util import AppVersionNumberMatcher

report_display_order = 1
logger = logging.getLogger(__name__)


def app_package_extractable(check):
    """
    Decorator to pre-check if package is extractable
    """

    @wraps(check)
    def wrap(app, reporter):
        if app.package.is_origin_artifact_valid_compressed_file():
            check(app, reporter)
        else:
            reporter_output = (
                "Splunk App package is not a valid compressed file and cannot be extracted."
                f" Origin artifact name: {app.package.origin_artifact_name}"
            )
            reporter.fail(reporter_output)

    return wrap


# ------------------------------------------------------------------------------
# ORIGIN ARTIFACT CHECKS
# ------------------------------------------------------------------------------
@splunk_appinspect.tags(
    "splunk_appinspect",
    "appapproval",
    "cloud",
    "packaging_standards",
    "self-service",
    "private_app",
    "private_victoria",
    "private_classic"
)
@splunk_appinspect.cert_version(min="1.5.0")
@app_package_extractable
def check_that_splunk_app_package_has_read_permission(app, reporter):
    """Check that the Splunk app provided does not contain incorrect permissions.
    Packages must have have the owner's read permission set to r (400).
    """
    # TODO(PBL-5212): produce actionable app inspect output instead of 'Permission denied' error
    if not app.package.does_origin_artifact_have_read_permission():
        reporter_output = (
            "Splunk App package does not contain owner read"
            " permission and cannot be extracted."
        )
        reporter.fail(reporter_output)


@splunk_appinspect.tags(
    "splunk_appinspect",
    "appapproval",
    "cloud",
    "packaging_standards",
    "self-service",
    "private_app",
    "private_victoria",
    "private_classic"
)
@splunk_appinspect.cert_version(min="1.5.0")
def check_that_splunk_app_package_valid_compressed_file(app, reporter):
    """Check that the Splunk app provided a valid compressed file."""
    if not app.package.is_origin_artifact_valid_compressed_file():
        reporter_output = (
            "Splunk App package is not a valid compressed file and cannot be extracted. "
            f"Origin artifact name: {app.package.origin_artifact_name}"
        )
        reporter.fail(reporter_output)


@splunk_appinspect.tags(
    "splunk_appinspect",
    "appapproval",
    "cloud",
    "packaging_standards",
    "self-service",
    "private_app",
    "private_victoria",
    "private_classic"
)
@splunk_appinspect.cert_version(min="1.5.0")
def check_that_splunk_app_package_name_does_not_start_with_period(app, reporter):
    """Check that the Splunk app provided does not start with a `.`
    character.
    """
    if app.package.does_origin_artifact_start_with_period():
        if app.package.origin_artifact_name.startswith("."):
            reporter_output = (
                "Splunk App packages cannot start with a `.` as its name. "
                f"Origin artifact name: {app.package.origin_artifact_name}"
            )
        else:
            reporter_output = (
                "Splunk App packages cannot start with a `.` as its name. "
                f"Origin package name: {app.package.origin_package_name}"
            )
        reporter.fail(reporter_output)


# ------------------------------------------------------------------------------
# WORKING ARTIFACT CHECKS
# ------------------------------------------------------------------------------
@splunk_appinspect.tags(
    "splunk_appinspect",
    "appapproval",
    "cloud",
    "packaging_standards",
    "self-service",
    "private_app",
    "private_victoria",
    "private_classic"
)
@splunk_appinspect.cert_version(min="1.5.0")
def check_that_splunk_app_package_extracts_to_visible_directory(app, reporter):
    """Check that the compressed artifact extracts to a directory that does not
    start with a `.` character.
    """
    if app.package.working_artifact_name.startswith("."):
        reporter_output = (
            "Splunk App packages must extract to a directory"
            " that is not hidden. The Splunk App package"
            f" extracted to: {app.package.working_artifact_name}"
        )

        reporter.fail(reporter_output)


@splunk_appinspect.tags(
    "splunk_appinspect",
    "appapproval",
    "cloud",
    "packaging_standards",
    "self-service",
    "private_app",
    "private_victoria",
    "private_classic"
)
@splunk_appinspect.cert_version(min="1.5.3")
@app_package_extractable
def check_that_splunk_app_package_does_not_contain_files_outside_of_app(app, reporter):
    """Check that the Splunk App package does not contain any non-app files.
    Files within a valid app folder or valid dependencies within a .dependencies
    folder are permitted, all other files are not.
    """
    # Files inside app package's working_artifact
    for file_or_folder_outside_app in app.package.find_files_not_part_of_valid_apps():
        # Relative path to the app_dir, since these are outside the app_dir they
        # will most likely be of the form "../myfile.txt"
        relative_loc = os.path.relpath(file_or_folder_outside_app, app.app_dir)
        if relative_loc == ".":
            pass
        else:
            reporter_output = (
                "A file or folder was found outside of the app"
                f" directory. Please remove this file or folder: {relative_loc}"
            )
            reporter.fail(reporter_output)

    # Special case: if an origin artifact has non-app files associated with it
    # those are passed to the app.package to be called out here
    # For example, a tarball of tarball apps mixed with non-app files.
    # The app.package would be the first valid app tarball, the paths to
    # the non-app files within the overall package are captured here.

    # Files inside the origin package's working_artifact
    for file_or_folder_outside_app in app.package.origin_package_non_app_files:
        # These paths are relative to the origin app package which may or may
        # not be relative to the app_dir.
        reporter_output = (
            "A file or folder was found outside of the app"
            " within the overall package. OR the file or folder does not have expected permission. "
            f"Please remove this file or folder OR modify the permission : {file_or_folder_outside_app}"
        )
        reporter.fail(reporter_output)


@splunk_appinspect.tags(
    "splunk_appinspect",
    "appapproval",
    "cloud",
    "packaging_standards",
    "self-service",
    "private_app",
    "private_victoria",
    "private_classic"
)
@splunk_appinspect.cert_version(min="1.5.3")
@app_package_extractable
def check_that_splunk_app_package_with_static_dependencies_has_exactly_one_app_folder(
        app, reporter
):
    """Check that the Splunk App package with a .dependencies directory also
    contains exactly one valid app folder.
    """
    # If no .dependencies folder exists, return N/A
    if not app.package.does_package_contain_dependencies_folder():
        reporter_output = (
            f"No {app.dependencies_directory_path} folder found. "
            "Please add a .dependencies directory with an valid "
            "app folder."
        )
        reporter.not_applicable(reporter_output)
        return

    # If .dependencies folder exists but more than one folder exists as
    # sibling directories, return FAIL (app of apps + .dependencies are not
    # supported, only one or the other)
    contents = os.listdir(app.package.working_artifact)
    all_contents_are_folders = all(
        [
            os.path.isdir(os.path.join(app.package.working_artifact, path))
            for path in contents
        ]
    )
    relative_dependencies_path = app.package.DEPENDENCIES_LOCATION
    relative_working_app_path = os.path.relpath(
        app.package.working_app_path, app.package.working_artifact
    )
    if (
            len(contents) != 2
            or not all_contents_are_folders
            or relative_dependencies_path not in contents
            or relative_working_app_path not in contents
    ):
        reporter_output = (
            f"Only a single app folder and a single {app.dependencies_directory_path} "
            "folder should be included for apps packaged with static dependencies "
            "using the Splunk Packaging Toolkit."
        )
        reporter.fail(reporter_output)


@splunk_appinspect.tags(
    "splunk_appinspect",
    "appapproval",
    "cloud",
    "packaging_standards",
    "self-service",
    "private_app",
    "private_victoria",
    "private_classic"
)
@splunk_appinspect.cert_version(min="1.5.3")
@app_package_extractable
def check_that_splunk_app_package_with_static_dependencies_has_app_manifest(
        app, reporter
):
    """Check that the Splunk App package with a .dependencies directory also
    contains an app folder with an app.manifest.
    """
    # If no .dependencies folder exists, return N/A
    if not app.package.does_package_contain_dependencies_folder():
        reporter_output = (
            f"No {app.dependencies_directory_path} folder found. "
            "Please add a .dependencies directory that contains "
            "an app folder with an app.manifest."
        )
        reporter.not_applicable(reporter_output)
        return

    # If .dependencies folder exists and single sibling directory is a valid
    # app but contains no app.manifest, return FAIL (.dependecies is only
    # valid when packaged and specified with slim)
    if not app.package.does_working_artifact_contain_app_manifest():
        reporter_output = (
            "App folder associated with package does not"
            f" contain an app.manifest file but contains "
            f" a {app.dependencies_directory_path} directory."
            " Apps packaged with static dependencies using the"
            " Splunk Packaging Toolkit are required to have an"
            " app.manifest file."
        )
        reporter.fail(reporter_output)


@splunk_appinspect.tags(
    "splunk_appinspect",
    "appapproval",
    "cloud",
    "packaging_standards",
    "self-service",
    "private_app",
    "private_victoria",
    "private_classic"
)
@splunk_appinspect.cert_version(min="1.5.3")
@app_package_extractable
def check_that_splunk_app_package_has_valid_static_dependencies(app, reporter):
    """Check that the Splunk App package contains only valid dependencies.
    Dependencies are valid if a .dependencies directory contains only valid
    app packages inside.
    """
    # If no .dependencies folder exists, return N/A
    if not app.package.does_package_contain_dependencies_folder():
        reporter_output = (
            f"No {app.dependencies_directory_path} folder found. "
            "Please check that the Splunk App "
            "package contains only valid dependencies."
        )
        reporter.not_applicable(reporter_output)
        return

    # At this point, we accept that the .dependencies folder is valid - now
    # let's validate the contents of it. It should contain only valid app
    # packages and nothing else
    dependencies_folder = app.package.dependencies_folder
    dependencies_contents = os.listdir(dependencies_folder)

    for dependency_resource in dependencies_contents:
        resource_path = os.path.join(
            app.package.dependencies_folder, dependency_resource
        )
        generated_app_package = app.package.generate_app_package_from_file_or_folder(
            resource_path
        )
        if generated_app_package is None:
            reporter_output = (
                "Resource within the .dependencies folder that"
                " does not appear to be a valid app package."
                " Please remove this file or folder: "
                f" {app.dependencies_directory_path}/{dependency_resource}"
            )
            reporter.fail(reporter_output)

    # TODO: we may want to do some sort of validation that the dependencies
    # listed in app.manifest match what we see in the .dependencies
    # directory at some point. SLIM is probably the best place to do this
    # validation, however it does not appear to be supported at this time.
    # (running `slim validate` on an app with extra apps in the
    # .dependencies folder not listed in the app.manifest does not raise any
    # errors) - see APPMAN-20.


@splunk_appinspect.tags(
    "splunk_appinspect",
    "appapproval",
    "cloud",
    "packaging_standards",
    "self-service",
    "private_app",
    "private_victoria",
    "private_classic"
)
@splunk_appinspect.cert_version(min="1.5.0")
@app_package_extractable
def check_that_extracted_splunk_app_does_not_contain_prohibited_directories_or_files(
        app, reporter
):
    """Check that the extracted Splunk App does not contain any directories or
    files that start with a `.`, or directories that start with `__MACOSX`.
    """
    prohibited_directories_and_files = app.package.find_prohibited_files(
        app.package.working_artifact, [app.package.DEPENDENCIES_LOCATION]
    )
    for prohibited_directory_or_file in prohibited_directories_and_files:
        # Relative path to the app_dir
        relative_loc = os.path.relpath(prohibited_directory_or_file, app.app_dir)
        reporter_output = (
            "A prohibited file or directory was found in the"
            f" extracted Splunk App: {relative_loc}"
        )
        reporter.fail(reporter_output)


@splunk_appinspect.tags(
    "splunk_appinspect",
    "appapproval",
    "cloud",
    "packaging_standards",
    "self-service",
    "private_app",
    "private_victoria",
    "private_classic"
)
@splunk_appinspect.cert_version(min="1.5.0")
def check_that_extracted_splunk_app_contains_default_app_conf_file(app, reporter):
    """Check that the extracted Splunk App contains a `default/app.conf`
    file.
    """
    _is_check_app_config_file(app, reporter, "fail")


@splunk_appinspect.tags(
    "splunk_appinspect",
    "appapproval",
    "cloud",
    "packaging_standards",
    "self-service",
    "private_app",
    "private_victoria"
)
@splunk_appinspect.cert_version(min="1.5.0")
def check_valid_version_number(app, reporter):
    """Check that the extracted Splunk App contains a `default/app.conf` file
    that contains an `[id]` or `[launcher]` stanza with a `version` property that
    is formatted as `Major.Minor.Revision`.
    """

    app_config_skip_check = _is_check_app_config_file(app, reporter, "skip")

    if not app_config_skip_check:
        filename = os.path.join("default", "app.conf")
        config = app.get_config(os.path.basename(filename))
        matcher = AppVersionNumberMatcher()
        id_version = launcher_version = None

        try:
            config.has_option("id", "version")
            id_version = config.get("id", "version")
            if not matcher.match(id_version):
                lineno_id_version = config.get_section("id").get_option("version").lineno
                reporter_output = (
                    "`Major.Minor.Revision` version numbering is required "
                    f"in `[id]` section of app.conf. File: {filename}, [id] Line: {lineno_id_version}."
                )
                reporter.fail(reporter_output, filename, lineno_id_version)

        except splunk_appinspect.configuration_file.NoOptionError:
            lineno_id = config.get_section("id").lineno
            reporter_output = (
                "No `version` specified in `[id]` "
                f"section of app.conf. File: {filename}, [id] Line: {lineno_id}."
            )
            reporter.fail(reporter_output, filename, lineno_id)

        except splunk_appinspect.configuration_file.NoSectionError:
            reporter_output = (
                "No `[id]` section found in app.conf file."
            )
            reporter.fail(reporter_output, filename)

        try:
            config.has_option("launcher", "version")
            launcher_version = config.get("launcher", "version")
            if not matcher.match(launcher_version):
                lineno_launcher_version = config.get_section("launcher").get_option("version").lineno
                reporter_output = (
                    "`Major.Minor.Revision` version numbering is required "
                    "in `[launcher]` section of app.conf. "
                    f"File: {filename}, launcher version lineno: {lineno_launcher_version}"
                )
                reporter.fail(reporter_output, filename, lineno_launcher_version)

        except splunk_appinspect.configuration_file.NoOptionError:
            lineno_launcher = config.get_section("launcher").lineno
            reporter_output = (
                "No `version` specified in `[launcher]` "
                f"section of app.conf. File: {filename}, [launcher] line: {lineno_launcher}."
            )
            reporter.fail(reporter_output, filename, lineno_launcher)

        except splunk_appinspect.configuration_file.NoSectionError:
            reporter_output = (
                "No `[launcher]` section found in app.conf file."
            )
            reporter.fail(reporter_output, filename)

        if id_version is not None and launcher_version is not None:
            if version.parse(id_version) != version.parse(launcher_version):
                lineno_id = config.get_section("id").get_option("version").lineno
                lineno_launcher = config.get_section("launcher").get_option("version").lineno
                reporter_output = (
                    "The `id.version` and `launcher.version` is not equivalent."
                    f"Please make sure that `version` of both `[id]` and `[launcher]` section is matching"
                    f"File: {filename}, id.version line: {lineno_id}, launcher.version line: {lineno_launcher}."
                )
                reporter.fail(reporter_output, filename, lineno_id, lineno_launcher)

    if not app.package.does_working_artifact_contain_app_manifest():
        reporter_output = (
            "Splunk App packages doesn't contain"
            " `default/app.manifest file`."
            " No `default/app.manifest` was found."
        )
        reporter.skip(reporter_output)
        return

    manifest_filename = os.path.join("app.manifest")
    try:
        filepath = open(os.path.join(app.app_dir, "app.manifest"), "r")
        manifest_json = json.loads(filepath.read())
        manifest_version = manifest_json.get("info").get("id").get("version")
        if not matcher.match(manifest_version):
            reporter_output = (
                "`Major.Minor.Revision` version numbering is required "
                "in `[info][id]` section of app.manifest. "
                f"File: {manifest_filename}."
            )
            reporter.fail(reporter_output, manifest_filename)

    except ValueError:
        reporter_output = (
            "The app.manifest file is not in correct format. "
            f"File: {manifest_filename}."
        )
        reporter.fail(reporter_output, manifest_filename)
        return

    except KeyError:
        reporter_output = (
            "No `version` specified under `[info][id]` "
            f"section of app.manifest. File: {manifest_filename}."
        )
        reporter.fail(reporter_output, manifest_filename)
        return
    except:
        reporter_output = (
            f"Some other exception came. File: {manifest_filename}"
        )
        reporter.fail(reporter_output, manifest_filename)
        return

    try:
        if version.parse(manifest_version) != version.parse(id_version) and version.parse(
                manifest_version) != version.parse(launcher_version):
            reporter_output = (
                "The `info.id.version` and `id.version` and `launcher.version` is not equivalent."
                "Please make sure that version of info.id, id and launcher tag is matching"
                f"File: {manifest_filename} or {filename}"
            )
            reporter.fail(reporter_output, manifest_filename)
    except:
        reporter_output = (
            f"No `version` found in app.conf or app.manifest file and hence won't be able to check the equivalency. "
            f"File; {manifest_filename} or {filename}"
        )
        reporter.fail(reporter_output, manifest_filename)


def _is_check_app_config_file(app, reporter, status='not_applicable'):
    if not app.package.does_working_artifact_contain_default_app_conf():
        reporter_output = (
            "Splunk App packages should contain a"
            " `default/app.conf file`."
            f" No `default/app.conf` was found in `{app.package.origin_artifact_name}`."
        )

        if status == "fail":
            reporter.fail(reporter_output)
        elif status == "warn":
            reporter.warn(reporter_output)
        elif status == "skip":
            reporter.skip(reporter_output)
        else:
            reporter.not_applicable(reporter_output)

        return True


@splunk_appinspect.tags(
    "splunk_appinspect",
    "appapproval",
    "cloud",
    "packaging_standards",
    "self-service",
    "private_app",
    "private_victoria",
    "private_classic"
)
@splunk_appinspect.cert_version(min="1.5.0")
@app_package_extractable
def check_that_extracted_splunk_app_does_not_contain_invalid_directories(app, reporter):
    """Check that the extracted Splunk App does not contain any directories
    with incorrect permissions. Directories and sub directories
    must have the owner's permissions set to r/w/x (700).
    """

    invalid_directories = app.package.find_invalid_directories_with_wrong_permission(
        app.package.working_artifact, stat.S_IRWXU
    )
    for invalid_directory in invalid_directories:
        reporter_output = f"An invalid directory was found in the extracted Splunk App: {invalid_directory}"
        reporter.fail(reporter_output)


@splunk_appinspect.tags(
    "splunk_appinspect",
    "appapproval",
    "cloud",
    "packaging_standards",
    "self-service",
    "private_app",
    "private_victoria",
    "private_classic"
)
@splunk_appinspect.cert_version(min="1.5.0")
@app_package_extractable
def check_that_extracted_splunk_app_does_not_contain_files_with_invalid_permissions(
        app, reporter
):
    """Check that the extracted Splunk App does not contain any files
    with incorrect permissions. Files must have the owner's
    permissions include read and write (600).
    """
    invalid_files = app.package.find_files_with_incorrect_permissions(
        app.package.working_artifact, stat.S_IRUSR | stat.S_IWUSR
    )
    for invalid_file in invalid_files:
        reporter_output = (
            f"An invalid file was found in the extracted Splunk App: {invalid_file}"
        )
        reporter.fail(reporter_output)


@splunk_appinspect.tags(
    "splunk_appinspect", "cloud", "packaging_standards", "private_app"
)
@splunk_appinspect.cert_version(min="1.0.0")
def check_requires_adobe_flash(app, reporter):
    """Check that the app does not use Adobe Flash files."""
    flash_file_types = [
        ".f4v",
        ".fla",
        ".flv",
        ".jsfl",
        ".swc",
        ".swf",
        ".swt",
        ".swz",
        ".xfl",
    ]
    flash_files = [
        os.path.join(f[0], f[1]) for f in app.iterate_files(types=flash_file_types)
    ]
    if len(flash_files) > 0:
        for flash_file in flash_files:
            reporter_output = f"Flash file was detected. File: {flash_file}"
            reporter.fail(reporter_output, flash_file)
    else:
        reporter_output = "Didn't find any flash files."
        reporter.not_applicable(reporter_output)
