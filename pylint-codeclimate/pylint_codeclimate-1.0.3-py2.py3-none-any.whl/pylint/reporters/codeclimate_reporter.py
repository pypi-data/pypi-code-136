import hashlib
import linecache

from pylint.reporters.json_reporter import JSONReporter

# Code Climate specs
#   https://github.com/codeclimate/platform/blob/master/spec/analyzers/SPEC.md
# GitLab specs:
#   https://docs.gitlab.com/ee/ci/testing/code_quality.html#implementing-a-custom-tool
#
# TODO: Allow a configuration file for severity, categories, etc... (in pyproject.toml?)
#
# FIXME: Use a precise map?
SEVERITY_MAP = {
    "convention": "info",
    "refactor": "minor",
    "warning": "normal",
    "error": "critical",
    "fatal": "blocker",
}

# FIXME: Use a precise map?
# CATEGORIES_MAP = {
#    "": "Potential bug",
#    "": "Clarity",
#    "": "Compatibility",
#    "": "Complexity",
#    "": "Duplication",
#    "": "Performance",
#    "": "Security",
#    "": "Style",
# }


def get_fingerprint(item):
    string = ""
    string += item["path"] + ","
    string += item["message-id"] + ","
    string += str(item["line"]) + ","
    string += str(item["column"] or "") + "\n"

    # FIXME: We should handle the exact string described by the positions
    string += linecache.getline(item["path"], item["line"])
    return hashlib.md5(string.encode("UTF-8")).hexdigest()


class CodeClimateReporter(JSONReporter):
    name = "codeclimate"
    extension = "codeclimate"

    @staticmethod
    def transform(item):
        output = {
            "type": "issue",
            # (required) check_name: "Bug Risk/Unused Variable",
            "description": item["message"].split("\n")[0],
            # "content": A markdown snippet describing the issue, including deeper explanations and links to other resources.
            # (required) "categories": At least one category indicating the nature of the issue being reported.
            "fingerprint": get_fingerprint(item),
            "location": {"path": item["path"]},
            "severity": SEVERITY_MAP[item["type"]],
        }
        # Handle lines vs position
        if item.get("endLine") is not None:
            output["location"]["lines"] = {"begin": item["line"]}
        else:
            # FIXME: if begin to ends spans the whole line, might as well use "lines"
            # and not "position"
            output["location"]["position"] = {
                "begin": {
                    "line": item["line"],
                    "column": item["column"],
                },
                "end": {
                    "line": item["endLine"],
                    "column": item["endColumn"],
                },
            }
        return output

    @staticmethod
    def serialize(message):
        item = JSONReporter.serialize(message)
        return CodeClimateReporter.transform(item)


def register(linter):
    linter.register_reporter(CodeClimateReporter)
