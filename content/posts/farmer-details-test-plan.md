---
title: Test Plan
date: 2020-11-17
tags: [testing]
description: a sample test plan
draft: false
---

# Test Plan Identifier

| **Name of Strategy**     | **Organizational Affiliation** | **Version** | **Status** |
|--------------------------|--------------------------------|-------------|------------|
| Farmer Details Test Plan |                                | version 1   | Open       |

# Test Plan Approvals

| **Name**       | **Department** | **Signature** |
|----------------|----------------|---------------|
| Josphat Mutuku |                |               |
|                |                |               |
|                |                |               |
|                |                |               |

# 1 .Introduction

## 1.1 Test Objectives

# 2. Test Items/Object

## 2.1 Type of Test Plan: Component Test Plan

Farmers Details Component, based on Mobile Application Screenshot provided.

Test object: we will be testing each individual component in isolation.The
Farmer Details Component consists of various functions as outlined below

## 2.2 Features to be tested

| **Component**  | **Feature/Function**         | **Overview** |
|----------------|------------------------------|--------------|
| Farmer Details | Enter Firstname              |              |
|                | Enter Lastname               |              |
|                | Enter Phone Number           |              |
|                | Change Avatar                |              |
|                | Enter Alternate Phone Number |              |
|                | Enter Village                |              |
|                | Click to Search Location     |              |
|                | Select Language              |              |
|                | Enter National ID            |              |
|                | Enter Age                    |              |
|                | Select Gender                |              |
|                | Enter Farm Size              |              |
|                | GPS Captured Label           |              |
|                | Finish Button                |              |
|                | Place Order Button           |              |

## 2.3 Features not to be tested

We won’t test how the Farmer Details Mobile Application component integrates
with the Billing component in the Web Application.We will test each component
individually in isolation first atleast for this test plan

# 3. Test Approach

The structure of the **test specification** to be produced and used will be
provided later.

Our items for the test specification will include the items in the **test
deliverable** (see Test Deliverable Section)

The measurements to collect are outlined in the Test Strategy for this document
as well as the **test techniques** to use.

# 4. Item Pass/Fail Criteria

Also known as Completion Criteria.This is the criterion upon which we can use to
determine if to stop testing or go on until we reach the objective of the
testing.

Completion criteria for farmer details component test level are:

-   100% statement coverage

-   95% decision coverage

-   No known faults

The outcome of our above criteria will determine if our item passed test or not.

# 5. Suspension Criteria and Resumption Requirements

## 5.1 Suspension Criteria

If any defects are found which seriously impact the progress, the QA Team Lead
may choose to suspend testing. Criteria that will justify test suspension are:

-   Source code contains one or more critical defects, which seriously prevents
    or limits testing progress.

-   Assigned test resources are not available when needed by the test team.

## 5.2 Resumption Criteria

The test team will resume testing once the issues identified above are fixed

# 6. Test Deliverables

The test deliverables are essentially the work products of the entire **test
regime**.

This is essentially all the documentation produced in the process at hand

**Everything** must be included for the purposes of estimation and setting of
expectations.

| **Deliverable**                  | **Descriptions** |
|----------------------------------|------------------|
| Test Plan                        |                  |
| Test Cases                       |                  |
| Test Logs                        |                  |
| Test Execution Results           |                  |
| Test Defect Management Procedure |                  |
| Defect Report                    |                  |
| Test Summary Reports             |                  |

# 7. Testing Tasks

Our **Testing Effort** will include almost all items of the Software Testing
Life Cycle as outlined in tabular below.

| **Serial.No** | **Phase Name** | **Entry Criteria**                  | **Activities Performed**                                                                         | **Deliverable**                            |
|---------------|----------------|-------------------------------------|--------------------------------------------------------------------------------------------------|--------------------------------------------|
| 1             | Requirements   | Requirements specification document | Do brainstorming of the requirements.Create a list of requirements and get your doubts clarified | RUD (Requirements understanding document.) |
|               |                | Application design document         | Understand the feasibility of the requirements whether it is testable or not.                    | Testing feasibility report                 |
|               |                | User acceptance criteria document   | If your project requires automation,do the automation feasibility study                          | Automation feasibility report              |
| 2             | Planning       | Updated requirements document       | Define the scope of the project                                                                  | Test Plan document                         |
|               |                | Test feasibility reports            | Do the risk analysis and prepare the risk mitigation plan                                        | Risk mitigation document                   |
|               |                | Automation feasibility report       | Perform test estimation                                                                          | Test estimation document                   |
|               |                |                                     | Determine the overall testing strategy and process                                               |                                            |
|               |                |                                     | Identify the tools and resources and check for any training needs                                |                                            |
|               |                |                                     | Identify the environment                                                                         |                                            |
| 3             | Analysis       | Updated requirements document       | Identify the detailed test conditions                                                            | Test conditions document                   |
|               |                | Test Plan document                  |                                                                                                  |                                            |
|               |                | Risk Document                       |                                                                                                  |                                            |
|               |                | Test Estimation document            |                                                                                                  |                                            |
| 4             | Design         | Updated requirements document       | Detailed out the test conditions Identify the test data                                          | Detailed test conditions document          |
|               |                | Test conditions document            | Create the traceability metrics                                                                  | Requirements traceability metrics          |
|               |                |                                     |                                                                                                  | Test coverage metrics                      |
| 5             | Implementation | Detailed test condition document    | Create and review the test cases.                                                                | Test cases                                 |
|               |                |                                     | Create and review the automation scripts                                                         | Test scripts                               |
|               |                |                                     | Identify the candidate test cases for regression and automation                                  |                                            |
|               |                |                                     | Identify /create the test data                                                                   |                                            |
|               |                |                                     | Take sign off of the test cases and scripts                                                      |                                            |
| 6             | Execution      | Test cases                          | Execute the test cases                                                                           | Test execution report                      |
|               |                | Test scripts                        | Log bugs/defects in case of discrepancy                                                          | Defect report                              |
|               |                |                                     | Report the status                                                                                | Test log and Defect log                    |
|               |                |                                     |                                                                                                  | Updated traceability metrics               |
| 7             | Conclusion     | Updated test cases with results     | Provide the accurate figures and result of testing                                               | Test Summary report                        |
|               |                |                                     |                                                                                                  | Updated risk management report             |
| 8             | Closure        | Test closure condition              | Do the retrospective meting and understand the lessons learnt                                    | Lessons learnt document                    |
|               |                | Test summary report                 |                                                                                                  | Test matrices                              |
|               |                |                                     |                                                                                                  | Test closure report                        |

# 8. Test Environment

| **Server Name**           | **URL**                   |
|---------------------------|---------------------------|
| Quality Assurance Server  | http://qa.tulaa.io/admin  |
| Staging Environment       |                           |
|                           |                           |

# 9. Task Distribution

## 9.1 Roles and Responsibilities

In this section we describe who is responsible for what.The distribution of
testing roles and responsibilities can be shown in a Responsibility Distribution
Matrix (RDM).

| RDM                                               | 1 | 2 | 3 | 4  | 5  | 6  |
|---------------------------------------------------|---|---|---|----|----|----|
| Test Leader                                       | R | C | I | I  | I  | I  |
| Test Department                                   | C | R | R | P  | P  | R  |
| Quality Assurance                                 | C | C | R | \- | \- | \- |
| Sales/Marketing                                   | C | C | C | \- | \- | P  |
| The Customer                                      | C | C | C | \- | R  | P  |
| Method Department                                 | I | I | P | R  | \- | \- |
| R-Responsible P-Performing C-Consulted I-Informed |   |   |   |    |    |    |

Where:

1.Test Management

2.Test Analysis & Design

3.Test Environment

4.Test Tools

5.Test Data

6.Test Execution

On the *x-axis* we have **organizational units** or **people**.On the *y-axis*
we have **roles** or **tasks**

# 10. Staffing and Training Needs

For this testing effort we will not training any member of staff aforementioned
in *Section: 9 Task Distribution*.We assume that each member thein is skilled
enough to perform their role/responsibilty

# 11. Test Schedule

Once we are done with Risk analysis *(See Section 12: Testing Risk Register),*
we will provide a test schedule so that we can prioritize our tests.We will
provide a gantt chart here!

The table below will suffice for now.

| **Test Activities**     | **Start Date** | **EndDate** |
|-------------------------|----------------|-------------|
| Create Test Plan        | 14/02/2018     | 14/02/2018  |
| Identify Issues to Test |                |             |
| Create Risk Analysis    |                |             |
| Identify Test Resources |                |             |
| Plan Tests              |                |             |
| Design Tests            |                |             |
| Implement Tests         |                |             |
| Execute Test Cases      |                |             |
| Evaluate test coverage  |                |             |

# 12. Testing Risk Register

| **Risk ID** | **Risk Factor**              | **Impact**              | **Possible Contingencies**                                                                    |
|-------------|------------------------------|-------------------------|-----------------------------------------------------------------------------------------------|
| 1           | Not enough time to test      | Testing may suffer      | Prioritize testing to ensure application functionality works for critical and major processes |
| 2           | Not enought time to complete | Testing will be delayed | Contingency 1: low priority test case to be skipped.                                          |
|             |                              |                         | Contingency 2:Use the other test environment                                                  |
