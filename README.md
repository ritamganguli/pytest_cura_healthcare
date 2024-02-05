# Project Name

A brief description of your project.

## Table of Contents

- [About](#about)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## About
In This Project I Have Automated A Website https://katalon-demo-cura.herokuapp.com/ using page object model.

## Getting Started

Firt Of All we Crated A File Called conftest.py where all the methoud of setting up the driver is written.
Then we have BaseClass.py where we are importing everything of the conftest.py (driver setup) and also have the logging setup
The mainpage.py contains all the function which are needed for running the testcase
test_learning.py conatins the impleation using page object model


```bash
py.test --browser Chrome -v -s
py.test --browser Chrome -v -s --html=index.html --> for reports in html format
