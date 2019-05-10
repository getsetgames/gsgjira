
import sys
import csv
import os
import jira
from jira import JIRA

user   = os.environ['GSGJIRA_USER']
apikey = os.environ['GSGJIRA_APIKEY']
server = os.environ['GSGJIRA_SERVER']

options = {
 'server': server
}

gsgjira = JIRA(options, basic_auth=(user,apikey) )

def main():
    # check for CSV on command line
    f = open('JIRA.csv')
    reader = csv.reader(f)

    # skip the first line from the file they are just column headers
    next(reader)

    for row in reader:
        print row

        issue_type = row[1]
        issue_summary = row[2]
        issue_description = row[3]
        issue_status = row[4]
        issue_project = row[5]
        issue_priority = row[7]
        issue_assignee = row[8]

        gsgjira.create_issue(project=issue_project,
                             summary=issue_summary,
                             description=issue_description,
                             issuetype={'name': issue_type});

if __name__ == '__main__':
    main()