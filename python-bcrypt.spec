#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module	bcrypt
Summary:	Library for password hashing for your software and your servers
Summary(pl.UTF-8):	Biblioteka do tworzenia skrótów haseł dla programów i serwerów
Name:		python-%{module}
# keep 3.1.x for python2 support
Version:	3.1.7
Release:	6
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/bcrypt/
Source0:	https://files.pythonhosted.org/packages/source/b/bcrypt/%{module}-%{version}.tar.gz
# Source0-md5:	5d6f93b575ce52470af37a8e7dce76fe
URL:		https://github.com/dstufft/bcrypt/
%if %{with python2}
BuildRequires:	python-cffi >= 1.1
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-pytest >= 3.2.1
BuildRequires:	python-six >= 1.4.1
%endif
%endif
%if %{with python3}
BuildRequires:	python3-cffi >= 1.1
BuildRequires:	python3-devel >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest >= 3.2.1
BuildRequires:	python3-six >= 1.4.1
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library should be compatible with py-bcrypt.

%description -l pl.UTF-8
Biblioteka powinna być zgodna z biblioteką py-bcrypt.

%package -n python3-%{module}
Summary:	Library for password hashing for your software and your servers
Summary(pl.UTF-8):	Biblioteka do tworzenia skrótów haseł dla programów i serwerów
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-%{module}
This library should be compatible with py-bcrypt.

%description -n python3-%{module} -l pl.UTF-8
Biblioteka powinna być zgodna z biblioteką py-bcrypt.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%dir %{py_sitedir}/bcrypt
%attr(755,root,root) %{py_sitedir}/bcrypt/*.so
%{py_sitedir}/bcrypt/*.py[co]
%{py_sitedir}/bcrypt-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc README.rst
%dir %{py3_sitedir}/bcrypt
%attr(755,root,root) %{py3_sitedir}/bcrypt/*.so
%{py3_sitedir}/bcrypt/*.py
%{py3_sitedir}/bcrypt/__pycache__
%{py3_sitedir}/bcrypt-%{version}-py*.egg-info
%endif
