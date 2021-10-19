# myapi
Example of CI/CD with GCP using Cloud Build, Artifact Registry, and GKE.

# Build & Deploy

1. Clone the repo
```
$ git lone https://github.com/sylvioneto/myapi.git
```

2. Trigger Cloud Build CI to build the app and store in Artifact Registry.
```
$ gcloud builds submit  . --config=cloudbuild_ci.yaml --substitutions=TAG_NAME=1
```

3. Trigger Cloud Build CD job to build the app and store in Artifact Registry.
```
$ gcloud builds submit  . --config=cloudbuild_cd.yaml --substitutions=_CLUSTER=gke-dev,_REGION=us-central1,_CUSTOMER_NAME=joao,_TAG_NAME=1
```
