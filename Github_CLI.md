## List all repos in Org, pushed at time, and languages and output as CSV

Requires gh (https://github.com/cli/cli#installation)

```
gh repo list ORG_NAME -L300 --json name,pushedAt,languages | jq -j '("repo",",","pushedAt",",","languages","\n",(.[]|.name,",",.pushedAt,",",(.languages[]|.node.name," "),"\n"))' > github_all_repo_list.csv
```

