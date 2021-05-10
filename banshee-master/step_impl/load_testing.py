from getgauge.python import step
import os

@step("load test by file <file>")
def load_test_by_file(file):
    os.system(f'locust -f load_testing/{file}.py --logfile=logs/locust.log')

@step("load test by file <file>, with NUM_USERS=<num_users> HATCH_RATE=<hatch_rate> RUN_TIME=<run_time>")
def load_test_by_with_configure(file, num_users, hatch_rate, run_time):
    os.system(f'locust -f load_testing/{file}.py -u {num_users} -r {hatch_rate} -t {run_time} --headless')

@step("load test by file <file>, with tags <tags>")
def load_test_by_file_with_tags(file, tags):
    os.system(f'locust -f load_testing/{file}.py --tags {tags} --headless')
