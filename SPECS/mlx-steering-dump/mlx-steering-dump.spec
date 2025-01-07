#
# Copyright (c) 2017 Mellanox Technologies. All rights reserved.
#
# This Software is licensed under one of the following licenses:
#
# 1) under the terms of the "Common Public License 1.0" a copy of which is
#    available from the Open Source Initiative, see
#    http://www.opensource.org/licenses/cpl.php.
#
# 2) under the terms of the "The BSD License" a copy of which is
#    available from the Open Source Initiative, see
#    http://www.opensource.org/licenses/bsd-license.php.
#
# 3) under the terms of the "GNU General Public License (GPL) Version 2" a
#    copy of which is available from the Open Source Initiative, see
#    http://www.opensource.org/licenses/gpl-license.php.
#
# Licensee has the right to choose one of the above licenses.
#
# Redistributions of source code must retain the above copyright
# notice and one of the license notices.
#
# Redistributions in binary form must reproduce both the above copyright
# notice, one of the license notices in the documentation
# and/or other materials provided with the distribution.
#
#

Summary:	 Mellanox steering dump parser
Name:		 mlx-steering-dump
Version:	 1.0.0
Release:	 1%{?dist}
License:	 GPLv2
Url:		 https://github.com/Mellanox/mlx_steering_dump
Group:		 Applications/System
Source0:         https://linux.mellanox.com/public/repo/mlnx_ofed/24.10-0.7.0.0/SRPMS/mlx-steering-dump-1.0.0.tar.gz#/%{name}-%{version}.tar.gz
BuildRoot:	 /var/tmp/%{name}-%{version}-build
Vendor:          Microsoft Corporation
Distribution:    Azure Linux
ExclusiveArch:   x86_64
Requires:	 python3

%description
This is Mellanox SW steering parser and triggering for dump files in CSV format.
The supported dump files are those generated by ConnectX5 and ConnectX6DX.

%prep
%setup -q %{name}-%{version}

%install
install -d %{buildroot}/usr/share/mlx-steering-dump/sws/src/parsers
install -d %{buildroot}/usr/share/mlx-steering-dump/hws/src
install -d %{buildroot}/usr/bin/

install -m 755 sws/mlx_steering_dump_parser.py  %{buildroot}/usr/share/mlx-steering-dump/sws
install -m 644 sws/src/*.py  %{buildroot}/usr/share/mlx-steering-dump/sws/src/
install -m 644 sws/src/parsers/*.py  %{buildroot}/usr/share/mlx-steering-dump/sws/src/parsers/
install -m 755 sws/mlx_steering_dump %{buildroot}/usr/bin/

install -m 755 hws/mlx_hw_steering_parser.py  %{buildroot}/usr/share/mlx-steering-dump/hws
install -m 644 hws/src/*.py  %{buildroot}/usr/share/mlx-steering-dump/hws/src/
install -m 755 hws/mlx_hw_steering_dump %{buildroot}/usr/bin/

%clean

%preun


%files
%license debian/copyright
/usr/share/mlx-steering-dump/*
/usr/bin/mlx_steering_dump
/usr/bin/mlx_hw_steering_dump

%changelog
* Tue Dec  17 2024 Binu Jose Philip <bphilip@microsoft.com>
- Initial Azure Linux import from NVIDIA (license: GPLv2)
- License verified
* Wed Oct 6 2021 Mohammad Kabat <mohammadkab@nvidia.com>
- Add rpm support