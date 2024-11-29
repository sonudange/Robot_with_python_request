*** Settings ***
Library     ../test/test.py

*** Test Cases ***
# get the request response and compare it with .json file data. Print any differences found during comparison
To Validate Countries Response
    Verify the Actual and Expected response for Country    sweden
