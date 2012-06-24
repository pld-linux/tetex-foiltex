%define _short_name 	foiltex
Summary:	Set of LaTeX macros for preparing slides
Summary(pl):	Zbi�r makr tekstowych do przygotowywania slajd�w
Name:		tetex-%{_short_name}
Version:	1
Release:	6
License:	non-commercial
Group:		Applications/Publishing/TeX
Source0:	ftp://tug.ctan.org/tex-archive/nonfree/macros/latex/contrib//%{_short_name}.zip
# Source0-md5:	f3c8204a28cd176af889549ab1f6dc18
Patch0:		%{name}-newcommand.patch
%requires_eq	tetex
%requires_eq	tetex-latex
BuildRequires:	tetex-latex
PreReq:		tetex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Set of LaTeX macros for preparing slides. Also very usefull in
preparing presentation using pdflatex.

%description -l pl
Zbi�r makr LaTeXa do przygotowywania slajd�w. R�wnie� u�yteczny w
przypadku przygotowywania prezentacji za pomoc� pdflatex.

%prep
%setup -q -n %{_short_name}
%patch0 -p0

%build
latex foiltex.ins

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{_short_name}

install {fltfonts.def,*.clo,*.sty,foiltex.log,foils.cls} \
	$RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{_short_name}


%clean
rm -rf $RPM_BUILD_ROOT

%post	-p %{_bindir}/mktexlsr
%postun	-p %{_bindir}/mktexlsr

%files
%defattr(644,root,root,755)
%doc README sampfoil.tex foiltex.pdf
%{_datadir}/texmf/tex/latex/%{_short_name}
