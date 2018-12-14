import os
import json

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('jenkins_master')


def test_total_executors(host):
    cmd = host.run("curl http://127.0.0.1:8080/computer/api/json")
    assert cmd.exit_status == 0

    data = json.loads(cmd.stdout)
# 2 on master, 1 on centos slave and 1 on ubuntu slave
    assert data["totalExecutors"] == 4
