---
title: Display API Response JSON Test Data In a Table
date: 2020-12-03
tags: [testing]
description: display json test data in table from a test api endpoint
draft: false
---

### Online REST API testing and prototyping resource
- http://reqres.in


### The URL Scheme
- http://reqres.in/api/users


### Response Displayed in a Table

{{<usersJSON url="https://reqres.in" scheme="/api/users">}}

### Create a Hugo ShortCode
`layout/shortcodes/usersJSON.html`

Put this as the content of the file

```html
{{ $urlPre := "https://reqres.in" }}
{{ $users := getJSON $urlPre "/api/users" }}
<table>
	<thead>
		<tr>
			<th>User ID</th>
			<th>Firstname</th>
			<th>Lastname</th>
			<th>Email</th>
			<th>Avatar</th>
		</tr>
	</thead>
	<tbody>
		{{ range $users.data }}
		<tr>
			<td>{{ .id }}</td>
			<td>{{ .first_name }}</td>
			<td>{{ .last_name }}</td>
			<td>{{ .email }}</td>
			<td><a href="{{ .avatar }}" target="_blank">{{ .avatar }}</a></td>
    </tr>
    {{ end }}
	</tbody>
</table>
```

Now to call the shortcode in the markdown file
`users-test-data.md`

```md
{{/*%<usersJSON url="https://reqres.in" scheme="/api/users">%*/}}
```
Just note that the above is commented to avoid been processed as shortcode.

### Sample JSON data from the above URL Scheme(/api/users)
```json
{
	"page": 1,
	"per_page": 6,
	"total": 12,
	"total_pages": 2,
	"data": [
		{
			"id": 1,
			"email": "george.bluth@reqres.in",
			"first_name": "George",
			"last_name": "Bluth",
			"avatar": "https://reqres.in/img/faces/1-image.jpg"
		},
		{
			"id": 2,
			"email": "janet.weaver@reqres.in",
			"first_name": "Janet",
			"last_name": "Weaver",
			"avatar": "https://reqres.in/img/faces/2-image.jpg"
		},
		{
			"id": 3,
			"email": "emma.wong@reqres.in",
			"first_name": "Emma",
			"last_name": "Wong",
			"avatar": "https://reqres.in/img/faces/3-image.jpg"
		},
		{
			"id": 4,
			"email": "eve.holt@reqres.in",
			"first_name": "Eve",
			"last_name": "Holt",
			"avatar": "https://reqres.in/img/faces/4-image.jpg"
		},
		{
			"id": 5,
			"email": "charles.morris@reqres.in",
			"first_name": "Charles",
			"last_name": "Morris",
			"avatar": "https://reqres.in/img/faces/5-image.jpg"
		},
		{
			"id": 6,
			"email": "tracey.ramos@reqres.in",
			"first_name": "Tracey",
			"last_name": "Ramos",
			"avatar": "https://reqres.in/img/faces/6-image.jpg"
		}
	],
	"support": {
		"url": "https://reqres.in/#support-heading",
		"text": "To keep ReqRes free, contributions towards server costs are appreciated!"
	}
}
```





