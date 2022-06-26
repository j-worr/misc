Requires gh (https://github.com/cli/cli#installation)

## list all Org repos in Github to file
```
gh repo list ORG_NAME -L300 --json name --jq '.[].name' > current_repos_in_github
```
Adding -L300 for 300 repo limit as default is only 30, adjust as necessary

## List all repos in Org, pushed at time, and languages and output as CSV

```
gh repo list ORG_NAME -L300 --json name,pushedAt,languages | jq -j '("repo",",","pushedAt",",","languages","\n",(.[]|.name,",",.pushedAt,",",(.languages[]|.node.name," "),"\n"))' > github_all_repo_list.csv
```

