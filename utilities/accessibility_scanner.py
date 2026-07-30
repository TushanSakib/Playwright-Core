import json
import allure


class AccessibilityScanner:

    def __init__(self, page):

        self.page = page

    def inject_axe(self):

        self.page.add_script_tag(
            path="axe/axe.min.js"
        )

    def scan(self):

        self.inject_axe()

        results = self.page.evaluate("""
            async() => {
                return await axe.run();
            }
        """)

        allure.attach(
            json.dumps(results, indent=4),
            name="Accessibility Report",
            attachment_type=allure.attachment_type.JSON
        )

        violations = results["violations"]

        critical_issues = []

        for issue in violations:

            if issue["impact"] in [
                "critical",
                "serious"
            ]:
                critical_issues.append(
                    issue
                )

        assert len(
            critical_issues
        ) == 0, (
            f"Critical Accessibility "
            f"Violations Found: "
            f"{len(critical_issues)}"
        )