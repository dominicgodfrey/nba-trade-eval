class PlayerSnapshot:
    def __init__(self, player_id, age, basic_stats, advanced_stats, position_vector,
                skill_vector, usage_profile):
        self.player_id = player_id
        self.age = age
        self.basic_stats = basic_stats
        self.advanced_stats = advanced_stats
        self.position_vector = position_vector
        self.skill_vector = skill_vector
        self.usage_profile = usage_profile
    def __repr__(self):
        return f"PlayerSnapshot(player_id={self.player_id}, age={self.age})"
class InjuryHistory:
    def __init__(self, games_played_1yr, games_played_3yr, minutes_1yr, minutes_3yr,
                   num_injuries, long_absences, body_part_flags, games_since_major_absence,
                   age_load_interaction):
        self.games_played_1yr = games_played_1yr
        self.games_played_3yr = games_played_3yr
        self.minutes_1yr = minutes_1yr
        self.minutes_3yr = minutes_3yr
        self.num_injuries = num_injuries
        self.long_absences = long_absences
        self.body_part_flags = body_part_flags
        self.games_since_major_absence = games_since_major_absence
        self.age_load_interaction = age_load_interaction
    def __repr__(self):
        return f"InjuryHistory(1yrGP={self.games_played_1yr})"
class Contract:
    def __init__(self, years_remaining, annual_salaries, cap_percentages,
                   total_guaranteed, player_option, team_option, nonguaranteed_flags):
        self.years_remaining = years_remaining
        self.annual_salaries = annual_salaries
        self.cap_percentages = cap_percentages
        self.total_guaranteed = total_guaranteed
        self.player_option = player_option
        self.team_option = team_option
        self.nonguaranteed_flags = nonguaranteed_flags
    def __repr__(self):
        return f"Contract(years_remaining={self.years_remaining})"
class Coach:
    def __init__(self, coach_id):
        self.coach_id = coach_id
class Organization:
    def __init__(self, org_id):
        self.org_id = org_id
class TeamSnapshot:
    def __init__(self, team_id, roster, team_stats, cap_state, coach_id=None, org_id=None):
        self.team_id = team_id
        self.roster = roster  # List of PlayerSnapshot instances
        self.team_stats = team_stats # e.g., offensive and defensive ratings
        self.cap_state = cap_state # payroll, tax, space
        self.coach_id = coach_id
        self.org_id = org_id

        self.roster_embedding = None
        self.team_embedding = None
        self.team_profile = None
        self.team_needs_vector = None
    def __repr__(self):
        return f"TeamSnapshot(team_id={self.team_id}, players={len(self.roster)})"