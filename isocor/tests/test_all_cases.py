"""Test the entire correction process at low- and high-resolution to cover all the situations that can be encountered.

This aims to verify that no error will be raised during normal usage.
This set of tests correct a measurement vector (set to unity, i.e. [1,1,1,1]
for a compound with 3 atoms of the tracer element) in all the possible combinations of the following situations:

* formulas: C1, C2, O1, O2, O3P3N3H3C3
* tracer elements: 13C, 17O, 18O
* derivative: H, H2, O, O2
* purity: 100%
* resolution (for high-resolution correction only): 10000, 100000, 1000000
* correct NA: True, False

Total number of tests: 240
"""

import numpy as np
import pytest
import isocor as hrcor


@pytest.mark.parametrize("data", [{"formula": "C1",
"resolution_at_400": 10000,
"derivative_formula": "H2",
"tracer": "13C",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0]},
{"formula": "C1",
"resolution_at_400": 100000,
"derivative_formula": "H2",
"tracer": "13C",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0]},
{"formula": "C1",
"resolution_at_400": 1000000,
"derivative_formula": "H2",
"tracer": "13C",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0]},
{"formula": "C1",
"resolution_at_400": 10000,
"derivative_formula": "H2",
"tracer": "13C",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0]},
{"formula": "C1",
"resolution_at_400": 100000,
"derivative_formula": "H2",
"tracer": "13C",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0]},
{"formula": "C1",
"resolution_at_400": 1000000,
"derivative_formula": "H2",
"tracer": "13C",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0]},
{"formula": "C2",
"resolution_at_400": 10000,
"derivative_formula": "H2",
"tracer": "13C",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0]},
{"formula": "C2",
"resolution_at_400": 100000,
"derivative_formula": "H2",
"tracer": "13C",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0]},
{"formula": "C2",
"resolution_at_400": 1000000,
"derivative_formula": "H2",
"tracer": "13C",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0]},
{"formula": "C2",
"resolution_at_400": 10000,
"derivative_formula": "H2",
"tracer": "13C",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0]},
{"formula": "C2",
"resolution_at_400": 100000,
"derivative_formula": "H2",
"tracer": "13C",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0]},
{"formula": "C2",
"resolution_at_400": 1000000,
"derivative_formula": "H2",
"tracer": "13C",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0]},
{"formula": "O1",
"resolution_at_400": 10000,
"derivative_formula": "H2",
"tracer": "17O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0, 0.0]},
{"formula": "O1",
"resolution_at_400": 100000,
"derivative_formula": "H2",
"tracer": "17O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0, 0.0]},
{"formula": "O1",
"resolution_at_400": 1000000,
"derivative_formula": "H2",
"tracer": "17O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0, 0.0]},
{"formula": "O1",
"resolution_at_400": 10000,
"derivative_formula": "H2",
"tracer": "17O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0, 0.0]},
{"formula": "O1",
"resolution_at_400": 100000,
"derivative_formula": "H2",
"tracer": "17O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0, 0.0]},
{"formula": "O1",
"resolution_at_400": 1000000,
"derivative_formula": "H2",
"tracer": "17O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0, 0.0]},
{"formula": "O2",
"resolution_at_400": 10000,
"derivative_formula": "H2",
"tracer": "17O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0, 0.0]},
{"formula": "O2",
"resolution_at_400": 100000,
"derivative_formula": "H2",
"tracer": "17O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0, 0.0]},
{"formula": "O2",
"resolution_at_400": 1000000,
"derivative_formula": "H2",
"tracer": "17O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0, 0.0]},
{"formula": "O2",
"resolution_at_400": 10000,
"derivative_formula": "H2",
"tracer": "17O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0, 0.0]},
{"formula": "O2",
"resolution_at_400": 100000,
"derivative_formula": "H2",
"tracer": "17O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0, 0.0]},
{"formula": "O2",
"resolution_at_400": 1000000,
"derivative_formula": "H2",
"tracer": "17O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0, 0.0]},
{"formula": "O1",
"resolution_at_400": 10000,
"derivative_formula": "H2",
"tracer": "18O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O1",
"resolution_at_400": 100000,
"derivative_formula": "H2",
"tracer": "18O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O1",
"resolution_at_400": 1000000,
"derivative_formula": "H2",
"tracer": "18O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O1",
"resolution_at_400": 10000,
"derivative_formula": "H2",
"tracer": "18O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O1",
"resolution_at_400": 100000,
"derivative_formula": "H2",
"tracer": "18O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O1",
"resolution_at_400": 1000000,
"derivative_formula": "H2",
"tracer": "18O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O2",
"resolution_at_400": 10000,
"derivative_formula": "H2",
"tracer": "18O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O2",
"resolution_at_400": 100000,
"derivative_formula": "H2",
"tracer": "18O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O2",
"resolution_at_400": 1000000,
"derivative_formula": "H2",
"tracer": "18O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O2",
"resolution_at_400": 10000,
"derivative_formula": "H2",
"tracer": "18O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O2",
"resolution_at_400": 100000,
"derivative_formula": "H2",
"tracer": "18O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O2",
"resolution_at_400": 1000000,
"derivative_formula": "H2",
"tracer": "18O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 10000,
"derivative_formula": "H2",
"tracer": "18O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 100000,
"derivative_formula": "H2",
"tracer": "18O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 1000000,
"derivative_formula": "H2",
"tracer": "18O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 10000,
"derivative_formula": "H2",
"tracer": "18O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 100000,
"derivative_formula": "H2",
"tracer": "18O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 1000000,
"derivative_formula": "H2",
"tracer": "18O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 10000,
"derivative_formula": "H2",
"tracer": "18O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 100000,
"derivative_formula": "H2",
"tracer": "18O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 1000000,
"derivative_formula": "H2",
"tracer": "18O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 10000,
"derivative_formula": "H2",
"tracer": "18O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 100000,
"derivative_formula": "H2",
"tracer": "18O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 1000000,
"derivative_formula": "H2",
"tracer": "18O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 10000,
"derivative_formula": "H2",
"tracer": "13C",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 100000,
"derivative_formula": "H2",
"tracer": "13C",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 1000000,
"derivative_formula": "H2",
"tracer": "13C",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 10000,
"derivative_formula": "H2",
"tracer": "13C",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 100000,
"derivative_formula": "H2",
"tracer": "13C",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 1000000,
"derivative_formula": "H2",
"tracer": "13C",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 10000,
"derivative_formula": "H2",
"tracer": "13C",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 100000,
"derivative_formula": "H2",
"tracer": "13C",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 1000000,
"derivative_formula": "H2",
"tracer": "13C",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 10000,
"derivative_formula": "H2",
"tracer": "13C",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 100000,
"derivative_formula": "H2",
"tracer": "13C",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 1000000,
"derivative_formula": "H2",
"tracer": "13C",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0]},
{"formula": "C1",
"resolution_at_400": 10000,
"derivative_formula": "O",
"tracer": "13C",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0]},
{"formula": "C1",
"resolution_at_400": 100000,
"derivative_formula": "O",
"tracer": "13C",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0]},
{"formula": "C1",
"resolution_at_400": 1000000,
"derivative_formula": "O",
"tracer": "13C",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0]},
{"formula": "C1",
"resolution_at_400": 10000,
"derivative_formula": "O",
"tracer": "13C",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0]},
{"formula": "C1",
"resolution_at_400": 100000,
"derivative_formula": "O",
"tracer": "13C",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0]},
{"formula": "C1",
"resolution_at_400": 1000000,
"derivative_formula": "O",
"tracer": "13C",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0]},
{"formula": "C2",
"resolution_at_400": 10000,
"derivative_formula": "O",
"tracer": "13C",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0]},
{"formula": "C2",
"resolution_at_400": 100000,
"derivative_formula": "O",
"tracer": "13C",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0]},
{"formula": "C2",
"resolution_at_400": 1000000,
"derivative_formula": "O",
"tracer": "13C",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0]},
{"formula": "C2",
"resolution_at_400": 10000,
"derivative_formula": "O",
"tracer": "13C",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0]},
{"formula": "C2",
"resolution_at_400": 100000,
"derivative_formula": "O",
"tracer": "13C",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0]},
{"formula": "C2",
"resolution_at_400": 1000000,
"derivative_formula": "O",
"tracer": "13C",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0]},
{"formula": "O1",
"resolution_at_400": 10000,
"derivative_formula": "O",
"tracer": "17O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0, 0.0]},
{"formula": "O1",
"resolution_at_400": 100000,
"derivative_formula": "O",
"tracer": "17O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0, 0.0]},
{"formula": "O1",
"resolution_at_400": 1000000,
"derivative_formula": "O",
"tracer": "17O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0, 0.0]},
{"formula": "O1",
"resolution_at_400": 10000,
"derivative_formula": "O",
"tracer": "17O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0, 0.0]},
{"formula": "O1",
"resolution_at_400": 100000,
"derivative_formula": "O",
"tracer": "17O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0, 0.0]},
{"formula": "O1",
"resolution_at_400": 1000000,
"derivative_formula": "O",
"tracer": "17O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0, 0.0]},
{"formula": "O2",
"resolution_at_400": 10000,
"derivative_formula": "O",
"tracer": "17O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0, 0.0]},
{"formula": "O2",
"resolution_at_400": 100000,
"derivative_formula": "O",
"tracer": "17O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0, 0.0]},
{"formula": "O2",
"resolution_at_400": 1000000,
"derivative_formula": "O",
"tracer": "17O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0, 0.0]},
{"formula": "O2",
"resolution_at_400": 10000,
"derivative_formula": "O",
"tracer": "17O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0, 0.0]},
{"formula": "O2",
"resolution_at_400": 100000,
"derivative_formula": "O",
"tracer": "17O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0, 0.0]},
{"formula": "O2",
"resolution_at_400": 1000000,
"derivative_formula": "O",
"tracer": "17O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0, 0.0]},
{"formula": "O1",
"resolution_at_400": 10000,
"derivative_formula": "O",
"tracer": "18O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O1",
"resolution_at_400": 100000,
"derivative_formula": "O",
"tracer": "18O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O1",
"resolution_at_400": 1000000,
"derivative_formula": "O",
"tracer": "18O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O1",
"resolution_at_400": 10000,
"derivative_formula": "O",
"tracer": "18O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O1",
"resolution_at_400": 100000,
"derivative_formula": "O",
"tracer": "18O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O1",
"resolution_at_400": 1000000,
"derivative_formula": "O",
"tracer": "18O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O2",
"resolution_at_400": 10000,
"derivative_formula": "O",
"tracer": "18O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O2",
"resolution_at_400": 100000,
"derivative_formula": "O",
"tracer": "18O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O2",
"resolution_at_400": 1000000,
"derivative_formula": "O",
"tracer": "18O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O2",
"resolution_at_400": 10000,
"derivative_formula": "O",
"tracer": "18O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O2",
"resolution_at_400": 100000,
"derivative_formula": "O",
"tracer": "18O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O2",
"resolution_at_400": 1000000,
"derivative_formula": "O",
"tracer": "18O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 10000,
"derivative_formula": "O",
"tracer": "18O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 100000,
"derivative_formula": "O",
"tracer": "18O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 1000000,
"derivative_formula": "O",
"tracer": "18O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 10000,
"derivative_formula": "O",
"tracer": "18O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 100000,
"derivative_formula": "O",
"tracer": "18O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 1000000,
"derivative_formula": "O",
"tracer": "18O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 10000,
"derivative_formula": "O",
"tracer": "18O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 100000,
"derivative_formula": "O",
"tracer": "18O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 1000000,
"derivative_formula": "O",
"tracer": "18O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 10000,
"derivative_formula": "O",
"tracer": "18O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 100000,
"derivative_formula": "O",
"tracer": "18O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 1000000,
"derivative_formula": "O",
"tracer": "18O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 10000,
"derivative_formula": "O",
"tracer": "13C",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 100000,
"derivative_formula": "O",
"tracer": "13C",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 1000000,
"derivative_formula": "O",
"tracer": "13C",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 10000,
"derivative_formula": "O",
"tracer": "13C",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 100000,
"derivative_formula": "O",
"tracer": "13C",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 1000000,
"derivative_formula": "O",
"tracer": "13C",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 10000,
"derivative_formula": "O",
"tracer": "13C",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 100000,
"derivative_formula": "O",
"tracer": "13C",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 1000000,
"derivative_formula": "O",
"tracer": "13C",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 10000,
"derivative_formula": "O",
"tracer": "13C",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 100000,
"derivative_formula": "O",
"tracer": "13C",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 1000000,
"derivative_formula": "O",
"tracer": "13C",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0]},
{"formula": "C1",
"resolution_at_400": 10000,
"derivative_formula": "O2",
"tracer": "13C",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0]},
{"formula": "C1",
"resolution_at_400": 100000,
"derivative_formula": "O2",
"tracer": "13C",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0]},
{"formula": "C1",
"resolution_at_400": 1000000,
"derivative_formula": "O2",
"tracer": "13C",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0]},
{"formula": "C1",
"resolution_at_400": 10000,
"derivative_formula": "O2",
"tracer": "13C",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0]},
{"formula": "C1",
"resolution_at_400": 100000,
"derivative_formula": "O2",
"tracer": "13C",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0]},
{"formula": "C1",
"resolution_at_400": 1000000,
"derivative_formula": "O2",
"tracer": "13C",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0]},
{"formula": "C2",
"resolution_at_400": 10000,
"derivative_formula": "O2",
"tracer": "13C",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0]},
{"formula": "C2",
"resolution_at_400": 100000,
"derivative_formula": "O2",
"tracer": "13C",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0]},
{"formula": "C2",
"resolution_at_400": 1000000,
"derivative_formula": "O2",
"tracer": "13C",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0]},
{"formula": "C2",
"resolution_at_400": 10000,
"derivative_formula": "O2",
"tracer": "13C",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0]},
{"formula": "C2",
"resolution_at_400": 100000,
"derivative_formula": "O2",
"tracer": "13C",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0]},
{"formula": "C2",
"resolution_at_400": 1000000,
"derivative_formula": "O2",
"tracer": "13C",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0]},
{"formula": "O1",
"resolution_at_400": 10000,
"derivative_formula": "O2",
"tracer": "17O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0, 0.0]},
{"formula": "O1",
"resolution_at_400": 100000,
"derivative_formula": "O2",
"tracer": "17O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0, 0.0]},
{"formula": "O1",
"resolution_at_400": 1000000,
"derivative_formula": "O2",
"tracer": "17O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0, 0.0]},
{"formula": "O1",
"resolution_at_400": 10000,
"derivative_formula": "O2",
"tracer": "17O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0, 0.0]},
{"formula": "O1",
"resolution_at_400": 100000,
"derivative_formula": "O2",
"tracer": "17O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0, 0.0]},
{"formula": "O1",
"resolution_at_400": 1000000,
"derivative_formula": "O2",
"tracer": "17O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0, 0.0]},
{"formula": "O2",
"resolution_at_400": 10000,
"derivative_formula": "O2",
"tracer": "17O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0, 0.0]},
{"formula": "O2",
"resolution_at_400": 100000,
"derivative_formula": "O2",
"tracer": "17O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0, 0.0]},
{"formula": "O2",
"resolution_at_400": 1000000,
"derivative_formula": "O2",
"tracer": "17O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0, 0.0]},
{"formula": "O2",
"resolution_at_400": 10000,
"derivative_formula": "O2",
"tracer": "17O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0, 0.0]},
{"formula": "O2",
"resolution_at_400": 100000,
"derivative_formula": "O2",
"tracer": "17O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0, 0.0]},
{"formula": "O2",
"resolution_at_400": 1000000,
"derivative_formula": "O2",
"tracer": "17O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0, 0.0]},
{"formula": "O1",
"resolution_at_400": 10000,
"derivative_formula": "O2",
"tracer": "18O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O1",
"resolution_at_400": 100000,
"derivative_formula": "O2",
"tracer": "18O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O1",
"resolution_at_400": 1000000,
"derivative_formula": "O2",
"tracer": "18O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O1",
"resolution_at_400": 10000,
"derivative_formula": "O2",
"tracer": "18O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O1",
"resolution_at_400": 100000,
"derivative_formula": "O2",
"tracer": "18O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O1",
"resolution_at_400": 1000000,
"derivative_formula": "O2",
"tracer": "18O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O2",
"resolution_at_400": 10000,
"derivative_formula": "O2",
"tracer": "18O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O2",
"resolution_at_400": 100000,
"derivative_formula": "O2",
"tracer": "18O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O2",
"resolution_at_400": 1000000,
"derivative_formula": "O2",
"tracer": "18O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O2",
"resolution_at_400": 10000,
"derivative_formula": "O2",
"tracer": "18O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O2",
"resolution_at_400": 100000,
"derivative_formula": "O2",
"tracer": "18O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O2",
"resolution_at_400": 1000000,
"derivative_formula": "O2",
"tracer": "18O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 10000,
"derivative_formula": "O2",
"tracer": "18O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 100000,
"derivative_formula": "O2",
"tracer": "18O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 1000000,
"derivative_formula": "O2",
"tracer": "18O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 10000,
"derivative_formula": "O2",
"tracer": "18O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 100000,
"derivative_formula": "O2",
"tracer": "18O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 1000000,
"derivative_formula": "O2",
"tracer": "18O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 10000,
"derivative_formula": "O2",
"tracer": "18O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 100000,
"derivative_formula": "O2",
"tracer": "18O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 1000000,
"derivative_formula": "O2",
"tracer": "18O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 10000,
"derivative_formula": "O2",
"tracer": "18O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 100000,
"derivative_formula": "O2",
"tracer": "18O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 1000000,
"derivative_formula": "O2",
"tracer": "18O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 10000,
"derivative_formula": "O2",
"tracer": "13C",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 100000,
"derivative_formula": "O2",
"tracer": "13C",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 1000000,
"derivative_formula": "O2",
"tracer": "13C",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 10000,
"derivative_formula": "O2",
"tracer": "13C",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 100000,
"derivative_formula": "O2",
"tracer": "13C",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 1000000,
"derivative_formula": "O2",
"tracer": "13C",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 10000,
"derivative_formula": "O2",
"tracer": "13C",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 100000,
"derivative_formula": "O2",
"tracer": "13C",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 1000000,
"derivative_formula": "O2",
"tracer": "13C",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 10000,
"derivative_formula": "O2",
"tracer": "13C",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 100000,
"derivative_formula": "O2",
"tracer": "13C",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 1000000,
"derivative_formula": "O2",
"tracer": "13C",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0]},
{"formula": "C1",
"resolution_at_400": 10000,
"derivative_formula": "H",
"tracer": "13C",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0]},
{"formula": "C1",
"resolution_at_400": 100000,
"derivative_formula": "H",
"tracer": "13C",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0]},
{"formula": "C1",
"resolution_at_400": 1000000,
"derivative_formula": "H",
"tracer": "13C",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0]},
{"formula": "C1",
"resolution_at_400": 10000,
"derivative_formula": "H",
"tracer": "13C",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0]},
{"formula": "C1",
"resolution_at_400": 100000,
"derivative_formula": "H",
"tracer": "13C",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0]},
{"formula": "C1",
"resolution_at_400": 1000000,
"derivative_formula": "H",
"tracer": "13C",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0]},
{"formula": "C2",
"resolution_at_400": 10000,
"derivative_formula": "H",
"tracer": "13C",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0]},
{"formula": "C2",
"resolution_at_400": 100000,
"derivative_formula": "H",
"tracer": "13C",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0]},
{"formula": "C2",
"resolution_at_400": 1000000,
"derivative_formula": "H",
"tracer": "13C",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0]},
{"formula": "C2",
"resolution_at_400": 10000,
"derivative_formula": "H",
"tracer": "13C",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0]},
{"formula": "C2",
"resolution_at_400": 100000,
"derivative_formula": "H",
"tracer": "13C",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0]},
{"formula": "C2",
"resolution_at_400": 1000000,
"derivative_formula": "H",
"tracer": "13C",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0]},
{"formula": "O1",
"resolution_at_400": 10000,
"derivative_formula": "H",
"tracer": "17O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0, 0.0]},
{"formula": "O1",
"resolution_at_400": 100000,
"derivative_formula": "H",
"tracer": "17O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0, 0.0]},
{"formula": "O1",
"resolution_at_400": 1000000,
"derivative_formula": "H",
"tracer": "17O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0, 0.0]},
{"formula": "O1",
"resolution_at_400": 10000,
"derivative_formula": "H",
"tracer": "17O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0, 0.0]},
{"formula": "O1",
"resolution_at_400": 100000,
"derivative_formula": "H",
"tracer": "17O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0, 0.0]},
{"formula": "O1",
"resolution_at_400": 1000000,
"derivative_formula": "H",
"tracer": "17O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0, 0.0]},
{"formula": "O2",
"resolution_at_400": 10000,
"derivative_formula": "H",
"tracer": "17O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0, 0.0]},
{"formula": "O2",
"resolution_at_400": 100000,
"derivative_formula": "H",
"tracer": "17O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0, 0.0]},
{"formula": "O2",
"resolution_at_400": 1000000,
"derivative_formula": "H",
"tracer": "17O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0, 0.0]},
{"formula": "O2",
"resolution_at_400": 10000,
"derivative_formula": "H",
"tracer": "17O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0, 0.0]},
{"formula": "O2",
"resolution_at_400": 100000,
"derivative_formula": "H",
"tracer": "17O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0, 0.0]},
{"formula": "O2",
"resolution_at_400": 1000000,
"derivative_formula": "H",
"tracer": "17O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0, 0.0]},
{"formula": "O1",
"resolution_at_400": 10000,
"derivative_formula": "H",
"tracer": "18O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O1",
"resolution_at_400": 100000,
"derivative_formula": "H",
"tracer": "18O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O1",
"resolution_at_400": 1000000,
"derivative_formula": "H",
"tracer": "18O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O1",
"resolution_at_400": 10000,
"derivative_formula": "H",
"tracer": "18O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O1",
"resolution_at_400": 100000,
"derivative_formula": "H",
"tracer": "18O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O1",
"resolution_at_400": 1000000,
"derivative_formula": "H",
"tracer": "18O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O2",
"resolution_at_400": 10000,
"derivative_formula": "H",
"tracer": "18O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O2",
"resolution_at_400": 100000,
"derivative_formula": "H",
"tracer": "18O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O2",
"resolution_at_400": 1000000,
"derivative_formula": "H",
"tracer": "18O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O2",
"resolution_at_400": 10000,
"derivative_formula": "H",
"tracer": "18O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O2",
"resolution_at_400": 100000,
"derivative_formula": "H",
"tracer": "18O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O2",
"resolution_at_400": 1000000,
"derivative_formula": "H",
"tracer": "18O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 10000,
"derivative_formula": "H",
"tracer": "18O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 100000,
"derivative_formula": "H",
"tracer": "18O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 1000000,
"derivative_formula": "H",
"tracer": "18O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 10000,
"derivative_formula": "H",
"tracer": "18O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 100000,
"derivative_formula": "H",
"tracer": "18O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 1000000,
"derivative_formula": "H",
"tracer": "18O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 10000,
"derivative_formula": "H",
"tracer": "18O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 100000,
"derivative_formula": "H",
"tracer": "18O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 1000000,
"derivative_formula": "H",
"tracer": "18O",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 10000,
"derivative_formula": "H",
"tracer": "18O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 100000,
"derivative_formula": "H",
"tracer": "18O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 1000000,
"derivative_formula": "H",
"tracer": "18O",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 10000,
"derivative_formula": "H",
"tracer": "13C",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 100000,
"derivative_formula": "H",
"tracer": "13C",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 1000000,
"derivative_formula": "H",
"tracer": "13C",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 10000,
"derivative_formula": "H",
"tracer": "13C",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 100000,
"derivative_formula": "H",
"tracer": "13C",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 1000000,
"derivative_formula": "H",
"tracer": "13C",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 10000,
"derivative_formula": "H",
"tracer": "13C",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 100000,
"derivative_formula": "H",
"tracer": "13C",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 1000000,
"derivative_formula": "H",
"tracer": "13C",
"correct_NA_tracer": True,
"tracer_purity": [0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 10000,
"derivative_formula": "H",
"tracer": "13C",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 100000,
"derivative_formula": "H",
"tracer": "13C",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0]},
{"formula": "O3P3N3H3C3",
"resolution_at_400": 1000000,
"derivative_formula": "H",
"tracer": "13C",
"correct_NA_tracer": False,
"tracer_purity": [0.0, 1.0]}])

def test_correction_process_misc(data, data_iso):
    """Tests the entire correction process at high resolution.

    Combination of all the following situations:
      - formulas: O3P3N3H3C3, C1, O1, O2, C2, O1
      - tracer elements: 13C (2 isotopes), 17O (3 isotopes), 18O (3 isotopes)
      - derivative: H, H2, O, O2
      - purity: 100%
      - resolution: 10000, 100000, 1000000
      - correct NA: True, False

    Total number of tests: 240
    """
    formula = data["formula"]
    derivative_formula = data["derivative_formula"]
    # Perform correction
    HRmetabolite = hrcor.HighResMetaboliteCorrector(formula, data["tracer"], data_isotopes=data_iso,
                                                    resolution=data["resolution_at_400"],
                                                    resolution_formula_code = "orbitrap",
                                                    mz_of_resolution=400,
                                                    derivative_formula=derivative_formula,
                                                    correct_NA_tracer=data["correct_NA_tracer"],
                                                    tracer_purity=data["tracer_purity"])
    LRmetabolite = hrcor.LowResMetaboliteCorrector(formula, data["tracer"], data_isotopes=data_iso,
                                                   correct_NA_tracer=data["correct_NA_tracer"],
                                                   derivative_formula=derivative_formula,
                                                   tracer_purity=data["tracer_purity"])
    tracer_element = data["tracer"][2]
    v_measured = [1] * (HRmetabolite.formula[tracer_element] + 1)
    _, v_correctedHR, _, _ = HRmetabolite.correct(v_measured)
    _, v_correctedLR, _, _ = LRmetabolite.correct(v_measured)
