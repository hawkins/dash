from scrapes.ezpass.ezpva_balance import EZPVAScrapeWidget
from scrapes.metro.metro_balance import WMATAScrapeWidget

from dashboard import Dashboard


class DCDashboard(Dashboard):
    def __init__(self):
        super().__init__(
            ["WMATA", "E-Z Pass"], [WMATAScrapeWidget(), EZPVAScrapeWidget()]
        )

    def render(self) -> str:
        length = len(self.labels)
        if length != len(self.widgets):
            raise ValueError("Number of labels must be the same as number of widgets")

        rendered = ""

        for i in range(0, length):
            rendered += f"{self.labels[i]}: {self.widgets[i].render()}"
            if i < length - 1:
                rendered += "\t"

        return rendered
