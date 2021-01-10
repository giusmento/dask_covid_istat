#bin/bash!

main_folder="dask_covid_istat"
git_repository='https://github.com/giusmento/dask_covid_istat.git'
entry_point="main.py"

echo "Start script"

rm -r ${main_folder}
git clone ${git_repository}
pwd
#pip install -r requirements.txt
bash ${main_folder}/run_job.sh
