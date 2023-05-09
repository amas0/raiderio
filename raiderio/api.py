import requests

BASE_URL = 'https://raider.io'


class RaiderIO:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({'accept': 'application/json'})

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_traceback):
        self.close()

    def close(self):
        self.session.close()

    def _get_results(self, endpoint, params) -> dict:
        res = self.session.get(endpoint, params=params)
        res.raise_for_status()
        return res.json()

    def get_character_profile(self, region: str, realm: str, name: str, fields: str = '') -> dict:
        endpoint = f'{BASE_URL}/api/v1/characters/profile'
        params = {
            'region': region,
            'realm': realm,
            'name': name,
        }
        if fields:
            params['fields'] = fields
        return self._get_results(endpoint, params)

    def get_guild_boss_kill(self, region: str, realm: str, guild: str, raid: str, boss: str,
                            difficulty: str) -> dict:
        endpoint = f'{BASE_URL}/api/v1/guilds/boss-kill'
        params = {
            'region': region,
            'realm': realm,
            'guild': guild,
            'raid': raid,
            'boss': boss,
            'difficulty': difficulty
        }
        return self._get_results(endpoint, params)

    def get_guild_profile(self, region: str, realm: str, name: str, fields: str = '') -> dict:
        endpoint = f'{BASE_URL}/api/v1/guilds/profile'
        params = {
            'region': region,
            'realm': realm,
            'name': name,
        }
        if fields:
            params['fields'] = fields
        return self._get_results(endpoint, params)

    def get_mythic_plus_affixes(self, region: str, locale: str = '') -> dict:
        endpoint = f'{BASE_URL}/api/v1/mythic-plus/affixes'
        params = {
            'region': region
        }
        if locale:
            params['locale'] = locale
        return self._get_results(endpoint, params)

    def get_mythic_plus_leaderboard_capacity(self, region: str, realm: str = '', scope: str = ''):
        endpoint = f'{BASE_URL}/api/v1/mythic-plus/leaderboard-capacity'
        params = {
            'region': region
        }
        if realm:
            params['realm'] = realm
        if scope:
            params['scope'] = scope
        return self._get_results(endpoint, params)

    def get_mythic_plus_run_details(self, season: str = '', id: int = 0) -> dict:
        endpoint = f'{BASE_URL}/api/v1/mythic-plus/run-details'
        params = {
            'season': season,
            'id': id,
        }
        return self._get_results(endpoint, params)

    def get_mythic_plus_runs(self, region: str = '', season: str = '', dungeon: str = '',
                             affixes: str = '', page: int = 0) -> dict:
        endpoint = f'{BASE_URL}/api/v1/mythic-plus/runs'
        params = {}
        if region:
            params['region'] = region
        if season:
            params['season'] = season
        if dungeon:
            params['dungeon'] = dungeon
        if affixes:
            params['affixes'] = affixes
        if page:
            params['page'] = page
        return self._get_results(endpoint, params)

    def get_mythic_plus_score_tiers(self, season: str = '') -> dict:
        endpoint = f'{BASE_URL}/api/v1/mythic-plus/score-tiers'
        params = {}
        if season:
            params['season'] = season
        return self._get_results(endpoint, params)

    def get_mythic_plus_season_cutoffs(self, season: str = '', region: str = '') -> dict:
        endpoint = f'{BASE_URL}/api/v1/mythic-plus/season-cutoffs'
        params = {
            'region': region,
            'season': season,
        }
        return self._get_results(endpoint, params)

    def get_mythic_plus_static_data(self, expansion_id: int) -> dict:
        endpoint = f'{BASE_URL}/api/v1/mythic-plus/static-data'
        params = {
            'expansion_id': expansion_id
        }
        return self._get_results(endpoint, params)

    def get_raiding_boss_rankings(self, raid: str, boss: str, difficulty: str,
                                  region: str, realm: str = '') -> dict:
        endpoint = f'{BASE_URL}/api/v1/raiding/boss-rankings'
        params = {
            'raid': raid,
            'boss': boss,
            'difficulty': difficulty,
            'region': region
        }
        if realm:
            params['realm'] = realm
        return self._get_results(endpoint, params)

    def get_raiding_hall_of_fame(self, raid: str, difficulty: str, region: str) -> dict:
        endpoint = f'{BASE_URL}/api/v1/raiding/hall-of-fame'
        params = {
            'raid': raid,
            'difficulty': difficulty,
            'region': region
        }
        return self._get_results(endpoint, params)

    def get_raiding_progression(self, raid: str, difficulty: str, region: str) -> dict:
        endpoint = f'{BASE_URL}/api/v1/raiding/progression'
        params = {
            'raid': raid,
            'difficulty': difficulty,
            'region': region
        }
        return self._get_results(endpoint, params)

    def get_raid_rankings(self, raid: str, difficulty: str, region: str, realm: str = '', guilds: str = '',
                                  page: int = 0, limit: int = 50) -> dict:
        endpoint = f'{BASE_URL}/api/v1/raiding/raid-rankings'
        params = {
            'raid': raid,
            'difficulty': difficulty,
            'region': region,
            'page': page,
            'limit': limit
        }
        if realm:
            params['realm'] = realm
        if guilds:
            params['guilds'] = guilds
        return self._get_results(endpoint, params)

    def get_raid_static_data(self, expansion_id: int) -> dict:
        endpoint = f'{BASE_URL}/api/v1/raiding/static-data'
        params = {
            'expansion_id': expansion_id
        }
        return self._get_results(endpoint, params)
