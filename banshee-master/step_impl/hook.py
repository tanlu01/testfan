from getgauge.python import data_store, before_step, after_step, before_scenario, after_scenario, before_spec, after_spec, before_suite, after_suite
from pathlib import Path
from test_result.step_result import StepResult
from datetime import datetime
import json, random, string

@before_suite
def before_suite_hook(context):
    data_store.suite['test_result'] = []

@before_spec
def before_spec_hook(context):
    pass

@before_scenario
def before_scenario_hook(context):
    pass

@before_step
def before_step_hook(context):
    data_store.scenario['step_result'] = StepResult()

@after_step
def after_step_hook(context):
    if context.step.is_failing: data_store.scenario['step_result'].result['result'] = 'Fail'
    data_store.scenario['step_result'].result['end_time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data_store.scenario['step_result'].result['case_name'] = context.step.text
    data_store.scenario['step_result'].result['case_full_path'] = context.scenario.name + data_store.scenario['step_result'].result['case_name']
    data_store.scenario['step_result'].result['err_message'] = context.step.error_message
    data_store.suite['test_result'].append(data_store.scenario['step_result'].result)

@after_scenario
def after_scenario_hook(context):
    pass

@after_spec
def after_spec_hook(context):
    if 'browser' in data_store.spec.keys():
        data_store.spec['browser'].quit()
    # if 'page_async' in data_store.spec.keys():
    #     await data_store.spec['page_async'].browser.close()

@after_suite
def after_suite_hook(context):
    test_result = json.dumps(data_store.suite['test_result'])
    data_json = Path('logs') / 'data.json'
    with open(data_json, 'w') as f:
        f.write(test_result)