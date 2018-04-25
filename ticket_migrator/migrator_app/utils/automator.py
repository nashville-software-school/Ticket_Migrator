import requests
from operator import itemgetter

class issue():
    def __init__(self, source_issue, index):
        self.source_id = source_issue['id']
        self.title = source_issue['title']
        self.body = source_issue['body']
        self.priority = index
        self.target_id = None

class automator():
    def __init__(self, selected_backlog, target_repos, authToken):
        self.source_issues = None
        self.sprint_name = selected_backlog.name
        self.source_repo = selected_backlog.source_repo.get_repo()
        self.issue_array = sorted(list(selected_backlog.backlog_issues_set.all().values()),key=itemgetter('priority'))
        self.target_repos = target_repos
        self.headers = {'Accept': 'application/vnd.github.inertia-preview+json',
                        'Authorization': f'token {authToken}'}

    def get_issues(self):

        url = f'https://api.github.com/repos/{self.source_repo}/issues'
        response = requests.get(url, headers=self.headers).json()

        self.source_issues = [issue(next(x for x in response if x['id'] == item['issue_id']), item['priority']) for item in self.issue_array]

        return self

    def automate(self):
        for target_repo in self.target_repos:
            robo = robot(self.source_issues, target_repo, self.headers, self.sprint_name)
            robo.run()
        return self

    def run(self):
        self.get_issues().automate()
        return "Success"

class robot():

    def __init__(self, source_issues, target_repo, headers, sprint_name):
        self.source_issues = source_issues
        self.target_repo = target_repo
        self.headers = headers
        self.sprint_name = sprint_name
        self.target_project_id = None
        self.target_backlog_id = None
        

    def run(self):
        self.migrate_issues().create_project().create_columns().groom_backlog()

    def migrate_issues(self):
        for source_issue in self.source_issues:
            body = {"title": source_issue.title, "body": source_issue.body}
            print(self.headers)
            print()
            response = requests.post(f'https://api.github.com/repos/{self.target_repo}/issues', json=body, headers=self.headers).json()
            source_issue.target_id = response['id']

        return self

    def create_project(self):
        body = {"name": self.sprint_name,
                "body": ""}
        response = requests.post(f'https://api.github.com/repos/{self.target_repo}/projects', json=body, headers=self.headers).json()
        print(response)
        self.target_project_id = response['id']

        return self

    def create_columns(self):
        url = f'https://api.github.com/projects/{self.target_project_id}/columns'
        columns=('Backlog', 'To Do', 'Ready For Testing', 'Done')
        for column in columns:
            response = requests.post(url, json={'name': column}, headers=self.headers)
            if column=='Backlog':
                self.target_backlog_id=response.json()['id']
            
        return self

    def groom_backlog(self):
        url = f'https://api.github.com/projects/columns/{self.target_backlog_id}/cards'
        sorted_issues = sorted(self.source_issues, key=lambda i: i.priority, reverse=True)

        for si in sorted_issues:
            body = {'content_id':si.target_id, "content_type":'Issue'}
            response = requests.post(url, json=body, headers=self.headers)
