Name:           python-versioningit
Version:        2.0.0
Release:        1
Summary:        Versioning It with your Version In Git
License:        MIT
URL:            https://pypi.org/pypi/versioningit
Source0:        https://files.pythonhosted.org/packages/source/v/versioningit/versioningit-%{version}.tar.gz
 
BuildArch:      noarch
 
BuildRequires:  pkgconfig(python)
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
mkdir wheels
pip wheel --wheel-dir wheels --no-deps --no-build-isolation --verbose .

%install
pip install --root=%{buildroot} --no-deps --verbose --ignore-installed --no-warn-script-location --no-index --no-cache-dir --find-links wheels wheels/*.whl

%files 
%doc README.rst CHANGELOG.md
%{_bindir}/versioningit
