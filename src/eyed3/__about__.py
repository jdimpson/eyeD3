import dataclasses

project_name = "eyeD3"
version      = "0.8.10a67"
release_name = "Descent Into..."
author       = "Travis Shirk"
author_email = "travis@pobox.com"
years        = "2002-2019"

@dataclasses.dataclass
class Version:
    major: int
    minor: int
    maint: int
    release: str
    release_name: str

version_info = Version(0, 8, 10, "a67", "Descent Into...")