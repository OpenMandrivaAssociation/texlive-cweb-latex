# revision 28878

# category Package
# catalog-ctan /macros/latex/contrib/cweb
# catalog-date 2013-01-19 01:25:39 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-cweb-latex
Version:	20130119
Release:	1
Summary:	A LaTeX version of CWEB
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cweb
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cweb-latex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cweb-latex.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This bundle allows marking-up of CWEB code in LaTeX. The
distribution includes the "Counting Words" program distributed
with CWEB, edited to run with LaTeX.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/cweb-latex/cwbl-german.sty
%{_texmfdistdir}/tex/latex/cweb-latex/cweb.cls
%{_texmfdistdir}/tex/latex/cweb-latex/cwebarray.sty
%{_texmfdistdir}/tex/latex/cweb-latex/cwebbase.tex
%{_texmfdistdir}/tex/latex/cweb-latex/keyvald.sty
%doc %{_texmfdistdir}/doc/latex/cweb-latex/CATALOG
%doc %{_texmfdistdir}/doc/latex/cweb-latex/History
%doc %{_texmfdistdir}/doc/latex/cweb-latex/INSTALL
%doc %{_texmfdistdir}/doc/latex/cweb-latex/License
%doc %{_texmfdistdir}/doc/latex/cweb-latex/MANIFEST
%doc %{_texmfdistdir}/doc/latex/cweb-latex/Makefile
%doc %{_texmfdistdir}/doc/latex/cweb-latex/README
%doc %{_texmfdistdir}/doc/latex/cweb-latex/contrib/Index
%doc %{_texmfdistdir}/doc/latex/cweb-latex/contrib/cwbl-deutsch.sty
%doc %{_texmfdistdir}/doc/latex/cweb-latex/contrib/cwbl-french.sty
%doc %{_texmfdistdir}/doc/latex/cweb-latex/contrib/cwbl-italian.sty
%doc %{_texmfdistdir}/doc/latex/cweb-latex/contrib/cweb-hy/README.txt
%doc %{_texmfdistdir}/doc/latex/cweb-latex/contrib/cweb-hy/cwbasehy.tex
%doc %{_texmfdistdir}/doc/latex/cweb-latex/contrib/cweb-hy/cweb-hy.cls
%doc %{_texmfdistdir}/doc/latex/cweb-latex/contrib/cweb-hy/nodoc.tex
%doc %{_texmfdistdir}/doc/latex/cweb-latex/contrib/wagner/cwebzw.sty
%doc %{_texmfdistdir}/doc/latex/cweb-latex/cweb-conf.pdf
%doc %{_texmfdistdir}/doc/latex/cweb-latex/cweb-user.pdf
%doc %{_texmfdistdir}/doc/latex/cweb-latex/examples/Makefile
%doc %{_texmfdistdir}/doc/latex/cweb-latex/examples/compare/wcltx.aux
%doc %{_texmfdistdir}/doc/latex/cweb-latex/examples/compare/wcltx.bbl
%doc %{_texmfdistdir}/doc/latex/cweb-latex/examples/compare/wcltx.dvi
%doc %{_texmfdistdir}/doc/latex/cweb-latex/examples/compare/wcltx.idx
%doc %{_texmfdistdir}/doc/latex/cweb-latex/examples/compare/wcltx.log
%doc %{_texmfdistdir}/doc/latex/cweb-latex/examples/compare/wcltx.scn
%doc %{_texmfdistdir}/doc/latex/cweb-latex/examples/compare/wcltx.tex
%doc %{_texmfdistdir}/doc/latex/cweb-latex/examples/rcs.sty
%doc %{_texmfdistdir}/doc/latex/cweb-latex/examples/tex-it
%doc %{_texmfdistdir}/doc/latex/cweb-latex/examples/wcltx.bib
%doc %{_texmfdistdir}/doc/latex/cweb-latex/examples/wcltx.w
%doc %{_texmfdistdir}/doc/latex/cweb-latex/src/Imakefile
%doc %{_texmfdistdir}/doc/latex/cweb-latex/src/README
%doc %{_texmfdistdir}/doc/latex/cweb-latex/src/TODO
%doc %{_texmfdistdir}/doc/latex/cweb-latex/src/cwbl-german.sty
%doc %{_texmfdistdir}/doc/latex/cweb-latex/src/cweave-spec.tex
%doc %{_texmfdistdir}/doc/latex/cweb-latex/src/cweb-conf.tex
%doc %{_texmfdistdir}/doc/latex/cweb-latex/src/cweb-doc.sty
%doc %{_texmfdistdir}/doc/latex/cweb-latex/src/cweb-fsa.fig
%doc %{_texmfdistdir}/doc/latex/cweb-latex/src/cweb-fsa.latex
%doc %{_texmfdistdir}/doc/latex/cweb-latex/src/cweb-fsa.ltx
%doc %{_texmfdistdir}/doc/latex/cweb-latex/src/cweb-user.tex
%doc %{_texmfdistdir}/doc/latex/cweb-latex/src/cweb.doc
%doc %{_texmfdistdir}/doc/latex/cweb-latex/src/cwebarray.sty
%doc %{_texmfdistdir}/doc/latex/cweb-latex/src/cwebbase.doc
%doc %{_texmfdistdir}/doc/latex/cweb-latex/src/cwebparts.doc
%doc %{_texmfdistdir}/doc/latex/cweb-latex/src/cwebx.sty
%doc %{_texmfdistdir}/doc/latex/cweb-latex/src/keyvald.dtx
%doc %{_texmfdistdir}/doc/latex/cweb-latex/src/keyvald.ins
%doc %{_texmfdistdir}/doc/latex/cweb-latex/src/style/cweb-doc.el
%doc %{_texmfdistdir}/doc/latex/cweb-latex/src/test/Imakefile
%doc %{_texmfdistdir}/doc/latex/cweb-latex/src/test/badend.w
%doc %{_texmfdistdir}/doc/latex/cweb-latex/src/test/badopts.w
%doc %{_texmfdistdir}/doc/latex/cweb-latex/src/test/change.ch
%doc %{_texmfdistdir}/doc/latex/cweb-latex/src/test/change.w
%doc %{_texmfdistdir}/doc/latex/cweb-latex/src/test/enddocbegin.w
%doc %{_texmfdistdir}/doc/latex/cweb-latex/src/test/flat.w
%doc %{_texmfdistdir}/doc/latex/cweb-latex/src/test/german.w
%doc %{_texmfdistdir}/doc/latex/cweb-latex/src/test/language-german.ch
%doc %{_texmfdistdir}/doc/latex/cweb-latex/src/test/language-german.w
%doc %{_texmfdistdir}/doc/latex/cweb-latex/src/test/minimal.w
%doc %{_texmfdistdir}/doc/latex/cweb-latex/src/test/modes.w
%doc %{_texmfdistdir}/doc/latex/cweb-latex/src/test/newif.w
%doc %{_texmfdistdir}/doc/latex/cweb-latex/src/test/nolists.w
%doc %{_texmfdistdir}/doc/latex/cweb-latex/src/test/parts-code.w
%doc %{_texmfdistdir}/doc/latex/cweb-latex/src/test/parts.tex
%doc %{_texmfdistdir}/doc/latex/cweb-latex/src/test/refname.w
%doc %{_texmfdistdir}/doc/latex/cweb-latex/src/test/report.w
%doc %{_texmfdistdir}/doc/latex/cweb-latex/src/test/section.w
%doc %{_texmfdistdir}/doc/latex/cweb-latex/src/test/sup-changes.w
%doc %{_texmfdistdir}/doc/latex/cweb-latex/src/test/sup-format.w
%doc %{_texmfdistdir}/doc/latex/cweb-latex/src/test/sup-lists.w
%doc %{_texmfdistdir}/doc/latex/cweb-latex/src/test/titlepage.w
%doc %{_texmfdistdir}/doc/latex/cweb-latex/src/test/token.w
%doc %{_texmfdistdir}/doc/latex/cweb-latex/src/test/vbar.w

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
