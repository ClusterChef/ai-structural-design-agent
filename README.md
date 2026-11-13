# AI Structural Design Agent

An open-source project to turn an **AutoCAD plan into a preliminary structural design** using AI agents, with a **licensed engineer in the loop** for review and final decisions.

> **Status: early stage (v0.1).** The core pipeline skeleton works end to end on a simple rectangular plan. Outputs are for learning and preliminary exploration only. **Not for construction use without review by a licensed structural engineer.**

## The problem

In civil and construction work, going from an architectural plan to a structural design is slow and manual. Engineers re-enter geometry into analysis tools, work out loads, choose member sizes and check code rules by hand. Small consultancies and builders, especially in India, often lack large teams or expensive software, so designs are delayed or over-conservative.

## What it does today

1. **Reads a DXF plan** and extracts the plot boundary (`plan_reader.py`)
2. **Proposes a column grid** for the footprint (`layout.py`)
3. **Analyses a beam with OpenSeesPy** and validates it against the closed-form solution (`analysis.py`)
4. **Checks deflection** against a span/250 limit (IS 456 style)

## Quick start

```bash
git clone https://github.com/<your-username>/ai-structural-design-agent.git
cd ai-structural-design-agent
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pip install -e .

python examples/make_sample_plan.py   # creates a 12 m x 8 m sample plan
python run_demo.py                    # runs the pipeline
pytest                                # runs tests
```

Expected demo output:

```
Plot: 12.0 m x 8.0 m, area 96.0 m2
Proposed grid: 3 x 2 bays, spans 4.00 m x 4.00 m, 12 columns
Beam span 4.00 m | OpenSees: 1.53 mm | Closed form: 1.53 mm
Deflection check (span/250): PASS
```

## Roadmap

- [ ] Parse walls, openings and non-rectangular plots
- [ ] Load calculation (dead, live, wind, seismic per IS 875 / IS 1893)
- [ ] Full 3D frame model in OpenSeesPy
- [ ] RC member design and checks (IS 456)
- [ ] AI agents: layout agent, load agent, code-check agent, reviewer agent
- [ ] Human-in-the-loop review step with an audit trail for every decision
- [ ] Validation against textbook examples and real past designs
- [ ] Report generation (calculation sheet)

## Design principles

- **Human in the loop.** The AI proposes and explains; an engineer approves member sizes and key decisions.
- **Traceable.** Every result should link back to the assumption and code clause behind it.
- **Open tools first.** OpenSeesPy and DXF so anyone can run it without paid licences.
- **Validated.** Each analysis step is tested against known closed-form or textbook results.

## Contributing

Issues and pull requests are welcome, especially from structural engineers who can review assumptions and code clauses.

## License

MIT. See `LICENSE`.

## Disclaimer

This software is provided for education and preliminary design exploration. It does not replace professional engineering judgment. Do not use its output for construction without independent verification by a licensed structural engineer.
