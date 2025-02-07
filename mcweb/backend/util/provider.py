import constance  
from mc_providers import provider_by_name
from settings import SENTRY_ENV

def get_provider(name: str, api_key: str, base_url: str, caching: int, session_id: str | None):
    """
    One place to get a provider configured for web use.
    """

    #A default sessionid that's attached to the sentry environment. 
    if session_id == None:
        session_id = provider_session("default")

    # BEGIN TEMPORARY CROCKERY!
    extras = {}
    if name == 'onlinenews-mediacloud':
        # if mediacloud, and emergency ripcord pulled, revert to (new) NSA-based provider
        if constance.config.OLD_MC_PROVIDER:
            name = 'onlinenews-mediacloud-old'
        elif constance.config.ES_PARTIAL_RESULTS:
            # new provider: return results even if some shards failed
            # with circuit breaker tripping:
            extras["partial_responses"] = True
    logger.debug("pq_provider %s %r", name, extras)

    return provider_by_name(name, api_key=api_key, base_url = base_url, caching = caching, 
            software_id="web-search", session_id = session_id)


def provider_session(task_name:str):
    return 'f{task_name}@{SENTRY_ENV}'