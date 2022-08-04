import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


JAVA_VERSION = "11.0.8+10"
JAVA_HOME = "/opt/java/jdk-{}".format(JAVA_VERSION)
JAVAFX_VERSION = "13.0.1"
PATH_TO_FX = "/opt/java/javafx-sdk-{}/lib".format(JAVAFX_VERSION)
ORACLE_JDK8_VERSION = "191"
JAVA8_HOME = "/opt/java/jdk1.8.0_{}".format(ORACLE_JDK8_VERSION)


def test_java_version(host):
    cmd = host.run("java -version 2>&1")
    if host.ansible.get_variables()["inventory_hostname"] == "ics-ans-role-java-and-oracle-jdk8":
        assert 'java version "1.8.0_{}"'.format(ORACLE_JDK8_VERSION) in cmd.stdout
    else:
        assert 'build {}'.format(JAVA_VERSION) in cmd.stdout


def test_java_home(host):
    cmd = host.run(r'su -l -c "echo \$JAVA_HOME"')
    java_home = cmd.stdout.strip()
    assert host.file(java_home).exists
    if host.ansible.get_variables()["inventory_hostname"] == "ics-ans-role-java-and-oracle-jdk8":
        assert java_home == JAVA8_HOME
    else:
        assert java_home == JAVA_HOME


def test_javafx_home(host):
    cmd = host.run(r'su -l -c "echo \$PATH_TO_FX"')
    assert cmd.stdout.strip() == PATH_TO_FX
    assert host.file(PATH_TO_FX).exists


def test_jce_policy(host):
    cmd = host.run(
        "jrunscript -e 'exit (javax.crypto.Cipher.getMaxAllowedKeyLength(\"RC5\") >= 256);'"
    )
    # The previous command returns 1, if the Unlimited Cryptography is available, 0 otherwise
    assert cmd.rc == 1


def test_secure_random_source(host):
    if host.ansible.get_variables()["inventory_hostname"] == "ics-ans-role-java-and-oracle-jdk8":
        java_security = host.file("{}/jre/lib/security/java.security".format(JAVA8_HOME))
    else:
        java_security = host.file("{}/conf/security/java.security".format(JAVA_HOME))
    assert not java_security.contains("securerandom.source=file:/dev/random")
    assert java_security.contains("securerandom.source=file:/dev/urandom")
