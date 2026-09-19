# GRC Control Mapper

A Python CLI tool that cross-references security controls across NIST 800-53, ISO 27001, and SOC 2 in seconds. Built as part of an end-to-end GRC engineering portfolio on AWS.

## What it does

- Maps a given control ID across multiple frameworks simultaneously
- Outputs cross-reference results as JSON and CSV for audit evidence
- Designed to replace hours of manual spreadsheet work with a repeatable, version-controlled process

## Tech stack

- Python 3
- CLI interface via argparse
- JSON and CSV output
- NIST 800-53, ISO 27001, SOC 2 control libraries

## Part of a larger pipeline

This tool is Project 1 in a ten-project GRC engineering portfolio built on AWS using Python, Terraform, boto3, GitHub Actions, OPA/Rego, OSCAL, and compliance-trestle.

Full portfolio: https://github.com/doneal78

Portfolio site: https://davidoneal.dev

GRC Engineering Pipeline (club challenges): https://github.com/doneal78/grc-engineering-pipeline

## Related projects

- [grc-compliance-checker](https://github.com/doneal78/grc-compliance-checker) — AWS Config and Security Hub compliance checker using boto3
- [grc-terraform-baseline](https://github.com/doneal78/grc-terraform-baseline) — Terraform baseline that moved a live AWS account from 40% AT RISK to 78% NEEDS IMPROVEMENT
- [grc-soc2-pipeline](https://github.com/doneal78/grc-soc2-pipeline) — SOC 2 evidence pipeline mapping 457 Security Hub findings to Trust Services Criteria
- [grc-engineering-pipeline](https://github.com/doneal78/grc-engineering-pipeline) — End-to-end evidence pipeline with CI/CD gate, Cosign signing, and OSCAL documentation