%define _short_name 	foiltex
Summary:	Set of LaTeX macros for preparing slides
Summary(pl):	Zbiór makr tekstowych do przygotowywania slajdów
Name:		tetex-foiltex
Version:	1
Release:	4
License:	nocommercial	
Group:		Applications/Publishing/TeX
Group(de):	Applikationen/Publizieren/TeX
Group(pl):	Aplikacje/Publikowanie/TeX
Source0:	ftp://ftp.dante.de/tex-archive/nonfree/macros/latex/contrib/supported/%{_short_name}.tar.gz
%requires_eq	tetex
%requires_eq	tetex-latex
BuildRequires:	tetex-latex
Prereq:		tetex
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

gzip -9nf readme.flt sampfoil.tex

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p %{_bindir}/mktexlsr
%postun	-p %{_bindir}/mktexlsr

%files 
%defattr(644,root,root,755)
%doc *.gz
%{_datadir}/texmf/tex/latex/%{_short_name}/*
