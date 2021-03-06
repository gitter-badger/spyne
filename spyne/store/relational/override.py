
#
# spyne - Copyright (C) Spyne contributors.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301
#


from sqlalchemy.ext.compiler import compiles

from sqlalchemy.dialects.postgresql import INET
from spyne.store.relational import PGXml, PGJson, PGHtml


@compiles(PGXml, "firebird")
def compile_xml_firebird(type_, compiler, **kw):
    return "blob"


@compiles(PGHtml, "firebird")
def compile_html_firebird(type_, compiler, **kw):
    return "blob"


@compiles(PGJson, "firebird")
def compile_json_firebird(type_, compiler, **kw):
    return "blob"


@compiles(INET, "firebird")
def compile_inet_firebird(type_, compiler, **kw):
    return "varchar(64)"
