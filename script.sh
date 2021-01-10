#bin/bash!

main_folder="dask_covid_istat"
git_repository='https://github.com/giusmento/dask_covid_istat.git'
entry_point="main.py"

echo "Start script"

#rm -r ${main_folder}
#git clone ${git_repository}
pwd
source /etc/profile
#pip install -r requirements.txt
#bash ${main_folder}/run_job.sh
nohup python3 ${main_folder}/${entry_point}
