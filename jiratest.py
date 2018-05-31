from jira import JIRA

#def main():
print "start....."
options = {'server': 'https://devops-poc.atlassian.net'}
jira = JIRA(options, basic_auth=('karnanikushal@gmail.com', 'Tcs!2345'))
print "connected"
issue = jira.issue('PYT-43')

print issue.fields.project.key
print issue.fields.issuetype.name
print issue.fields.reporter.displayName
print issue.fields.summary
print issue.fields.project.id
