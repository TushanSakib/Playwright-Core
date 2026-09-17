import allure
import time
from allure_pytest.utils import ALLURE_LINK_MARK


class NetworkMonitor:
    def __init__(self,page):
        self.page = page

        self.failed_requests = []
        self.responses = []
        self.request_timings = {}
    def start_monitoring(self):
        self.page.on(
            "request",
            self._request_started
        )
        self.page.on(
            "requestFailed",
            self._capture_failed_request
        )
        self.page.on(
            "response",
            self._capture_response
        )

    def _request_started(self,request):
        self.request_timings[
            request.url
        ] = time.time()
    def _capture_failed_request(self,request):
        self.failed_requests.append({
            "url":request.url,
            "method":request.method
        })

    def _capture_response(
            self,
            response
    ):

        start_time = (
            self.request_timings.get(
                response.url
            )
        )

        duration = None

        if start_time:
            duration = (
                    time.time() -
                    start_time
            )

        self.responses.append({
            "url": response.url,
            "status": response.status,
            "duration": duration
        })

    def attach_results(self):
        allure.attach(
            str(self.failed_requests),
            name="Failed Requests",
            attachment_type=allure.attachment_type.TEXT
        )

        allure.attach(
            str(self.responses),
            name = "Responses",
            attachment_type=allure.attachment_type.TEXT
        )

    def verify_no_failed_requests(self):
        assert len(
            self.failed_requests
        ) == 0,(
            f"Failed Requests found: "
            f"{len(self.failed_requests)}"
        )
    def get_server_errors(self):
        server_errors = []
        for response in self.responses:
            if response["status"] >= 500:
                server_errors.append(response)
        return server_errors

    def verify_no_server_errors(self):
        errors = self.get_server_errors()
        assert len(errors) == 0,(
            f"Server Errors found: "
            f"{len(errors)}"
        )

    def verify_response_time(self,max_time=3):
        slow_apis = []

        for response in self.responses:
            duration = response.get("duration")
            if(duration and duration > max_time):
                slow_apis.append(response)

        assert len(slow_apis) ==0,(
            f"Slow APIs found: "
            f"{len(slow_apis)}"
        )