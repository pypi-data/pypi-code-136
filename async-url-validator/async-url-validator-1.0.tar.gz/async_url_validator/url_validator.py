import csv
import aiohttp
import asyncio
import platform

from async_url_validator.status_assigner import BaseStatusAssigner, StatusAssigner
from async_url_validator.throttle import BaseThrottler, DomainThrottler
import argparse

if platform.system() == 'Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


class URLValidator:
    def __init__(self, timeout=5, request_method='GET', throttler=None, status_assigner=None):
        self._timeout = aiohttp.ClientTimeout(total=timeout)
        self.request_method = request_method
        self._throttler = throttler or BaseThrottler()
        self._status_assigner = status_assigner or BaseStatusAssigner()

    async def validate(self, *urls):
        async with aiohttp.ClientSession(timeout=self._timeout) as self._session:
            for task in self._create_request_tasks(*urls):
                try:
                    await task
                    yield task.result()
                except Exception as e:
                    self._status_assigner.handle_exceptions(e)

    def _create_request_tasks(self, *urls):
        tasks = []
        for url in urls:
            test_url = self._status_assigner.preprocess_url(url)
            fetch_task = asyncio.create_task(self._fetch(test_url))
            tasks.append(fetch_task)
        return tasks

    async def _fetch(self, url):
        await self._throttler(url)
        async with self._session.request(self.request_method, url, allow_redirects=True) as response:
            return await self._status_assigner.parse_response(response)


def read_urls(file_path):
    with open(file_path) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            yield row[0]


def save_results(file_path, data):
    with open(file_path, 'w', newline='') as csvfile:
        csv.writer(csvfile).writerows(data)


async def validate_ulrs_file(input_path, output_path, page_text=None):
    status_assigner = StatusAssigner(page_text=page_text)
    request_method = (status_assigner.page_text and 'GET') or 'HEAD'
    validator = URLValidator(request_method=request_method,
                             throttler=DomainThrottler(rate_limit_per_sec=10),
                             status_assigner=status_assigner)
    urls = tuple(read_urls(input_path))
    statuses = [status async for status in validator.validate(*urls)]
    results = tuple(zip(urls, statuses))
    save_results(output_path, results)


def main():
    parser = argparse.ArgumentParser(
        description="Validate URLs in input file. Print list of URLs with statuses to output file. "
                    "Valid URL: HTTP code=200, response doesn't contains search string")
    parser.add_argument("-i", "--input", help="Path to the list of urls", required=True)
    parser.add_argument("-o", "--output", help="Path to the csv of urls with statuses", required=True)
    parser.add_argument("-s", "--search_string", help="This string should not be in the response", default=None)

    args = parser.parse_args()

    asyncio.run(validate_ulrs_file(args.input, args.output, args.search_string))


if __name__ == '__main__':
    main()
