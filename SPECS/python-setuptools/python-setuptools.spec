Summary:        Easily build and distribute Python packages
Name:           python-setuptools
Version:        69.0.3
Release:        1%{?dist}
License:        MIT
Vendor:         Microsoft Corporation
Distribution:   Azure Linux
Group:          Development/Tools
URL:            https://pypi.python.org/pypi/setuptools
Source0:        https://pypi.org/packages/source/s/setuptools/setuptools-%{version}.tar.gz
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
BuildRequires:  python3-flit-core
Requires:       python3
BuildArch:      noarch

%description
Setuptools is a fully-featured, actively-maintained, and stable library designed to facilitate packaging Python projects.

%package -n python3-setuptools
Summary:        Easily download, build, install, upgrade, and uninstall Python packages

%description -n python3-setuptools
Setuptools is a fully-featured, actively-maintained, and stable library designed to facilitate packaging Python projects.

%prep
%autosetup -n setuptools-%{version}

%build

%install
pip3 wheel -w dist --no-cache-dir --no-build-isolation --no-deps $PWD
pip3 install --no-cache-dir --no-index --ignore-installed --root %{buildroot} \
    --no-user --find-links=dist setuptools

# add path file pointing to distutils
cat > %{python3_sitelib}/distutils-precedence.pth <<- "EOF"
import os; var = 'SETUPTOOLS_USE_DISTUTILS'; enabled = os.environ.get(var, 'local') == 'local'; enabled and __import__('_distutils_hack').add_shim();
EOF

%files -n python3-setuptools
%defattr(-,root,root,755)
%{python3_sitelib}/distutils-precedence.pth
%{python3_sitelib}/pkg_resources/*
%{python3_sitelib}/setuptools/*
%{python3_sitelib}/_distutils_hack/
%{python3_sitelib}/setuptools-%{version}.dist-info/*

%changelog
* Tue Feb 13 2024 Andrew Phelps anphel@microsoft.com - 69.0.3-1
- Initial version