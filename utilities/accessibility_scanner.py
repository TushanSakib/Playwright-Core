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
        async () => {
            return await axe.run();
        }
        """)

        allure.attach(
            json.dumps(results, indent=2),
            name="Accessibility_Report",
            attachment_type=allure.attachment_type.JSON
        )

        violations = results.get("violations", [])

        serious_issues = []

        for violation in violations:

            impact = violation.get("impact")

            if impact in ["critical", "serious"]:

                serious_issues.append(
                    {
                        "rule": violation["id"],
                        "impact": impact,
                        "description": violation["description"],
                        "affected_nodes": len(
                            violation["nodes"]
                        )
                    }
                )

        if serious_issues:

            details = "\n\nAccessibility Violations:\n\n"

            for issue in serious_issues:

                details += (
                    f"Rule: {issue['rule']}\n"
                    f"Impact: {issue['impact']}\n"
                    f"Description: {issue['description']}\n"
                    f"Affected Nodes: {issue['affected_nodes']}\n\n"
                )

            assert False, details

        return violations