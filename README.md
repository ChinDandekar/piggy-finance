# piggy-finance
This repo holds the code for my website, [piggy-finance.com](https://www.piggy-finance.com)

# About the website

This website will allow users to log in via Google OAuth, and connect to credit card transactions (either manually or using Plaid for supported providers). Using this data, the website will help them with their personal finance goals, such as creating a budget, detecting price increases in recurring purchases, and predicting their future purchases to help manage purchases for the next month.

# Technologies

This website was built using React.js for the frontend and Python Django for the backend. Google OAuth is handled by Django All-Auth. These two components communicate over HTTPS using REST API. The website is hosted on an AWS EC2 instance. CDN is handled by AWS Cloudfront and AWS Route 53. Amazon Certificate Manager is also the provider of the SSL certificate that this website uses. It connects to a AWS DynamoDB database where it stores data.

This website is containerized in one container using Docker, and uses an Nginx reverse proxy to route appropriate requests to the backend. It uses Supervisord to manage running both the front and backend in one container.

# Goals

- [X] INFRASTRUCTURE: Setup basic frontend
- [X] INFRASTRUCTURE: Setup basic backend
- [X] INFRASTRUCTURE: Communicate over REST API
- [X] INFRASTRUCTURE: Run website on AWS EC2 instance
- [X] INFRASTRUCTURE: Setup CDN for the website
- [X] INFRASTRUCTURE: Connect to DynamoDB
- [X] INFRASTRUCTURE: Setup Google OAuth (In progress)
- [ ] FEATURE: Setup Plaid Auth (Dev version)
- [ ] FEATURE: Create option to upload data manually 
- [ ] FEATURE: Create ML model to predict next months cost
- [ ] FEATURE: Automatically detect price increases in recurring purchases
