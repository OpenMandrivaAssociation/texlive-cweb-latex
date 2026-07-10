%global tl_name cweb-latex
%global tl_revision 28878

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A LaTeX version of CWEB
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/cweb
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cweb-latex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cweb-latex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This bundle allows marking-up of CWEB code in LaTeX. The distribution
includes the "Counting Words" program distributed with CWEB, edited to
run with LaTeX.

