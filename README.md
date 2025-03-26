# Baseline for API Testing in Python

#### Architecture

pytest -> requests clients -> DTOs (Data Transfer Objects) with dataclasses

#### What is this?

It's a baseline for API testing in Python, intended to be extended. The **tests** and assertions are pytest. The requests clients return **DTOs** (Data Transfer Objects) to assert against.

#### How to set this up and run it?

1. Git clone
2. Assuming you have Python3 and pytest on your PATH, run the tests from root with: `pytest test_get_slideshow.py`

#### ToDo:

1. Make this runnable from repository dashboard