#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import warnings

import parcyl

setup = parcyl.Setup()

gz = "{name}-{version}.tar.gz".format(**setup.attrs)
setup.attrs["download_url"] = (
    f"{setup.attrs['github_url']}/releases/downloads/v{setup.attrs['version']}/{gz}"
)





def package_files(directory, prefix=".."):
    paths = []
    for (path, _, filenames) in os.walk(directory):
        if "__pycache__" in path:
            continue
        for filename in filenames:
            if filename.endswith(".pyc"):
                continue
            paths.append(os.path.join(prefix, path, filename))
    return paths


if sys.argv[1:] and sys.argv[1] == "--release-name":
    print(extra_attrs["release_name"])
    sys.exit(0)
else:
    # The extra command line options we added cause warnings, quell that.
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", message="Unknown distribution option")
        warnings.filterwarnings("ignore", message="Normalizing")

        setup = parcyl.Setup()(package_dir={"eyed3": "./src/eyed3"},
                               packages=parcyl.find_packages("./src", exclude=["test", "test.*"]),
                               zip_safe=False,
                               platforms=["Any"],
                               keywords=["id3", "mp3", "python"],
                               test_suite="./src/tests",
                               include_package_data=True,
                               package_data={},
                               entry_points={
                                   "console_scripts": [
                                       "eyeD3 = eyed3.main:_main",
                                   ]
                               }
                              )

