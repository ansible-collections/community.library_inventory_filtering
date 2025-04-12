# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2025 Felix Fontein <felix@fontein.de>

# /// script
# dependencies = ["nox>=2025.02.09", "antsibull-nox"]
# ///

import sys

import nox


try:
    import antsibull_nox
except ImportError:
    print("You need to install antsibull-nox in the same Python environment as nox.")
    sys.exit(1)


antsibull_nox.setup(
    collection_sources={
        "community.internal_test_tools": "git+https://github.com/ansible-collections/community.internal_test_tools.git,main",
    },
)


antsibull_nox.add_lint_sessions(
    isort_config="tests/nox-config-isort.cfg",
    black_config="tests/nox-config-black.toml",
    flake8_config="tests/nox-config-flake8.ini",
    pylint_rcfile="tests/nox-config-pylint.rc",
    run_yamllint=True,
    yamllint_config="tests/nox-config-yamllint.yml",
    mypy_config="tests/nox-config-mypy.ini",
    mypy_extra_deps=[
        "types-mock",
    ],
)

antsibull_nox.add_docs_check(
    validate_collection_refs="all",
)

antsibull_nox.add_license_check()

antsibull_nox.add_extra_checks(
    run_no_unwanted_files=True,
    no_unwanted_files_module_extensions=[".py"],
    no_unwanted_files_yaml_extensions=[".yml"],
    no_unwanted_files_skip_paths=[
        "plugins/plugin_utils/py.typed",
    ],
)

antsibull_nox.add_build_import_check(
    run_galaxy_importer=True,
)


# Allow to run the noxfile with `python noxfile.py`, `pipx run noxfile.py`, or similar.
# Requires nox >= 2025.02.09
if __name__ == "__main__":
    nox.main()
