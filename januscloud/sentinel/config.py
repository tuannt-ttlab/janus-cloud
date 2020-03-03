# -*- coding: utf-8 -*-

from januscloud.common.schema import Schema, StrVal, Default, AutoDel, Optional, BoolVal, IntVal, \
    StrRe, EnumVal, Or, DoNotCare
from januscloud.common.confparser import parse as parse_config
from pkg_resources import Requirement, resource_filename
import os

config_schema = Schema({
    Optional("general"): Default({
        Optional("daemonize"): Default(BoolVal(), default=False),

        AutoDel(str): object  # for all other key remove
    }, default={}),
    Optional("log"): Default({
        Optional('log_to_stdout'): Default(BoolVal(), default=True),
        Optional('log_to_file'): Default(StrVal(), default=''),
        Optional('debug_level'): Default(EnumVal(['DEBUG', 'INFO', 'WARN', 'ERROR', 'FATAL']), default='DEBUG'),
        Optional('log_file_size'): Default(IntVal(), default=104857600),
        Optional('log_file_rotate'): Default(IntVal(), default=10),
        AutoDel(str): object  # for all other key remove
    }, default={}),
    Optional("janus"): Default({
        Optional("server_name"): Default(StrVal(min_len=1, max_len=64), default=''),
        Optional("server_ip"): Default(StrVal(), default='127.0.0.1'),
        Optional("ws_port"): Default(IntVal(min=0, max=65536), default=8188),
        Optional("admin_ws_port"): Default(IntVal(min=0, max=65536), default=0),
        Optional("pingpong_interval"): Default(IntVal(min=1, max=3600), default=5),
        Optional("statistic_interval"): Default(IntVal(min=1, max=3600), default=10),
        Optional("request_timout"): Default(IntVal(min=1, max=3600), default=10),
        AutoDel(str): object  # for all other key remove
    }, default={}),

    Optional("proc_watcher"): Default({
        Optional("cmdline"): Default(StrVal(), default=''),
        Optional("error_restart_interval"): Default(IntVal(min=0, max=86400), default=30),
        Optional("poll_interval"): Default(IntVal(min=1, max=3600), default=1),
        AutoDel(str): object  # for all other key remove
    }, default={}),
    Optional("admin_api"): Default({
        Optional("json"): Default(EnumVal(['indented', 'plain', 'compact']), default='indented'),
        Optional("http_listen"): Default(StrRe('^\S+:\d+$'), default='0.0.0.0:8200'),
        AutoDel(str): object  # for all other key we don't care
    }, default={}),
    Optional("poster"): Default([{
        "type": StrVal(min_len=1, max_len=64),
        DoNotCare(str): object  # for all other key we don't care
    }], default=[]),
})


def load_conf(path):
    if path is None or path == '':
        config = config_schema.validate({})
    else:
        config = parse_config(path, config_schema)

    # check other configure option is valid or not
    # TODO

    return config


if __name__ == '__main__':
    conf = config_schema.validate({})
    import pprint
    pprint.pprint(conf)
