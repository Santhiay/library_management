# Library Management

A Frappe v15 app to manage a library: articles, members, memberships and issue/return transactions.

## Features

- Article, Library Member, Library Membership, Library Transaction, Library Settings (Single)
- Membership validation (no overlapping active membership)
- Issue/return validation (article availability, membership validity, max issued articles)
- Librarian role with permissions
- Public web view of published articles at /articles

## Setup

1. bench init --frappe-branch version-15 frappe-bench-v15
2. cd frappe-bench-v15
3. bench new-site library.localhost
4. bench get-app <repo-url>
5. bench --site library.localhost install-app library_management
6. bench start
