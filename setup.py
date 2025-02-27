from setuptools import setup, find_packages

try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements

# Set the library's long description to the repo's README.md
with open('README.md', 'r') as readme_file:
    readme = readme_file.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

requirements = required

setup(
    name='abstract_python_company_enrichment',
    version='0.0.4',
    author='Kathryn Schmitt',
    author_email='kass@inreachventure.com',
    description="AbstractCompanyEnrichment - Wrapper to quickly start using AbstractAPI's company enrichment service in your projects.",
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/kassschmitt/python-company-enrichment',
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
    ],
)
