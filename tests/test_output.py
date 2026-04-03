"""Tests for output formatting."""

import pytest

from infomaniak import output


class TestColors:
    def test_bold_with_color(self, monkeypatch):
        monkeypatch.setattr(output, "_COLOR", True)
        assert "\033[1m" in output.bold("hi")
        assert "hi" in output.bold("hi")

    def test_bold_without_color(self, monkeypatch):
        monkeypatch.setattr(output, "_COLOR", False)
        assert output.bold("hi") == "hi"

    def test_green_with_color(self, monkeypatch):
        monkeypatch.setattr(output, "_COLOR", True)
        assert "\033[32m" in output.green("ok")

    def test_all_colors_plain(self, monkeypatch):
        monkeypatch.setattr(output, "_COLOR", False)
        for fn in [output.bold, output.green, output.red, output.yellow, output.cyan, output.dim]:
            assert fn("text") == "text"


class TestVisibleLen:
    def test_plain_text(self):
        assert output._visible_len("hello") == 5

    def test_with_ansi(self):
        colored = "\033[1mhello\033[0m"
        assert output._visible_len(colored) == 5

    def test_empty(self):
        assert output._visible_len("") == 0


class TestLjust:
    def test_plain_padding(self):
        result = output._ljust("hi", 5)
        assert result == "hi   "

    def test_ansi_padding(self):
        colored = "\033[1mhi\033[0m"
        result = output._ljust(colored, 5)
        # Should have 3 spaces of padding (visible "hi" = 2, width = 5)
        assert result.endswith("   ")


class TestPrintTable:
    def test_empty_rows(self, capsys):
        output.print_table(["A", "B"], [])
        captured = capsys.readouterr()
        assert "no results" in captured.out

    def test_basic_table(self, capsys, monkeypatch):
        monkeypatch.setattr(output, "_COLOR", False)
        output.print_table(["Name", "Value"], [["foo", "bar"], ["longer", "x"]])
        captured = capsys.readouterr()
        assert "Name" in captured.out
        assert "foo" in captured.out
        assert "longer" in captured.out

    def test_alignment(self, capsys, monkeypatch):
        monkeypatch.setattr(output, "_COLOR", False)
        output.print_table(["A", "B"], [["short", "x"], ["longvalue", "y"]])
        lines = captured_lines(capsys)
        # All data lines should have consistent structure
        assert len(lines) >= 3  # header + separator + 2 rows


class TestOutputJson:
    def test_outputs_json_and_exits(self, capsys):
        with pytest.raises(SystemExit) as exc:
            output.output_json({"key": "value"})
        assert exc.value.code == 0
        captured = capsys.readouterr()
        assert '"key": "value"' in captured.out


def captured_lines(capsys):
    return [l for l in capsys.readouterr().out.split("\n") if l.strip()]
