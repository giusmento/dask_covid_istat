


CREATE CLUSTER

First step: Create a Data Proc Cluster

````
export PROJECT=dask-data-proc;export CLUSTER_NAME=cluster-dask;export REGION=us-east1; export ZONE=us-east1-b
````
````
gcloud dataproc clusters create ${CLUSTER_NAME} \
  --region ${REGION} \
  --master-machine-type e2-standard-2 \
  --master-boot-disk-size 40GB \
  --worker-machine-type e2-standard-2 \
  --worker-boot-disk-size 40GB \
  --image-version preview \
  --initialization-actions gs://goog-dataproc-initialization-actions-${REGION}/dask/dask.sh \
  --metadata dask-runtime=yarn \
  --optional-components JUPYTER \
  --enable-component-gateway
````
 
TUNNEL SSH
````
gcloud compute ssh ${CLUSTER_NAME}-m \
  --project=${PROJECT} \
  --zone=${ZONE} -- -D 1080 -N
````

````
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --proxy-server="socks5://localhost:1080" \
  --user-data-dir="/tmp/${CLUSTER_NAME}-m" http://${CLUSTER_NAME}-m:8088
````
Open 
  
connect ssh

````
gcloud compute ssh ${CLUSTER_NAME}-m --zone ${ZONE}-b
````

RUN JOB

export INPUT_FOLDER=gs://gm_bucket_data/covid_data/; export OUTPUT_FOLDER=gs://gm_bucket_data/covid_data/output/

git clone 