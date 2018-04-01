# Copyright (C) 2018 The NeoVintageous Team (NeoVintageous).
#
# This file is part of NeoVintageous.
#
# NeoVintageous is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# NeoVintageous is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with NeoVintageous.  If not, see <https://www.gnu.org/licenses/>.

from .tokens import TokenEof
from .tokens import TokenCommand


def scan_cmd_file(state):
    command = TokenCommand('file')
    bang = state.consume()
    if bang == state.EOF:
        return None, [command, TokenEof()]

    bang = bang == '!'
    if not bang:
        raise Exception("E488: Trailing characters")

    state.expect_eof(on_error=lambda: Exception("E488: Trailing characters"))

    command.forced = bang

    return None, [command, TokenEof()]
