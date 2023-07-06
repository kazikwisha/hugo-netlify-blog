---
title: Grey Box UI Testing Checklist
date: 2020-11-17
tags: [testing]
description: a sample gray box manual UI testing checklist
draft: false
---

#### 1. CREATE Retailer
Adding a new retailer,the following steps will be followed:

##### Test Steps

   1. Load 'Retailer Add' form.
   2. Enter the retailer name, say ‘Oleleshao Agrovet’.
   3. Enter retailer description, say ‘this is test retailer detail’.
   4. Enter retailer location, say ‘Melili’.
   5. Submit the form.

##### Checking the result:

   - Tester manually verifies if the retailer is displayed with all the details in the front end of the software application.
   - Tester executes the query in PostgreSQL database server to check if the particular row is present

##### Query:

```sql
SELECT * FROM rschema.retailers WHERE retailer_name = 'Oleleshao Agrovet';
```

##### Other cases to consider:

   1. For some systems, different users will have different privileges. In that case, testers might have to check the response for each user roles.
   2. If duplicate retailers are not allowed, a tester can check that by adding a retailer with the same details once again. This time the database should not have a second entry corresponding to the same retailer.
   3. If the software allows multiple retailer creations at a time, then the tester can check if all the details of all retailers in the submission were entered into the database properly or not.
   4. Try different input combinations.
   5. Check what happens during server downtime.

#### 2. READ Retailer

To check if the created entry is readable, the following steps can be followed:

##### Test Steps
   - Create some retailers with different input combinations through CREATE functionality, say test name 1, test name 2, test name 3.
   - Try searching for the retailers.

##### Checking the result:

-  Tester manually verifies if the retailer details are correct.
-  Tester compares the details with the ones saved in the database.

##### Query:

```sql
SELECT * FROM retailers WHERE retailer_name = 'Oleleshao Agrovet' OR retailer_name = 'test name 12' OR retailer_name = 'test name 3';
```
##### Test Steps
##### Other cases to consider:

   1. View items one at a time.
   2. View multiple items at a time.
   3. Trying to view an item that doesn’t exist.
   4. Try searching with different conditions.
   5. Try checking the functionality for different user roles.
   6. Check what happens during server downtime.

#### 3. UPDATE Retailer

To edit or update existing entries, following steps can be followed:

##### Test Steps

   1. Create a retailer using CREATE functionality.
   2. Edit different fields of the retailer, say 'Oleleshao' to 'Mrefu Agrovet'.
   3. Submit

##### Checking the result:

   - Tester manually verifies that the retailer details have changed
   - Tester executes PostgresSQL query and sees the details

##### Query:

```sql
SELECT * FROM retailers WHERE retailer_name = 'Mrefu Agrovet';
```

##### Other cases to consider:

   1. Update multiple items at a time.
   2. Update to a key value that already exists.
   3. Update all the details or partial details.
   4. Update the fields with different input combinations.
   5. Check the updated feature for different Privileges.
   6. Check what happens during server downtimes.


#### 4. DELETE Retailer

To test the delete functionality, following steps will be followed:

##### Test Steps

   - Create a retailer with CREATE functionality.
   - Delete the retailer.

##### Verifying the result:

   - Tester manually checks if the retailer is removed from the UI
   - Tester manually checks the PostgreSQL database and confirms that the corresponding row has been deleted.

##### Query to run:

```sql
		SELECT * FROM retailers WHERE retailer_name = 'Oleleshao Agrovet';
```

##### Other cases to consider:

1. Delete multiple items in a single request
2. Delete an updated item.
3. Take two tabs and try to give delete request for a retailer from both tabs altogether.


