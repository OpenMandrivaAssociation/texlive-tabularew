Name:		texlive-tabularew
Version:	15878
Release:	1
Summary:	A variation on the tabular environment
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tabularew
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabularew.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabularew.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabularew.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package offers a modification of the tabular environment,
which deals with the problem of column heads that are
significantly wider than the body of the column.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tabularew/tabularew.sty
%doc %{_texmfdistdir}/doc/latex/tabularew/README
%doc %{_texmfdistdir}/doc/latex/tabularew/tabularew.pdf
#- source
%doc %{_texmfdistdir}/source/latex/tabularew/tabularew.dtx
%doc %{_texmfdistdir}/source/latex/tabularew/tabularew.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
