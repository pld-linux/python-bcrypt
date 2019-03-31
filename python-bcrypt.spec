#
# Conditional build:
%bcond_with	doc		# don't build doc
%bcond_without	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module	bcrypt
Summary:	Library for password hashing for your software and your servers
Summary(pl.UTF-8):	Biblioteka do tworzenia skrótów haseł dla twojego oprogramowania i serwerów
Name:		python-%{module}
Version:	3.1.6
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
Source0:	https://pypi.debian.net/bcrypt/%{module}-%{version}.tar.gz
# Source0-md5:	4d8ab82e5e0c86b15f4ba5aff2bec6b5
URL:		https://github.com/dstufft/bcrypt/
BuildRequires:	rpm-pythonprov
# if py_postclean is used
BuildRequires:	rpmbuild(macros) >= 1.710
%if %{with python2}
BuildRequires:	python-cffi
BuildRequires:	python-d2to1
BuildRequires:	python-devel
BuildRequires:	python-distribute
BuildRequires:	python-modules
BuildRequires:	python-py
BuildRequires:	python-pytest
BuildRequires:	python-six
%endif
%if %{with python3}
BuildRequires:	python3-cffi
BuildRequires:	python3-devel
BuildRequires:	python3-devel-tools
BuildRequires:	python3-distribute
BuildRequires:	python3-modules
BuildRequires:	python3-py
BuildRequires:	python3-pytest
BuildRequires:	python3-six
%endif
Requires:	python-cffi > 0.8
Requires:	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library should be compatible with py-bcrypt and it will run on
Python 2.6, 2.7, 3.2, 3.3 and PyPy 2.0

%description -l pl.UTF-8
Biblioteka powinna byc kompatybilna z biblioteką py-bcrypt, działa dla
Python 2.6, 2.7, 3.2, 3.3 and PyPy 2.0

%package -n python3-%{module}
Summary:	Library for password hashing for your software and your servers
Summary(pl.UTF-8):	Biblioteka do tworzenia skrótów haseł dla twojego oprogramowania i serwerów
Group:		Libraries/Python
Requires:	python3-cffi > 0.8
Requires:	python3-modules

%description -n python3-%{module}
This library should be compatible with py-bcrypt and it will run on
Python 2.6-3.4 and PyPy 2.0

%description -n python3-%{module} -l pl.UTF-8
Biblioteka powinna byc kompatybilna z biblioteką py-bcrypt, działa dla
Python 2.6-3.4 and PyPy 2.0

%package apidocs
Summary:	%{module} API documentation
Summary(pl.UTF-8):	Dokumentacja API %{module}
Group:		Documentation

%description apidocs
API documentation for %{module}.

%description apidocs -l pl.UTF-8
Dokumentacja API %{module}.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
CC="%{__cc}" \
CFLAGS="%{rpmcppflags} %{rpmcflags}" \
%py_build %{?with_tests:test}
%endif

%if %{with python3}
CC="%{__cc}" \
CFLAGS="%{rpmcppflags} %{rpmcflags}" \
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
cd docs
%{__make} -j1 html
rm -rf _build/html/_sources
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
%dir %{py_sitedir}/%{module}
%attr(755,root,root) %{py_sitedir}/bcrypt/*.so
%{py_sitedir}/%{module}/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitedir}/%{module}-%{version}-py*.egg-info
%endif
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc README.rst
%dir %{py3_sitedir}/%{module}
%attr(755,root,root) %{py3_sitedir}/bcrypt/*.so
%{py3_sitedir}/%{module}/*.py
%dir %{py3_sitedir}/%{module}/__pycache__
%{py3_sitedir}/%{module}/__pycache__/*.py[co]
%{py3_sitedir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/*
%endif
