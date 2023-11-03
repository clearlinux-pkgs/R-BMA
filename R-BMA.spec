#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-BMA
Version  : 3.18.17
Release  : 30
URL      : https://cran.r-project.org/src/contrib/BMA_3.18.17.tar.gz
Source0  : https://cran.r-project.org/src/contrib/BMA_3.18.17.tar.gz
Summary  : Bayesian Model Averaging
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-BMA-lib = %{version}-%{release}
Requires: R-inline
Requires: R-leaps
Requires: R-robustbase
Requires: R-rrcov
BuildRequires : R-inline
BuildRequires : R-leaps
BuildRequires : R-robustbase
BuildRequires : R-rrcov
BuildRequires : buildreq-R

%description
generalized linear models and survival models (cox
        regression).

%package lib
Summary: lib components for the R-BMA package.
Group: Libraries

%description lib
lib components for the R-BMA package.


%prep
%setup -q -c -n BMA
cd %{_builddir}/BMA

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1650738840

%install
export SOURCE_DATE_EPOCH=1650738840
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library BMA
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library BMA
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library BMA
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc BMA || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/BMA/DESCRIPTION
/usr/lib64/R/library/BMA/INDEX
/usr/lib64/R/library/BMA/Meta/Rd.rds
/usr/lib64/R/library/BMA/Meta/data.rds
/usr/lib64/R/library/BMA/Meta/features.rds
/usr/lib64/R/library/BMA/Meta/hsearch.rds
/usr/lib64/R/library/BMA/Meta/links.rds
/usr/lib64/R/library/BMA/Meta/nsInfo.rds
/usr/lib64/R/library/BMA/Meta/package.rds
/usr/lib64/R/library/BMA/NAMESPACE
/usr/lib64/R/library/BMA/R/BMA
/usr/lib64/R/library/BMA/R/BMA.rdb
/usr/lib64/R/library/BMA/R/BMA.rdx
/usr/lib64/R/library/BMA/data/race.RData
/usr/lib64/R/library/BMA/data/vaso.txt.gz
/usr/lib64/R/library/BMA/help/AnIndex
/usr/lib64/R/library/BMA/help/BMA.rdb
/usr/lib64/R/library/BMA/help/BMA.rdx
/usr/lib64/R/library/BMA/help/aliases.rds
/usr/lib64/R/library/BMA/help/paths.rds
/usr/lib64/R/library/BMA/html/00Index.html
/usr/lib64/R/library/BMA/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/BMA/libs/BMA.so
/usr/lib64/R/library/BMA/libs/BMA.so.avx2
/usr/lib64/R/library/BMA/libs/BMA.so.avx512
