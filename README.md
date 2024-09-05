## Cloud Resume Challenge

https://nicvasiu.ca/

This website was created using AWS in order to practice cloud and DevOps skills. Features:
* Front-end in HTML/JavaScript and back-end in Python.
* Data is stored in DynamoDB, a NoSQL database.
* API is used to update the database, created using API Gateway and Lambda.
* This website uses HTTPS, SSL Certificates are setup using CloudFront.
* Infrastructure as code: AWS resources are specified in code and are deployed using AWS SAM CLI.
* CI/CD: Front-end changes are automatically deployed to the website, and back-end changes are deployed to AWS using Github Actions.
* Testing: Unit tests are run automatically before deployment through Github Actions.
