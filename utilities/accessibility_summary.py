from logging import critical


class AccessibilitySummary:
    @staticmethod
    def get_summary(results):
        critical = 0,
        serious = 0,
        moderate = 0,
        minor = 0

        for violation in results["violations"]:
            impact = (
                violation["impact"]
            )
            if impact == "critical":
                critical+=1
            elif impact == "serious":
                serious+=1
            elif impact == "moderate":
                moderate+=1
            elif impact == "minor":
                minor+=1
        return{
            "critical": critical,
            "serious": serious,
            "moderate": moderate,
            "minor": minor
        }