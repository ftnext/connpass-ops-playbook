from setuptools import find_packages, setup

setup(
    name="connpass-ops-playbook",
    version="0.0.1",
    packages=find_packages(
        exclude=["tests.*", "tests", "examples.*", "examples"]
    ),
    install_requires=[
        "helium~=3.0.7",
        "chromedriver-autoinstaller",
        "Send2Trash",
    ],
    extras_require={"dev": ["black", "flake8", "pytest", "pytest-randomly"]},
)
