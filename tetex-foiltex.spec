%define _short_name 	foiltex
Summary:	Set of LaTeX macros for preparing slides
Summary(pl):	Zbiór makr tekstowych do przygotowywania slajdów
Name:		tetex-%{_short_name}
Version:	1
Release:	5
License:	non-commercial
Group:		Applications/Publishing/TeX
Source0:	ftp://tug.ctan.org/tex-archive/nonfree/macros/latex/contrib//%{_short_name}.tar.gz
# Source0-md5:	3d6c4425e941f09db4ea3987daa02e09
%requires_eq	tetex
%requires_eq	tetex-latex
BuildRequires:	tetex-latex
PreReq:		tetex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Set of LaTeX macros for preparing slides. Also very usefull in
preparing presentation using pdflatex.

%description -l pl
Zbiór makr LaTeXa do przygotowywania slajdów. Równie¿ u¿yteczny w
przypadku przygotowywania prezentacji za pomoc± pdflatex.

%prep
%setup -q -n %{_short_name}

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
%doc readme.flt sampfoil.tex
%{_datadir}/texmf/tex/latex/%{_short_name}
