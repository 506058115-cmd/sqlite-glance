# sqlite-glance

只读查看 SQLite 数据库中的表、视图和列名，不会打印任何行数据，也不会写入数据库。

## 使用

需要 Python 3.8+，SQLite 随 Python 提供，无需额外安装依赖。

~~~sh
python sqlite_glance.py ./app.db
~~~

工具以只读模式打开数据库，并启用查询只读保护。它会显示表名、列名、声明类型、主键和非空标记；不可打印字符会转义显示。名称等结构信息也可能敏感，请只对你有权查看的文件使用。

## 许可

MIT，见 [LICENSE](LICENSE)。
## Linux x86_64 下载

- [单文件版](https://github.com/506058115-cmd/sqlite-glance/releases/download/v1.0.0/sqlite-glance-linux-x86_64-onefile.tar.gz)
- [目录版](https://github.com/506058115-cmd/sqlite-glance/releases/download/v1.0.0/sqlite-glance-linux-x86_64-onedir.tar.gz)
- [v1.0.0 Release 页面](https://github.com/506058115-cmd/sqlite-glance/releases/tag/v1.0.0)

压缩包附带构建信息和依赖许可证；Release 另附 SHA-256 校验文件。产物在 WSL Ubuntu 24.04（Python 3.12.3、PyInstaller 6.22.2）中构建，目标为 GNU/Linux x86_64。较旧的发行版可能需要兼容的 glibc。
