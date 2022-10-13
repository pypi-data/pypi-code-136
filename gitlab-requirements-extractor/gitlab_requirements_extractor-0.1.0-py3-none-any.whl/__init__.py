import argparse
import sys

from loguru import logger

from requirements_extractor.gitlab_connector import GitlabConnector


@logger.catch
def process_once(args=None):
    logger.trace(args)
    parser = argparse.ArgumentParser()
    parser.add_argument('-q', '--quiet', action='store_true', help="Show only warnigns and errors")
    parser.add_argument('-d', '--debug', action='store_true', help="Show more context")
    parser.add_argument('-t', '--trace', action='store_true', help="Show even more context / trace")
    parser.add_argument('-i', '--ignore', action='store_true',
                        help="Ignore state of issue (closed issues will be accepted then)")

    parser.add_argument('-s', '--source', type=str, required=True, help="Source labels (comma separated list)")
    parser.add_argument('-D', '--destination', type=str, default='requirement', help="Destination label")
    parser.add_argument('-p', '--prefix', type=str, default='[REQ]', help="Issue title prefix to add")

    PROCESSED_LABEL = 'requirements_extracted'

    if not args:
        args = sys.argv[1:]
    args = parser.parse_args(args)

    _setup_logger(args)

    gc = GitlabConnector.factory()

    state = 'opened'
    if args.ignore:
        state = None

    if args.prefix and args.prefix[-1] != " ":
        prefix = args.prefix + ' '
    else:
        prefix = args.prefix

    labels = args.source.split(',')
    logger.debug(f"source labels: {labels}")
    logger.debug(f"destination label: {args.destination}")
    logger.debug(f"state: {state}")
    destination_label = args.destination

    # # clean
    # issues = gc.get_all_issues()
    # for i in issues:
    #     if i.iid >= 13:
    #         issue = gc.project.issues.get(i.iid)
    #         logger.info(f"del {i.iid}")
    #         issue.delete()
    # logger.info("deleted")

    issues = gc.get_issues(state=state, labels=labels)
    if not issues:
        logger.info("No matching issues found")
    for parent_req_issue in issues:
        description = parent_req_issue.description
        if PROCESSED_LABEL in parent_req_issue.labels:
            logger.debug(f"Skipping #{parent_req_issue.iid} as it was already processed")
            continue
        logger.info(f"Handling #{parent_req_issue.iid} '{parent_req_issue.title}'")
        req = parent_req_issue.get_requirements()
        for r in req:
            # new issue, set label, link
            issue_args = {
                'title': f'{prefix}{r}',
                'description': f'automatically generated from #{parent_req_issue.iid} ({parent_req_issue.title})'
            }
            issue = gc.project.issues.create(issue_args)
            issue.labels = [destination_label]
            issue.save()
            logger.info(f" - #{issue.iid} {r}")
            gc.link_issues(parent_req_issue.iid, issue)
            description = description.replace(r, f"{r} - #{issue.iid}")

        logger.debug(description)
        handled_issue = gc.project.issues.get(parent_req_issue.iid)
        handled_issue.description = description
        handled_issue.save()
        gc.append_label(PROCESSED_LABEL, parent_req_issue)


def _setup_logger(args):
    level = "INFO"
    if args.trace:
        level = "TRACE"
    elif args.debug:
        level = "DEBUG"
    elif args.quiet:
        level = "WARN"
    logger.remove()
    logger.add(sys.stdout, colorize=True, level=level)
