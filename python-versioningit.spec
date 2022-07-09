Name:           python-versioningit
Version:        2.0.0
Release:        %{autorelease}
Summary:        Versioning It with your Version In Git
 
License:        MIT
URL:            https://pypi.org/pypi/versioningit
Source0:        %{pypi_source versioningit}
# Man page written for Fedora in groff_man(7) format based on --help output
Source1:        versioningit.1
 
BuildArch:      noarch
 
%description %_description
 
%package -n python3-versioningit
Summary:        %{summary}
 
# It calls git and hg so these need to be installed
Recommends:     git-core
Recommends:     mercurial
 
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  git-core
BuildRequires:  mercurial
%endif
 
%description -n python3-versioningit %_description
 
%prep
%autosetup -n versioningit-%{version}
# Tweak build requirements to use what we have in Fedora. For test
# dependencies, we change all semver pins to minimum versions.
sed -r -i 's/~=/>=/g' tox.ini
 
# Comment out to remove /usr/bin/env shebangs
# Can use something similar to correct/remove /usr/bin/python shebangs also
# find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'
 
 
%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-t}
 
 
%build
%pyproject_wheel
 
%install
%pyproject_install
%pyproject_save_files versioningit
 
install -p -m 0644 -Dt %{buildroot}%{_mandir}/man1/ %{SOURCE1}
 
 
%check
%if %{with tests}
# Editable mode doesn’t work when operating on the system site-packages
k="${k-}${k+ and }not test_editable_mode"
 
%pytest -k "${k-}"
%endif
 
 
%files -n python3-versioningit -f %{pyproject_files}
%doc README.rst CHANGELOG.md
%{_bindir}/versioningit
%{_mandir}/man1/versioningit.1*
