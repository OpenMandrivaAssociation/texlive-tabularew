%global tl_name tabularew
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	A variation on the tabular environment
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tabularew
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tabularew.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tabularew.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tabularew.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package offers a modification of the tabular environment, which
deals with the problem of column heads that are significantly wider than
the body of the column.

