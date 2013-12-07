# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/tabularew
# catalog-date 2009-11-10 00:58:07 +0100
# catalog-license lppl
# catalog-version 0.1
Name:		texlive-tabularew
Version:	0.1
Release:	6
Summary:	A variation on the tabular environment
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tabularew
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabularew.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabularew.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabularew.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.1-2
+ Revision: 756460
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.1-1
+ Revision: 719647
- texlive-tabularew
- texlive-tabularew
- texlive-tabularew

