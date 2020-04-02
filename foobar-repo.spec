# TODO: set repository name here.
%global reponame foobar

Name: %{reponame}-release
Version: 32
Release: 1%{?dist}

Summary: FooBar package repository
License: MIT
URL: https://example.org/
BuildArch: noarch

Source1: %{reponame}.repo
Source2: RPM-GPG-KEY-%{reponame}-32

Requires: system-release(%{version})
Provides: %{reponame}-repos(%{version})

%description
FooBar package repository files for yum and dnf along with gpg
public keys.

%prep
%setup -q -c -T

%build
# There is nothing to build.

%install
install -d -m 0755 %{buildroot}%{_sysconfdir}/{pki/rpm-gpg,yum.repos.d}
install -m 0644 -p %{SOURCE1} %{buildroot}%{_sysconfdir}/yum.repos.d/
install -m 0644 -p %{SOURCE2} %{buildroot}%{_sysconfdir}/pki/rpm-gpg/

%files
%config(noreplace) %{_sysconfdir}/yum.repos.d/*.repo
%{_sysconfdir}/pki/rpm-gpg/*

%changelog
* Wed Mar 25 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 32-1
- Initial package release.
