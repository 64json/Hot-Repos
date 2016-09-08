import facebook
import private

graph = facebook.GraphAPI(private.fb_access_token)


def post(repo):
    repo_name = repo['full_name']
    repo_desc = repo['description']
    repo_lang = repo['language'] if not repo['language'] is None else 'unknown'
    repo_url = repo['html_url']
    repo_star = repo['stargazers_count']
    repo_avatar = repo['owner']['avatar_url']
    graph.put_wall_post(repo_name + '\n\n' + repo_desc + '\n#hotrepo #hotrepo_' + repo_lang,
                        {'name': repo_name, 'link': repo_url, 'caption': repr(repo_star) + ' stars on GitHub',
                         'description': repo_desc, 'picture': repo_avatar},
                        private.fb_page_id)
    return True