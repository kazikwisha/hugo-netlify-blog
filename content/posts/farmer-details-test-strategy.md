---
title: Test Strategy
date: 2020-11-17
tags: [testing]
description: a sample test strategy
draft: false
---

# Test Strategy Identifier

| **Name of Strategy**         | **Organizational Affiliation** | **Version** | **Status** |
|------------------------------|--------------------------------|-------------|------------|
| Farmer Details Test Strategy |                                | version 1   | Open       |

# Approvals

| **Name**       | **Department** | **Signature** |
|----------------|----------------|---------------|
| Josphat Mutuku |                |               |
|                |                |               |
|                |                |               |
|                |                |               |

# 1. Introduction

The purpose of this test strategy is to highlight the scope of testing the
farmer details component.Hence the scope of this strategy lies with this
specific component.The reader should familiarize herself with the requirement
design document section detailing this specific component.

# 2. Standards to use

For this component,we wont be referring to any proprietary standard only the
internal standards set in the test policy of tulaa.

# 3. Risks

The basis for this strategy will be to mitigate the project risk not the overall
product risk.

# 4. Test Levels and their relationships

| **Test Level**    | **Test Basis**  | **Coverage Items** |
|-------------------|-----------------|--------------------|
| Component Testing | Requirements    | Statements         |
|                   | Detailed Design | Decisions          |
|                   | Code            | Condition Coverage |

## 4.1 Component Testing

### 4.1.1 Entry Criteria

These are our entry criteria for this component;

1.The code has been frozen(i.e.the system is not being improved on as testing
continues.

2.The test environment has been configured and considered operational.

### 4.1.2 Exit Criteria

These are out exit criteria for this component;

-   All the test case have been executed and test results passed/logged into the
    defect tracking system

### 4.1.3 Degree of Independence

Testing for this vital component needs to be objective as possible.Therefore the
degree of independence have been defined:

-   Tests will be designed by independent testers in tulaa

-   Tests will be designed by consultants(external testers)

### 4.1.4 Test Design Techniques to be used

Test design techniques to use will be Requirement Based Test Design(Static
Testing),Statement Coverage,Function Coverage and Condition Coverage (White Box
Test Design) and Automation(Techique for Agile Testers)

### 4.1.5 Extent of Reuse

The following work products will be reused.This will be in consultation will the
Configuration Management:

-   Generic Test Specification (Test Scenarios)

-   Specific Test Environment ( QA Environment at this
    location:http://qa.abdc.io)

### 4.1.6 Environment in Which the Test Will Be Executed

The requirement for this test environment will definately depend on the degree
of independence mentioned before and the test level at which we are working on
of which is component testing of billing details.So the component testing will
be conducted on external tester PC.

### 4.1.7 Approach to Test Automation

This indeed is component in our web application and we will be conducting black
box testing.The tool selected for this task is Selenium WebDriver with C\#
bindings.We could also use Java Bindings.

### 4.1.8 Measures to Be Captured

Our measurement will be based on test execution

That is;

\-The number of test cases passed

\-The number of test cases failed

\-The number of test cases not executed

### 4.1.9 Approach to Confirmation Testing and Regression Testing

Component Testing:Rerun the test scripts for Dashboard Module to ensure that the
fault fixed didn’t break some existing functionality.Pick tests that you feel
might break or rather provide an explanation why you picked those ones.

# 5. Approach to Incident Management

Reference to the Configuration System Management should suffice here since they
are the one responsible for handling incident as the occur.The test environment
should be configured such a way that an incident report is sent automatically as
it occurs.Good cooperation with this department function will sort out issues
without reinventing procedures that are already in place.

# 6. Approach to Configuration Management of Testware

The testing team will liase with the Configuration Management to ensure that the
correct test data is provided and the right versions of the system is in place.

# 7. Approach to Test Process Improvement

Failure reports shall be analyzed to determine any trends in the faults found in
system test
