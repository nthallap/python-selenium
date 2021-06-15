*** Settings ***

Library  myrobotlib.py
*** Test Cases ***
Test1
    Log  Hello
    series  10
    series  200