from setuptools import setup, find_packages

setup(
    name="nimbus",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pyyaml>=6.0",
        "apache-airflow>=2.0.0"
    ],
    entry_points={
        "console_scripts": [
            "nimbus-export=nimbus.cli:main",
        ],
    },
    author="StackBlitz",
    description="Export Airflow plugins as YAML for DAG Factory",
    python_requires=">=3.8",
)