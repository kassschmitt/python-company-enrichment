# AbstractAPI python-company-enrichment library

Integrate the [Company Enrichment API from Abstract](https://app.abstractapi.com/api/company-enrichment/documentation) in your Python project in a few lines of code.

Abstract's Company Enrichment API is a fast, lightweight, modern, and RESTful JSON API allowing you to look up the location, timezone, country details, and more of an IPv4 or IPv6 address.

It's very simple to use: you only need to submit your API key and a company domain, and the API will respond with 

# Documentation

## Supported Python Versions

This library supports the **Python version 3.6** and higher.

## Installation

You can install **python-company-enrichment** by downloading the source.

### Via Composer:

**python-company-enrichment** is available on Pypi
[`abstract-python-company-enrichment`](https://pypi.org/project/abstract-python-company-enrichment/) package:

```bash
pip install abstract-python-company-enrichment
```

## API key

Get your API key for free and without hassle from the [Abstract website](https://app.abstractapi.com/users/signup?target=/api/company-enrichment/pricing/select).

## Quickstart

### Company information from a domain

```python
# Get company information from a domain using Abstract's Company Enrichment API and Python
from python_company_enrichment import AbstractCompanyEnrichment

COMPANY_ENRICHMENT_API_KEY =  "YYYYYY"; # Get your API Key from https://app.abstractapi.com/api/company-enrichment/documentation

AbstractCompanyEnrichment.configure(COMPANY_ENRICHMENT_API_KEY)
AbstractCompanyEnrichment.look_up("airbnb.com")
```

## API response

The API response is returned in a `CompanyEnrichmentData` object.

| PARAMETER | TYPE | DETAILS |
| - | - | - |
| Parameter | Type | Details |
| domain | String | The requested company domain |
| name | String | The name of the company |
| domain | String | The domain the company website is hosted on |
| country | String | The country the company is based in |
| locality | String | The city or region the company headquarter is based in |
| employees count | String | The approximate number of employees of the company |
| industry | String | The industry the company is operating in |
| year_founded | Uint32 | The year the company was founded |
| linkedin_url | String | The linkedin URL of the company |




## Detailed documentation

You will find additional information and request examples in the [Abstract help page](https://app.abstractapi.com/api/company-enrichment/documentation).

## Getting help

If you need help installing or using the library, please contact [Abstract's Support](https://app.abstractapi.com/api/company-enrichment/support).

For bug report and feature suggestion, please use [this repository issues page](https://github.com/abstractapi/python-company-enrichment/issues).

# Contribution

Contributions are always welcome, as they improve the quality of the libraries we provide to the community.

Please provide your changes covered by the appropriate unit tests, and post them in the [pull requests page](https://github.com/abstractapi/python-company-enrichment/pulls).

## Setup

To install the requirements, run:

```bash
python3 setup.py install --user
```

Once you implementer all your changes and the unit tests, run the following command to run the tests:

```bash
COMPANY_ENRICHMENT_API_KEY=YYYYYY python3 tests/test_python_company_enrichment.py
```
