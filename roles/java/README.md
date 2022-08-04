# ics-ans-role-java

Ansible role to install java.

This role installs OpenJDK and OpenJFX SDK 1x.
It can also install Oracle JDK 8 in parallel (default is always openjdk) and maven if requested.

## Role Variables

```yaml
java_openjdk_version: "11.0.8+10"
java_openjdk_archive: "https://artifactory.esss.lu.se/artifactory/swi-pkg/java/OpenJDK{{ java_openjdk_version | regex_replace('^(\\d+).*', '\\1') }}U-jdk_x64_linux_hotspot_{{ java_openjdk_version | regex_replace('\\+', '_') }}.tar.gz"
java_openjfx_version: "13.0.1"
java_openjfx_archive: "https://artifactory.esss.lu.se/artifactory/swi-pkg/java/openjfx-{{ java_openjfx_version }}_linux-x64_bin-sdk.zip"

# Set to false to disable oracle jdk 8 installation
java_install_oracle_jdk8: true
java_oracle_jdk8_version: "191"
java_oracle_jdk8_archive: "https://artifactory.esss.lu.se/artifactory/swi-pkg/java/jdk-8u{{ java_oracle_jdk8_version }}-linux-x64.tar.gz"

# Set to true to install maven
java_install_maven: false
java_maven_version: "3.6.0"
java_maven_archive: "https://artifactory.esss.lu.se/artifactory/swi-pkg/apache/maven/{{ java_maven_version }}/apache-maven-{{ java_maven_version }}-bin.tar.gz"
```

## Example Playbook

```yaml
- hosts: servers
  roles:
    - role: ics-ans-role-java
```

## License

BSD 2-clause
