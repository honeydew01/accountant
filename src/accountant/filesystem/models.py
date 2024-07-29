import os

from datetime import datetime
from pydantic import BaseModel, Field
from pathlib import Path
from typing import Union, Optional, Any, Dict, List


class AccountantModel:
    def __init__(
        self,
        root_dir: Optional[Union[Path, str]] = None,
        cache_dir: Optional[Union[Path, str]] = None,
    ):
        self.root_dir = Path(root_dir)
        self.cache_dir = Path(cache_dir)
        self.year_dirs: Dict[str, Path] = {}

    def scan_dir(self):
        pass


class TimelineModel(BaseModel):
    month: Optional[datetime] = Field(
        None, description="The date in the month the timeline is describing."
    )
    context: Optional[str] = Field(
        None, description="A short summary of the spending of that month"
    )
    timeline: Optional[Dict[datetime, str]] = Field(
        None,
        description="A timeline of activities related to the accounting of this timeline.",
    )
    notes: Optional[List[str]] = Field(
        None, description="Additional notes for the timeline"
    )


class BaseFileModel(BaseModel):
    physical_location: Optional[Path] = Field(
        None, description="Path to the actual location of the contents"
    )
    name = physical_location.name


class MonthModel(BaseFileModel):
    timeline_file: TimelineModel = Field(
        None, description="The timeline model for this month."
    )


class YearModel(BaseFileModel):
    children: List[MonthModel] = Field(
        [None for _ in range(12)],
        description="An ordered list of months associated with the year",
    )
