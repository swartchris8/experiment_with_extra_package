from setuptools import setup, find_packages

setup(
    name="my_package",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # Your normal dependencies here
    ],
    extras_require={
        'extra': ["my_local_package @ file:my_local_package"]
    }
)

