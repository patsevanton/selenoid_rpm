%global _prefix /usr/local

Name:    selenoid
Version: 1.5.0
Release: 1%{?dist}
Summary: Selenoid is a powerful implementation of Selenium hub to launch browsers.

Group:   Development Tools
URL:     https://github.com/prometheus/selenoid
License: ASL 2.0
Source0: https://github.com/aerokube/%{name}/releases/download/%{version}/%{name}_linux_amd64
#Source1: selenoid.service
#Source2: selenoid.conf

%description
Selenium Hub successor running browsers within containers.
Scalable, immutable, self hosted Selenium-Grid on any platform with single binary.
http://aerokube.com/selenoid/latest/

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/%{_bindir}
%{__install} -m 755 %{SOURCE0} %{buildroot}/%{_bindir}/%{name}

%files
%{_bindir}/%{name}
