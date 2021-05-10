import json
from copy import deepcopy


class GenerateSchema:
    # 经调研 json格式如下：
    # [{}]、[1,2,3], 不存在[[]]
    # {k: {}}, {k: []}, {k: v}
    def __init__(self, resp):
        self.resp = resp
        self.schema = {
            "$schema": "http://json-schema.org/draft-06/schema#",
            "title": "expected_data",
            "type": "object",
            "required": [],
            "properties": {}
        }

        self.t1 = {
            'type': 'array',
            'items': {
                'type': 'object',
                'properties': {}
            }
        }

        self.t2 = {
            'type': 'object',
            'required': [],
            'properties': {}
        }

        self.t3 = {
            'type': 'array',
            'items': []
        }

    def run(self, res=None, k=None, v=None, flag=True):
        if flag:
            for key, value in self.resp.items():
                self.schema['required'].append(key)

                if isinstance(value, str):
                    self.schema['properties'][key] = {'type': 'string'}
                elif isinstance(value, bool):
                    self.schema['properties'][key] = {'type': 'boolean'}
                elif isinstance(value, int):
                    self.schema['properties'][key] = {'type': 'number'}
                elif isinstance(value, list):
                    if value:
                        self.schema['properties'][key] = deepcopy(self.t1) if isinstance(value[0], dict) else deepcopy(self.t3)
                        self.run(self.schema['properties'][key]['items'], key, value, False)
                    else:
                        self.schema['properties'][key] = deepcopy(self.t1)
                elif isinstance(value, dict):
                    self.schema['properties'][key] = deepcopy(self.t2)
                    self.run(self.schema['properties'][key], '', value, False)

            # return json.dumps(self.schema, indent=4)
            return self.schema
        else:
            if isinstance(v, list):
                if isinstance(v[0], dict):
                    for k1, v1 in v[0].items():
                        if isinstance(v1, dict):
                            res['properties'][k1] = deepcopy(self.t2)
                            self.run(res['properties'][k1], k1, v1, False)
                        elif isinstance(v1, list):
                            if v1:
                                res['properties'][k1] = deepcopy(self.t1) if isinstance(v1[0], dict) else deepcopy(self.t3)
                                self.run(res['properties'][k1]['items'], k1, v1, False)
                            else:
                                res['properties'][k1] = deepcopy(self.t1)
                        else:
                            self.run(res['properties'], k1, v1, False)
                else:
                    for i in v:
                        if isinstance(i, bool):
                            res.append({'type': 'boolean'})
                        elif isinstance(i, int):
                            res.append({'type': 'number'})
                        elif isinstance(i, str):
                            res.append({'type': 'string'})

            elif isinstance(v, dict):
                for k1, v1 in v.items():
                    res['required'].append(k1)

                    if isinstance(v1, list):
                        if v1:
                            res['properties'][k1] = deepcopy(self.t1) if isinstance(v1[0], dict) else deepcopy(self.t3)
                            self.run(res['properties'][k1]['items'], k1, v1, False)
                        else:
                            res['properties'][k1] = deepcopy(self.t1)
                    elif isinstance(v1, dict):
                        res['properties'][k1] = deepcopy(self.t2)
                        self.run(res['properties'][k1], k1, v1, False)
                    else:
                        self.run(res['properties'], k1, v1, False)
            else:
                if isinstance(v, bool):
                    res[k] = {'type': 'boolean'}
                elif isinstance(v, int):
                    res[k] = {'type': 'number'}
                elif isinstance(v, str):
                    res[k] = {'type': 'string'}
