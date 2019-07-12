from setuptools import setup, find_packages

setup(
    name='bigquery-dl',
    description='A download script for Google BigQuery',
    version='0.0.1',
    author='ROYALBEFF',
    license='MIT',
    platforms='ALL',
    install_requires=['pydata-google-auth>=0.1.3', 'pandas-gbq>=0.10.0'],
    packages=find_packages(),
    entry_points={'console_scripts': ['bigquery-dl = bigquery_dl:main']}
)