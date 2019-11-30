#!/usr/bin/env python
from parcyl import Setup

setup = Setup(info_file="eyed3/__about__.py").with_packages("./", exclude=["test", "test.*"])
setup.attrs["download_url"] = "{github}/releases/downloads/v{version}/{name}-{version}.tar.gz"\
                              .format(github=setup.attrs['github_url'],
                                      **setup.attrs)

setup(package_dir={"eyed3": "./eyed3"},
      entry_points={
          "console_scripts": ["eyeD3 = eyed3.main:_main"]
      },
      zip_safe=False,
      platforms=["Any"],
      test_suite="./tests",
      include_package_data=True,
      package_data={},
     )
