rpmbuild-demo-without-compilation
=================================

RPM build demonstration without compiling source code, only use checkouted source tree, and reictly build from plain files and directories.

ソースコードのビルドを必要とせず、リポジトリからcheckoutしたらそのままパッケージングできるような、PHPや設定ファイル等を想定したPRMパッケージの作り方の練習です。

日本語解説記事 : http://www.glamenv-septzen.net/view/1295

環境：
```
CentOS 6.5 x86_64版
$ rpm --version
RPM version 4.8.0
$ rpmbuild --version
RPM version 4.8.0
```
