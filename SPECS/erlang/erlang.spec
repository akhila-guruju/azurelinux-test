%define  debug_package %{nil}
Summary:        erlang
Name:           erlang
Version:        26.2.5.13
Release:        1%{?dist}
License:        Apache-2.0
Vendor:         Microsoft Corporation
Distribution:   Azure Linux
Group:          Development/Languages
URL:            https://erlang.org
Source0:        https://github.com/erlang/otp/archive/OTP-%{version}/otp-OTP-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel
BuildRequires:  unixODBC-devel
BuildRequires:  unzip

%if 0%{?with_check}
BuildRequires:  clang-tools-extra
%endif

%description
Erlang is a programming language and runtime system for building massively scalable soft real-time systems with requirements on high availability.

%prep
%autosetup -n otp-OTP-%{version} -p1

%build
export ERL_TOP=`pwd`
%configure
%make_build

%install
%make_install

%check
export ERL_TOP=`pwd`
./otp_build check --no-docs --no-format-check

%post

%files
%defattr(-,root,root)
%license LICENSE.txt
%{_bindir}/ct_run
%{_bindir}/dialyzer
%{_bindir}/epmd
%{_bindir}/erl
%{_bindir}/erlc
%{_bindir}/escript
%{_bindir}/run_erl
%{_bindir}/to_erl
%{_bindir}/typer
%{_libdir}/erlang/*

%changelog
* Tue Jun 24 2025 Kevin Lockwood <v-klockwood@microsoft.com> - 26.2.5.13-1
- Upgrade to 26.2.5.13 to fix CVE-2025-4748

* Wed Jun 04 2025 Muhammad Falak <mwani@microsoft.com> - 26.2.5.12-2
- Skip format-check in tests

* Wed May 14 2025 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 26.2.5.12-1
- Auto-upgrade to 26.2.5.12 - for CVE-2025-46712

* Thu Apr 17 2025 Kshitiz Godara <kgodara@microsoft.com> - 26.2.5.11-1
- Upgrade to 26.2.5.11 - fix cve CVE-2025-32433.

* Thu Apr 03 2025 Sandeep Karambelkar <skarambelkar@microsoft.com> - 26.2.5.10-1
- Upgrade to 26.2.5.10 - fix cve CVE-2025-30211.

* Tue Feb 25 2025 CBL-Mariner Servicing Account <cblmargh@microsoft.com> - 26.2.5.9-1
- Auto-upgrade to 26.2.5.9 - for CVE-2025-26618

* Fri Dec 13 2024 Ahmed Badawi <ahmedbadawi@microsoft.com> - 26.2.5.6-1
- Upgrade to 26.2.5.6 - fix cve CVE-2024-53846. Removed previous patch below as vulnerability is addressed in new version

* Mon Apr 01 2024 Sam Meluch <sammeluch@microsoft.com> - 26.2.3-2
- Add patch to fix issue when running with compiled code from OTP-24 on aarch64

* Thu Mar 21 2024 Sam Meluch <sammeluch@microsoft.com> - 26.2.3-1
- Update to version 26.2.3

* Tue Feb 14 2023 Sam Meluch <sammeluch@microsoft.com> - 25.2-1
- Update to version 25.2

* Wed Jan 19 2022 Cameron Baird <cameronbaird@microsoft.com> - 24.2-1
- Update to version 24.2

* Sat May 09 2020 Nick Samson <nisamson@microsoft.com> - 22.0.7-2
- Added %%license line automatically

* Thu Mar 19 2020 Henry Beberman <henry.beberman@microsoft.com> 22.0.7-1
- Update to 22.0.7. Fix URL. Fix Source0 URL. License verified.

* Tue Sep 03 2019 Mateusz Malisz <mamalisz@microsoft.com> 19.3-4
- Initial CBL-Mariner import from Photon (license: Apache2).

* Thu Jan 31 2019 Siju Maliakkal <smaliakkal@vmware.com> 19.3-3
- Revert to old version to fix rabbitmq-server startup failure

* Fri Dec 07 2018 Ashwin H <ashwinh@vmware.com> 21.1.4-1
- Update to version 21.1.4

* Mon Sep 24 2018 Dweep Advani <dadvani@vmware.com> 21.0-1
- Update to version 21.0

* Fri Oct 13 2017 Alexey Makhalov <amakhalov@vmware.com> 19.3-2
- Remove BuildArch

* Thu Apr 06 2017 Chang Lee <changlee@vmware.com> 19.3-1
- Updated Version

* Mon Dec 12 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 19.1-1
- Initial.
