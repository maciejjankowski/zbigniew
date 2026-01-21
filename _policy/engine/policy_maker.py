#!/usr/bin/env python3
"""
ZBIGNIEW Policy Maker Engine

Generates policy recommendations for Poland based on:
- Current geopolitical assessment (ZBIGNIEW Protocol)
- Strategic objectives (poland_strategic_objectives.yaml)
- nSENS multi-perspective analysis
- Stress simulation scenarios

Output: 1/5/20-year recommendations with cui bono analysis
"""

import json
import yaml
from datetime import datetime, date
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional
from enum import Enum

# ANSI colors
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
CYAN = '\033[96m'
MAGENTA = '\033[95m'
RESET = '\033[0m'
BOLD = '\033[1m'


class Horizon(Enum):
    IMMEDIATE = "1_year"
    MEDIUM = "5_year"
    LONG = "20_year"


class Priority(Enum):
    CRITICAL = 1  # Must do, existential
    HIGH = 2      # Should do, structural
    MEDIUM = 3    # Good to do, quality improvement
    LOW = 4       # Nice to have, positioning


class Vector(Enum):
    INSTITUTIONAL = "INSTITUTIONAL"
    ALLIANCE = "ALLIANCE"
    ECONOMIC = "ECONOMIC"
    INFORMATION = "INFORMATION"
    MILITARY = "MILITARY"
    POLITICAL = "POLITICAL"
    SOCIAL = "SOCIAL"


@dataclass
class Recommendation:
    """A single policy recommendation."""
    id: str
    title: str
    description: str
    horizon: Horizon
    priority: Priority
    vectors: list[Vector]
    objectives_served: list[str]
    actions: list[str]
    resources_required: str
    risks: list[str]
    cui_bono: dict  # Who benefits analysis
    confidence: float
    dependencies: list[str] = field(default_factory=list)
    contraindications: list[str] = field(default_factory=list)
    metrics: list[str] = field(default_factory=list)


@dataclass
class PolicyAssessment:
    """Complete policy assessment output."""
    timestamp: str
    geopolitical_context: str
    threat_level: str
    recommendations_1y: list[Recommendation]
    recommendations_5y: list[Recommendation]
    recommendations_20y: list[Recommendation]
    trade_offs: list[dict]
    red_lines: list[str]
    monitoring_triggers: list[str]


class PolicyMaker:
    """Main policy generation engine."""

    def __init__(self, base_path: Path):
        self.base_path = base_path
        self.objectives = self._load_objectives()
        self.assessments = self._load_assessments()
        self.predictions = self._load_predictions()
        self.events = self._load_events()

    def _load_objectives(self) -> dict:
        """Load strategic objectives."""
        obj_path = self.base_path / '_policy' / 'objectives' / 'poland_strategic_objectives.yaml'
        if obj_path.exists():
            with open(obj_path, 'r') as f:
                return yaml.safe_load(f)
        return {}

    def _load_assessments(self) -> list[dict]:
        """Load ZBIGNIEW assessments."""
        assessments = []
        assess_dir = self.base_path / '_assessments' / 'active'
        if assess_dir.exists():
            for f in assess_dir.glob('*.md'):
                assessments.append({'file': f.name, 'path': str(f)})
        return assessments

    def _load_predictions(self) -> list[dict]:
        """Load active predictions."""
        predictions = []
        pred_path = self.base_path / '_predictions' / 'active.jsonl'
        if pred_path.exists():
            with open(pred_path, 'r') as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        obj = json.loads(line)
                        if not obj.get('_schema'):
                            predictions.append(obj)
                    except json.JSONDecodeError:
                        pass
        return predictions

    def _load_events(self) -> list[dict]:
        """Load timeline events."""
        events = []
        events_path = self.base_path / '_timeline' / 'events.jsonl'
        if events_path.exists():
            with open(events_path, 'r') as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        obj = json.loads(line)
                        if not obj.get('_schema'):
                            events.append(obj)
                    except json.JSONDecodeError:
                        pass
        return events

    def assess_threat_level(self) -> tuple[str, str]:
        """Assess current threat level from predictions and events."""
        # Count active predictions by vector
        alliance_threats = sum(1 for p in self.predictions
                              if 'ALLIANCE' in p.get('vectors', [])
                              and p.get('status') == 'active')

        military_threats = sum(1 for p in self.predictions
                              if 'MILITARY' in p.get('vectors', [])
                              and p.get('status') == 'active')

        # Check for imminent predictions
        imminent = [p for p in self.predictions
                   if p.get('status') == 'active'
                   and self._days_until(p.get('deadline', '2099-01-01')) < 90]

        # Determine threat level
        if military_threats > 0 or len(imminent) > 3:
            level = "ELEVATED"
            context = f"Active threats: {alliance_threats} alliance, {military_threats} military. {len(imminent)} predictions due within 90 days."
        elif alliance_threats > 2:
            level = "HEIGHTENED"
            context = f"Alliance stress detected: {alliance_threats} active alliance-related predictions."
        else:
            level = "BASELINE"
            context = "No imminent threats detected in prediction set."

        return level, context

    def _days_until(self, deadline_str: str) -> int:
        """Calculate days until deadline."""
        try:
            deadline = datetime.strptime(deadline_str, '%Y-%m-%d').date()
            return (deadline - date.today()).days
        except:
            return 9999

    def generate_recommendations(self) -> PolicyAssessment:
        """Generate full policy recommendations."""
        threat_level, context = self.assess_threat_level()

        # Generate recommendations by horizon
        recs_1y = self._generate_immediate_recommendations(threat_level)
        recs_5y = self._generate_medium_recommendations(threat_level)
        recs_20y = self._generate_long_recommendations(threat_level)

        # Extract trade-offs from objectives
        trade_offs = self.objectives.get('tradeoffs', [])

        # Extract red lines
        red_lines = []
        for obj in self.objectives.get('objectives', {}).get('tier_4_positioning', []):
            if 'red_lines' in obj:
                red_lines.extend(obj['red_lines'])

        # Monitoring triggers
        monitoring = self.objectives.get('monitoring', {}).get('trigger_based', [])

        return PolicyAssessment(
            timestamp=datetime.now().isoformat(),
            geopolitical_context=context,
            threat_level=threat_level,
            recommendations_1y=recs_1y,
            recommendations_5y=recs_5y,
            recommendations_20y=recs_20y,
            trade_offs=trade_offs,
            red_lines=red_lines,
            monitoring_triggers=monitoring
        )

    def _generate_immediate_recommendations(self, threat_level: str) -> list[Recommendation]:
        """Generate 1-year recommendations based on current situation."""
        recs = []

        # Check alliance-related predictions
        alliance_stressed = any('ALLIANCE' in p.get('vectors', [])
                               for p in self.predictions if p.get('status') == 'active')

        if alliance_stressed or threat_level in ['ELEVATED', 'HEIGHTENED']:
            recs.append(Recommendation(
                id="REC_2026_001",
                title="Accelerate Bilateral Security Arrangements",
                description="Given NATO stress, establish backup bilateral defense agreements with key allies (UK, Baltic states, Romania) without undermining NATO.",
                horizon=Horizon.IMMEDIATE,
                priority=Priority.CRITICAL,
                vectors=[Vector.ALLIANCE, Vector.MILITARY],
                objectives_served=["OBJ_SEC_001", "OBJ_SOV_001"],
                actions=[
                    "Initiate bilateral defense consultations with UK (Feb 2026)",
                    "Formalize Baltic Defense Coordination Agreement (Q1 2026)",
                    "Joint exercises with Romania and Nordic countries (ongoing)",
                    "Defense industry cooperation agreements (Q2 2026)"
                ],
                resources_required="Diplomatic effort, minimal fiscal impact",
                risks=[
                    "Could be seen as undermining NATO (messaging critical)",
                    "May trigger EU defense integration pressure",
                    "Requires careful US relationship management"
                ],
                cui_bono={
                    "primary_beneficiaries": ["Poland (security redundancy)", "Baltic states (Polish depth)", "UK (European foothold post-Brexit)"],
                    "secondary_beneficiaries": ["NATO (bilateral ties strengthen overall)", "Regional stability"],
                    "potential_losers": ["EU defense integration advocates", "Russia (deterrence improved)"],
                    "who_opposes": "France (competing with NATO), Germany (prefers EU framework)"
                },
                confidence=0.85,
                metrics=["Number of bilateral agreements signed", "Joint exercise frequency", "Interoperability scores"]
            ))

        # Tax optimization (always relevant)
        recs.append(Recommendation(
            id="REC_2026_002",
            title="VAT Gap Reduction Initiative",
            description="Implement digital invoicing mandate and AI-based fraud detection to reduce VAT gap from ~10% to <7%.",
            horizon=Horizon.IMMEDIATE,
            priority=Priority.HIGH,
            vectors=[Vector.ECONOMIC, Vector.INSTITUTIONAL],
            objectives_served=["OBJ_TAX_001", "OBJ_INST_001"],
            actions=[
                "Mandate e-invoicing for B2B transactions (Q2 2026)",
                "Deploy AI fraud detection system (Q3 2026)",
                "Cross-border VAT cooperation with EU partners",
                "Amnesty program for voluntary disclosure (time-limited)"
            ],
            resources_required="€50-100M for systems, significant political capital",
            risks=[
                "Business compliance burden (SME impact)",
                "IT implementation challenges",
                "Political opposition from affected interests"
            ],
            cui_bono={
                "primary_beneficiaries": ["State budget (€3-5B additional revenue)", "Compliant businesses (level playing field)"],
                "secondary_beneficiaries": ["Public services (more funding)", "EU (VAT harmonization)"],
                "potential_losers": ["Tax evaders", "Grey economy participants"],
                "who_opposes": "Some business lobbies, cash-economy sectors"
            },
            confidence=0.80,
            metrics=["VAT gap percentage", "E-invoice adoption rate", "Fraud detection rate"]
        ))

        # Energy independence (critical given current events)
        recs.append(Recommendation(
            id="REC_2026_003",
            title="Energy Independence Acceleration",
            description="Fast-track energy diversification given geopolitical uncertainty.",
            horizon=Horizon.IMMEDIATE,
            priority=Priority.CRITICAL,
            vectors=[Vector.ECONOMIC, Vector.ALLIANCE],
            objectives_served=["OBJ_ECON_001"],
            actions=[
                "Baltic Pipe capacity utilization optimization",
                "LNG terminal expansion (Gdańsk)",
                "Nuclear power plant construction acceleration",
                "Renewable energy permits fast-track",
                "Strategic reserve audit and expansion"
            ],
            resources_required="Significant investment (€5-10B over 5 years), regulatory reform",
            risks=[
                "Cost overruns",
                "Technical delays (nuclear)",
                "NIMBY opposition (renewables)",
                "Supply chain constraints"
            ],
            cui_bono={
                "primary_beneficiaries": ["Poland (energy security)", "Industry (stable prices)", "Baltic region (hub potential)"],
                "secondary_beneficiaries": ["Norway (gas exports)", "US (LNG)", "Nuclear industry"],
                "potential_losers": ["Russia (reduced leverage)", "Coal sector (transition)"],
                "who_opposes": "Coal lobby, some environmental groups (nuclear)"
            },
            confidence=0.90,
            metrics=["Energy import dependency %", "Strategic reserve days", "Renewable capacity GW"]
        ))

        # Cybersecurity capacity (immediate given tech threats)
        recs.append(Recommendation(
            id="REC_2026_004",
            title="Cybersecurity Capacity Building",
            description="Establish robust cyber defense given digital threats to critical infrastructure.",
            horizon=Horizon.IMMEDIATE,
            priority=Priority.HIGH,
            vectors=[Vector.MILITARY, Vector.INSTITUTIONAL],
            objectives_served=["OBJ_TECH_001", "OBJ_SEC_001"],
            actions=[
                "National Cybersecurity Center expansion",
                "Critical infrastructure audit and hardening",
                "Cyber reservist program launch",
                "Information sharing with NATO partners",
                "Supply chain security review (5G, cloud)"
            ],
            resources_required="€200-400M initial investment, ongoing operational costs",
            risks=[
                "Talent shortage",
                "Technology obsolescence",
                "Coordination challenges across agencies"
            ],
            cui_bono={
                "primary_beneficiaries": ["Poland (digital security)", "Critical infrastructure operators", "Citizens (data protection)"],
                "secondary_beneficiaries": ["NATO (collective defense)", "Tech sector (demand)"],
                "potential_losers": ["Cyber adversaries", "Vendors of insecure systems"],
                "who_opposes": "Those profiting from current vulnerabilities"
            },
            confidence=0.85,
            metrics=["Incidents detected/prevented", "Response time", "Infrastructure compliance"]
        ))

        # Education reform initiation
        recs.append(Recommendation(
            id="REC_2026_005",
            title="Education Reform Consultation",
            description="Launch comprehensive education system review with all stakeholders.",
            horizon=Horizon.IMMEDIATE,
            priority=Priority.MEDIUM,
            vectors=[Vector.SOCIAL, Vector.INSTITUTIONAL],
            objectives_served=["OBJ_EDU_001"],
            actions=[
                "National education consultation (teachers, parents, employers)",
                "Vocational training needs assessment",
                "Teacher compensation review",
                "Curriculum modernization working groups",
                "International best practices study"
            ],
            resources_required="Administrative effort, consultation budget",
            risks=[
                "Stakeholder resistance",
                "Political interference",
                "Implementation capacity"
            ],
            cui_bono={
                "primary_beneficiaries": ["Students (better preparation)", "Economy (skilled workforce)", "Teachers (if pay addressed)"],
                "secondary_beneficiaries": ["Employers", "Universities"],
                "potential_losers": ["Status quo beneficiaries", "Ideological extremes (both sides)"],
                "who_opposes": "Those using education for political ends"
            },
            confidence=0.75,
            metrics=["Consultation participation", "Stakeholder satisfaction", "Reform roadmap quality"]
        ))

        return recs

    def _generate_medium_recommendations(self, threat_level: str) -> list[Recommendation]:
        """Generate 5-year recommendations."""
        recs = []

        # Central European leadership
        recs.append(Recommendation(
            id="REC_2026_010",
            title="Three Seas Investment Fund Leadership",
            description="Position Poland as the hub of Three Seas infrastructure investment.",
            horizon=Horizon.MEDIUM,
            priority=Priority.HIGH,
            vectors=[Vector.ECONOMIC, Vector.ALLIANCE, Vector.INSTITUTIONAL],
            objectives_served=["OBJ_LEAD_001", "OBJ_ECON_001"],
            actions=[
                "Host Three Seas summit annually",
                "Establish Warsaw as Three Seas Investment Fund HQ",
                "Lead North-South infrastructure corridor projects",
                "Coordinate regional positions on EU policies",
                "Create Central European think tank network"
            ],
            resources_required="Diplomatic investment, fund contributions (€500M over 5 years)",
            risks=[
                "Competition from other regional actors",
                "EU friction (parallel structures)",
                "Internal CE disagreements"
            ],
            cui_bono={
                "primary_beneficiaries": ["Poland (regional leadership)", "CE states (infrastructure)", "US (CE cohesion)"],
                "secondary_beneficiaries": ["EU (completed single market)", "Private investors"],
                "potential_losers": ["Germany (reduced dominance)", "Western EU (reduced influence)"],
                "who_opposes": "Those preferring EU-only frameworks"
            },
            confidence=0.75,
            metrics=["Infrastructure projects completed", "Fund size growth", "Summit attendance"]
        ))

        # Healthcare reform
        recs.append(Recommendation(
            id="REC_2026_011",
            title="Healthcare System Modernization",
            description="Transform healthcare through digitization, prevention focus, and workforce investment.",
            horizon=Horizon.MEDIUM,
            priority=Priority.MEDIUM,
            vectors=[Vector.SOCIAL, Vector.ECONOMIC, Vector.INSTITUTIONAL],
            objectives_served=["OBJ_HEALTH_001", "OBJ_LIVING_001"],
            actions=[
                "National health IT system integration",
                "Medical professional pay parity program",
                "Preventive care incentive restructuring",
                "Hospital network optimization",
                "Medical education capacity expansion"
            ],
            resources_required="€10-15B over 5 years, significant reform effort",
            risks=[
                "Reform resistance from stakeholders",
                "Brain drain during transition",
                "IT implementation failures",
                "Budget pressures"
            ],
            cui_bono={
                "primary_beneficiaries": ["Citizens (better care)", "Medical professionals (better pay)", "Economy (healthier workforce)"],
                "secondary_beneficiaries": ["Insurance sector", "Health IT companies"],
                "potential_losers": ["Inefficient providers", "Private sector if public improves"],
                "who_opposes": "Those benefiting from current inefficiencies"
            },
            confidence=0.70,
            metrics=["Wait times", "Medical emigration rate", "Life expectancy", "Preventable deaths"]
        ))

        # Defense industry
        recs.append(Recommendation(
            id="REC_2026_012",
            title="Defense Industry Self-Sufficiency",
            description="Build domestic defense manufacturing for critical systems.",
            horizon=Horizon.MEDIUM,
            priority=Priority.HIGH,
            vectors=[Vector.MILITARY, Vector.ECONOMIC],
            objectives_served=["OBJ_SEC_001", "OBJ_ECON_001"],
            actions=[
                "Ammunition production capacity tripling",
                "Drone manufacturing development",
                "Electronics/sensors domestic production",
                "Defense R&D investment increase",
                "Technology transfer agreements execution"
            ],
            resources_required="€5-8B investment over 5 years",
            risks=[
                "Technology gaps",
                "Cost competitiveness",
                "Export market development",
                "Alliance friction (Buy American pressure)"
            ],
            cui_bono={
                "primary_beneficiaries": ["Poland (security autonomy)", "Defense workers", "Regional economy"],
                "secondary_beneficiaries": ["Export markets (CE states)", "R&D sector"],
                "potential_losers": ["Foreign defense contractors"],
                "who_opposes": "US defense lobby, EU defense integration advocates"
            },
            confidence=0.75,
            metrics=["Domestic production %", "Export volume", "R&D spending", "Employment"]
        ))

        # Education system transformation
        recs.append(Recommendation(
            id="REC_2026_013",
            title="Education System Transformation",
            description="Implement comprehensive education reform balancing skills and values.",
            horizon=Horizon.MEDIUM,
            priority=Priority.HIGH,
            vectors=[Vector.SOCIAL, Vector.ECONOMIC, Vector.INSTITUTIONAL],
            objectives_served=["OBJ_EDU_001"],
            actions=[
                "Curriculum overhaul (critical thinking + civic education)",
                "Vocational track prestige restoration",
                "Teacher pay competitiveness (80% of average wage)",
                "University-industry partnerships program",
                "Digital literacy universal by grade 6"
            ],
            resources_required="€3-5B over 5 years, significant political capital",
            risks=[
                "Political polarization of education",
                "Teacher resistance to change",
                "Implementation quality variation"
            ],
            cui_bono={
                "primary_beneficiaries": ["Students", "Economy (human capital)", "Teachers (if implemented well)"],
                "secondary_beneficiaries": ["Employers", "Innovation ecosystem"],
                "potential_losers": ["Ideological gatekeepers", "Low-quality institutions"],
                "who_opposes": "Those using education for ideological ends"
            },
            confidence=0.70,
            metrics=["PISA scores", "Vocational enrollment", "Teacher retention", "Employer satisfaction"]
        ))

        # Judicial system modernization
        recs.append(Recommendation(
            id="REC_2026_014",
            title="Judicial System Modernization",
            description="Achieve efficient, independent judiciary trusted by citizens and investors.",
            horizon=Horizon.MEDIUM,
            priority=Priority.HIGH,
            vectors=[Vector.INSTITUTIONAL, Vector.POLITICAL],
            objectives_served=["OBJ_JUDICIARY_001", "OBJ_INST_001"],
            actions=[
                "Case management system digitization",
                "Judicial appointment transparency reform",
                "Commercial court specialization",
                "Alternative dispute resolution expansion",
                "Court infrastructure modernization"
            ],
            resources_required="€1-2B over 5 years, constitutional considerations",
            risks=[
                "Political interference attempts",
                "EU rule of law disputes",
                "Judicial resistance to efficiency measures"
            ],
            cui_bono={
                "primary_beneficiaries": ["Citizens (access to justice)", "Business (contract enforcement)", "Democracy (rule of law)"],
                "secondary_beneficiaries": ["Foreign investors", "EU relations"],
                "potential_losers": ["Those benefiting from delays", "Political actors seeking control"],
                "who_opposes": "Both those wanting executive control AND those fearing any reform"
            },
            confidence=0.65,
            metrics=["Case processing time", "Trust in judiciary %", "Commercial dispute resolution speed"]
        ))

        # Food security and agriculture
        recs.append(Recommendation(
            id="REC_2026_015",
            title="Agricultural Modernization & Food Security",
            description="Achieve food self-sufficiency while building competitive export agriculture.",
            horizon=Horizon.MEDIUM,
            priority=Priority.MEDIUM,
            vectors=[Vector.ECONOMIC, Vector.SOCIAL],
            objectives_served=["OBJ_FOOD_001", "OBJ_ECON_001"],
            actions=[
                "Strategic grain reserve expansion (6 months)",
                "Irrigation infrastructure investment",
                "Agricultural technology adoption incentives",
                "Processing capacity domestic expansion",
                "Export market diversification (Asia, Middle East)"
            ],
            resources_required="€2-4B over 5 years, CAP utilization optimization",
            risks=[
                "Climate variability",
                "CAP reform uncertainty",
                "Rural labor shortage"
            ],
            cui_bono={
                "primary_beneficiaries": ["Food security", "Farmers", "Rural communities"],
                "secondary_beneficiaries": ["Processing industry", "Export economy"],
                "potential_losers": ["Import-dependent sectors"],
                "who_opposes": "Free trade absolutists, cheap food importers"
            },
            confidence=0.75,
            metrics=["Food self-sufficiency %", "Agricultural exports", "Rural income"]
        ))

        # Local government empowerment
        recs.append(Recommendation(
            id="REC_2026_016",
            title="Local Government Empowerment",
            description="Strengthen local democracy through fiscal decentralization.",
            horizon=Horizon.MEDIUM,
            priority=Priority.MEDIUM,
            vectors=[Vector.INSTITUTIONAL, Vector.POLITICAL],
            objectives_served=["OBJ_LOCAL_001", "OBJ_INST_001"],
            actions=[
                "Local tax base expansion",
                "Revenue sharing formula reform",
                "Inter-municipal cooperation incentives",
                "Smart city programs for medium cities",
                "Rural broadband completion"
            ],
            resources_required="Fiscal reform, €1B transition fund",
            risks=[
                "Capacity variation across municipalities",
                "Accountability gaps",
                "Regional inequality initial increase"
            ],
            cui_bono={
                "primary_beneficiaries": ["Local communities", "Regional development", "Democracy (closer to citizens)"],
                "secondary_beneficiaries": ["Municipal innovation", "Local businesses"],
                "potential_losers": ["Central government control", "Warsaw-centric interests"],
                "who_opposes": "Centralizers, those benefiting from current distribution"
            },
            confidence=0.70,
            metrics=["Local fiscal autonomy %", "Local turnout", "Service satisfaction"]
        ))

        return recs

    def _generate_long_recommendations(self, threat_level: str) -> list[Recommendation]:
        """Generate 20-year recommendations."""
        recs = []

        # Demographic challenge
        recs.append(Recommendation(
            id="REC_2026_020",
            title="Demographic Sustainability Program",
            description="Address demographic decline through family support and selective migration.",
            horizon=Horizon.LONG,
            priority=Priority.CRITICAL,
            vectors=[Vector.SOCIAL, Vector.ECONOMIC, Vector.POLITICAL],
            objectives_served=["OBJ_VALUES_001", "OBJ_LIVING_001"],
            actions=[
                "Family support expansion (housing, childcare, flexibility)",
                "Diaspora return incentive program",
                "Selective skilled migration (cultural compatibility)",
                "Pension system long-term reform",
                "Automation investment (offset workforce decline)"
            ],
            resources_required="Sustained fiscal commitment (1-2% GDP)",
            risks=[
                "Fertility policies may not work",
                "Migration politically sensitive",
                "Pension system transition costs"
            ],
            cui_bono={
                "primary_beneficiaries": ["Future generations", "Families", "Economy (workforce)"],
                "secondary_beneficiaries": ["Pension system", "Social cohesion"],
                "potential_losers": ["Short-term budget priorities"],
                "who_opposes": "Those preferring short-term spending"
            },
            confidence=0.60,
            metrics=["Birth rate", "Net migration (educated)", "Dependency ratio"]
        ))

        # EU relationship evolution
        recs.append(Recommendation(
            id="REC_2026_021",
            title="EU Constitutional Settlement",
            description="Work toward explicit subsidiarity enforcement and competence boundaries.",
            horizon=Horizon.LONG,
            priority=Priority.MEDIUM,
            vectors=[Vector.POLITICAL, Vector.INSTITUTIONAL, Vector.ALLIANCE],
            objectives_served=["OBJ_EU_001", "OBJ_SOV_001"],
            actions=[
                "Coalition building with like-minded states",
                "Constitutional court cooperation network",
                "Subsidiarity enforcement mechanisms",
                "Treaty change proposals (when opportunity arises)",
                "Alternative opt-out frameworks"
            ],
            resources_required="Sustained diplomatic effort, legal expertise",
            risks=[
                "EU confrontation",
                "Isolation risk",
                "Economic retaliation"
            ],
            cui_bono={
                "primary_beneficiaries": ["National democracies", "Smaller states", "Subsidiarity principles"],
                "secondary_beneficiaries": ["EU legitimacy (if reformed)", "Citizens (closer democracy)"],
                "potential_losers": ["EU institutions (reduced power)", "Federalists"],
                "who_opposes": "Federal Europe advocates, EU Commission"
            },
            confidence=0.50,
            metrics=["Subsidiarity challenges won", "Like-minded coalition size", "Competence creep stopped"]
        ))

        # Regional stability anchor
        recs.append(Recommendation(
            id="REC_2026_022",
            title="Central European Stability Anchor",
            description="Establish Poland as the indispensable actor for regional stability.",
            horizon=Horizon.LONG,
            priority=Priority.HIGH,
            vectors=[Vector.ALLIANCE, Vector.MILITARY, Vector.ECONOMIC],
            objectives_served=["OBJ_LEAD_001", "OBJ_SEC_001"],
            actions=[
                "NATO northeastern flank leadership",
                "Regional crisis management capacity",
                "Economic integration deepening (CE)",
                "Cultural and educational exchange expansion",
                "Conflict prevention diplomacy"
            ],
            resources_required="Sustained investment in all instruments of power",
            risks=[
                "Overreach",
                "Regional jealousies",
                "Great power friction"
            ],
            cui_bono={
                "primary_beneficiaries": ["Poland (influence)", "CE region (stability)", "NATO (burden sharing)"],
                "secondary_beneficiaries": ["Ukraine (if stabilized)", "Democracy"],
                "potential_losers": ["Revisionist powers", "Regional competitors"],
                "who_opposes": "Russia, those preferring weak CE"
            },
            confidence=0.65,
            metrics=["Regional influence surveys", "Crisis response capacity", "Economic integration depth"]
        ))

        # Environmental transition
        recs.append(Recommendation(
            id="REC_2026_023",
            title="Energy Transition with Security",
            description="Achieve carbon neutrality trajectory while maintaining energy security and industrial base.",
            horizon=Horizon.LONG,
            priority=Priority.MEDIUM,
            vectors=[Vector.ECONOMIC, Vector.SOCIAL],
            objectives_served=["OBJ_ENV_001", "OBJ_ECON_001"],
            actions=[
                "Nuclear power program completion (3+ reactors by 2040)",
                "Baltic offshore wind development (10+ GW)",
                "Grid modernization for renewables integration",
                "Silesian transformation fund (coal region transition)",
                "Building efficiency program (net-zero new builds by 2035)"
            ],
            resources_required="€50-80B over 20 years, EU funding optimization",
            risks=[
                "Nuclear delays/cost overruns",
                "Grid stability during transition",
                "Energy poverty if mismanaged",
                "Industrial competitiveness if too fast"
            ],
            cui_bono={
                "primary_beneficiaries": ["Future generations (climate)", "Energy security", "New energy industries"],
                "secondary_beneficiaries": ["EU (climate goals)", "Technology sector", "Construction"],
                "potential_losers": ["Coal sector (managed decline)", "High-emission industries"],
                "who_opposes": "Coal lobby, climate absolutists (too slow for some)"
            },
            confidence=0.60,
            metrics=["CO2 emissions trajectory", "Energy mix %", "Air quality", "Energy poverty rate"]
        ))

        # Technology sovereignty
        recs.append(Recommendation(
            id="REC_2026_024",
            title="Technology Sovereignty Achievement",
            description="Establish domestic control over critical digital infrastructure and capabilities.",
            horizon=Horizon.LONG,
            priority=Priority.HIGH,
            vectors=[Vector.ECONOMIC, Vector.MILITARY, Vector.INSTITUTIONAL],
            objectives_served=["OBJ_TECH_001", "OBJ_SEC_001", "OBJ_ECON_001"],
            actions=[
                "National AI research institute establishment",
                "Sovereign cloud infrastructure (government + critical)",
                "Cybersecurity industry development (export capability)",
                "Tech talent retention program (competitive with Western hubs)",
                "Critical technology manufacturing (semiconductors, defense electronics)"
            ],
            resources_required="€15-25B over 20 years, significant policy coordination",
            risks=[
                "Global competition for talent",
                "Technology obsolescence",
                "Protectionism backlash",
                "Cost of catching up"
            ],
            cui_bono={
                "primary_beneficiaries": ["National security", "Tech industry", "Skilled workforce"],
                "secondary_beneficiaries": ["Digital economy", "Education sector", "Startups"],
                "potential_losers": ["Foreign tech giants (reduced dominance)", "Status quo importers"],
                "who_opposes": "Those profiting from tech dependency, free trade absolutists"
            },
            confidence=0.55,
            metrics=["Tech sector GDP %", "Talent net migration", "Critical systems domestic %", "R&D spending"]
        ))

        # Cultural diplomacy and soft power
        recs.append(Recommendation(
            id="REC_2026_025",
            title="Polish Soft Power Projection",
            description="Build Polish cultural presence and influence globally through authentic engagement.",
            horizon=Horizon.LONG,
            priority=Priority.LOW,
            vectors=[Vector.INFORMATION, Vector.SOCIAL],
            objectives_served=["OBJ_CULTURE_001", "OBJ_LEAD_001"],
            actions=[
                "Polish Institute network expansion (50+ countries)",
                "Film/game industry international competitiveness",
                "Academic exchange programs (net positive)",
                "Heritage site investment (UNESCO candidates)",
                "Digital cultural presence (streaming, social media)"
            ],
            resources_required="€2-4B over 20 years, creative sector investment",
            risks=[
                "Cultural export difficult to manufacture",
                "Propaganda perception if heavy-handed",
                "Resource competition with hard power"
            ],
            cui_bono={
                "primary_beneficiaries": ["Polish identity abroad", "Tourism", "Cultural industries"],
                "secondary_beneficiaries": ["Diplomacy (soft power)", "Diaspora identity"],
                "potential_losers": ["Competing cultural narratives"],
                "who_opposes": "Those preferring different Polish narrative, budget hawks"
            },
            confidence=0.50,
            metrics=["Cultural institute reach", "Polish learners abroad", "Creative exports", "Tourism brand"]
        ))

        # Diaspora engagement
        recs.append(Recommendation(
            id="REC_2026_026",
            title="Diaspora as Strategic Asset",
            description="Transform 20 million Poles abroad from brain drain into strategic national asset.",
            horizon=Horizon.LONG,
            priority=Priority.MEDIUM,
            vectors=[Vector.SOCIAL, Vector.ECONOMIC, Vector.POLITICAL],
            objectives_served=["OBJ_DIASPORA_001", "OBJ_ECON_001"],
            actions=[
                "Diaspora investment vehicles (development bonds)",
                "Return incentive package (housing, job placement, pension portability)",
                "Consular services excellence program",
                "Online Polish education for children abroad",
                "Diaspora voting accessibility improvement"
            ],
            resources_required="€1-2B over 20 years, institutional reform",
            risks=[
                "Return incentives may not work",
                "Political polarization of diaspora",
                "Dual loyalty concerns in host countries"
            ],
            cui_bono={
                "primary_beneficiaries": ["Diaspora (connection maintained)", "Poland (talent/investment return)"],
                "secondary_beneficiaries": ["Children of emigrants (identity)", "Economy (remittances, investment)"],
                "potential_losers": ["Host countries (if return successful)"],
                "who_opposes": "Those viewing diaspora as lost, isolationists"
            },
            confidence=0.60,
            metrics=["Return migration (educated)", "Diaspora investment", "Voting participation", "Identity retention"]
        ))

        return recs

    def print_report(self):
        """Print comprehensive policy report."""
        assessment = self.generate_recommendations()

        print(f"\n{BOLD}{'=' * 70}{RESET}")
        print(f"{BOLD}ZBIGNIEW POLICY MAKER - POLAND STRATEGIC ASSESSMENT{RESET}")
        print(f"{BOLD}{'=' * 70}{RESET}")
        print(f"Generated: {assessment.timestamp}")
        print(f"Threat Level: {self._colorize_threat(assessment.threat_level)}")
        print(f"Context: {assessment.geopolitical_context}")

        # 1-Year Recommendations
        print(f"\n{CYAN}{BOLD}═══ IMMEDIATE ACTIONS (1 YEAR) ═══{RESET}")
        for rec in assessment.recommendations_1y:
            self._print_recommendation(rec)

        # 5-Year Recommendations
        print(f"\n{BLUE}{BOLD}═══ MEDIUM-TERM STRATEGY (5 YEARS) ═══{RESET}")
        for rec in assessment.recommendations_5y:
            self._print_recommendation(rec)

        # 20-Year Recommendations
        print(f"\n{MAGENTA}{BOLD}═══ LONG-TERM VISION (20 YEARS) ═══{RESET}")
        for rec in assessment.recommendations_20y:
            self._print_recommendation(rec)

        # Red Lines
        print(f"\n{RED}{BOLD}═══ RED LINES (Non-Negotiable) ═══{RESET}")
        for rl in assessment.red_lines:
            print(f"  {RED}▪{RESET} {rl}")

        # Trade-offs
        print(f"\n{YELLOW}{BOLD}═══ TRADE-OFFS (Explicit) ═══{RESET}")
        for to in assessment.trade_offs:
            print(f"  {YELLOW}•{RESET} {to.get('area')}: {to.get('tension')}")
            print(f"    Resolution: {to.get('resolution')}")

        # Monitoring Triggers
        print(f"\n{GREEN}{BOLD}═══ MONITORING TRIGGERS ═══{RESET}")
        for mt in assessment.monitoring_triggers:
            print(f"  {GREEN}◉{RESET} {mt}")

    def _print_recommendation(self, rec: Recommendation):
        """Print single recommendation."""
        priority_colors = {
            Priority.CRITICAL: RED,
            Priority.HIGH: YELLOW,
            Priority.MEDIUM: BLUE,
            Priority.LOW: GREEN
        }
        color = priority_colors.get(rec.priority, RESET)

        print(f"\n{color}▶ [{rec.id}] {rec.title}{RESET}")
        print(f"  Priority: {rec.priority.name} | Confidence: {rec.confidence:.0%}")
        print(f"  Vectors: {', '.join(v.value for v in rec.vectors)}")
        print(f"  {rec.description}")

        print(f"\n  {BOLD}Actions:{RESET}")
        for action in rec.actions[:4]:  # Limit to 4
            print(f"    • {action}")

        print(f"\n  {BOLD}Cui Bono:{RESET}")
        print(f"    Benefits: {', '.join(rec.cui_bono.get('primary_beneficiaries', []))}")
        print(f"    Opposes: {rec.cui_bono.get('who_opposes', 'Unknown')}")

        print(f"\n  {BOLD}Risks:{RESET}")
        for risk in rec.risks[:3]:
            print(f"    ⚠ {risk}")

    def _colorize_threat(self, level: str) -> str:
        colors = {
            'ELEVATED': f"{RED}{BOLD}{level}{RESET}",
            'HEIGHTENED': f"{YELLOW}{BOLD}{level}{RESET}",
            'BASELINE': f"{GREEN}{level}{RESET}"
        }
        return colors.get(level, level)

    def export_json(self, output_path: Path):
        """Export assessment as JSON."""
        assessment = self.generate_recommendations()

        def rec_to_dict(rec: Recommendation) -> dict:
            return {
                'id': rec.id,
                'title': rec.title,
                'description': rec.description,
                'horizon': rec.horizon.value,
                'priority': rec.priority.name,
                'vectors': [v.value for v in rec.vectors],
                'objectives_served': rec.objectives_served,
                'actions': rec.actions,
                'resources_required': rec.resources_required,
                'risks': rec.risks,
                'cui_bono': rec.cui_bono,
                'confidence': rec.confidence,
                'metrics': rec.metrics
            }

        output = {
            'timestamp': assessment.timestamp,
            'geopolitical_context': assessment.geopolitical_context,
            'threat_level': assessment.threat_level,
            'recommendations': {
                '1_year': [rec_to_dict(r) for r in assessment.recommendations_1y],
                '5_year': [rec_to_dict(r) for r in assessment.recommendations_5y],
                '20_year': [rec_to_dict(r) for r in assessment.recommendations_20y]
            },
            'trade_offs': assessment.trade_offs,
            'red_lines': assessment.red_lines,
            'monitoring_triggers': assessment.monitoring_triggers
        }

        with open(output_path, 'w') as f:
            json.dump(output, f, indent=2, ensure_ascii=False)

        print(f"Exported to: {output_path}")


def main():
    script_dir = Path(__file__).parent
    base_path = script_dir.parent.parent

    maker = PolicyMaker(base_path)

    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd == 'export':
            output = base_path / '_policy' / 'recommendations' / f'assessment_{date.today()}.json'
            maker.export_json(output)
        elif cmd == 'threat':
            level, context = maker.assess_threat_level()
            print(f"Threat Level: {level}")
            print(f"Context: {context}")
        else:
            print(f"Unknown command: {cmd}")
    else:
        maker.print_report()


if __name__ == '__main__':
    import sys
    main()
