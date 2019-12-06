from abc import ABC, abstractmethod
from typing import List

from widget import Widget


class Dashboard(ABC):
    labels: List[str] = []
    widgets: List[Widget] = []

    def __init__(self, labels: List[str], widgets: List[Widget]):
        self.labels = labels
        self.widgets = widgets

    @abstractmethod
    def render(self) -> str:
        return ""

