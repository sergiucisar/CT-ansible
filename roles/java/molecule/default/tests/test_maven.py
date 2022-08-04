import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("ics-ans-role-java-and-maven")


MAVEN_VERSION = "3.6.0"


def test_mvn_version(host):
    cmd = host.run('su -l -c "mvn -version"')
    assert 'Apache Maven {}'.format(MAVEN_VERSION) in cmd.stdout
