from collections import Counter

def generate_case_json(case):
    case_json = {}
    case_json["case_name"] = case.case_name
    case_json["case_description"] = case.case_description
    case_json["log_message"] = case.log_message
    case_json["start_time"] = case.start_time
    case_json["end_time"] = case.end_time
    case_json["status"] = case.status
    case_json["message"] = case.message
    return case_json

def generate_test_json(test):
    test_json = {}
    test_json["test_name"] = test.test_name
    test_json["test_description"] = test.test_description
    test_json["start_time"] = test.start_time
    test_json["end_time"] = test.end_time
    test_json["message"] = test.message
    test_json["case"] = []
    case_status_list = []
    for case in test.cases:
        test_json["case"].append(generate_case_json(case))
        case_status_list.append(case.status)
    test_json["summary"] = get_summary_from_statuses(case_status_list)
    test_json["status"] = get_status_from_summary(test_json["summary"])
    return test_json

def get_summary_from_statuses(status_list):
    status_summary_mapping = {
        "UNKNOWN" : "unknown",
        "PASS" : "passed",
        "WARN" : "warned",
        "FAIL" : "failed",
        "SKIP" : "skipped"
    }
    status_counts = dict(Counter(status_list))
    summary_dict = {
        "unknown": 0,
        "passed":0,
        "warned":0,
        "failed":0,
        "skipped":0
    }
    for status in status_counts.keys():
        summary_dict[status_summary_mapping[status]] = status_counts[status]
    return summary_dict

def get_status_from_summary(summary):
    if (summary["failed"] > 0):
        return "FAIL"
    elif (summary["passed"] > 0):
        return "PASS"
    elif (summary["skipped"] > 0):
        return "SKIP"
    elif (summary["warned"] > 0):
        return "WARN"
    return "UNKNOWN"

def generate_phase_json(phase):
    phase_json = {}
    phase_json["phase_name"] = phase.phase_name
    phase_json["phase_description"] = phase.phase_description
    phase_json["start_time"] = phase.start_time
    phase_json["end_time"] = phase.end_time
    phase_json["tests"] = []
    test_summary_list = []
    for test in phase.tests:
        test_json = generate_test_json(test)
        phase_json["tests"].append(test_json)
        test_summary_list.append(test_json["summary"])
    phase_json["summary"] = get_summary_from_summaries(test_summary_list)
    phase_json["status"] = get_status_from_summary(phase_json["summary"])
    return phase_json

def get_summary_from_summaries(summary_list):
    summary_dict = {
        "unknown": 0,
        "passed":0,
        "warned":0,
        "failed":0,
        "skipped":0
    }
    for summary in summary_list:
        for key in summary:
            summary_dict[key] += summary[key]
    return summary_dict

def generate_report_json(report):
    report_json = {}
    report_json["schema_name"] = report.schema_name
    report_json["schema_version"] = report.schema_version
    report_json["testbed_name"] = report.testbed_name
    report_json["testbed_version"] = report.testbed_version
    report_json["testbed_description"] = report.testbed_description
    report_json["platform_name"] = report.platform_name
    report_json["platform_description"] = report.platform_description
    # report_json["input_parameters"] = self.input_parameters
    report_json["start_time"] = report.start_time
    report_json["end_time"] = report.end_time
    report_json["phases"] =[]
    phase_summary_list = []
    for phase in report.phases:
        phase_json = generate_phase_json(phase)
        report_json["phases"].append(phase_json)
        phase_summary_list.append(phase_json["summary"])
    report_json["summary"] = get_summary_from_summaries(phase_summary_list)
    report_json["status"] = get_status_from_summary(report_json["summary"])
    return report_json