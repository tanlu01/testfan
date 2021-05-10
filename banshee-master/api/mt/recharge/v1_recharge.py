from api.mt.mt import Mt
import os
import datetime
from random import randint


class Recharge(Mt):
    method = 'get'
    api = '/v1/recharge'
    data = {}


    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }

    expected_schema = {
        "$schema": "http://json-schema.org/draft-06/schema#",
        "title": "expected_data",
        "type": "object",
        "required": [
            "code",
            "time",
            "data"
        ],
        "properties": {
            "code": {
                "type": "number"
            },
            "time": {
                "type": "number"
            },
            "data": {
                "type": "object",
                "required": [
                    "default_mobile",
                    "default_mobile_area",
                    "mobile_panel",
                    "other_panels",
                    "share_params"
                ],
                "properties": {
                    "default_mobile": {
                        "type": "string"
                    },
                    "default_mobile_area": {
                        "type": "string"
                    },
                    "mobile_panel": {
                        "type": "object",
                        "required": [
                            "header",
                            "items",
                            "recv_type"
                        ],
                        "properties": {
                            "header": {
                                "type": "object",
                                "required": [
                                    "icon",
                                    "title"
                                ],
                                "properties": {
                                    "icon": {
                                        "type": "string"
                                    },
                                    "title": {
                                        "type": "string"
                                    }
                                }
                            },
                            "items": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "recharge_id": {
                                            "type": "number"
                                        },
                                        "recharge_name": {
                                            "type": "string"
                                        },
                                        "recharge_sub_name": {
                                            "type": "string"
                                        },
                                        "reach_coupon": {
                                            "type": "boolean"
                                        },
                                        "price": {
                                            "type": "number"
                                        },
                                        "market_price": {
                                            "type": "number"
                                        }
                                    }
                                }
                            },
                            "recv_type": {
                                "type": "number"
                            }
                        }
                    },
                    "other_panels": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "header": {
                                    "type": "object",
                                    "required": [
                                        "icon",
                                        "title"
                                    ],
                                    "properties": {
                                        "icon": {
                                            "type": "string"
                                        },
                                        "title": {
                                            "type": "string"
                                        }
                                    }
                                },
                                "entries": {
                                    "type": "array",
                                    "items": {
                                        "type": "object",
                                        "properties": {
                                            "name": {
                                                "type": "string"
                                            },
                                            "icon": {
                                                "type": "string"
                                            },
                                            "link": {
                                                "type": "string"
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "share_params": {
                        "type": "object",
                        "required": [
                            "link",
                            "title",
                            "subtitle",
                            "image",
                            "hint",
                            "bakcup_image"
                        ],
                        "properties": {
                            "link": {
                                "type": "string"
                            },
                            "title": {
                                "type": "string"
                            },
                            "subtitle": {
                                "type": "string"
                            },
                            "image": {
                                "type": "string"
                            },
                            "hint": {
                                "type": "string"
                            },
                            "bakcup_image": {
                                "type": "string"
                            }
                        }
                    }
                }
            }
        }
    }