*** Settings ***
Library     ../source/bank_keywords.py
Library     BuiltIn

*** Variables ***
${EXPECTED_AMOUNT}    1104.7131
${EXPECTED_AMOUNT_HIGH_PERCENT}    2613.0353

*** Test Cases ***
Test Deposit
    [Documentation]    Testing deposit method.
    ${bank}=    Create Bank
    ${result}=    Deposit Money    1000    12    0.1
    Log    Testing deposit: expected ${EXPECTED_AMOUNT}, got ${result}
    Should Be Equal As Numbers    ${result}    ${EXPECTED_AMOUNT}    4
    Log    Successfully verified deposit calculation


Test High Percent
    [Documentation]    Testing deposit with a high percent.
    ${bank}=    Create Bank
    ${result}=    Deposit Money    1000    12    1.0
    Log    Testing high percent: expected ${EXPECTED_AMOUNT_HIGH_PERCENT}, got ${result}
    Should Be Equal As Numbers    ${result}    ${EXPECTED_AMOUNT_HIGH_PERCENT}    4
    Log    Successfully verified high percent calculation

Test Negative Deposit Amount
    [Documentation]    Testing deposit with negative deposit amount.
    ${bank}=    Create Bank
    ${result}=    Deposit Money    -1000    12    0.1
    Log    Testing negative deposit amount: got ${result}
    Should Be None    ${result}
    Log    Successfully verified negative deposit amount

Test Negative Deposit Term
    [Documentation]    Testing deposit with negative deposit term.
    ${bank}=    Create Bank
    ${result}=    Deposit Money    1000    -12    0.1
    Log    Testing negative term: got ${result}
    Should Be None    ${result}
    Log    Successfully verified negative term

Test Zero Deposit Percent
    [Documentation]    Testing deposit with zero percent.
    ${bank}=    Create Bank
    ${result}=    Deposit Money    1000    12    0.0
    Log    Testing zero percent: got ${result}
    Should Be None    ${result}
    Log    Successfully verified zero percent calculation

Test Bank Creation
    [Documentation]    Testing bank method.
    ${bank}=    Create Bank
    Log    Bank created: ${bank}
    Should Not Be None    ${bank}
    Log    Successfully created bank instance
