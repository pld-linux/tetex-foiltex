%define _short_name 	foiltex
Summary:	Set of LaTeX macros for prepering slides.
Version:	1
Name:		tetex-foiltex
Release:	1
Copyright:	nocommercial	
Group:		Applications/Publishing/TeX
Group(pl):	Aplikacje/Publikowanie/TeX
Source0:	%{_short_name}.tar.gz
Requires:	tetex
Requires:	tetex-latex
BuildRequires:	tetex-latex
Prereq:		tetex
Prereq:		/usr/bin/mktexlsr
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Set of LaTeX macros for prepering slides. Also very usefull in
prepering presentation using pdflatex.

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

%post 
/usr/bin/mktexlsr

%postun
/usr/bin/mktexlsr

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc *.gz
%{_datadir}/texmf/tex/latex/%{_short_name}/*
