#!/usr/bin/env python3
"""Show SQLite tables and columns without printing database rows."""

import argparse
from pathlib import Path
import sqlite3
import sys


def terminal_safe(value):
    return "".join(
        char if char.isprintable() else char.encode("unicode_escape").decode("ascii")
        for char in value
    )


def quote_identifier(value):
    return '"' + value.replace('"', '""') + '"'


def inspect_database(path):
    uri = path.resolve().as_uri() + "?mode=ro"
    connection = sqlite3.connect(uri, uri=True)
    try:
        connection.execute("PRAGMA query_only = ON")
        objects = connection.execute(
            "SELECT type, name FROM sqlite_master "
            "WHERE type IN ('table', 'view') "
            "AND substr(name, 1, 7) != 'sqlite_' ORDER BY type, name"
        ).fetchall()
        if not objects:
            print("没有找到用户表或视图。")
            return

        for kind, name in objects:
            columns = connection.execute(
                f"PRAGMA table_info({quote_identifier(name)})"
            ).fetchall()
            print(f"\n{kind}: {terminal_safe(name)}")
            if not columns:
                print("  （没有列信息）")
                continue
            for column in columns:
                _, column_name, column_type, not_null, _, primary_key = column
                details = terminal_safe(column_type) if column_type else "未声明类型"
                if primary_key:
                    details += ", 主键"
                if not_null:
                    details += ", 非空"
                print(f"  {terminal_safe(column_name)}: {details}")
    finally:
        connection.close()


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="只读查看 SQLite 数据库中的表、视图和列，不显示行数据。"
    )
    parser.add_argument("database", help="SQLite 数据库文件")
    args = parser.parse_args(argv)

    path = Path(args.database).expanduser()
    try:
        inspect_database(path)
    except (OSError, UnicodeError, sqlite3.Error) as error:
        print(
            f"sqlite-glance: 无法读取数据库：{terminal_safe(str(error))}",
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
