import os
import logging
import eons
from pathlib import Path
import jsonpickle

######## START CONTENT ########

# All builder errors
class BuildError(Exception, metaclass=eons.ActualType): pass


# Exception used for miscellaneous build errors.
class OtherBuildError(BuildError, metaclass=eons.ActualType): pass


# Project types can be things like "lib" for library, "bin" for binary, etc. Generally, they are any string that evaluates to a different means of building code.
class ProjectTypeNotSupported(BuildError, metaclass=eons.ActualType): pass


class EBBS(eons.Executor):

	def __init__(this):
		super().__init__(name="Eons Basic Build System", descriptionStr="A hackable build system for all builds!")

		# this.RegisterDirectory("ebbs")


	# Register included files early so that they can be used by the rest of the system.
	# If we don't do this, we risk hitting infinite loops because modular functionality relies on these modules.
	# NOTE: this method needs to be overridden in all children which ship included Functors, Data, etc. This is because __file__ is unique to the eons.py file, not the child's location.
	def RegisterIncludedClasses(this):
		super().RegisterIncludedClasses()
		includePaths = [
			'build',
		]
		for path in includePaths:
			this.RegisterAllClassesInDirectory(str(Path(__file__).resolve().parent.joinpath(path)))


	#Configure class defaults.
	#Override of eons.Executor method. See that class for details
	def Configure(this):
		super().Configure()

		this.defaultConfigFile = "build.json"
		this.defaultPrefix = "build"


	#Override of eons.Executor method. See that class for details
	def RegisterAllClasses(this):
		super().RegisterAllClasses()
		# this.RegisterAllClassesInDirectory(os.path.join(os.path.dirname(os.path.abspath(__file__)), "build"))


	#Override of eons.Executor method. See that class for details
	def AddArgs(this):
		super().AddArgs()
		this.argparser.add_argument('-b','--build', type = str, metavar = 'cpp', help = 'script to use for building', dest = 'builder')
		this.argparser.add_argument('-e','--event', type = str, action='append', nargs='*', metavar = 'release', help = 'what is going on that triggered this build?', dest = 'events')


	#Override of eons.Executor method. See that class for details
	def ParseArgs(this):
		super().ParseArgs()

		this.parsedArgs.path = os.getcwd() #used to be arg; now we hard code
		this.rootPath = str(Path(this.parsedArgs.path).resolve())

		this.events = set()
		if (this.parsedArgs.events is not None):
			[[this.events.add(str(e)) for e in l] for l in this.parsedArgs.events]

			if (not this.parsedArgs.builder):
				logging.debug("No build specified. Assuming build pipeline is written in config.")


	#Override of eons.Executor method. See that class for details
	def InitData(this):
		this.rootPath = Path(this.Fetch('path', default='../')).resolve() #ebbs is usually called from a build folder in a project, i.eons. .../build/../ = /


	#Override of eons.Executor method. See that class for details
	def Function(this):
		super().Function()
		build_in = this.Fetch('build_in', default="build")
		if (not this.Build(this.parsedArgs.builder, this.parsedArgs.path, build_in, this.events, **this.extraArgs)):
			logging.critical("Build failed.")


	#Run a build script.
	#RETURNS whether or not the build was successful.
	def Build(this, build, path, build_in, events, **kwargs):
		if (not build):
			build = "default"

		# prettyPath = str(Path(path).joinpath(build_in).resolve())
		# logging.debug(f"Building {build} in {prettyPath} with events {events} and additional args: {kwargs}")

		return this.Execute(build, path=path, build_in=build_in, events=events, **kwargs)


class Builder(eons.StandardFunctor):
	def __init__(this, name=eons.INVALID_NAME()):
		super().__init__(name)

		# What can this build, "bin", "lib", "img", ... ?
		this.supportedProjectTypes = []

		this.projectType = None
		this.projectName = None
		this.clearBuildPath = False

		this.configNameOverrides = {
			"name": "projectName",
			"type": "projectType",
		}

		this.enableRollback = False

		this.events = []


	# Build things!
	# Override this or die.
	# Empty Builders can be used with build.json to start build trees.
	def Build(this):
		pass


	# Override this to perform whatever success checks are necessary.
	# This will be called before running the next build step.
	def DidBuildSucceed(this):
		return True


	# API compatibility shim
	def DidFunctionSucceed(this):
		return this.DidBuildSucceed()


	# Hook for any pre-build configuration
	def PreBuild(this):
		pass


	# Hook for any post-build configuration
	def PostBuild(this):
		pass


	# Sets the build path that should be used by children of *this.
	# Also sets src, inc, lib, and dep paths, if they are present.
	def PopulatePaths(this, rootPath, buildFolder):
		if (rootPath is None):
			logging.warning("no \"dir\" supplied. buildPath is None")
			return

		this.rootPath = str(Path(rootPath).resolve())
		logging.debug(f"rootPath for {this.name} is {this.rootPath}")

		this.buildPath = str(Path(this.rootPath).joinpath(buildFolder))
		Path(this.buildPath).mkdir(parents=True, exist_ok=True)

		logging.debug(f"buildPath for {this.name} is {this.buildPath}")

		paths = [
			"src",
			"inc",
			"dep",
			"lib",
			"bin",
			"test"
		]
		for path in paths:
			tmpPath = os.path.abspath(os.path.join(this.rootPath, path))
			if (os.path.isdir(tmpPath)):
				setattr(this, f"{path}Path", tmpPath)
			else:
				setattr(this, f"{path}Path", None)
			logging.debug(f"{path}Path for {this.name} is {getattr(this, f'{path}Path')}")


	# Populate the configuration details for *this.
	def PopulateLocalConfig(this, configName="build.json"):
		this.config = None
		localConfigFile = os.path.join(this.rootPath, configName)
		logging.debug(f"Looking for local configuration: {localConfigFile}")
		if (os.path.isfile(localConfigFile)):
			configFile = open(localConfigFile, "r")
			this.config = jsonpickle.decode(configFile.read())
			configFile.close()
			logging.debug(f"Got local config contents: {this.config}")


	# Calls PopulatePaths and PopulateVars after getting information from local directory
	# Projects should have a name of {project-type}_{project-name}.
	# For information on how projects should be labelled see: https://eons.llc/convention/naming/
	# For information on how projects should be organized, see: https://eons.llc/convention/uri-names/
	def PopulateProjectDetails(this):
		this.PopulatePaths(this.kwargs.pop("path"), this.kwargs.pop('build_in'))
		this.PopulateLocalConfig()

		# This is messy because we can't query this.name or executor.name and need to get "name" from a config or arg val to set projectName.
		for key, mem in this.configNameOverrides.items():
			this.Set(key, this.FetchWithout(['this', 'executor', 'precursor'], key, default=this.executor.FetchWithout(['this'], key, default=None, start=False)))
			if (getattr(this, mem) is None):
				logging.warning(f"Not configured: {key}")

		# The clearBuildPath needs to be even more conserved than the configNameOverrides.
		# The 'clear_build_path' key is required but must come from either an argument or the config.
		this.clearBuildPath = this.Fetch('clear_build_path', False, ['args', 'config'])

		details = os.path.basename(this.rootPath).split("_")
		if (this.projectType is None):
			this.projectType = details[0]
		if (this.projectName is None):
			if (len(details) > 1):
				this.projectName = '_'.join(details[1:])
			else:
				this.projectName = eons.INVALID_NAME()


	# When Fetching what to do next, we want either the executor's config or our config. Everything else will just muck things up.
	def PopulateNext(this):
		this.Set('next', this.Fetch('next', [], ['args', 'config']))


	# Override of eons.UserFunctor method. See that class for details.
	def ParseInitialArgs(this):
		super().ParseInitialArgs()
		this.events = this.kwargs.pop('events')
		this.PopulateProjectDetails()


	# RETURNS whether or not we should trigger the next Builder based on what events invoked ebbs.
	# Anything in the "run_when_any" list will require a corresponding --event specification to run.
	# For example "run_when_any":["publish"] would require `--event publish` to enable publication Builders in the workflow.
	def ValidateNext(this, nextBuilder):
		if ("run_when_none" in nextBuilder):
			if ([r for r in nextBuilder["run_when_none"] if r in this.events]):
				logging.info(f"Skipping next builder: {nextBuilder['build']}; prohibitive events found (cannot have any of {nextBuilder['run_when_none']} and have {this.events})")
				return False

		if ("run_when_any" in nextBuilder):
			if (not [r for r in nextBuilder["run_when_any"] if r in this.events]): #[] is false
				logging.info(f"Skipping next builder: {nextBuilder['build']}; required events not met (needs any of {nextBuilder['run_when_any']} but only have {this.events})")
				return False

		if ("run_when_all" in nextBuilder):
			if (not set([str(r) for r in nextBuilder["run_when_all"]]).issubset(this.events)):
				logging.info(f"Skipping next builder: {nextBuilder['build']}; required events not met (needs all {nextBuilder['run_when_all']} but only have {this.events})")
				return False

		return True


	# Creates the folder structure for the next build step.
	# RETURNS the next buildPath.
	def PrepareNext(this, nextBuilder):
		logging.debug(f"<---- Preparing for next builder: {nextBuilder['build']} ---->")
		# logging.debug(f"Preparing for next builder: {nextBuilder}")

		nextPath = "."
		if ("path" in nextBuilder):
			nextPath = nextBuilder["path"]
		nextPath = os.path.join(this.buildPath, nextPath)
		# mkpath(nextPath) <- just broken.
		Path(nextPath).mkdir(parents=True, exist_ok=True)
		logging.debug(f"Next build path is: {nextPath}")

		if ("copy" in nextBuilder):
			for cpy in nextBuilder["copy"]:
				# logging.debug(f"copying: {cpy}")
				for src, dst in cpy.items():
					this.Copy(src, dst, root=this.executor.rootPath)

		if ("config" in nextBuilder):
			nextConfigFile = os.path.join(nextPath, "build.json")
			logging.debug(f"writing: {nextConfigFile}")
			nextConfig = open(nextConfigFile, "w")
			for key, var in this.configNameOverrides.items():
				if (key not in nextBuilder["config"]):
					val = getattr(this, var)
					logging.debug(f"Adding to config: {key} = {val}")
					nextBuilder["config"][key] = val
			nextConfig.write(jsonpickle.encode(nextBuilder["config"]))
			nextConfig.close()

		logging.debug(f">---- Completed preparation for: {nextBuilder['build']} ----<")
		return nextPath


	# Runs the next Builder.
	# Uses the Executor passed to *this.
	# RETURNS: True if all next build steps succeeded; False if any Failed.
	def CallNext(this):
		if (this.next is None):
			return None

		ret = True
		for nxt in this.next:
			if (not this.ValidateNext(nxt)):
				continue
			nxtPath = this.PrepareNext(nxt)
			buildFolder = f"then_build_{nxt['build']}"
			if ("build_in" in nxt):
				buildFolder = nxt["build_in"]
			ret = this.executor.Build(
				build=nxt["build"],
				path=nxtPath,
				build_in=buildFolder,
				events=this.events,
				precursor=this)
			if (not ret):
				ret = False
				if ('tolerate_failure' not in nxt or not nxt['tolerate_failure']):
					logging.error(f"Building {nxt['build']} failed. Aborting.")
					return ret
		return ret


	# Override of eons.UserFunctor method. See that class for details.
	def ValidateArgs(this):
		super().ValidateArgs()


	# Override of eons.Functor method. See that class for details
	def Function(this):
		logging.debug(f"<---- Preparing {this.name} ---->")

		if (this.clearBuildPath):
			this.Delete(this.buildPath)

		# mkpath(this.buildPath) <- This just straight up doesn't work. Race condition???
		Path(this.buildPath).mkdir(parents=True, exist_ok=True)
		os.chdir(this.buildPath)

		this.PreBuild()

		if (len(this.supportedProjectTypes) and this.projectType not in this.supportedProjectTypes):
			raise ProjectTypeNotSupported(
				f"{this.projectType} is not supported. Supported project types for {this.name} are {this.supportedProjectTypes}")

		logging.debug(f">---- Done Preparing {this.name} ----<")

		logging.info(f"Using {this.name} to build \"{this.projectName}\", a \"{this.projectType}\" in {this.buildPath}")

		logging.debug(f"<---- Building {this.name} ---->")
		this.Build()
		logging.debug(f">---- Done Building {this.name} ----<")

		this.PostBuild()

