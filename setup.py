from setuptools import setup

setup(
    name="noobaa-sa-common",
    version="0.1",
    packages=[""],
    url="",
    license="MIT",
    author="Noobaa SA QE",
    author_email="ocs-ci@redhat.com",
    description=(
        "Noobaa Standalone(SA) Common contains commonly used functions."
    ),
    install_requires=[
        "jinja2",
        "pyyaml",
        "requests",
    ],
)
