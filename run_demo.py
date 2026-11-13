"""End-to-end demo: DXF plan -> column grid -> beam analysis -> deflection check.

Preliminary / educational only. Not for construction use without review by a
licensed structural engineer.
"""
import sys

from structural_agent.analysis import analytical_deflection, beam_midspan_deflection, check_deflection
from structural_agent.layout import max_beam_span, propose_column_grid
from structural_agent.plan_reader import read_plot_boundary

path = sys.argv[1] if len(sys.argv) > 1 else "examples/sample_plan.dxf"

plot = read_plot_boundary(path)
print(f"Plot: {plot.width:.1f} m x {plot.length:.1f} m, area {plot.area:.1f} m2")

cols, bx, by, sx, sy = propose_column_grid(plot, target_spacing=4.0)
print(f"Proposed grid: {bx} x {by} bays, spans {sx:.2f} m x {sy:.2f} m, {len(cols)} columns")

# Example beam: M25 concrete, 230 x 450 mm section, 20 kN/m total load
L = max_beam_span(sx, sy)
E = 5000 * (25 ** 0.5) * 1e6          # IS 456: Ec = 5000*sqrt(fck) MPa -> Pa
b, d = 0.230, 0.450
I = b * d**3 / 12
A = b * d
w = 20e3

fem = beam_midspan_deflection(L, w, E, I, A)
exact = analytical_deflection(L, w, E, I)
print(f"Beam span {L:.2f} m | OpenSees: {fem*1000:.2f} mm | Closed form: {exact*1000:.2f} mm")
print("Deflection check (span/250):", "PASS" if check_deflection(fem, L) else "FAIL")
print("NOTE: engineer review required before any real use.")
