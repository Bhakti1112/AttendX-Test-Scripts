# AttendX-Test-Scripts

## Project Description
This repository contains sample automation test scripts for
the AttendX student attendance application.

## Test Scripts

### 1. test_login.py
Tests valid login credentials, an invalid password,
and an invalid username.

### 2. test_attendance.py
Tests marking attendance as Present or Absent,
a missing student ID, and an invalid attendance status.

## Technology Used
- Git
- GitHub
- Visual Studio Code
- Python unittest

## How to Run
Open a terminal in the project root and execute:

```bash
python -m unittest discover -s tests -v
```

On systems where Python is invoked as `python3`, use:

```bash
python3 -m unittest discover -s tests -v
```

## Purpose
Git and GitHub are used to maintain version history,
share test scripts, and collaborate with the QA team.