# AWS Guard Duty Trusted IP Set
![Python 3.9.0](https://img.shields.io/badge/Python-v3.9.0-blue)
[![github-license](https://img.shields.io/github/license/dad2jrn/aws-boto3-lib?style=social&logo=github)](https://github.com/user/repo)
[![github-stars](https://img.shields.io/github/stars/dad2jrn/aws-boto3-lib?style=social&logo=github)](https://github.com/dad2jrn/aws-boto3-lib)

---

## About
AWS Gurd Duty is a powerful native security platform that tracks all kinds of security related findings within the AWS cloud.  One challenge often faced within a large enterprise is the increasing amount of false positive findings due to the inability of Guard Duty to exlude trusted IPs by default.

This library for creating an IP set within Guard Duty will reduce the white noise and allow Guard Duty to provide more accurate findings from truly external and/or untrusted IPs.  This increases the value that Guard Duty brings to your organization.

## Using
- Clone this repo and navigate to the directory locally within your terminal.
- To use this script, download and set your AWS Security Tokens for your terminal session.
- execute the following command:
    ```Python
    pipenv run python app.py
    ```

