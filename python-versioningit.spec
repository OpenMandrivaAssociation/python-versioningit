Name:           python-versioningit
Version:        3.1.2
Release:        2
Summary:        Versioning It with your Version In Git
License:        MIT
URL:            https://pypi.org/pypi/versioningit
Source0:        https://files.pythonhosted.org/packages/source/v/versioningit/versioningit-%{version}.tar.gz
 
BuildArch:      noarch
 
BuildRequires:  pkgconfig(python)
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python-wheel
BuildRequires:	python-pip

# It calls git and hg so these need to be installed
Recommends:     git-core
Recommends:     mercurial
 
%description
versioningit is yet another setuptools plugin for automatically determining your package’s version based on your version control repository’s tags. 
Unlike others, it allows easy customization of the version format and even lets you easily override the separate functions used for version extraction & calculation.
 
%prep
%autosetup -n versioningit-%{version} -p1
 
%build
%py_build

%install
%py_install

%files 
%doc README.rst CHANGELOG.md
%{_bindir}/versioningit
%{python_sitelib}/versioningit-%{version}.dist-info
%{python_sitelib}/versioningit/
