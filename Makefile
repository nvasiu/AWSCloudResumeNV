.PHONY: build

build:
	sam build

deploy-infra:
	sam build && aws-vault exec cloudnv --no-session -- sam deploy

deploy-site:
	aws-vault exec cloudnv --no-session -- aws s3 sync ./resume-site s3://cloud-resume-nv