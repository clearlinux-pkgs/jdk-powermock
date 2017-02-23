#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jdk-powermock
Version  : 1.6.5
Release  : 2
URL      : https://github.com/jayway/powermock/archive/powermock-1.6.5.tar.gz
Source0  : https://github.com/jayway/powermock/archive/powermock-1.6.5.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause
Requires: jdk-powermock-data
BuildRequires : apache-maven
BuildRequires : apache-maven2
BuildRequires : javapackages-tools
BuildRequires : jdk-aether
BuildRequires : jdk-aopalliance
BuildRequires : jdk-apache-parent
BuildRequires : jdk-aqute-bndlib
BuildRequires : jdk-assertj-core
BuildRequires : jdk-atinject
BuildRequires : jdk-cdi-api
BuildRequires : jdk-cglib
BuildRequires : jdk-commons-beanutils
BuildRequires : jdk-commons-cli
BuildRequires : jdk-commons-codec
BuildRequires : jdk-commons-collections
BuildRequires : jdk-commons-compress
BuildRequires : jdk-commons-digester
BuildRequires : jdk-commons-io
BuildRequires : jdk-commons-lang
BuildRequires : jdk-commons-lang3
BuildRequires : jdk-commons-logging
BuildRequires : jdk-commons-validator
BuildRequires : jdk-doxia
BuildRequires : jdk-doxia-sitetools
BuildRequires : jdk-easymock3
BuildRequires : jdk-eclipse-eclipse
BuildRequires : jdk-eclipse-osgi
BuildRequires : jdk-eclipse-osgi-services
BuildRequires : jdk-felix
BuildRequires : jdk-felix-bundlerepository
BuildRequires : jdk-felix-framework
BuildRequires : jdk-felix-osgi-foundation
BuildRequires : jdk-felix-utils
BuildRequires : jdk-glassfish-servlet-api
BuildRequires : jdk-guava
BuildRequires : jdk-guice
BuildRequires : jdk-hamcrest
BuildRequires : jdk-httpcomponents-client
BuildRequires : jdk-httpcomponents-core
BuildRequires : jdk-javassist
BuildRequires : jdk-jsoup
BuildRequires : jdk-jsr-305
BuildRequires : jdk-junit4
BuildRequires : jdk-kxml
BuildRequires : jdk-log4j
BuildRequires : jdk-maven-archiver
BuildRequires : jdk-maven-bundle-plugin
BuildRequires : jdk-maven-common-artifact-filters
BuildRequires : jdk-maven-compiler-plugin
BuildRequires : jdk-maven-dependency-tree
BuildRequires : jdk-maven-filtering
BuildRequires : jdk-maven-invoker
BuildRequires : jdk-maven-jar-plugin
BuildRequires : jdk-maven-javadoc-plugin
BuildRequires : jdk-maven-plugin-tools
BuildRequires : jdk-maven-reporting-api
BuildRequires : jdk-maven-reporting-impl
BuildRequires : jdk-maven-resources-plugin
BuildRequires : jdk-maven-shared-incremental
BuildRequires : jdk-maven-shared-utils
BuildRequires : jdk-mockito
BuildRequires : jdk-objectweb-asm
BuildRequires : jdk-objenesis
BuildRequires : jdk-osgi-compendium
BuildRequires : jdk-osgi-core
BuildRequires : jdk-plexus-archiver
BuildRequires : jdk-plexus-build-api
BuildRequires : jdk-plexus-cipher
BuildRequires : jdk-plexus-classworlds
BuildRequires : jdk-plexus-compiler
BuildRequires : jdk-plexus-containers
BuildRequires : jdk-plexus-i18n
BuildRequires : jdk-plexus-interactivity
BuildRequires : jdk-plexus-interpolation
BuildRequires : jdk-plexus-io
BuildRequires : jdk-plexus-sec-dispatcher
BuildRequires : jdk-plexus-utils
BuildRequires : jdk-plexus-velocity
BuildRequires : jdk-sisu
BuildRequires : jdk-slf4j
BuildRequires : jdk-snappy
BuildRequires : jdk-sonatype-oss-parent
BuildRequires : jdk-surefire
BuildRequires : jdk-testng
BuildRequires : jdk-velocity
BuildRequires : jdk-wagon
BuildRequires : jdk-xbean
BuildRequires : jdk-xmlunit
BuildRequires : jdk-xz
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six
BuildRequires : xmvn
Patch1: 0001-Fix-junit3-compat.patch
Patch2: 0002-Setting-naming-policy.patch

%description
![PowerMock](powermock.png)
[![Build Status](https://travis-ci.org/jayway/powermock.svg)](https://travis-ci.org/jayway/powermock)
[![Maven Central](https://maven-badges.herokuapp.com/maven-central/org.powermock/powermock/badge.svg)](https://maven-badges.herokuapp.com/maven-central/org.powermock/powermock)
[![Javadoc](https://javadoc-emblem.rhcloud.com/doc/org.powermock/powermock/badge.svg)](http://www.javadoc.io/doc/org.powermock/powermock)
[![Dependency Status](https://www.versioneye.com/user/projects/570b66ddfcc96900102d09f6/badge.svg?style=flat)](https://www.versioneye.com/user/projects/570b66ddfcc96900102d09f6)

%package data
Summary: data components for the jdk-powermock package.
Group: Data

%description data
data components for the jdk-powermock package.


%prep
%setup -q -n powermock-powermock-1.6.5
%patch1 -p1
%patch2 -p1

rm -r modules/module-impl/agent
rm -r api/mockito2/src/main/java/org/powermock/api/mockito/repackaged/{cglib,asm}
find -name '*.java' | xargs sed -i 's/org\.mockito\.cglib/net.sf.cglib/g;
s/org\.powermock\.api\.mockito\.repackaged\.cglib/net.cf.cglib/g;
s/org\.powermock\.api\.mockito\.repackaged\.asm/org.objectweb.asm/g'
rm modules/module-impl/junit4-common/src/test/java/org/powermock/modules/junit4/common/internal/impl/JUnitVersionTest.java
sed -i '/shouldLoadClassAndOverrideMethodGreaterThanJvmLimit/i@org.junit.Ignore' \
core/src/test/java/org/powermock/core/transformers/impl/ClassMockTransformerTest.java
python3 /usr/share/java-utils/pom_editor.py pom_disable_module module-test modules
python3 /usr/share/java-utils/pom_editor.py pom_disable_module junit4-legacy modules/module-impl
python3 /usr/share/java-utils/pom_editor.py pom_disable_module junit4-rule-agent modules/module-impl
python3 /usr/share/java-utils/pom_editor.py pom_disable_module junit3 modules/module-impl
python3 /usr/share/java-utils/pom_editor.py pom_disable_module testng-agent modules/module-impl
python3 /usr/share/java-utils/pom_editor.py pom_disable_module agent modules/module-impl
python3 /usr/share/java-utils/pom_editor.py pom_disable_module examples
python3 /usr/share/java-utils/pom_editor.py pom_disable_module release
python3 /usr/share/java-utils/pom_editor.py pom_disable_module classloading-xstream classloading
python3 /usr/share/java-utils/pom_editor.py pom_disable_module mockito2 api
python3 /usr/share/java-utils/pom_editor.py pom_remove_plugin  :rat-maven-plugin
python3 /usr/share/java-utils/pom_editor.py pom_remove_plugin  :maven-source-plugin
python3 /usr/share/java-utils/pom_editor.py pom_xpath_remove   "pom:plugin[pom:artifactId='maven-javadoc-plugin']/pom:executions"
python3 /usr/share/java-utils/mvn_package.py :powermock-core core
python3 /usr/share/java-utils/mvn_package.py :powermock-classloading-base core
python3 /usr/share/java-utils/mvn_package.py :powermock-classloading-objenesis core
python3 /usr/share/java-utils/mvn_package.py :powermock-module-junit4 junit4
python3 /usr/share/java-utils/mvn_package.py :powermock-module-junit4-rule junit4
python3 /usr/share/java-utils/mvn_package.py :powermock-module-junit4-common junit4
python3 /usr/share/java-utils/mvn_package.py :powermock-api-mockito api-mockito
python3 /usr/share/java-utils/mvn_package.py :powermock-api-mockito-common api-mockito
python3 /usr/share/java-utils/mvn_package.py :powermock-api-support api-support
python3 /usr/share/java-utils/mvn_package.py :powermock-api-easymock api-easymock
python3 /usr/share/java-utils/mvn_package.py :powermock-reflect reflect
python3 /usr/share/java-utils/mvn_package.py :powermock-module-testng testng
python3 /usr/share/java-utils/mvn_package.py :powermock-module-testng-common testng
python3 /usr/share/java-utils/mvn_package.py org.powermock.tests: __noinstall
python3 /usr/share/java-utils/mvn_package.py ::pom: __noinstall

%build
python3 /usr/share/java-utils/mvn_build.py

%install
xmvn-install  -R .xmvn-reactor -n powermock -d %{buildroot}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/powermock/powermock-api-easymock.jar
/usr/share/java/powermock/powermock-api-mockito-common.jar
/usr/share/java/powermock/powermock-api-mockito.jar
/usr/share/java/powermock/powermock-api-support.jar
/usr/share/java/powermock/powermock-classloading-base.jar
/usr/share/java/powermock/powermock-classloading-objenesis.jar
/usr/share/java/powermock/powermock-core.jar
/usr/share/java/powermock/powermock-module-junit4-common.jar
/usr/share/java/powermock/powermock-module-junit4-rule.jar
/usr/share/java/powermock/powermock-module-junit4.jar
/usr/share/java/powermock/powermock-module-testng-common.jar
/usr/share/java/powermock/powermock-module-testng.jar
/usr/share/java/powermock/powermock-reflect.jar
/usr/share/maven-metadata/powermock-api-easymock.xml
/usr/share/maven-metadata/powermock-api-mockito.xml
/usr/share/maven-metadata/powermock-api-support.xml
/usr/share/maven-metadata/powermock-core.xml
/usr/share/maven-metadata/powermock-junit4.xml
/usr/share/maven-metadata/powermock-reflect.xml
/usr/share/maven-metadata/powermock-testng.xml
/usr/share/maven-poms/powermock/powermock-api-easymock.pom
/usr/share/maven-poms/powermock/powermock-api-mockito-common.pom
/usr/share/maven-poms/powermock/powermock-api-mockito.pom
/usr/share/maven-poms/powermock/powermock-api-support.pom
/usr/share/maven-poms/powermock/powermock-classloading-base.pom
/usr/share/maven-poms/powermock/powermock-classloading-objenesis.pom
/usr/share/maven-poms/powermock/powermock-core.pom
/usr/share/maven-poms/powermock/powermock-module-junit4-common.pom
/usr/share/maven-poms/powermock/powermock-module-junit4-rule.pom
/usr/share/maven-poms/powermock/powermock-module-junit4.pom
/usr/share/maven-poms/powermock/powermock-module-testng-common.pom
/usr/share/maven-poms/powermock/powermock-module-testng.pom
/usr/share/maven-poms/powermock/powermock-reflect.pom
