from collections import OrderedDict

from conans.errors import ConanException
from conans.model.pkg_type import PackageType
from conans.model.recipe_ref import RecipeReference
from conans.model.version_range import VersionRange


class Requirement:
    """ A user definition of a requires in a conanfile
    """
    def __init__(self, ref, *, headers=None, libs=None, build=False, run=None, visible=None,
                 transitive_headers=None, transitive_libs=None, test=None, package_id_mode=None,
                 force=None, override=None, direct=None, options=None):
        # * prevents the usage of more positional parameters, always ref + **kwargs
        # By default this is a generic library requirement
        self.ref = ref
        self._headers = headers  # This dependent node has headers that must be -I<headers-path>
        self._libs = libs
        self._build = build  # This dependent node is a build tool that runs at build time only
        self._run = run  # node contains executables, shared libs or data necessary at host run time
        self._visible = visible  # Even if not libsed or visible, the node is unique, can conflict
        self._transitive_headers = transitive_headers
        self._transitive_libs = transitive_libs
        self._test = test
        self._package_id_mode = package_id_mode
        self._force = force
        self._override = override
        self._direct = direct
        self.options = options

    @property
    def skip(self):
        return not (self.headers or self.libs or self.run or self.build)

    @staticmethod
    def _default_if_none(field, default_value):
        return field if field is not None else default_value

    @property
    def headers(self):
        return self._default_if_none(self._headers, True)

    @headers.setter
    def headers(self, value):
        self._headers = value

    @property
    def libs(self):
        return self._default_if_none(self._libs, True)

    @libs.setter
    def libs(self, value):
        self._libs = value

    @property
    def visible(self):
        return self._default_if_none(self._visible, True)

    @visible.setter
    def visible(self, value):
        self._visible = value

    @property
    def test(self):
        return self._default_if_none(self._test, False)

    @test.setter
    def test(self, value):
        self._test = value

    @property
    def force(self):
        return self._default_if_none(self._force, False)

    @force.setter
    def force(self, value):
        self._force = value

    @property
    def override(self):
        return self._default_if_none(self._override, False)

    @override.setter
    def override(self, value):
        self._override = value

    @property
    def direct(self):
        return self._default_if_none(self._direct, True)

    @direct.setter
    def direct(self, value):
        self._direct = value

    @property
    def build(self):
        return self._build

    @build.setter
    def build(self, value):
        self._build = value

    @property
    def run(self):
        return self._default_if_none(self._run, False)

    @run.setter
    def run(self, value):
        self._run = value

    @property
    def transitive_headers(self):
        return self._transitive_headers

    @transitive_headers.setter
    def transitive_headers(self, value):
        self._transitive_headers = value

    @property
    def transitive_libs(self):
        return self._transitive_libs

    @transitive_libs.setter
    def transitive_libs(self, value):
        self._transitive_libs = value

    @property
    def package_id_mode(self):
        return self._package_id_mode

    @package_id_mode.setter
    def package_id_mode(self, value):
        self._package_id_mode = value

    def __repr__(self):
        return repr(self.__dict__)

    def __str__(self):
        traits = 'build={}, headers={}, libs={}, '  \
                 'run={}, visible={}'.format(self.build, self.headers, self.libs, self.run,
                                             self.visible)
        return "{}, Traits: {}".format(self.ref, traits)

    def copy_requirement(self):
        return Requirement(self.ref, headers=self.headers, libs=self.libs, build=self.build,
                           run=self.run, visible=self.visible,
                           transitive_headers=self.transitive_headers,
                           transitive_libs=self.transitive_libs)

    @property
    def version_range(self):
        """ returns the version range expression, without brackets []
        or None if it is not an expression
        """
        version = repr(self.ref.version)
        if version.startswith("[") and version.endswith("]"):
            return VersionRange(version[1:-1])

    @property
    def alias(self):
        version = repr(self.ref.version)
        if version.startswith("(") and version.endswith(")"):
            return RecipeReference(self.ref.name, version[1:-1], self.ref.user, self.ref.channel,
                                   self.ref.revision)

    def process_package_type(self, node):
        """If the requirement traits have not been adjusted, then complete them with package type
        definition"""

        pkg_type = node.conanfile.package_type

        def set_if_none(field, value):
            if getattr(self, field) is None:
                setattr(self, field, value)

        if pkg_type is PackageType.APP:
            # Change the default requires headers&libs to False for APPS
            set_if_none("_headers", False)
            set_if_none("_libs", False)
            set_if_none("_run", True)
        elif pkg_type is PackageType.SHARED:
            set_if_none("_run", True)
        elif pkg_type is PackageType.STATIC:
            set_if_none("_run", False)
        elif pkg_type is PackageType.HEADER:
            set_if_none("_run", False)
            set_if_none("_libs", False)
            set_if_none("_headers", True)
        elif pkg_type is PackageType.BUILD_SCRIPTS:
            set_if_none("_run", False)
            set_if_none("_libs", False)
            set_if_none("_headers", False)
            set_if_none("_visible", False)  # Conflicts might be allowed for this kind of package

    def __hash__(self):
        return hash((self.ref.name, self.build))

    def __eq__(self, other):
        """If the name is the same and they are in the same context, and if both of them are
        propagating includes or libs or run info or both are visible or the reference is the same,
        we consider the requires equal, so they can conflict"""
        return (self.ref.name == other.ref.name and self.build == other.build and
                (self.override or  # an override with same name and context, always match
                 (self.headers and other.headers) or
                 (self.libs and other.libs) or
                 (self.run and other.run) or
                 (self.visible and other.visible) or
                 (self.ref == other.ref)))

    def aggregate(self, other):
        """ when closing loop and finding the same dependency on a node, the information needs
        to be aggregated
        :param other: is the existing Require that the current node has, which information has to be
        appended to "self", which is the requires that is being propagated to the current node
        from upstream
        """
        assert self.build == other.build
        if other.override:
            # If the other aggregated is an override, it shouldn't add information
            # it already did override upstream, and the actual information used in this node is
            # the propagated one.
            self.force = True
            return
        self.headers |= other.headers
        self.libs |= other.libs
        self.run = self.run or other.run
        self.visible |= other.visible
        self.force |= other.force
        if not other.test:
            self.test = False  # it it was previously a test, but also required by non-test
        # TODO: self.package_id_mode => Choose more restrictive?

    def transform_downstream(self, pkg_type, require, dep_pkg_type):
        """

        consumer ---self--->  foo<pkg_type> ---require---> bar<dep_pkg_type>
            \\ -------------------????-------------------- /
        Compute new Requirement to be applied to "consumer" translating the effect of the dependency
        to such "consumer".
        Result can be None if nothing is to be propagated
        """
        if require.visible is False:
            # TODO: We could implement checks in case private is violated (e.g shared libs)
            return

        if require.build:  # public!
            # TODO: To discuss if this way of conflicting build_requires is actually useful or not
            downstream_require = Requirement(require.ref, headers=False, libs=False, build=True,
                                             run=False, visible=True, direct=False)
            return downstream_require

        if self.build:  # Build-requires
            # If the above is shared or the requirement is explicit run=True
            if dep_pkg_type is PackageType.SHARED or require.run:
                downstream_require = Requirement(require.ref, headers=False, libs=False, build=True,
                                                 run=True, visible=False, direct=False)
                return downstream_require
            return

        # Regular and test requires
        if dep_pkg_type is PackageType.SHARED:
            if pkg_type is PackageType.SHARED:
                downstream_require = Requirement(require.ref, headers=False, libs=False, run=True)
            elif pkg_type is PackageType.STATIC:
                downstream_require = Requirement(require.ref, headers=False, libs=True, run=True)
            elif pkg_type is PackageType.APP:
                downstream_require = Requirement(require.ref, headers=False, libs=False, run=True)
            else:
                assert pkg_type in (PackageType.UNKNOWN, PackageType.HEADER)
                # TODO: This is undertested, changing it did not break tests
                downstream_require = require.copy_requirement()
        elif dep_pkg_type is PackageType.STATIC:
            if pkg_type is PackageType.SHARED:
                downstream_require = Requirement(require.ref, headers=False, libs=False, run=False)
            elif pkg_type is PackageType.STATIC:
                downstream_require = Requirement(require.ref, headers=False, libs=True, run=False)
            elif pkg_type is PackageType.APP:
                downstream_require = Requirement(require.ref, headers=False, libs=False, run=False)
            else:
                assert pkg_type in (PackageType.UNKNOWN, PackageType.HEADER)
                # TODO: This is undertested, changing it did not break tests
                downstream_require = require.copy_requirement()
        elif dep_pkg_type is PackageType.HEADER:
            downstream_require = Requirement(require.ref, headers=False, libs=False, run=False)
        else:
            # Unknown, default. This happens all the time while check_downstream as shared is unknown
            # FIXME
            downstream_require = require.copy_requirement()
            if pkg_type in (PackageType.SHARED, PackageType.STATIC, PackageType.APP):
                downstream_require.headers = False
            if pkg_type in (PackageType.SHARED, PackageType.APP):
                downstream_require.libs = False

        assert require.visible, "at this point require should be visible"

        if require.transitive_headers is not None:
            downstream_require.headers = require.transitive_headers

        if require.transitive_libs is not None:
            downstream_require.libs = require.transitive_libs

        # If non-default, then the consumer requires has priority
        if self.visible is False:
            downstream_require.visible = False

        if self.headers is False:
            downstream_require.headers = False

        if self.libs is False:
            downstream_require.libs = False

        # TODO: Automatic assignment invalidates user possibility of overriding default
        # if required.run is not None:
        #    downstream_require.run = required.run

        if self.test:
            downstream_require.test = True

        downstream_require.direct = False
        return downstream_require

    def deduce_package_id_mode(self, pkg_type, dep_node, non_embed_mode, embed_mode, build_mode,
                               unknown_mode):
        # If defined by the ``require(package_id_mode=xxx)`` trait, that is higher priority
        # The "conf" values are defaults, no hard overrides
        if self.package_id_mode:
            return

        dep_conanfile = dep_node.conanfile
        dep_pkg_type = dep_conanfile.package_type
        if self.build:
            build_mode = getattr(dep_conanfile, "build_mode", build_mode)
            if build_mode and self.direct:
                self.package_id_mode = build_mode
            return  # At the moment no defaults

        if pkg_type is PackageType.HEADER:
            self.package_id_mode = "unrelated_mode"
            return

        # If the dependency defines the mode, that has priority over default
        embed_mode = getattr(dep_conanfile, "package_id_embed_mode", embed_mode)
        non_embed_mode = getattr(dep_conanfile, "package_id_non_embed_mode", non_embed_mode)
        unknown_mode = getattr(dep_conanfile, "package_id_unknown_mode", unknown_mode)
        if self.headers or self.libs:  # only if linked
            if pkg_type in (PackageType.SHARED, PackageType.APP):
                if dep_pkg_type is PackageType.SHARED:
                    self.package_id_mode = non_embed_mode
                else:
                    self.package_id_mode = embed_mode
            elif pkg_type is PackageType.STATIC:
                if dep_pkg_type is PackageType.HEADER:
                    self.package_id_mode = embed_mode
                else:
                    self.package_id_mode = non_embed_mode

            if self.package_id_mode is None:
                self.package_id_mode = unknown_mode

        # For cases like Application->Application, without headers or libs, package_id_mode=None
        # It will be independent by default


class BuildRequirements:
    # Just a wrapper around requires for backwards compatibility with self.build_requires() syntax
    def __init__(self, requires):
        self._requires = requires

    def __call__(self, ref, package_id_mode=None, visible=False, run=None, options=None):
        # TODO: Check which arguments could be user-defined
        self._requires.build_require(ref, package_id_mode=package_id_mode, visible=visible, run=run,
                                     options=options)


class ToolRequirements:
    # Just a wrapper around requires for backwards compatibility with self.build_requires() syntax
    def __init__(self, requires):
        self._requires = requires

    def __call__(self, ref, package_id_mode=None, visible=False, run=True, options=None,
                 override=None):
        # TODO: Check which arguments could be user-defined
        self._requires.tool_require(ref, package_id_mode=package_id_mode, visible=visible, run=run,
                                    options=options, override=override)


class TestRequirements:
    # Just a wrapper around requires for backwards compatibility with self.build_requires() syntax
    def __init__(self, requires):
        self._requires = requires

    def __call__(self, ref, run=None):
        self._requires.test_require(ref, run=run)


class Requirements:
    """ User definitions of all requires in a conanfile
    """
    def __init__(self, declared=None, declared_build=None, declared_test=None,
                 declared_build_tool=None):
        self._requires = OrderedDict()
        # Construct from the class definitions
        if declared is not None:
            if isinstance(declared, str):
                declared = [declared, ]
            for item in declared:
                # FIXME: Conan 2.0 Deprecate Conan 1.X definition of tuples, force to use method
                self.__call__(item)
        if declared_build is not None:
            if isinstance(declared_build, str):
                declared_build = [declared_build, ]
            for item in declared_build:
                self.build_require(item)
        if declared_test is not None:
            if isinstance(declared_test, str):
                declared_test = [declared_test, ]
            for item in declared_test:
                self.test_require(item)
        if declared_build_tool is not None:
            if isinstance(declared_build_tool, str):
                declared_build_tool = [declared_build_tool, ]
            for item in declared_build_tool:
                self.build_require(item, run=True)

    def values(self):
        return self._requires.values()

    # TODO: Plan the interface for smooth transition from 1.X
    def __call__(self, str_ref, **kwargs):
        if str_ref is None:
            return
        assert isinstance(str_ref, str)
        ref = RecipeReference.loads(str_ref)
        req = Requirement(ref, **kwargs)
        if self._requires.get(req):
            raise ConanException("Duplicated requirement: {}".format(ref))
        self._requires[req] = req

    def build_require(self, ref, raise_if_duplicated=True, package_id_mode=None, visible=False,
                      run=None, options=None):
        """
             Represent a generic build require, could be a tool, like "cmake" or a bundle of build
             scripts.

             visible = False => Only the direct consumer can see it, won't conflict
             build = True => They run in the build machine (e.g cmake)
             libs = False => We won't link with it, is a tool, no propagate the libs.
             headers = False => We won't include headers, is a tool, no propagate the includes.
             run = None => It will be determined by the package_type of the ref
        """
        if ref is None:
            return
        # FIXME: This raise_if_duplicated is ugly, possibly remove
        ref = RecipeReference.loads(ref)
        req = Requirement(ref, headers=False, libs=False, build=True, run=run, visible=visible,
                          package_id_mode=package_id_mode, options=options)

        if raise_if_duplicated and self._requires.get(req):
            raise ConanException("Duplicated requirement: {}".format(ref))
        self._requires[req] = req

    def override(self, ref):
        req = Requirement(ref)
        old_requirement = self._requires.get(req)
        if old_requirement is not None:
            req.force = True
            self._requires[req] = req
        else:
            req.override = True
            self._requires[req] = req

    def test_require(self, ref, run=None, options=None):
        """
             Represent a testing framework like gtest

             visible = False => Only the direct consumer can see it, won't conflict
             build = False => The test are linked in the host context to run in the host machine
             libs = True => We need to link with gtest
             headers = True => We need to include gtest.
             run = None => It will be determined by the package_type of ref, maybe is gtest shared
        """
        ref = RecipeReference.loads(ref)
        # visible = False => Only the direct consumer can see it, won't conflict
        # build = False => They run in host context, e.g the gtest application is a host app
        # libs = True => We need to link with it
        # headers = True => We need to include it
        req = Requirement(ref, headers=True, libs=True, build=False, run=run, visible=False,
                          test=True, package_id_mode=None, options=options)
        if self._requires.get(req):
            raise ConanException("Duplicated requirement: {}".format(ref))
        self._requires[req] = req

    def tool_require(self, ref, raise_if_duplicated=True, package_id_mode=None, visible=False,
                     run=True, options=None, override=None):
        """
         Represent a build tool like "cmake".

         visible = False => Only the direct consumer can see it, won't conflict
         build = True => They run in the build machine (e.g cmake)
         libs = False => We won't link with it, is a tool, no propagate the libs.
         headers = False => We won't include headers, is a tool, no propagate the includes.
        """
        if ref is None:
            return
        # FIXME: This raise_if_duplicated is ugly, possibly remove
        ref = RecipeReference.loads(ref)
        req = Requirement(ref, headers=False, libs=False, build=True, run=run, visible=visible,
                          package_id_mode=package_id_mode, options=options, override=override)
        if raise_if_duplicated and self._requires.get(req):
            raise ConanException("Duplicated requirement: {}".format(ref))
        self._requires[req] = req

    def __repr__(self):
        return repr(self._requires.values())
