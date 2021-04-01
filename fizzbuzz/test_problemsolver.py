# -*- coding: utf-8 -*-
from unittest import TestCase
from unittest.mock import patch
from solver import ProblemSolver

# ... définition des fonctions mock_convert et mock_display


def mock_convert(number, static={"count": 0}):
    static["count"] += 1
    if(static["count"] == 1):
        return ("first", static["count"])
    else:
        return ("other", static["count"])


def mock_display(chaine, first={"count": 0}, other={"count": 0}):
    if(chaine == "first"):
        first["count"] += 1
    elif(chaine == "other"):
        other["count"] += 1
    return (first["count"], other["count"])


class ProblemSolverTest(TestCase):

    def setUp(self):
        with patch('solver.Int2String') as mock:
            mock.convert = mock_convert
            converter = mock
        with patch('solver.Displayer') as mock:
            mock.display = mock_display
            displayer = mock
        self.solver = ProblemSolver(converter, displayer)

    def test_solve(self):
        self.solver.solve(100)
        # verify(converter, times(100)).convert(anyInt());
        self.assertEqual(100, self.solver.convert(0)[1]-1)
        # verify(printer, times(1)).display("first");
        self.assertEqual(1, self.solver.display("None")[0])
        # verify(printer, times(99)).display("other");
        self.assertEqual(99, self.solver.display("None")[1])

# ... méthodes testant le retour d'un appel à self.solver.solve
