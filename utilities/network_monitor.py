import allure
from allure_pytest.utils import ALLURE_LINK_MARK


class NetworkMonitor:
    def __init__(self,page):
        self.page = page

        self.failed_requests = []
        self.responses = []

    def start_monitoring(self):
        self.page.on(
            "requestFailed",
            self._capture_failed_request
        )
        self.page.on(
            "response",
            self._capture_response
        )
    def _capture_failed_request(self,request):
        self.failed_requests.append({
            "url":request.url,
            "method":request.method
        })

    def _capture_response(self,response):
        self.responses.append({
            "url":response.url,
            "status":response.status
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